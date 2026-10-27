#!/usr/bin/env python3
"""Render a VALORISLAB content JSON into carousel JPEGs.

Usage: python3 kit/render.py content/2026-W45/2026-11-03-frais-etf.json [--out media]

Produces, for each slide i:
  <out>/<YYYY>/<MM>/<id>/feed-<i>.jpg    1080x1350 (Instagram + Facebook, 4:5)
  <out>/<YYYY>/<MM>/<id>/tiktok-<i>.jpg  1080x1920 (TikTok photo mode, 9:16)
and a render-report.json next to them. Exits non-zero if any slide overflows.
"""
import html, json, re, sys, tempfile, pathlib, argparse
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup
from PIL import Image
from playwright.sync_api import sync_playwright

KIT = pathlib.Path(__file__).resolve().parent
ROOT = KIT.parent

THEMES = {  # accent gradient per theme (gold = Bourse/finance, electric blue = Crypto)
    "bourse":  ("#F3DB9C", "#D3AA55", "#9C7633"),
    "finance": ("#F3DB9C", "#D3AA55", "#9C7633"),
    "crypto":  ("#A6DCFF", "#3E9BFF", "#1F5FCC"),
}
FORMATS = {
    # TikTok overlays: caption/buttons bottom ~420px, action icons right ~150px
    "feed":   dict(W=1080, H=1350, pad_t=112, pad_r=80, pad_b=64, pad_l=80, h1=84, h2=68, body=35, stat=200, cover_copy=590, cover_lead=470),
    "tiktok": dict(W=1080, H=1920, pad_t=200, pad_r=140, pad_b=420, pad_l=80, h1=86, h2=74, body=40, stat=210, cover_copy=560, cover_lead=500),
}
# cover character: (height feed, height tiktok, right offset feed, right offset tiktok)
CHARACTERS = {
    "34":     (860, 1150, -70, -170),
    "hoodie": (1120, 1500, 0, -60),
    "polo":   (1120, 1500, 0, -60),
    "face":   (720, 900, -80, -200),
}
DEFAULT_CHARACTER = {"erreur": "34", "mecanisme": "hoodie", "belgique": "polo"}


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("content")
    ap.add_argument("--out", default=str(ROOT / "media"))
    ap.add_argument("--quality", type=int, default=90)
    a = ap.parse_args()

    c = json.loads(pathlib.Path(a.content).read_text(encoding="utf-8"))
    cid, date = c["id"], c["date"]  # date: YYYY-MM-DD (planned publication week)
    theme = c.get("theme", "bourse")
    acc1, acc2, acc3 = THEMES[theme]
    character = c.get("character") or DEFAULT_CHARACTER.get(c.get("pillar"), "34")
    if character not in CHARACTERS:
        character = "34"
    kicker = c["kicker"]
    slides = c["slides"]
    n = len(slides)
    for s in slides:
        if isinstance(s.get("body"), str):
            s["body_paras"] = [p for p in s["body"].split("\n\n") if p.strip()]

    out_dir = pathlib.Path(a.out) / date[:4] / date[5:7] / cid
    out_dir.mkdir(parents=True, exist_ok=True)

    env = Environment(loader=FileSystemLoader(str(KIT / "templates")), autoescape=True)
    env.filters["md"] = md
    tpl = env.get_template("slide.html.j2")

    report = {"id": cid, "files": [], "errors": []}
    tmp = pathlib.Path(tempfile.mkdtemp(dir=KIT / "templates"))  # same depth -> ../fonts resolves
    tmp_html = KIT / "templates" / "_render.html"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for fmt, f in FORMATS.items():
            page = browser.new_page(viewport={"width": f["W"], "height": f["H"]}, device_scale_factor=1)
            for i, s in enumerate(slides, 1):
                ch = CHARACTERS[character]
                hero = dict(hero_h=ch[0] if fmt == "feed" else ch[1],
                            hero_right=ch[2] if fmt == "feed" else ch[3], hero_bottom=0)
                tmp_html.write_text(tpl.render(s=s, i=i, n=n, kicker=kicker, theme=theme, fmt=fmt,
                                               character=character, acc1=acc1, acc2=acc2, acc3=acc3,
                                               **f, **hero), encoding="utf-8")
                page.goto(tmp_html.as_uri())
                fit = page.evaluate("window.__fit()")
                png = tmp / f"{fmt}-{i:02d}.png"
                page.screenshot(path=str(png), type="png")
                jpg = out_dir / f"{fmt}-{i:02d}.jpg"
                Image.open(png).convert("RGB").save(jpg, "JPEG", quality=a.quality, optimize=True,
                                                    progressive=False, subsampling=0)
                rec = {"file": str(jpg.relative_to(ROOT)), "format": fmt, "slide": i,
                       "scale": fit["scale"], "bytes": jpg.stat().st_size}
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
                      "errors": report["errors"]}, ensure_ascii=False))
    sys.exit(1 if report["errors"] else 0)


if __name__ == "__main__":
    main()
