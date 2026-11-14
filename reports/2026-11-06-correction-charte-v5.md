# Correction du 06/11/2026 : charte v5 rétablie, décors sans or

- Le run du 06/11 avait rétabli la charte v4 (prompt de la routine périmé). Charte v5 rétablie depuis `0f702d4`/`7a20553`, sans toucher aux contenus, décors ni à l'historique.
- Demande de Laurent : plus d'images trop dorées, pureté du style de référence. Nouveau prompt de décor (neutre, désaturé, aucun objet doré) et contrôle `kit/decor_check.py` (or ≤ 5 %, saturation ≤ 0,45). Les décors dorés existants mesurent 7 à 30 % d'or et 0,57 à 0,88 de saturation : tous refusés.
- 7 générations Make (1 test + 6 décors) : or 0 %, saturation 0,02 à 0,08. Budget IA : 21/40 en novembre.
- Contenus W46 re-rendus en v5 (commit `8a40d5d`), validate et qa sans erreur, URL publiques en HTTP 200.
- 9 posts Buffer mis à jour (images seulement ; texte, date, mode et tag inchangés, statut `scheduled` confirmé) :
  ETF (TikTok 09/11, Instagram 10/11, Facebook 11/11), garantie des dépôts (Instagram 11/11, Facebook 12/11, TikTok 14/11), faux courtier (Instagram 12/11, Facebook 13/11, TikTok 15/11).
- Non modifié : l'ancien post TikTok « faux support » du 08/11 (créé avant, hors de ce lot).

## 14/11/2026 : couverture plus claire
- Gabarit : décor visible en bas de la couverture (y 790 à 1350), ombre limitée au fondu du titre et au pied de page. Prompt de décor lumineux (testé : luminosité moyenne 117 contre 56 à 67, 0,2 % d'or).
- 9 posts W47 (16 au 22/11) mis à jour avec le nouveau gabarit et leurs décors existants (aucune génération), commit `e544e2c`.
- Règles ajoutées au RUNBOOK : accroche forte (titre 4 à 9 mots, 5 variantes, critère Accroche ≥ 16/20) et décor qui raconte le sujet au premier regard.
