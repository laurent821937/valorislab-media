# Génération des visuels par IA (Make + OpenAI + Cloudinary) — BROUILLON, non actif

Statut : non référencé par RUNBOOK.md. À activer seulement après test réussi du scénario Make « VALORISLAB - AI Visual Generator ».
Décision de Laurent (28/10/2026) : l'IA génère l'image complète de chaque slide, dans le style VALORISLAB. Cette décision remplace, une fois activée, la règle « aucune nouvelle image générée » de STRATEGIE.md.

## Prérequis
- Connecteur Make activé dans la session et dans la routine.
- Module « Upload Cloudinary » corrigé (3 erreurs sur la capture du 28/10).
- Fichier de la maquette du guide PDF « Les 20 erreurs du débutant en Bourse et en Crypto » (image haute définition) ajouté dans kit/assets/ : MANQUANT pour l'instant.
- Logo : kit/assets/logo-full.webp (déjà présent), à joindre en référence d'image.

## Contenu de chaque prompt (à construire par slide)
1. Style : charte v3 de STRATEGIE.md (fond noir chaud, lumière dorée, bokeh, titres blancs avec mots d'accent dorés, bleu électrique pour la Crypto, filet drapeau belge pour « Belgique pratique »).
2. Format : 1080×1350 (4:5), sans zone de texte sur les 160 px du bas ni sur le bord droit (zones TikTok).
3. Logo VALORISLAB complet centré en haut de chaque slide, compteur « 01 / 07 » en bas.
4. Texte exact de la slide, fourni mot pour mot dans le prompt, en français, sans rien ajouter.
5. Dernière slide (CTA) : maquette du PDF « Les 20 erreurs du débutant en Bourse et en Crypto », bouton doré « GUIDE GRATUIT – LIEN EN BIO », mention « Contenu éducatif, pas un conseil financier ».

## Contrôles obligatoires avant programmation (non négociables)
- Relecture visuelle de chaque slide : fautes, lettres déformées, chiffres exacts, logo fidèle. Une slide ratée est régénérée (3 essais maximum), sinon le contenu n'est pas programmé.
- Les chiffres restent calculés en Python et recopiés tels quels dans le prompt.
- Format JPEG 1080×1350 contrôlé par kit/validate.py, puis hébergement GitHub ou Cloudinary, vérifié en HTTP 200 image/jpeg.
- Plafond de coût : 10 images maximum par contenu, 30 par exécution.

## Repli
Si Make, OpenAI ou Cloudinary échoue, la routine utilise le rendu du kit (render.py) et le signale dans le rapport.
