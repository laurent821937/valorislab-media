#!/usr/bin/env bash
# Installs the brand font (Plus Jakarta Sans, from npm — reachable in Claude cloud environments) into kit/fonts.
# Chromium, Pillow and Jinja2 are preinstalled in the cloud environment; Python Playwright is installed if missing.
set -euo pipefail
KIT="$(cd "$(dirname "$0")" && pwd)"
TMP="$(mktemp -d)"
( cd "$TMP" && npm init -y >/dev/null 2>&1 && npm install --silent @fontsource/plus-jakarta-sans@5.3.0 )
mkdir -p "$KIT/fonts"
for w in 400 500 600 700 800; do
  cp "$TMP/node_modules/@fontsource/plus-jakarta-sans/files/plus-jakarta-sans-latin-$w-normal.woff2" "$KIT/fonts/"
  cp "$TMP/node_modules/@fontsource/plus-jakarta-sans/files/plus-jakarta-sans-latin-ext-$w-normal.woff2" "$KIT/fonts/"
done
rm -rf "$TMP"
# Python Playwright is not always preinstalled: install the version matching the preinstalled Chromium
# (same version as the Node package, which ships with the browser in /opt/pw-browsers).
if ! python3 -c "import playwright" 2>/dev/null; then
  V="$(node -e "console.log(require('playwright/package.json').version)" 2>/dev/null || true)"
  pip install -q "playwright${V:+==$V}" 2>/dev/null || pip install -q --break-system-packages "playwright${V:+==$V}"
fi
python3 -c "import playwright, PIL, jinja2" && echo "kit ready: $(ls "$KIT/fonts" | wc -l) fonts, $(ls "$KIT/assets" | wc -l) assets"
