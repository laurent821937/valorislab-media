# Retour en arrière (passage à la charte v4 du 29/10/2026)

Deux points de restauration existent :
- **Branche Git `sauvegarde-avant-charte-v4`** (commit `042a3b9`) : dépôt tel qu'il était avant la charte v4 (kit v3, slides générées par IA, ancienne procédure).
- **`state/backups/routine-caroussel-2026-10-29-avant-v4.md`** : texte intégral de la routine « Caroussel » (`trig_01RQZRgAfAGx1Qn5rjDHNRDb`) avant sa mise à jour, avec sa planification et son état (désactivée).

La branche **`sauvegarde-charte-v4`** garde l'état après la mise à jour, pour y revenir ensuite si besoin. Ne jamais supprimer ces deux branches.

## Procédure (à demander à Claude : « applique docs/RETOUR-ARRIERE.md »)
1. Désactiver la routine « Caroussel » (`update_trigger`, `enabled: false`).
2. Restaurer la procédure et le kit, sans toucher à `media/` ni à `content/` (les posts programmés pointent vers `media/`) :
   ```bash
   git fetch origin sauvegarde-avant-charte-v4
   git checkout origin/sauvegarde-avant-charte-v4 -- docs kit state/config.json
   git commit -m "Retour à l'état avant la charte v4" && git push origin HEAD:main
   ```
   Les nouveaux fichiers ajoutés depuis (références, maquette du guide, ce document) peuvent rester : ils ne sont plus lus.
3. Remettre le prompt d'origine de la routine (copie dans `state/backups/…`) avec `update_trigger` (`prompt`), et la laisser désactivée comme avant.
4. Ne pas modifier les posts déjà programmés dans Buffer : la vérification de l'étape 8 bis ne s'applique plus une fois l'ancien `kit/RENDER_VERSION` restauré.
