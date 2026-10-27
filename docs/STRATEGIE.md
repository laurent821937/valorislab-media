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

## Format visuel (charte VALORISLAB, mise à jour du 27/10/2026)
- Carrousel de 6 à 8 slides, gabarits du kit (`kit/templates/slide.html.j2`). Style premium noir et or : fond noir chaud, typographie moderne **Plus Jakarta Sans** (Cormorant Garamond abandonnée), mots d'accent en dégradé or. Pour la Crypto, accent bleu électrique (comme la Crypto Academy) ; le logo reste toujours or.
- Logo officiel (emblème + « VALORISLAB ») en en-tête de chaque slide, barre de progression et compteur, signature « Laurent, fondateur de VALORISLAB » avec avatar du protagoniste en pied de slide.
- **Protagoniste** (personnage illustré noir et blanc de Laurent) détouré sur la couverture. Champ `character` du contenu : `34` (buste trois-quarts, sérieux), `hoodie` (en pied, sweat), `polo` (en pied, polo), `face` (visage). Par défaut : erreur → `34`, mécanisme → `hoodie`, Belgique → `polo`. Varier d'une semaine à l'autre.
- Instagram + Facebook : 1080×1350 (4:5). TikTok : 1080×1920 (9:16, mode photo, zone de sécurité respectée).
- Structure type : `cover` (accroche + protagoniste) → 3 à 5 slides de fond (`point`, `stat`, `compare`, `list`) → `cta` (couverture du guide gratuit + bouton).
- Limites de texte par slide : titre ≤ 60 caractères, corps ≤ 280 caractères, liste ≤ 4 éléments de ≤ 95 caractères, valeur chiffrée ≤ 10 caractères. Le moteur de rendu réduit le texte si besoin et signale tout débordement : raccourcir, ne jamais forcer.
- Balises : `*mot*` = accent (1 à 2 mots par titre), `**mot**` = gras.

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
- Pas de visage généré par IA, pas de logo de marque tierce, pas de capture d'écran d'un produit tiers.
- Les sources sont listées dans le fichier de contenu (`sources`) et mentionnées en légende quand un chiffre externe est cité.
- Si un contenu ne passe pas ces règles → le remplacer par un autre sujet de la banque ci-dessous.

## Originalité et doublons
- Ne jamais reprendre un sujet présent dans `state/history.json` au cours des 120 derniers jours (même sujet, même angle ou même accroche).
- Comparer aussi avec les 60 derniers posts Buffer (publiés, programmés, brouillons) sur les 3 réseaux, y compris les posts publiés à la main.
- Un même sujet peut revenir après 120 jours seulement avec un angle et des exemples nouveaux.

## Banque de sujets (point de départ, à enrichir)
**Mécanisme chiffré** : coût de 1,8 % de frais par an sur 30 ans (fonds vs ETF) · perdre 50 % exige +100 % pour revenir · rendement nominal vs réel · le coût d'attendre 5 ans pour commencer · intérêts composés à l'envers (crédit à la consommation) · investissement programmé vs investissement en une fois (illustration hypothétique) · diversification : 1 titre vs 500 · volatilité ≠ risque de perte définitive · frais d'entrée et de sortie · rééquilibrer un portefeuille · capitalisant vs distribuant (principe) · épargne de précaution : combien de mois ?
**Belgique pratique** : compte d'épargne réglementé (taux de base + prime de fidélité, exonération) · précompte mobilier et exonération des dividendes · TOB : comment elle s'applique · épargne-pension (3e pilier) · garantie des dépôts 100 000 € · déclarer un compte-titres étranger au Point de contact central de la BNB · liste d'avertissements de la FSMA · bons d'État · taxe sur les comptes-titres (seuil) · fiscalité crypto en Belgique : ce qui est flou et ce qui est clair · comparer les frais de courtage
**Erreurs et arnaques** : faux support crypto · empoisonnement d'adresse (address poisoning) · pump & dump · faux courtiers clonés (FSMA) · romance scam crypto · trading à effet de levier · tout miser sur une seule crypto · investir sans épargne de précaution · vendre dans la panique · acheter ce dont tout le monde parle (FOMO) · ignorer les frais · copier un influenceur · confondre spéculer et investir
