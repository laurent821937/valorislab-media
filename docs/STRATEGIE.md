# Stratégie éditoriale VALORISLAB (validée par Laurent le 27/10/2026)

Ce document est la référence pour toute génération automatique de contenu.
Toute modification de la stratégie passe par Laurent.

## Positionnement
- Plateforme éducative belge francophone : Bourse, ETF, Crypto, finances personnelles.
- Cible : débutants et intermédiaires en Belgique (FR), 20–45 ans, qui veulent comprendre avant d'agir.
- Promesse : « comprendre avant d'agir ». Ton direct, pédagogique, chiffré, sans hype ni promesse de gain.
- Tutoiement. Phrases courtes. Pas de jargon non expliqué. Zéro émoji dans les visuels ; 0 à 2 émojis maximum dans une légende (de préférence aucun).
- Offre : guide gratuit « Les 20 erreurs du débutant en Bourse et en Crypto » (valorislab.be, lien en bio), puis formations Bourse et Crypto à 149 €. Le pack IA n'est plus mis en avant.

## Rythme et mix (3 contenus par semaine, chacun décliné sur Facebook, Instagram, TikTok)
1. **Mécanisme chiffré** : intérêts composés, inflation, frais, ETF, diversification, volatilité, coût d'attendre…
2. **Belgique pratique** : banques, épargne réglementée, précompte mobilier, TOB, épargne-pension, garantie des dépôts, déclaration des comptes étrangers, FSMA…
3. **Erreur ou arnaque à éviter** (Bourse ou Crypto), avec un appel à l'action vers le guide gratuit.

Alternance des thèmes : au moins 1 contenu Crypto toutes les 2 semaines, et au moins 1 contenu Bourse/ETF par semaine.

## Format visuel
**Charte v4 (29/10/2026) : `docs/STYLE-CARROUSEL.md` et les 9 slides de référence `kit/assets/references/carrousel-v4/`, rendue par le kit (`kit/render.py`).** Elle prime sur la charte v3 ci-dessous, qui n'est gardée qu'en archive pour les règles non contredites (format 4:5, zones TikTok). **8 slides au maximum.**

### Charte v3 (27/10/2026, archive)
- **Un seul format : 1080×1350 (4:5), pour Instagram, Facebook ET TikTok** (choix de Laurent : en 9:16, TikTok masquait une partie de l'image). TikTok affiche la photo 4:5 entière ; sa légende recouvre les 160 px du bas et ses boutons le bord droit : aucun texte à ces endroits (vérifié par `qa.py`).
- Carrousel de 6 à 8 slides, gabarit `kit/templates/slide.html.j2`. Style premium noir et or : fond noir chaud, lumière dorée et bokeh, typographie **Plus Jakarta Sans**, titres blancs, mots d'accent en dégradé or (bleu électrique pour la Crypto). Logo officiel complet centré en haut, compteur « 01 / 07 » avec barre de progression et flèche en bas. Pour le pilier Belgique, filet aux couleurs du drapeau belge sous le surtitre.
- **Couverture et dernière slide = photo premium** (rendus photoréalistes du protagoniste fournis par Laurent, `kit/assets/scenes/`, catalogue `scenes.json`) : la photo occupe le haut ou le bas de la slide et se fond dans le noir, le texte est posé sur la partie sombre. Champ `scene` de la slide `cover` (et de la `cta`) : choisir dans le catalogue la scène dont l'ambiance (`mood`) colle au sujet, et ne pas réutiliser la scène des 2 dernières couvertures (voir `history.json`). Sans champ `scene`, le moteur fait tourner les scènes automatiquement (jamais deux fois la même dans une semaine). La dernière slide utilise la scène `role: "cta"` (portrait de Laurent).
- **Couverture courte** : titre ≤ 55 caractères (3 lignes maximum), sous-titre ≤ 90 caractères. Si la place manque, le moteur supprime le sous-titre plutôt que de réduire le titre.
- **Poses du protagoniste dans les slides de fond** (`kit/assets/pose-*.webp`, illustrations de Laurent détourées, teinte chaude et halo doré) : champ `pose` sur une slide `point`, `stat`, `compare`, `list` ou `cta` sans scène, ou `"none"`. Poses : `reflexion` (comprendre, principe), `pointe` (expliquer, montrer un chiffre), `graphique-hausse` (croissance, bonne nouvelle), `checklist` (liste, règles), `pouce` (bon réflexe), `stress-tablette` (mauvaise surprise, frais), `stress-baisse` (perte, krach), `choc-polo` (erreur grave), `doute-telephone` (message suspect), `doute-telephone-hoodie` (arnaque crypto). Jamais deux fois la même pose dans un carrousel ; 2 à 3 slides avec pose maximum.
- Une slide avec pose a une colonne de texte étroite (520 px) : titre ≤ 30 caractères, corps ≤ 160 caractères. Si le texte est plus long ou touche le protagoniste, le moteur retire la pose automatiquement (le rapport le signale) : écrire court pour la garder.
- Structure type : `cover` (scène + accroche) → 3 à 5 slides de fond (`point`, `stat`, `compare`, `list`) → `cta` (scène portrait + bouton).
- Limites de texte (slides sans pose) : titre ≤ 60 caractères, corps ≤ 260 caractères, liste ≤ 4 éléments de ≤ 90 caractères, valeur chiffrée ≤ 10 caractères. Le moteur réduit le texte si besoin et signale tout débordement : raccourcir, ne jamais forcer.
- Balises : `*mot*` = accent (1 à 2 mots par titre), `**mot**` = gras.
- Le champ `character` des anciens contenus est ignoré.

## Structure des légendes (style actuel de Laurent)
1. Accroche en 1 ligne (question, contraste chiffré ou citation).
2. 2 à 4 phrases d'explication.
3. « À retenir : » + 3 puces ( • ).
4. Une question qui appelle un commentaire.
5. Un appel à enregistrer ou à partager.
6. CTA guide : Instagram et TikTok → « mon guide gratuit, lien en bio » ; Facebook → lien direct https://www.valorislab.be
7. « Contenu éducatif, pas un conseil financier. » (+ hypothèses chiffrées si un calcul est présenté, + « Performances passées… » si des performances historiques sont citées).
8. 5 hashtags, dont toujours #belgique.

Limites : Instagram ≤ 2 200 caractères ; titre TikTok ≤ 90 caractères, description TikTok ≤ 500 caractères ; Facebook sans limite pratique (rester ≤ 1 500).
Texte alternatif (alt) obligatoire pour chaque visuel.

## Règles de fiabilité (non négociables)
- **Tout calcul est fait en Python** dans le run, jamais de tête. Hypothèses affichées (taux, durée, « avant frais et impôts », « rendement non garanti »).
- **Données belges ou réglementaires** (taux, plafonds, montants d'exonération, fiscalité) : vérifier sur une source officielle de l'année en cours (SPF Finances, FSMA, BNB, Wikifin, FEBELFIN). Si une donnée ne peut pas être vérifiée → changer d'angle ; ne jamais publier un chiffre douteux.
- Pas de recommandation d'achat ou de vente d'un titre, d'une crypto ou d'un produit nommé ; pas de prédiction de prix ; pas de promesse de rendement ; pas de « rendement garanti ».
- **Images générées par IA (décision de Laurent, 29/10/2026)** : les slides sont rendues par le kit (texte et chiffres exacts), jamais générées par IA. L'IA (OpenAI via le scénario Make 8230680) ne sert qu'à créer, si nécessaire, un décor de couverture sans personne ni texte, dans les budgets des plans gratuits (`RUNBOOK.md` : 2 générations par exécution, 8 par mois). Pas de logo de marque tierce, pas de capture d'écran d'un produit tiers.
- Les sources sont listées dans le fichier de contenu (`sources`) et mentionnées en légende quand un chiffre externe est cité.
- Si un contenu ne passe pas ces règles → le remplacer par un autre sujet de la banque ci-dessous.

## Score de viralité (avant publication, obligatoire)
Chaque contenu reçoit une note sur 100, calculée et justifiée dans le champ `virality` du fichier de contenu :
| Critère | Poids | Ce qui donne 10/10 |
|---|---|---|
| Accroche (couverture + 1re ligne) | 20 | Arrête le scroll en moins d'une seconde : chiffre choc, contraste, citation ou question ; 12 mots maximum |
| Boucle de curiosité | 15 | La couverture promet une réponse qu'on n'obtient qu'en glissant |
| Valeur à enregistrer | 15 | Calcul, checklist ou règles qu'on veut garder (déclenche les enregistrements) |
| Partage | 10 | Donne une raison d'envoyer le post à quelqu'un (protéger un proche, débutant, injustice) |
| Ancrage belge | 10 | Exemple, règle ou chiffre propre à la Belgique |
| Clarté débutant | 10 | Une idée par slide, aucun jargon non expliqué |
| Rétention du carrousel | 10 | Chaque slide donne envie de la suivante ; la dernière récompense et appelle à l'action |
| Actualité / saison | 10 | Lié à un moment (déclaration fiscale, fin d'année, krach, arnaque du moment…) |
- Note ≥ 70 : publiable. Entre 55 et 69 : retravailler l'accroche (écrire 5 variantes, garder la meilleure) et la couverture, puis renoter. Sous 55 : changer de sujet.
- Les enseignements de l'analyse de performance (ci-dessous) priment sur ces poids : ce qui marche chez l'audience VALORISLAB l'emporte sur la théorie.

## Analyse de performance (après publication, à chaque exécution)
- Récupérer les statistiques Buffer des posts publiés depuis 28 jours, posts natifs compris (vues, portée, taux d'engagement, enregistrements, partages, commentaires ; temps de visionnage pour les vidéos). Ignorer les posts de moins de 48 h (statistiques incomplètes).
- Comparer chaque post à la médiane de son réseau. Identifier le top 3 et le flop 3, puis ce qui les distingue : pilier, thème, type d'accroche (chiffre, question, citation, contraste), pose du protagoniste, jour et heure, carrousel automatique ou vidéo native.
- Appliquer les enseignements à la semaine suivante : favoriser le pilier et le type d'accroche gagnants, mais garder au moins 1 contenu sur 3 en exploration pour continuer à apprendre.
- Repère connu (oct. 2026) : la vidéo explicative animée sur l'inflation a dépassé 70 000 vues sur TikTok ; les vidéos natives tournent autour de 150 à 300 vues. Les explications chiffrées et visuelles pour débutants sont le meilleur filon.

## Sons et musique
- Les publications automatiques via Buffer ne peuvent pas ajouter les sons proposés par Instagram ou TikTok (limite des API). Les carrousels partent donc sans musique.
- `state/config.json` → `buffer.schedulingType` : passer un réseau en `notification` fait publier ce réseau par rappel Buffer. Laurent reçoit une notification à l'heure prévue et publie depuis l'application en choisissant un son tendance (environ 1 minute par post).

## Originalité et doublons
- Ne jamais reprendre un sujet présent dans `state/history.json` au cours des 120 derniers jours (même sujet, même angle ou même accroche).
- Comparer aussi avec les 60 derniers posts Buffer (publiés, programmés, brouillons) sur les 3 réseaux, y compris les posts publiés à la main.
- Un même sujet peut revenir après 120 jours seulement avec un angle et des exemples nouveaux.

### Angles et exemples chiffrés déjà publiés (ne pas réutiliser avant 120 jours)
Un même exemple chiffré, une même comparaison ou une même statistique qu'un post récent est un doublon, même si le titre change.
- 26/10/2026 (carrousel banques belges) : frais de fonds 1,5 % vs ETF 0,2 % sur 10 000 € pendant 30 ans à 6 % ; 97 % des fonds actions Europe sous leur indice sur 10 ans (SPIVA) ; compte à vue à 0 % ; prime de fidélité après 12 mois ; exonération des dividendes (833 €) ; conseil bancaire non indépendant.
- 27/10/2026 : intérêts composés (centime qui double 30 jours, Emma vs Lucas, règle de 72) ; 100 € par mois jusqu'à 65 ans.
- 21 et 23/10/2026 : inflation (100 € de 2002 = 58 €, S&P 500 et or depuis 2002).

### Sujets rejetés (ne jamais reprogrammer)
- `2026-11-02-frais-1-8-pourcent` (frais 1,8 % vs 0,2 % sur 30 ans) : doublon du carrousel banques belges du 26/10/2026.

### Contenus supprimés avant publication (disponibles, à reprogrammer en priorité)
- `2026-11-02-perdre-50-pour-cent` et `2026-11-02-faux-support-crypto` : programmés le 27/10/2026 puis supprimés de Buffer par Laurent avant publication (27/10, 19 h). Jamais publiés : ils ne comptent pas comme doublons.

## Sources officielles belges (pilier « Belgique pratique »)
FSMA (fsma.be), Wikifin (wikifin.be), SPF Finances (finances.belgium.be), Banque nationale (nbb.be), Statbel (statbel.fgov.be), SPF Économie (economie.fgov.be), Febelfin (febelfin.be). Utiliser WebFetch sur ces sites ; si l'accès est bloqué, WebSearch avec `allowed_domains` limité à ces domaines. Si aucun chiffre n'est vérifiable, garder le pilier Belgique avec un sujet sans chiffre volatil (obligation, procédure, mécanisme de protection : déclaration d'un compte étranger au Point de contact central de la BNB, liste d'avertissements de la FSMA, garantie des dépôts…), plutôt que de le remplacer par un autre pilier.

## Banque de sujets (point de départ, à enrichir)
**Mécanisme chiffré** : coût de 1,8 % de frais par an sur 30 ans (fonds vs ETF) · perdre 50 % exige +100 % pour revenir · rendement nominal vs réel · le coût d'attendre 5 ans pour commencer · intérêts composés à l'envers (crédit à la consommation) · investissement programmé vs investissement en une fois (illustration hypothétique) · diversification : 1 titre vs 500 · volatilité ≠ risque de perte définitive · frais d'entrée et de sortie · rééquilibrer un portefeuille · capitalisant vs distribuant (principe) · épargne de précaution : combien de mois ?
**Belgique pratique** : compte d'épargne réglementé (taux de base + prime de fidélité, exonération) · précompte mobilier et exonération des dividendes · TOB : comment elle s'applique · épargne-pension (3e pilier) · garantie des dépôts 100 000 € · déclarer un compte-titres étranger au Point de contact central de la BNB · liste d'avertissements de la FSMA · bons d'État · taxe sur les comptes-titres (seuil) · fiscalité crypto en Belgique : ce qui est flou et ce qui est clair · comparer les frais de courtage
**Erreurs et arnaques** : faux support crypto · empoisonnement d'adresse (address poisoning) · pump & dump · faux courtiers clonés (FSMA) · romance scam crypto · trading à effet de levier · tout miser sur une seule crypto · investir sans épargne de précaution · vendre dans la panique · acheter ce dont tout le monde parle (FOMO) · ignorer les frais · copier un influenceur · confondre spéculer et investir
