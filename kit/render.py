#!/usr/bin/env python3
"""Render a VALORISLAB content JSON into carousel JPEGs.

Usage: python3 kit/render.py content/2026-W45/2026-11-03-frais-etf.json [--out media]

Produces, for each slide i:
  <out>/<YYYY>/<MM>/<id>/feed-<i>.jpg    1080x1350 (4:5)
(the same 4:5 images are posted on Instagram, Facebook and TikTok)
and a render-report.json next to them. Exits non-zero if any slide overflows.
"""
import html, json, re, sys, tempfile, pathlib, argparse
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup
from PIL import Image
from playwright.sync_api import sync_playwright

SS = 2  # supersampling factor
KIT = pathlib.Path(__file__).resolve().parent
ROOT = KIT.parent

THEMES = {  # accent gradient per theme (gold = Bourse/finance, electric blue = Crypto)
    "bourse":  ("#F6E0A6", "#D6AD58", "#9A7432"),
    "finance": ("#F6E0A6", "#D6AD58", "#9A7432"),
    "crypto":  ("#A6DCFF", "#3E9BFF", "#1F5FCC"),
}
FORMATS = {
    # One 4:5 format for Instagram, Facebook and TikTok (TikTok shows 4:5 photos whole, letterboxed).
    # Text stays clear of the bottom 160 px and of the right edge, where TikTok draws its caption and buttons.
    "feed": dict(W=1080, H=1350, pad_t=46, pad_r=104, pad_b=46, pad_l=80, logo_h=104, h1=96, h2=80, body=40, stat=210, ghost=500,
                 col_w=520, fig_h=880, scene_top_max=800, scene_bottom_max=756),
}
# Protagonist poses (kit/assets/pose-<name>.webp, cut from Laurent's white-background renders).
# side: where the figure stands; mirror: flip so the gesture points towards the text; crop: share of the
# figure height shown (head to mid-thigh), the rest fades out at the bottom of the slide.
POSES = {
    "reflexion":              dict(side="right", crop=0.64, mood="comprendre, question, principe"),
    "pointe":                 dict(side="right", crop=0.60, mirror=True, mood="expliquer, montrer un chiffre"),
    "graphique-hausse":       dict(side="right", crop=0.62, mood="croissance, intérêts composés, bonne nouvelle"),
    "checklist":              dict(side="right", crop=0.60, mood="liste, étapes, règles"),
    "pouce":                  dict(side="right", crop=0.62, mood="validation, bon réflexe, appel à l'action"),
    "stress-tablette":        dict(side="right", crop=0.62, mood="mauvaise surprise, frais cachés"),
    "stress-baisse":          dict(side="right", crop=0.60, mood="perte, krach, chute"),
    "choc-polo":              dict(side="right", crop=0.62, mood="erreur grave, choc"),
    "doute-telephone":        dict(side="right", crop=0.62, mood="message suspect, arnaque"),
    "doute-telephone-hoodie": dict(side="right", crop=0.62, mood="arnaque crypto, faux support"),
}
DEFAULT_COVER_POSE = {"erreur": "choc-polo", "mecanisme": "graphique-hausse", "belgique": "reflexion"}
DEFAULT_TYPE_POSE = {"list": "checklist", "cta": "pouce", "stat": "pointe", "compare": "reflexion"}
POINT_POOL = ["reflexion", None, "pointe", None, "graphique-hausse", None]
MIN_SCALE_WITH_FIG = 0.86  # below this, the slide is re-rendered without the protagonist (full-width text)


def pick_poses(c):
    """One pose per slide (or None), never the same pose twice in a carousel."""
    pillar, theme = c.get("pillar"), c.get("theme")
    used, out, k_point = set(), [], 0
    for s in c["slides"]:
        p = s.get("pose")
        if p in (None, ""):
            if s["type"] == "cover":
                p = DEFAULT_COVER_POSE.get(pillar, "reflexion")
                if pillar == "erreur" and theme == "crypto":
                    p = "doute-telephone-hoodie"
            elif s["type"] == "point":
                p = POINT_POOL[k_point % len(POINT_POOL)]; k_point += 1
            else:
                p = DEFAULT_TYPE_POSE.get(s["type"])
        if p == "none" or p not in POSES or p in used:
            p = None
        if p:
            used.add(p)
        out.append(p)
    return out


def fig_geometry(name, f):
    """Figure placement in px for a format."""
    meta = POSES[name]
    from PIL import Image as _I
    w0, h0 = _I.open(KIT / "assets" / f"pose-{name}.webp").size
    top_pad = 30
    vis_h = f["fig_h"]
    full_h = int((vis_h - top_pad) / meta["crop"])
    w = int(full_h * w0 / h0)
    offset = -int(w * 0.04)
    spot_d = int(full_h * 0.62)
    return dict(src=f"../assets/pose-{name}.webp", name=name, side=meta["side"], mirror=meta.get("mirror", False),
                vis_h=vis_h, full_h=full_h, w=w, top_pad=top_pad, offset=offset, bottom=0, fade_from=78,
                spot_x=offset + w // 2 - spot_d // 2, spot_y=f["H"] - vis_h - int(spot_d * 0.08), spot_d=spot_d)


def bokeh_for(seed, f, theme):
    import random
    r = random.Random(seed)
    W, H = f["W"], f["H"]
    cols = ["rgba(246,214,140,1)", "rgba(232,180,90,1)", "rgba(255,236,190,1)"]
    if theme == "crypto":
        cols += ["rgba(120,190,255,1)"]
    out = []
    for _ in range(11):
        d = r.randint(30, 150)
        out.append(dict(x=int(r.uniform(0.42, 1.0) * W - d / 2), y=int(r.uniform(0.0, 0.55) * H - d / 2), d=d,
                        c=r.choice(cols), o=round(r.uniform(0.10, 0.34), 2), blur=r.randint(3, 14)))
    return out


def md(text):
    """Escape, then **bold** -> <strong>, *accent* -> <em>."""
    t = html.escape(str(text))
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
    # French typography: no orphan punctuation at line start
    t = re.sub(r"[ \u00a0]+([?!:;\u00bb])", "\u202f\\1", t)
    t = re.sub(r"\u00ab[ \u00a0]+", "\u00ab\u00a0", t)
    t = re.sub(r"(\d) (?=\S)", "\\1\u00a0", t)  # keep a number with the word that follows
    return Markup(t.replace("\n", "<br>"))


# Layout probe: geometry of every text block (and the protagonist pose) for kit/qa.py
LAYOUT_JS = """() => {
  const roles = {kicker: '.kicker', title: '.t1,.t2', lead: '.lead', body: '.body p', index: '.idx',
    stat: '.stat', statLabel: '.stat-label', card: '.card', compare: '.cmp .col', note: '.foot-note',
    listItem: 'ol.list li', button: '.cta-btn', book: '.book', disclaimer: '.disclaimer',
    brand: 'header .brand', count: 'header .count', author: 'footer .author', next: 'footer .next'};
  const boxes = [];
  for (const [role, q] of Object.entries(roles)) {
    document.querySelectorAll(q).forEach(e => {
      const r = e.getBoundingClientRect(), cs = getComputedStyle(e);
      boxes.push({role, x: r.x, y: r.y, w: r.width, h: r.height, font: parseFloat(cs.fontSize),
                  color: cs.color, text: (e.innerText || '').replace(/\\s+/g, ' ').slice(0, 70)});
    });
  }
  const h = document.querySelector('.hero');
  let hero = null;
  if (h) { const r = h.getBoundingClientRect();
    hero = {x: r.x, y: r.y, w: r.width, h: r.height, src: h.getAttribute('src'), nw: h.naturalWidth, nh: h.naturalHeight,
      mirror: getComputedStyle(h).transform.startsWith('matrix(-1')}; }
  return {boxes, hero};
}"""


def text_over_figure(layout, W, H):
    """Share of each text block covered by opaque protagonist pixels (max over blocks)."""
    import numpy as np
    hero = layout.get("hero")
    if not hero:
        return 0.0, None
    src = KIT / "templates" / hero["src"]
    alpha = Image.open(src).convert("RGBA").getchannel("A").resize(
        (max(1, int(round(hero["w"]))), max(1, int(round(hero["h"])))), Image.BILINEAR)
    if hero.get("mirror"):
        alpha = alpha.transpose(Image.FLIP_LEFT_RIGHT)
    a = np.asarray(alpha, dtype=float) / 255
    worst, who = 0.0, None
    for b in layout["boxes"]:
        if b["role"] in {"brand", "count", "next"} or b["w"] < 3 or b["h"] < 3:
            continue
        x0 = int(max(b["x"], hero["x"]) - hero["x"]); x1 = int(min(b["x"] + b["w"], hero["x"] + hero["w"], W) - hero["x"])
        y0 = int(max(b["y"], hero["y"]) - hero["y"]); y1 = int(min(b["y"] + b["h"], hero["y"] + hero["h"], H) - hero["y"])
        if x1 > x0 and y1 > y0:
            cov = (a[y0:y1, x0:x1] > 0.35).sum() / max(1, b["w"] * b["h"])
            if cov > worst:
                worst, who = cov, b["text"][:40]
    return worst, who


def scene_catalog():
    cat_p = KIT / "assets" / "scenes" / "scenes.json"
    return json.loads(cat_p.read_text(encoding="utf-8")) if cat_p.exists() else {}


def pick_scenes(c):
    """Scene per slide: explicit `scene` on the cover / CTA slide, else an automatic choice.
    Covers: per-pillar preference rotated by ISO week, so the 3 contents of a week get 3 different scenes."""
    import datetime
    cat = scene_catalog()
    covers = [k for k, v in cat.items() if v.get("role") == "cover"]
    ctas = [k for k, v in cat.items() if v.get("role") == "cta"]
    week = datetime.date.fromisoformat(c["date"]).isocalendar()[1]
    pillar = c.get("pillar")
    out = []
    for s in c["slides"]:
        name = s.get("scene")
        if name == "none":
            name = None
        elif not name and s["type"] == "cover" and covers:
            base = {"belgique": 0, "erreur": 1, "mecanisme": 2}.get(pillar, 0)
            name = sorted(covers)[(base + 3 * week) % len(covers)]  # 3 contents of a week never share a scene
        elif not name and s["type"] == "cta" and ctas:
            name = ctas[week % len(ctas)]
        out.append(name if name in cat else None)
    return out


def load_scene(name, f):
    if not name:
        return None
    meta = scene_catalog().get(name, {})
    src = KIT / "assets" / "scenes" / meta.get("file", f"{name}.jpg")
    if not src.exists():
        print(f"scène introuvable : {name}", file=sys.stderr)
        return None
    w0, h0 = Image.open(src).size
    place = meta.get("place", "top")
    h = min(int(f["W"] * h0 / w0), f["scene_top_max"] if place == "top" else f["scene_bottom_max"])
    # text area kept off the opaque part of the photo (the fade zone may sit under the text)
    main_top = f["pad_t"] + f["logo_h"]                      # where <main> starts on the page
    main_bottom = f["H"] - f["pad_b"] - 60                    # where the footer starts
    if place == "top":
        pad_top, pad_bottom = max(0, int(h * meta.get("text_from", 0.70)) - main_top), 64
    else:
        pad_top, pad_bottom = 24, max(64, main_bottom - (f["H"] - h + int(h * meta.get("text_into", 0.20))))
    return dict(src=f"../assets/scenes/{src.name}", name=name, place=place, logo=meta.get("logo", False),
                pos=meta.get("focus", "50% 0%"), h=h, keep=60 if place == "top" else 70,
                pad_top=pad_top, pad_bottom=pad_bottom, upscale=round(f["W"] / w0, 2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("content")
    ap.add_argument("--out", default=str(ROOT / "media"))
    ap.add_argument("--quality", type=int, default=92)
    a = ap.parse_args()

    c = json.loads(pathlib.Path(a.content).read_text(encoding="utf-8"))
    cid, date = c["id"], c["date"]  # date: YYYY-MM-DD (planned publication week)
    theme = c.get("theme", "bourse")
    acc1, acc2, acc3 = THEMES[theme]
    flag_be = c.get("pillar") == "belgique"
    kicker = c["kicker"]
    slides = c["slides"]
    n = len(slides)
    for s in slides:
        if isinstance(s.get("body"), str):
            s["body_paras"] = [p for p in s["body"].split("\n\n") if p.strip()]
    poses = pick_poses(c)
    scenes = pick_scenes(c)

    out_dir = pathlib.Path(a.out) / date[:4] / date[5:7] / cid
    out_dir.mkdir(parents=True, exist_ok=True)

    env = Environment(loader=FileSystemLoader(str(KIT / "templates")), autoescape=True)
    env.filters["md"] = md
    tpl = env.get_template("slide.html.j2")

    kit_version = (KIT / "VERSION").read_text().strip() if (KIT / "VERSION").exists() else "?"
    report = {"id": cid, "kit_version": kit_version, "files": [], "errors": []}
    tmp = pathlib.Path(tempfile.mkdtemp(dir=KIT / "templates"))  # same depth -> ../fonts resolves
    tmp_html = KIT / "templates" / "_render.html"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for fmt, f in FORMATS.items():
            page = browser.new_page(viewport={"width": f["W"], "height": f["H"]}, device_scale_factor=SS)
            for i, s in enumerate(slides, 1):
                scene = load_scene(scenes[i - 1], f)
                pose = None if scene else poses[i - 1]
                note = None

                def render(pose_name):
                    fig = fig_geometry(pose_name, f) if pose_name else None
                    tmp_html.write_text(tpl.render(s=s, i=i, n=n, kicker=kicker, theme=theme, fmt=fmt, flag_be=flag_be,
                                                   fig=fig, scene=scene, bokeh=bokeh_for(f"{cid}-{i}", f, theme),
                                                   acc1=acc1, acc2=acc2, acc3=acc3, **f), encoding="utf-8")
                    page.goto(tmp_html.as_uri())
                    return page.evaluate("window.__fit()"), page.evaluate(LAYOUT_JS)

                fit, layout = render(pose)
                if pose:
                    cov, who = text_over_figure(layout, f["W"], f["H"])
                    if fit["overflow"] or fit["scale"] < MIN_SCALE_WITH_FIG or cov > 0.02:
                        note = (f"pose {pose} retirée : texte trop long (échelle {fit['scale']})" if cov <= 0.02
                                else f"pose {pose} retirée : chevauche « {who} »")
                        pose = None
                        fit, layout = render(None)
                png = tmp / f"{fmt}-{i:02d}.png"
                page.screenshot(path=str(png), type="png")
                jpg = out_dir / f"{fmt}-{i:02d}.jpg"
                # supersampled render (2x) downscaled with Lanczos: crisper text, smoother gradients
                Image.open(png).convert("RGB").resize((f["W"], f["H"]), Image.LANCZOS).save(
                    jpg, "JPEG", quality=a.quality, optimize=True, progressive=False, subsampling=0)
                rec = {"file": str(jpg.relative_to(ROOT)), "format": fmt, "slide": i, "type": s["type"],
                       "pose": pose, "scene": scene["name"] if scene else None, "note": note,
                       "scale": fit["scale"], "overflow": fit["overflow"], "bytes": jpg.stat().st_size,
                       "W": f["W"], "H": f["H"], "boxes": layout["boxes"], "hero": layout["hero"]}
                report["files"].append(rec)
                if fit["overflow"]:
                    report["errors"].append(f"{fmt} slide {i}: text overflows even at scale {fit['scale']} -> shorten it")
            page.close()
        browser.close()
    tmp_html.unlink(missing_ok=True)
    for f in tmp.iterdir():
        f.unlink()
    tmp.rmdir()

    (out_dir / "render-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"out": str(out_dir.relative_to(ROOT)), "slides": n,
                      "min_scale": min(r["scale"] for r in report["files"]),
                      "poses": [r["pose"] for r in report["files"] if r["format"] == "feed"],
                      "notes": [f"{r['format']} {r['slide']}: {r['note']}" for r in report["files"] if r["note"]],
                      "errors": report["errors"]}, ensure_ascii=False))
    sys.exit(1 if report["errors"] else 0)


if __name__ == "__main__":
    main()
