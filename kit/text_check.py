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
  hook (v7)   hook_style is one of the 12 styles of STRATEGIE.md and not reused in the same week folder
  spoilers    no caption reveals the answer/verdict/first place listed in `spoilers` (error on Facebook)
  jargon (v7) no technical word on the cover (ETF, TOB, TAEG, précompte…); warning in the slide 2 title
Prints one JSON line per file; exits 1 on any error.
"""
import json, pathlib, re, sys, unicodedata

END = "Guide gratuit : lien dans ma bio."
HOOK_STYLES = {"scene", "miroir", "chiffre-choc", "mythe", "defi", "avant-apres", "moment", "message",
               "contre-intuitif", "liste", "personnage", "episode", "pov", "objet"}
JARGON = ["etf", "tob", "taeg", "ter", "précompte", "capitalisant", "distribuant", "cfd", "levier", "reynders",
          "domiciliation", "staking", "wallet", "dividende", "obligation", "tracker", "plus-value"]


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
        for ref in (re.findall(r"slide (\d+)", norm(cap), flags=re.I)):
            if int(ref) != n - 1:
                errors.append(f"{net} : renvoie à la slide {ref}, la révélation est en slide {n - 1}")
        # never reveal the answer, the verdict or the first place (Laurent, 23/11/2026)
        for sp in c.get("spoilers", []):
            if norm(sp).lower() in norm(cap).lower():
                (errors if net == "facebook" else warnings).append(f"{net} : la légende révèle « {sp} » (réponse, verdict ou première place)")
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
    if c.get("charte") == "v7":
        # human tone (Laurent, 20/11/2026): hook style in rotation, no jargon on the cover
        hs = c.get("hook_style")
        if hs not in HOOK_STYLES:
            errors.append(f"hook_style « {hs} » absent ou inconnu ({', '.join(sorted(HOOK_STYLES))})")
        else:
            for other in sorted(pathlib.Path(path).parent.glob("*.json")):
                if other.resolve() == pathlib.Path(path).resolve():
                    continue
                try:
                    o = json.load(open(other, encoding="utf-8"))
                except Exception:
                    continue
                if o.get("hook_style") == hs:
                    errors.append(f"hook_style « {hs} » déjà utilisé cette semaine ({other.name}) : varier les accroches")
        cov_txt = norm(" ".join(str(cover.get(k) or "") for k in ("title", "subtitle", "number"))).lower()
        for w in JARGON:
            if re.search(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", cov_txt):
                errors.append(f"jargon « {w} » sur la couverture : parler de la situation, expliquer le mot en slide 2")
        s2 = norm(str(slides[1].get("title") or "")).lower() if len(slides) > 1 else ""
        for w in JARGON:
            if re.search(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", s2):
                warnings.append(f"jargon « {w} » dans le titre de la slide 2 : l'expliquer en mots simples sur la slide")
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
