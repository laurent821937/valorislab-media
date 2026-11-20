# Refonte charte v6 et run en brouillons (20/11/2026, demande de Laurent)

**Résultat : 9 nouveaux brouillons Buffer en charte v6 (3 contenus × 3 réseaux), aucun post programmé. 8 des 9 posts W48 (charte v5) repassés en brouillon ; le 9e (TikTok crédit Black Friday) était déjà « sent ».**

## Appliqué
- Brief enregistré : `docs/brief-refonte-carrousels-2026-11.md`.
- `docs/STRATEGIE.md` : ligne éditoriale remplacée par les sections 2 (8 formats), 3 (sujets), 6 (dernière slide, légende) et 7 (score) ; mesure (section 8) ajoutée.
- `docs/STYLE-CARROUSEL.md` : charte v6 (sections 4 et 5), v5 en archive. `docs/RUNBOOK.md` aligné.
- Kit : gabarit `kit/templates/slide-v6.html.j2`, `render_v6()` dans `kit/render.py` (contrôles du brief bloquants : titre ≤ 12 mots, ≥ 110 px, ≤ 4 lignes, sous-titre ≤ 6 mots, 5 à 7 slides, raison de swiper, slide du guide en dernier), `kit/qa.py` (5 à 7 slides v6, contraste mesuré du bon côté du texte). Les contenus v5 se rendent comme avant.
- `kit/RENDER_VERSION` et `kit/VERSION` : 2026-11-20.1.
- Nouveaux fichiers d'état : `state/guide-erreurs.json` (à remplir), `state/series.json` (numéros des dossiers et épisodes).

## Brouillons v6 (aucune date, aucun tag)
| Contenu | Format | Fond / visuel | Score | Brouillons (IG / TikTok / FB) |
|---|---|---|---|---|
| Petites dépenses : laquelle coûte 3 000 € en 10 ans ? | F1 boucle ouverte (budget) | sombre / visage | 82 | 6b003c1a… / 6b003c24… / 6b003c29… |
| « Une action à 5 € monte plus facilement » | F2 tribunal du mythe (bourse) | clair / tampon | 80 | 6b003c34… / 6b003c3d… / 6b003c42… |
| Message suspect, arnaque crypto | F7 message suspect (arnaque) | sombre / visage + bulle | 81 | 6b003c4c… / 6b003c56… / 6b003c5b… |

Contrôles : seo_check, render, validate (URL publique incluse), qa : 0 erreur, 0 avertissement. Visuels (commit 27900fa, branche claude/eloquent-faraday-bua232) :
- https://raw.githubusercontent.com/laurent821937/valorislab-media/27900fa5b5b4ae32d6922d8910e77b3b70dae720/media/2026/11/2026-11-23-petites-depenses-10-ans/
- https://raw.githubusercontent.com/laurent821937/valorislab-media/27900fa5b5b4ae32d6922d8910e77b3b70dae720/media/2026/11/2026-11-23-mythe-action-5-euros/
- https://raw.githubusercontent.com/laurent821937/valorislab-media/27900fa5b5b4ae32d6922d8910e77b3b70dae720/media/2026/11/2026-11-23-message-suspect-crypto/
Sources : FSMA (fausses plateformes de trading crypto, « Peut-on devenir riche en quelques clics ? »). Calculs en Python, montants fictifs.

## Posts W48 (charte v5)
- Repassés en brouillon (dates et tag conservés, rien ne part) : IG 24/11, 25/11, 26/11 ; FB 25/11, 26/11, 27/11 ; TikTok 28/11, 29/11.
- **TikTok crédit Black Friday (6b000b16…)** : statut « sent », `sharedNow` le 20/11/2026 à 10:26 (rappel publié depuis Buffer). Non modifiable : à vérifier par Laurent dans TikTok.
- Non touchés : les 2 TikTok W47 (TOB 21/11, arnaque sentimentale 22/11).

## À faire par Laurent
1. Valider le rendu des 3 carrousels (brouillons Buffer ou liens ci-dessus).
2. Donner la liste numérotée des 20 erreurs du guide (`state/guide-erreurs.json`) : sans elle, la dernière slide dit « l'une des 20 erreurs » (valorislab.be inaccessible depuis la session).
3. Après validation : fusion de la branche dans `main` (sinon la routine du prochain run applique encore la v5) et choix des dates de la semaine 48.

## Mise à jour du 20/11 (soir) : finition premium et couvertures IA du protagoniste (demande de Laurent)
- Gabarit v6 premium : titres Playfair Display, filets or fins, cadre intérieur, cartes sobres, maquette du guide sur la dernière slide.
- Couvertures pleine image générées par IA (Make 8230680) : **2 avec le protagoniste à partir de sa photo de référence** (`kit/assets/protagonist/`), F1 cuisine le soir, F7 message suspect la nuit ; 1 nature morte (maillet de juge sur lin ivoire) pour F2. Budget IA : 3 générations, 30/40 en novembre.
- Make 8230680 : nouvelle entrée facultative `reference_url` → branche OpenAI « Edit images » (même modèle, format, qualité). Sans référence, le scénario fonctionne comme avant. Sauvegarde : `state/backups/make-8230680-blueprint-2026-11-20-avant-reference.json`.
- Contrôles : render, validate (URL publique), qa, seo_check : 0 erreur, 0 avertissement. `decor_check.py` non applicable aux photos avec visage (relecture visuelle faite : aucun texte, logo ni objet doré).
- Buffer : les 9 brouillons v6 mis à jour avec les nouveaux visuels (commit 8ba855b) ; **8 anciens posts v5 de W48 supprimés** (ils étaient en brouillon) ; TikTok crédit Black Friday déjà « sent » (non supprimé) ; 2 TikTok W47 conservés.
- Visuels :
  - https://raw.githubusercontent.com/laurent821937/valorislab-media/8ba855bb7ffa0f407675ed43305322de100c652a/media/2026/11/2026-11-23-petites-depenses-10-ans/
  - https://raw.githubusercontent.com/laurent821937/valorislab-media/8ba855bb7ffa0f407675ed43305322de100c652a/media/2026/11/2026-11-23-mythe-action-5-euros/
  - https://raw.githubusercontent.com/laurent821937/valorislab-media/8ba855bb7ffa0f407675ed43305322de100c652a/media/2026/11/2026-11-23-message-suspect-crypto/
