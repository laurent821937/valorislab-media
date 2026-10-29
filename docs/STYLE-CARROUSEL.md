# Charte carrousel VALORISLAB v4 (référence visuelle de Laurent, 29/10/2026)

Remplace la charte v3 pour toute nouvelle génération. Modèle à reproduire : `kit/assets/references/carrousel-v4/slide-01.jpg` à `slide-09.jpg` (carrousel « 6 choses sur ton argent que ta banque ne met pas en avant »). En cas de doute, ces 9 images font foi.

## Ambiance générale
- Éditorial premium, sobre, noir et or. Beaucoup d'espace vide, aucun élément décoratif superflu (pas de bokeh chargé, pas d'icônes, pas d'émoji, pas de cadre doré épais).
- Fond : noir presque pur `#0A0A0B`, avec un halo chaud très léger (brun doré `#231E18` à 10-20 % d'opacité) derrière le titre ou le chiffre clé. Jamais de dégradé visible ni de texture.
- Typographie unique : **Plus Jakarta Sans** (géométrique, sans empattement). Titres en gras serré (interlettrage légèrement négatif), corps en regular.
- Format 1080×1350 (4:5). Marges latérales 72 px. Texte aligné à gauche, jamais centré (sauf la maquette du guide en slide finale).

## Couleurs
| Rôle | Couleur |
|---|---|
| Fond | `#0A0A0B` |
| Titre (partie blanche), chiffres en gras dans le corps | blanc cassé `#F4EFE6` |
| Mots d'accent du titre, grands chiffres | dégradé or `#E8D3A0` → `#BD9756` (haut-gauche vers bas-droite) |
| Corps de texte | gris chaud `#B8B2A8` |
| Surtitres, « Source », compteur actif, « Glisse » | or mat `#C9A96E` |
| Ligne de source, url | gris `#8A857D` |
| Cartes | fond `#15130F`, bordure 1 px `#2A251D`, coins arrondis 22 px |
| Bouton CTA | dégradé or `#E7D5A7` → `#BA9755`, texte noir `#141210` |

Crypto : même charte (pas de bleu électrique en v4, sauf demande contraire de Laurent).

## Éléments fixes de chaque slide (gabarit)
1. **En-tête de marque, en haut à gauche** (x 72, y 56, environ 246 × 54 px) : emblème rond + « VALORISLAB » (blanc, capitales espacées) + « FINANCE BELGIQUE » (or mat, plus petit). **Jamais dessiné par l'IA** : superposé ensuite avec `kit/assets/header-brand.png` (voir RUNBOOK). Zone à laisser vide dans l'image générée.
2. **Compteur en haut à droite** : « 02 / 9 » (numéro en or mat gras, « / 9 » en gris), aligné à droite sur la marge de 72 px, à la hauteur de l'en-tête.
3. **Pied de page** : « valorislab.be » en gris à gauche (y ≈ 1275) ; à droite « Glisse » en or mat + cercle fin (48 px, bordure 1,5 px gris clair) contenant une flèche →. Dernière slide : la mention « Contenu éducatif, pas un conseil financier. » remplace « Glisse ».
4. **Barre de progression** tout en bas (y ≈ 1320, de x 72 à x 1008, 3 px) : piste gris très sombre `#1A1A1C`, partie remplie en or proportionnelle au rang de la slide (slide k/n = k/n de la largeur). Dernière slide : barre entièrement or.

## Types de slides
- **Couverture (cover)** : photo photoréaliste du protagoniste (scène du catalogue `kit/assets/scenes/`) sur les 60 % supérieurs, fondue dans le noir vers le bas. En bas : surtitre (trait or 40 px + texte or mat en capitales très espacées, ex. « VERSION BELGIQUE »), titre géant sur 3 lignes maximum (≈ 76 px, blanc, fin du titre en or : « ne met pas en avant. »), sous-titre d'une ligne en gris clair (« Rien d'illégal. Juste rarement expliqué au guichet. »). Le texte n'est jamais posé sur le visage.
- **Point numéroté (point)** : pastille arrondie contour fin (≈ 92 × 56 px) avec le numéro « 01 » en or mat, puis titre sur 2-3 lignes (≈ 60 px, début blanc, fin en or), puis contenu. Le contenu varie selon le point :
  - **chiffre géant** : valeur en or dégradé (≈ 150-190 px, ex. « 92 » + « milliards € » en blanc ≈ 60 px, ou « 97 % », « 249,90 € »), légende d'une ligne en dessous en blanc cassé ;
  - **barre partagée** (comparaison de deux composantes) : barre arrondie pleine largeur coupée en deux, partie gauche sombre avec bordure, partie droite en dégradé or ; valeur en gras + petite légende dans chaque partie ;
  - **cartes chiffrées** : 2 cartes côte à côte (la première avec un léger reflet or), puis une carte pleine largeur pour la phrase de comparaison ;
  - **encadré liste** : carte avec surtitre or en capitales espacées (« AVANT DE SIGNER, DEMANDE ») et 3 lignes précédées de « → ».
  Puis 1 à 2 paragraphes courts en gris chaud (≈ 30 px), les mots clés en gras blanc. Enfin la ligne de source : « **Source** · Organisme (date) » en petit (≈ 18 px), « Source » en or mat, le reste en gris.
- **Récapitulatif (list)** : surtitre « —— CE QU'IL FAUT RETENIR », titre (« Ton plan : 4 vérifications cette semaine. »), filet fin, puis 4 lignes séparées par des filets : cercle fin numéroté « 01 » (or mat), titre de l'action en blanc (≈ 30 px), sous-ligne grise.
- **Dernière slide (cta)** : surtitre « —— POUR ALLER PLUS LOIN », titre (« Évite les 20 erreurs de débutant. »), sous-titre gris, maquette du guide PDF au centre (couverture noire « 20 erreurs de débutant » entourée de deux pages claires inclinées), bouton or arrondi « Lien en bio → » à gauche, à côté « Enregistre ce post pour le retrouver. » en gris clair.

## Structure et densité
- Carrousel : couverture → 4 à 6 points numérotés → récapitulatif → CTA. 9 slides au maximum, 7 recommandé tant que le scénario Make limite `slide_index` à 8 et le plafond à 10 générations par contenu.
- Titre de point ≤ 60 caractères, 1 à 2 segments en or (toujours la fin de la phrase). Corps ≤ 2 paragraphes de ≤ 140 caractères chacun. Chaque point de fond porte une source datée.
- Contenu essentiel entre y 150 et y 1150 et à au moins 100 px du bord droit entre y 700 et y 1215 (boutons TikTok). Seuls le pied de page et la barre de progression vont plus bas (éléments accessoires, ils peuvent être recouverts par la légende TikTok).
- Protagoniste : toujours sur la couverture (photo de scène). Le modèle de référence n'a aucune pose dans les slides de fond : poses facultatives, 0 à 2 par carrousel, seulement sur un point sans chiffre géant, jamais deux fois la même.

## Bloc STYLE à placer au début de chaque `image_prompt`
```
STYLE : slide de carrousel Instagram 1080×1350, éditorial premium noir et or. Fond noir uni #0A0A0B avec un très léger halo brun doré derrière le titre. Typographie unique Plus Jakarta Sans, texte aligné à gauche, marges de 72 px. Titre en gras serré blanc cassé #F4EFE6 dont la fin est en dégradé or #E8D3A0→#BD9756. Corps en gris chaud #B8B2A8, mots clés en gras blanc. Grands chiffres en dégradé or. Cartes sombres #15130F à bordure fine et coins arrondis. Aucune icône, aucun émoji, aucun motif décoratif. En haut à droite : compteur « {k} / {n} » (numéro en or, « / {n} » en gris). En bas à gauche : « valorislab.be » en gris ; en bas à droite : « Glisse » en or et une flèche → dans un cercle fin. Tout en bas : fine barre de progression or remplie à {k}/{n} de la largeur.
ZONE RÉSERVÉE : laisser entièrement vide le coin supérieur gauche (de x 0 à x 360, de y 0 à y 130) : ni texte, ni logo, ni élément graphique. Le logo est ajouté ensuite.
```
Remplacer `{k}` et `{n}` par le rang de la slide et le nombre total. Pour la dernière slide, remplacer « Glisse » et sa flèche par « Contenu éducatif, pas un conseil financier. » et dire « barre de progression entièrement or ».
