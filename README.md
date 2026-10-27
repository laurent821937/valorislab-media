# valorislab-media

Kit de publication automatique VALORISLAB (Facebook, Instagram, TikTok via Buffer).

- `docs/STRATEGIE.md` : ligne éditoriale validée (référence de toute génération).
- `docs/RUNBOOK.md` : procédure hebdomadaire suivie par la tâche planifiée Claude.
- `kit/` : gabarits de slides (HTML → JPEG via Playwright), rendu, validation, installation des polices.
- `content/` : contenus générés (JSON : slides + légendes + sources).
- `media/` : visuels publiés. URL publique permanente (liée au commit) :
  `https://raw.githubusercontent.com/laurent821937/valorislab-media/<SHA>/media/...`
- `state/` : configuration Buffer et historique des sujets (anti-doublons).
- `reports/` : rapport de chaque exécution.

Ne pas supprimer `media/` : les posts programmés pointent vers ces fichiers.
