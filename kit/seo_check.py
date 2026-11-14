#!/usr/bin/env python3
"""SEO check of a VALORISLAB content JSON (search on Instagram, TikTok, Facebook and Google).

Usage: python3 kit/seo_check.py content/<week>/<id>.json [...]

The content must carry `seo: {keyword, secondary[], cluster}` (docs/STRATEGIE.md, "Référencement").
Checks that the primary keyword (case and accents ignored) appears where the platforms index text:
  - cover slide (title, subtitle or kicker) or slide 2 title   -> on-screen text read by TikTok/Instagram
  - first 125 characters of the Instagram caption               -> visible line + search match
  - first 150 characters of the Facebook and TikTok captions
  - the TikTok title
  - the global alt text
and that each caption has 3 to 5 hashtags, with #belgique among them, and the keyword at most
4 times outside hashtags (no stuffing). Prints one JSON line per file; exits 1 on any error.
"""
import json, re, sys, unicodedata


def norm(t):
    t = unicodedata.normalize("NFKD", str(t or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9%€ ]+", " ", t).replace("  ", " ")


def count(text, kw):
    return len(re.findall(r"(?<![a-z0-9])" + re.escape(norm(kw).strip()) + r"(?![a-z0-9])", norm(text)))


def has(text, kw):
    return count(text, kw) > 0


def check(path):
    c = json.load(open(path, encoding="utf-8"))
    errors, warnings = [], []
    seo = c.get("seo") or {}
    kw = seo.get("keyword")
    if not kw:
        return {"file": path, "ok": False, "errors": ["champ seo.keyword absent"], "warnings": []}
    caps = c.get("captions", {})
    slides = c.get("slides", [])
    cover = next((s for s in slides if s.get("type") == "cover"), {})
    second = slides[1] if len(slides) > 1 else {}
    on_screen = " ".join(str(x) for x in (cover.get("title"), cover.get("subtitle"), cover.get("kicker") or c.get("kicker"),
                                            second.get("title")))
    if not has(on_screen, kw):
        errors.append(f"mot-clé « {kw} » absent du texte de la couverture et du titre de la slide 2")
    for net, n in (("instagram", 125), ("facebook", 150), ("tiktok", 150)):
        cap = caps.get(net, "")
        if not has(cap[:n], kw):
            errors.append(f"{net} : mot-clé absent des {n} premiers caractères de la légende")
        if count(re.sub(r"#\w+", " ", cap), kw) > 4:
            errors.append(f"{net} : mot-clé répété plus de 4 fois hors hashtags (bourrage)")
        tags = re.findall(r"#\w+", cap)
        if not 3 <= len(tags) <= 5:
            errors.append(f"{net} : {len(tags)} hashtags (3 à 5 attendus)")
        if "#belgique" not in [t.lower() for t in tags]:
            warnings.append(f"{net} : #belgique absent")
    if not has(caps.get("tiktok_title", ""), kw):
        errors.append("titre TikTok sans le mot-clé")
    if not has(c.get("alt", ""), kw):
        errors.append("texte alternatif global sans le mot-clé")
    sec = [s for s in seo.get("secondary", []) if not has(caps.get("instagram", ""), s)]
    if sec:
        warnings.append(f"mots-clés secondaires absents de la légende Instagram : {', '.join(sec)}")
    return {"file": path, "keyword": kw, "ok": not errors, "errors": errors, "warnings": warnings}


def main():
    bad = False
    for p in sys.argv[1:]:
        r = check(p)
        bad |= not r["ok"]
        print(json.dumps(r, ensure_ascii=False))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
