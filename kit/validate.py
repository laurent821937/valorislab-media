#!/usr/bin/env python3
"""Check rendered carousels against Buffer / Instagram / TikTok / Facebook constraints,
and optionally that their public URLs answer 200 with an image/jpeg body.

Usage:
  python3 kit/validate.py media/2026/11/<id>                 # local files only
  python3 kit/validate.py media/2026/11/<id> --base-url URL  # + public URL check
     URL = https://raw.githubusercontent.com/<owner>/valorislab-media/<commit-sha>
Prints a JSON report; exits 1 on any error.
"""
import argparse, json, pathlib, sys, urllib.request
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPECS = {
    # format: (width, height, max slides, max MB)
    "feed":   (1080, 1350, 10, 8),    # 4:5, posted on Instagram, Facebook and TikTok (photo mode)
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--base-url")
    a = ap.parse_args()
    folder = pathlib.Path(a.folder)
    if not folder.is_absolute():
        folder = ROOT / folder
    errors, files = [], []
    for fmt, (w, h, max_n, max_mb) in SPECS.items():
        imgs = sorted(folder.glob(f"{fmt}-*.jpg"))
        if not imgs:
            errors.append(f"{fmt}: no images")
        if len(imgs) > max_n:
            errors.append(f"{fmt}: {len(imgs)} slides > {max_n}")
        for p in imgs:
            im = Image.open(p)
            size_mb = p.stat().st_size / 1e6
            rec = {"file": str(p.relative_to(ROOT)), "format": im.format, "mode": im.mode,
                   "size": im.size, "mb": round(size_mb, 3)}
            if im.format != "JPEG": errors.append(f"{p.name}: not JPEG")
            if im.mode != "RGB": errors.append(f"{p.name}: mode {im.mode} (needs RGB/sRGB)")
            if im.size != (w, h): errors.append(f"{p.name}: {im.size} != {(w, h)}")
            if size_mb > max_mb: errors.append(f"{p.name}: {size_mb:.1f} MB > {max_mb} MB")
            if a.base_url:
                url = f"{a.base_url.rstrip('/')}/{rec['file']}"
                rec["url"] = url
                try:
                    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "valorislab-check"})
                    with urllib.request.urlopen(req, timeout=20) as r:
                        body = r.read()
                        ctype = r.headers.get("Content-Type", "")
                        rec["http"] = r.status
                        rec["content_type"] = ctype
                        if r.status != 200: errors.append(f"{url}: HTTP {r.status}")
                        if not ctype.startswith("image/jpeg"): errors.append(f"{url}: content-type {ctype}")
                        if len(body) != p.stat().st_size: errors.append(f"{url}: size mismatch")
                except Exception as e:  # noqa: BLE001
                    errors.append(f"{url}: {e}")
            files.append(rec)
    print(json.dumps({"ok": not errors, "errors": errors, "files": files}, ensure_ascii=False, indent=1))
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
