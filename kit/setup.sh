#!/usr/bin/env bash
# Installs the brand fonts (from npm, reachable in Claude cloud environments) into kit/fonts.
# Playwright + Chromium, Pillow and Jinja2 are preinstalled in the cloud environment.
set -euo pipefail
KIT="$(cd "$(dirname "$0")" && pwd)"
TMP="$(mktemp -d)"
( cd "$TMP" && npm init -y >/dev/null 2>&1 && npm install --silent @fontsource/cormorant-garamond@5.3.0 @fontsource/outfit@5.3.0 )
mkdir -p "$KIT/fonts"
for w in 500 600 700; do for s in normal italic; do
  cp "$TMP/node_modules/@fontsource/cormorant-garamond/files/cormorant-garamond-latin-$w-$s.woff2" "$KIT/fonts/"
done; done
for w in 300 400 500 600; do
  cp "$TMP/node_modules/@fontsource/outfit/files/outfit-latin-$w-normal.woff2" "$KIT/fonts/"
done
rm -rf "$TMP"
python3 -c "import playwright, PIL, jinja2" && echo "kit ready: $(ls "$KIT/fonts" | wc -l) fonts"
