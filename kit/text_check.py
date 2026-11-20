#!/usr/bin/env python3
"""Text coherence check of a charte v6 content (slides <-> captions <-> alt), before rendering and scheduling.

Usage: python3 kit/text_check.py content/<week>/<id>.json [...]

Blocking errors:
  numbers     every figure of the captions and the TikTok title (amounts, %, durations) appears in the slides,
              the alt text or the sources: no number in the post that the carousel does not show or justify
  reveal      a "slide N" in a caption points to the reveal slide (the one before last, brief section 5)
  question    exactly one engagement question per caption (a question inside « quotes » is the myth, not counted)
  ending      the caption ends with « Guide gratuit : lien dans ma bio. » ; no « Commente GUIDE » anywhere
  mention     « Contenu éducatif, pas un conseil financier » in every caption
  lines       at most 3 lines before the first blank line (what Instagram shows before « … plus »)
  cover       the cover's key number (if any) is in the Instagram caption
Prints one JSON line per file; exits 1 on any error.
"""
import json, re, sys, unicodedata

END = "Guide gratuit : lien dans ma bio."


def norm(t):
    t = unicodedata.normalize("NFKC", str(t or "")).replace(" ", " ").replace(" ", " ")
    return re.sub(r"[*]", "", t)


def numbers(t):
    t = norm(t)
    found = re.findall(r"\d[\d  ]*(?:,\d+)?", t)
    return {re.sub(r"\s", "", n) for n in found if re.sub(r"\D", "", n)}


def slide_text(s):
    out = []
    def walk(o):
        if isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
        elif isinstance(o, (str, int, float)):
            out.append(str(o))
    walk(s)
    return " ".join(out)


def questions(cap):
    body = re.sub(r"«[^»]*»", " ", norm(cap))
    return len(re.findall(r"\?", body))


def check(path):
    c = json.load(open(path, encoding="utf-8"))
    errors, warnings = [], []
    slides = c["slides"]
    n = len(slides)
    pool = numbers(" ".join(slide_text(s) for s in slides) + " " + c.get("alt", "") + " " + " ".join(c.get("sources", [])))
    caps = c.get("captions", {})
    for net in ("instagram", "facebook", "tiktok", "tiktok_title"):
        cap = caps.get(net, "")
        missing = sorted(x for x in numbers(re.sub(r"(#\w+|slide \d+)", " ", cap, flags=re.I)) if x not in pool)
        if missing:
            errors.append(f"{net} : chiffres absents du carrousel et des sources : {', '.join(missing)}")
        for ref in ([] if net == "facebook" else re.findall(r"slide (\d+)", norm(cap), flags=re.I)):
            if int(ref) != n - 1:
                errors.append(f"{net} : renvoie à la slide {ref}, la révélation est en slide {n - 1}")
        if net == "facebook" and re.search(r"slide \d|swip|carrousel", norm(cap), flags=re.I):
            errors.append("facebook : une seule image est publiée sur Facebook, pas de renvoi à une slide")
        if "commente guide" in norm(cap).lower():
            errors.append(f"{net} : « Commente GUIDE » est supprimé (brief, section 6)")
        if net == "tiktok_title":
            continue
        if not norm(cap).rstrip().endswith(END):
            errors.append(f"{net} : la dernière ligne doit être « {END} »")
        if "contenu éducatif, pas un conseil financier" not in norm(cap).lower():
            errors.append(f"{net} : mention « Contenu éducatif, pas un conseil financier » absente")
        q = questions(cap)
        if q != 1:
            errors.append(f"{net} : {q} questions, une seule question d'engagement attendue")
        if net != "tiktok":
            first = norm(cap).split("\n\n")[0]
            if len(first.split("\n")) > 3:
                errors.append(f"{net} : {len(first.splitlines())} lignes avant la première ligne vide (3 au maximum)")
    cover = next((s for s in slides if s.get("type") == "cover"), {})
    if cover.get("number"):
        if not numbers(cover["number"]) <= numbers(caps.get("instagram", "")):
            errors.append("le chiffre clé de la couverture n'apparaît pas dans la légende Instagram")
    return {"file": path, "ok": not errors, "errors": errors, "warnings": warnings}


def main():
    bad = False
    for p in sys.argv[1:]:
        r = check(p)
        bad |= not r["ok"]
        print(json.dumps(r, ensure_ascii=False))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
