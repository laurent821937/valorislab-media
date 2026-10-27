#!/usr/bin/env bash
# Installs the brand font (Plus Jakarta Sans, from npm — reachable in Claude cloud environments) into kit/fonts.
# Playwright + Chromium, Pillow and Jinja2 are preinstalled in the cloud environment.
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
python3 -c "import playwright, PIL, jinja2" && echo "kit ready: $(ls "$KIT/fonts" | wc -l) fonts, $(ls "$KIT/assets" | wc -l) assets"
