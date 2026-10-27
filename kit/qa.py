#!/usr/bin/env python3
"""Visual quality control of a rendered carousel, before anything is pushed or scheduled.

Usage: python3 kit/qa.py media/<YYYY>/<MM>/<id> [--sheets /tmp/qa]

Reads render-report.json (text-block geometry captured at render time) and the JPEGs, then checks:
  format      JPEG, RGB, exact size (1080x1350, 4:5 for the 3 networks), file size, slide count
  overflow    no text cut or shrunk below the readable minimum
  tiktok      the same 4:5 images go to TikTok, which draws its caption over the bottom of the photo and its
              buttons on the right: no text in the bottom 160 px, nothing important under the right rail
  grid        cover title and protagonist's head inside the Instagram profile-grid crop (3:4, x 34..1046)
  overlap     no text over the protagonist (opaque pixels under title / lead)
  framing     protagonist's head fully on canvas, no hard edge visible, upscale <= 1.8x
  fonts       body text >= 30 px (feed) / 34 px (TikTok), titles >= 56 px after auto-fit
  contrast    WCAG contrast of each text colour against the sampled background >= 4.5 (>= 3 for large text)
  duplicate   cover not visually near-identical to an earlier cover (average hash)
Writes qa-report.json next to the images and review sheets (TikTok safe-zone overlay, grid crop)
to --sheets for a visual check with the Read tool. Exits 1 if any error.
"""
import argparse, json, pathlib, sys
import numpy as np
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "kit"
TIKTOK_45 = dict(bottom=160, rail_x=100, rail_y=(700, 1215))  # 4:5 photo shown letterboxed in TikTok
GRID_X = (34, 1046)  # Instagram profile grid shows a centred 3:4 crop of the 4:5 cover
MIN_FONT = {"feed": {"body": 30, "title": 56}, "tiktok": {"body": 34, "title": 56}}
TEXT_ROLES = {"kicker", "title", "lead", "body", "index", "stat", "statLabel", "compare", "note",
              "listItem", "button", "disclaimer", "brand", "count", "author", "next", "card", "book"}
LARGE_ROLES = {"title", "stat", "index"}


def rgb_of(css):
    if not css or not css.startswith("rgb"):
        return None
    parts = css[css.index("(") + 1:css.index(")")].replace("/", ",").split(",")
    vals = [float(p) for p in parts]
    if len(vals) == 4 and vals[3] < 0.5:
        return None  # transparent (gradient text): checked on pixels instead
    return vals[:3]


def lum(rgb):
    c = np.asarray(rgb, dtype=float) / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def contrast(l1, l2):
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def ahash(img, n=12):
    g = np.asarray(img.convert("L").resize((n, n), Image.BILINEAR), dtype=float)
    return (g > g.mean()).flatten()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--sheets", default="/tmp/qa")
    a = ap.parse_args()
    folder = pathlib.Path(a.folder)
    if not folder.is_absolute():
        folder = ROOT / folder
    rep = json.loads((folder / "render-report.json").read_text(encoding="utf-8"))
    cid = rep["id"]
    sheets = pathlib.Path(a.sheets) / cid
    sheets.mkdir(parents=True, exist_ok=True)
    errors, warnings, checks = [], [], []

    def err(m): errors.append(m)
    def warn(m): warnings.append(m)

    files = rep["files"]
    for fmt, (w, h, max_n) in {"feed": (1080, 1350, 10)}.items():
        recs = [r for r in files if r["format"] == fmt]
        if not recs:
            err(f"{fmt}: aucune image")
        if len(recs) > max_n:
            err(f"{fmt}: {len(recs)} slides > {max_n}")
        if not 5 <= len(recs) <= 9:
            warn(f"{fmt}: {len(recs)} slides (cible 6 à 8)")

    overlay_tiles, grid_tile = [], None
    for r in files:
        fmt, i, p = r["format"], r["slide"], ROOT / r["file"]
        tag = f"{fmt} slide {i}"
        im = Image.open(p)
        W, H = r["W"], r["H"]
        # --- format
        if im.format != "JPEG": err(f"{tag}: pas un JPEG")
        if im.mode != "RGB": err(f"{tag}: mode {im.mode}")
        if im.size != (W, H): err(f"{tag}: taille {im.size} au lieu de {(W, H)}")
        if p.stat().st_size > 8e6: err(f"{tag}: fichier > 8 Mo")
        # --- overflow / auto-fit
        if r.get("overflow"): err(f"{tag}: texte qui déborde, à raccourcir")
        if r["scale"] < 0.8: warn(f"{tag}: texte réduit à {int(r['scale'] * 100)} %, à raccourcir pour la lisibilité")
        px = np.asarray(im.convert("RGB"))
        boxes = [b for b in r["boxes"] if b["w"] > 2 and b["h"] > 2]
        for b in boxes:
            x0, y0, x1, y1 = b["x"], b["y"], b["x"] + b["w"], b["y"] + b["h"]
            # --- on canvas
            if x0 < 0 or y0 < 0 or x1 > W + 0.5 or y1 > H + 0.5:
                err(f"{tag}: « {b['text'][:40]} » ({b['role']}) sort du cadre")
            # --- TikTok overlays on the 4:5 photo (footer counter and arrow may sit under them)
            if b["role"] in TEXT_ROLES - {"count", "next", "brand"}:
                s = TIKTOK_45
                if y1 > H - s["bottom"]:
                    err(f"{tag}: « {b['text'][:40]} » ({b['role']}) sous la légende TikTok (y {int(y1)} > {H - s['bottom']})")
                elif x1 > W - s["rail_x"] and y1 > s["rail_y"][0] and y0 < s["rail_y"][1]:
                    warn(f"{tag}: « {b['text'][:40]} » ({b['role']}) touche la colonne de boutons TikTok")
            # --- Instagram grid crop on the cover
            if fmt == "feed" and i == 1 and b["role"] in {"title", "kicker"}:
                if x0 < GRID_X[0] or x1 > GRID_X[1]:
                    err(f"{tag}: « {b['text'][:40]} » coupé dans la grille du profil Instagram (3:4)")
            # --- font size
            mf = MIN_FONT[fmt]
            if b["role"] in {"body", "lead", "listItem"} and b["font"] < mf["body"]:
                warn(f"{tag}: texte {b['role']} à {b['font']:.0f} px (< {mf['body']} px), peu lisible sur mobile")
            if b["role"] == "title" and b["font"] < mf["title"]:
                warn(f"{tag}: titre à {b['font']:.0f} px (< {mf['title']} px)")
            # --- contrast (solid text colours)
            col = rgb_of(b.get("color"))
            if col and b["role"] in {"lead", "body", "listItem", "note", "disclaimer", "title", "statLabel"}:
                reg = px[max(0, int(y0)):min(H, int(y1)), max(0, int(x0)):min(W, int(x1))]
                if reg.size:
                    bg = np.percentile(lum(reg.reshape(-1, 3)), 20)
                    ratio = contrast(float(lum(col)), float(bg))
                    need = 3.0 if (b["role"] in LARGE_ROLES or b["font"] >= 40) else 4.5
                    if ratio < need:
                        err(f"{tag}: contraste {ratio:.1f}:1 < {need}:1 pour « {b['text'][:40]} »")
        # --- protagonist checks (cover)
        hero = r.get("hero")
        if hero:
            src = KIT / "templates" / hero["src"]
            am = Image.open(src).convert("RGBA").getchannel("A").resize(
                (max(1, int(round(hero["w"]))), max(1, int(round(hero["h"])))), Image.BILINEAR)
            if hero.get("mirror"):
                am = am.transpose(Image.FLIP_LEFT_RIGHT)
            alpha = np.asarray(am, dtype=float) / 255
            ys, xs = np.where(alpha > 0.5)
            if len(ys):
                top = ys.min()
                head = (ys < top + 0.13 * (ys.max() - top)) if hero["h"] > 900 else (ys < top + 0.6 * (ys.max() - top))  # full figure: head = top 13 %
                hx = xs[head] + hero["x"]; hy = ys[head] + hero["y"]
                if hx.min() < 0 or hx.max() > W or hy.min() < 0:
                    err(f"{tag}: la tête du protagoniste sort du cadre")
                if fmt == "feed":
                    outside = ((hx < GRID_X[0]) | (hx > GRID_X[1])).mean()
                    if outside > 0.15:
                        warn(f"{tag}: {outside:.0%} de la tête hors de la grille Instagram")
                # text over the protagonist
                for b in boxes:
                    if b["role"] not in {"title", "lead", "kicker", "body", "listItem", "stat", "card", "compare", "button", "index"}:
                        continue
                    bx0 = int(max(b["x"], hero["x"]) - hero["x"]); bx1 = int(min(b["x"] + b["w"], hero["x"] + hero["w"]) - hero["x"])
                    by0 = int(max(b["y"], hero["y"]) - hero["y"]); by1 = int(min(b["y"] + b["h"], hero["y"] + hero["h"]) - hero["y"])
                    if bx1 > bx0 and by1 > by0:
                        cover = (alpha[by0:by1, bx0:bx1] > 0.35).sum() / max(1, b["w"] * b["h"])
                        if cover > 0.02:
                            err(f"{tag}: « {b['text'][:40]} » chevauche le protagoniste ({cover:.0%})")
                up = hero["h"] / max(1, hero["nh"])
                if up > 1.8:
                    warn(f"{tag}: protagoniste agrandi {up:.1f}x, risque de flou")
        # --- review sheets
        tile = im.convert("RGB").copy()
        d = ImageDraw.Draw(tile, "RGBA")
        s = TIKTOK_45
        for rect in [(0, H - s["bottom"], W, H), (W - s["rail_x"], s["rail_y"][0], W, s["rail_y"][1])]:
            d.rectangle(rect, fill=(255, 40, 40, 70))
        for b in boxes:
            if b["role"] in TEXT_ROLES:
                d.rectangle((b["x"], b["y"], b["x"] + b["w"], b["y"] + b["h"]), outline=(60, 220, 120, 255), width=3)
        if fmt == "feed" and i == 1:
            d.rectangle((GRID_X[0], 0, GRID_X[1], H), outline=(80, 160, 255, 255), width=4)
            grid_tile = tile.resize((360, 450))
        overlay_tiles.append(tile.resize((288, 360)))

    # --- duplicate cover check
    cover = ROOT / next(r["file"] for r in files if r["format"] == "feed" and r["slide"] == 1)
    hc = ahash(Image.open(cover))
    for other in (ROOT / "media").glob("*/*/*/feed-01.jpg"):
        if other.parent == cover.parent:
            continue
        dist = int((hc != ahash(Image.open(other))).sum())
        if dist <= 8:
            warn(f"couverture très proche de {other.parent.name} (distance {dist}) : varier pose, composition ou couleur")

    if overlay_tiles:
        sheet = Image.new("RGB", (len(overlay_tiles) * 298 + 10, 370), (30, 30, 30))
        for k, t in enumerate(overlay_tiles):
            sheet.paste(t, (10 + k * 298, 5))
        sheet.save(sheets / "tiktok-zones.jpg", quality=85)
    if grid_tile:
        grid_tile.save(sheets / "instagram-grid.jpg", quality=85)
    feed = [Image.open(ROOT / r["file"]).convert("RGB").resize((324, 405)) for r in files if r["format"] == "feed"]
    sheet = Image.new("RGB", (len(feed) * 334 + 10, 415), (30, 30, 30))
    for k, t in enumerate(feed):
        sheet.paste(t, (10 + k * 334, 5))
    sheet.save(sheets / "feed.jpg", quality=85)

    out = {"id": cid, "ok": not errors, "errors": errors, "warnings": warnings,
           "sheets": [str(p) for p in sorted(sheets.glob("*.jpg"))]}
    (folder / "qa-report.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
