#!/usr/bin/env python3
"""Check that an AI cover decor respects the sober VALORISLAB charter (charte v5): no dominant gold.

Usage: python3 kit/decor_check.py kit/assets/scenes/ia-<slug>.jpg [...]

Measures, on the visible part of the image, the share of saturated gold/orange pixels and the mean saturation.
Prints one JSON line per image; exits 1 if any image is too gold (the decor must be regenerated or replaced).
"""
import json, sys
import numpy as np
from PIL import Image

MAX_GOLD = 0.05       # share of bright, saturated gold pixels (hue 20-55°, S > 0.45, V > 0.30)
MAX_SATURATION = 0.45  # mean saturation of the non-black pixels


def measure(path):
    hsv = np.asarray(Image.open(path).convert("RGB").resize((360, 450)).convert("HSV"), dtype=float) / 255
    h, s, v = hsv[..., 0] * 360, hsv[..., 1], hsv[..., 2]
    lit = v > 0.12
    gold = (h >= 20) & (h <= 55) & (s > 0.45) & (v > 0.30)
    return float(gold.mean()), float(s[lit].mean()) if lit.any() else 0.0


def main():
    bad = False
    for p in sys.argv[1:]:
        g, sat = measure(p)
        ok = g <= MAX_GOLD and sat <= MAX_SATURATION
        bad |= not ok
        print(json.dumps({"file": p, "gold": round(g, 3), "saturation": round(sat, 3), "ok": ok,
                          "max": {"gold": MAX_GOLD, "saturation": MAX_SATURATION}}))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
