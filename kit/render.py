#!/usr/bin/env python3
"""Render a VALORISLAB content JSON into carousel JPEGs.

Usage: python3 kit/render.py content/2026-W45/2026-11-03-frais-etf.json [--out media]

Produces, for each slide i:
  <out>/<YYYY>/<MM>/<id>/feed-<i>.jpg    1080x1350 (4:5), carousel for Instagram and TikTok
and <out>/<YYYY>/<MM>/<id>/fb-01.jpg     1080x1350 (4:5), single hook image for Facebook
(hook = title of the cover, or the optional `fb` block of the content: {title, subtitle, scene})
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

FORMATS = {
    # One 4:5 format for Instagram, Facebook and TikTok (TikTok shows 4:5 photos whole, letterboxed).
    # Text stays clear of the bottom 160 px and of the right edge, where TikTok draws its caption and buttons.
    # Charte v4 (docs/STYLE-CARROUSEL.md): content between y 150 and y 1190, footer and progress bar below.
    "feed": dict(W=1080, H=1350, col_w=540, fig_h=880, scene_max=1050),
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
MAX_POSES = 2  # charte v4: poses are optional, at most 2 per carousel
MIN_SCALE_WITH_FIG = 0.86  # below this, the slide is re-rendered without the protagonist (full-width text)


def pick_poses(c):
    """Charte v4: a pose only where the content asks for one (`pose` on a point slide without a big figure,
    split bar, cards or box), never the same pose twice, at most MAX_POSES per carousel."""
    used, out = set(), []
    for s in c["slides"]:
        p = s.get("pose")
        plain_point = s["type"] == "point" and not any(s.get(k) for k in ("stat", "split", "cards", "card_note", "box"))
        if not plain_point or p not in POSES or p in used or len(used) >= MAX_POSES:
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


def halo_for(seed):
    """Position (in %) of the faint warm halo behind the content, varied per slide."""
    import random
    r = random.Random(seed)
    return round(r.uniform(35, 70)), round(r.uniform(28, 48))


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
  const roles = {kicker: '.kicker', title: '.title', lead: '.lead', body: '.body p', index: '.pill',
    stat: '.big', statLabel: '.figure .lab,.split .k', card: '.cards .c,.card-note,.box,.split', note: '.source,.split-note,.save',
    listItem: 'ol.recap .it', button: '.cta-btn', book: '.mock',
    brand: '.brand', count: '.count', next: 'footer .next,footer .url,footer .disclaimer'};
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
        if s["type"] != "cover" or name == "none":  # charte v4: only the cover carries a photo
            name = None
        elif not name and s["type"] == "cover" and covers:
            base = {"belgique": 0, "erreur": 1, "mecanisme": 2}.get(pillar, 0)
            name = sorted(covers)[(base + 3 * week) % len(covers)]  # 3 contents of a week never share a scene
        out.append(name if name in cat else None)
    return out


def load_scene(name, f):
    """Charte v4: the photo fills the top of the cover and fades into black, the text sits at the bottom."""
    if not name:
        return None
    meta = scene_catalog().get(name, {})
    src = KIT / "assets" / "scenes" / meta.get("file", f"{name}.jpg")
    if not src.exists():
        print(f"scène introuvable : {name}", file=sys.stderr)
        return None
    w0, h0 = Image.open(src).size
    h = min(f["scene_max"], int(f["W"] * h0 / w0 * 1.05))
    return dict(src=f"../assets/scenes/{src.name}", name=name, hide_header=meta.get("hide_header", False),
                pos=meta.get("focus", "50% 0%"), h=h, upscale=round(max(f["W"] / w0, h / h0), 2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("content")
    ap.add_argument("--out", default=str(ROOT / "media"))
    ap.add_argument("--quality", type=int, default=92)
    a = ap.parse_args()

    c = json.loads(pathlib.Path(a.content).read_text(encoding="utf-8"))
    cid, date = c["id"], c["date"]  # date: YYYY-MM-DD (planned publication week)
    theme = c.get("theme", "bourse")
    kicker = c["kicker"]
    slides = c["slides"]
    n = len(slides)
    for s in slides:
        if isinstance(s.get("body"), str):
            s["body_paras"] = [p for p in s["body"].split("\n\n") if p.strip()]
    poses = pick_poses(c)
    mock = next((KIT / "assets" / f"guide-mockup.{e}" for e in ("png", "webp", "jpg") if (KIT / "assets" / f"guide-mockup.{e}").exists()), None)
    guide_mockup = f"../assets/{mock.name}" if mock else None
    scenes = pick_scenes(c)

    out_dir = pathlib.Path(a.out) / date[:4] / date[5:7] / cid
    out_dir.mkdir(parents=True, exist_ok=True)

    env = Environment(loader=FileSystemLoader(str(KIT / "templates")), autoescape=True)
    env.filters["md"] = md
    tpl = env.get_template("slide.html.j2")

    kit_version = ((KIT / "RENDER_VERSION") if (KIT / "RENDER_VERSION").exists() else (KIT / "VERSION")).read_text().strip() if ((KIT / "RENDER_VERSION").exists() or (KIT / "VERSION").exists()) else "?"
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
                hx, hy = halo_for(f"{cid}-{i}")

                def render(pose_name):
                    fig = fig_geometry(pose_name, f) if pose_name else None
                    tmp_html.write_text(tpl.render(s=s, i=i, n=n, kicker=kicker, theme=theme, fmt=fmt, date=date,
                                                   fig=fig, scene=scene, guide_mockup=guide_mockup,
                                                   halo_x=hx, halo_y=hy, **f), encoding="utf-8")
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
            if fmt == "feed":
                # Facebook: one single image, the cover's hook as a big headline (same scene as the cover)
                cover = next(s for s in slides if s["type"] == "cover")
                fb = c.get("fb") or {}
                hook = dict(cover, type="hook", title=fb.get("title", cover["title"]),
                            subtitle=fb.get("subtitle", cover.get("subtitle")))
                hook.pop("scene", None)
                fb_scene = fb.get("scene")  # own AI decor for Facebook (kit/assets/scenes/ia-<slug>-fb.jpg), else the cover's scene
                scene = load_scene(fb_scene if fb_scene in scene_catalog() else scenes[slides.index(cover)], f)
                hx, hy = halo_for(f"{cid}-fb")
                tmp_html.write_text(tpl.render(s=hook, i=1, n=1, kicker=kicker, theme=theme, fmt="fb", date=date,
                                               fig=None, scene=scene, guide_mockup=None,
                                               halo_x=hx, halo_y=hy, **f), encoding="utf-8")
                page.goto(tmp_html.as_uri())
                fit, layout = page.evaluate("window.__fit()"), page.evaluate(LAYOUT_JS)
                png = tmp / "fb-01.png"
                page.screenshot(path=str(png), type="png")
                jpg = out_dir / "fb-01.jpg"
                Image.open(png).convert("RGB").resize((f["W"], f["H"]), Image.LANCZOS).save(
                    jpg, "JPEG", quality=a.quality, optimize=True, progressive=False, subsampling=0)
                report["fb"] = {"file": str(jpg.relative_to(ROOT)), "scale": fit["scale"], "overflow": fit["overflow"],
                                "scene": scene["name"] if scene else None, "bytes": jpg.stat().st_size,
                                "W": f["W"], "H": f["H"], "boxes": layout["boxes"]}
                if fit["overflow"]:
                    report["errors"].append(f"fb: text overflows even at scale {fit['scale']} -> shorten it")
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
