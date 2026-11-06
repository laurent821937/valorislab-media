# Charte carrousel VALORISLAB v5 (référence visuelle de Laurent, 02/11/2026)

Remplace la charte v4 (archivée sur la branche `sauvegarde-charte-v4`). **Rendu : `kit/render.py` + `kit/templates/slide.html.j2`**, jamais d'image IA pour les slides. Modèle : `kit/assets/references/carrousel-v5/slide-01.jpg` à `slide-05.jpg`.

**Règle de Laurent : ces 5 images sont une référence de STYLE uniquement** (format, design, couleurs, structure, qualité). Leur sujet (Apple, résultats trimestriels), leurs textes et leurs chiffres ne sont jamais réutilisés. Tout le reste (sujets, textes, chiffres, décor) est produit par la routine. Les défauts des images de référence ne sont pas reproduits : chevauchements du guide, du bouton et du pied de page (slide 5), filet vertical qui traverse le texte (slide 3), carte collée au filet du pied de page (slide 4).

## Format et grille
- 1080 × 1350 (4:5), mêmes images pour Instagram et TikTok ; image unique `fb-01.jpg` (même charte) pour Facebook.
- Fond noir `#0A0A0B`, halo chaud brun très doux, **grille fine** (traits blancs à 5 % d'opacité tous les 220 px, à partir de x 96 et y 180), visible aussi sur la photo de couverture.
- Typographie unique **Inter**. Titres **en majuscules**, gras, interlignage serré. Texte aligné à gauche, marges de 96 px.
- Zones : en-tête à y 214 ; contenu de y 290 à y 1060 ; filet or du pied de page à y 1084 ; **rien sous le pied de page** (zone de la légende TikTok).

## Couleurs
| Rôle | Couleur |
|---|---|
| Fond | `#0A0A0B` |
| Titre (partie blanche) | `#F4F0E8` |
| Partie or du titre, chiffres clés | `#E5C07B` (aplat, pas de dégradé) |
| Surtitre, libellés de carte, numéros | `#D4AF6A` |
| Corps de texte | `#D6D1C8` ; seconde ligne des étapes `#BDB7AD` |
| Pied de page, compteur, notes | `#A8A29A` |
| Cartes | fond `#151516`, bordure or `#B8975A` 1,5 px, coins arrondis 18 à 22 px |
| Bouton | `#E3BE78`, texte `#1A1612`, majuscules |

## Éléments fixes (toutes les slides)
1. En-tête : emblème rond + « VALORISLAB » (capitales espacées) + « FINANCE BELGIQUE » (or), en haut à gauche.
2. Compteur « 01 / 05 » en gris, en haut à droite.
3. Surtitre : trait or + texte or en majuscules (`kicker` de la slide ; couverture : thème · date, ex. « BOURSE · 02 NOVEMBRE 2026 »).
4. Pied de page : filet or, « valorislab.be » à gauche, « Contenu éducatif · Pas un conseil financier » à droite.

## Structure de référence (5 slides par défaut, 8 au maximum)
1. **Couverture (`cover`)** : surtitre thème · date, titre-accroche en majuscules (fin en or), sous-titre qui explique le « pourquoi » (`subtitle`), ligne or d'actualité facultative (`highlight`, ex. « X publie ses résultats aujourd'hui. »). Décor IA du sujet dans la partie basse, sous la grille.
2. **Le point essentiel (`compare` sans valeur)** : surtitre « Le point essentiel », titre (fin en or), une phrase d'explication (`body`), puis une carte à 2 colonnes : libellé or + texte (`left{label, note}`, `right{label, note}`).
3. **Exemple chiffré (`compare` avec valeurs)** : surtitre « Exemple fictif · pour comprendre » (ou « Exemple réel » avec source), titre, carte à 2 colonnes : libellé gris + grand chiffre (gauche or, droite blanc) + phrase de conclusion sous un filet (`caption`), puis une note grise (`note`, ex. « Chiffres illustratifs » ou la source).
4. **Méthode (`list`)** : surtitre « Ta méthode de débutant », titre, 4 étapes en cartes numérotées 01 à 04 ; chaque étape = 1re ligne blanche (`title`) + 2e ligne grise (`sub`).
5. **CTA (`cta`)** : surtitre « Pour aller plus loin », titre « 20 erreurs de débutant à éviter. », sous-titre « Bourse & Crypto · Guide gratuit », maquette du guide, bouton or « LIEN EN BIO → ».

Pour un sujet qui le demande, ajouter 1 à 3 slides du même type (`point`, `stat`, `compare`, `list`), sans dépasser 8.

## Limites de texte (lisibilité sur téléphone)
- Titre de couverture ≤ 55 caractères ; autres titres ≤ 60 caractères ; 1 segment en or, toujours la fin.
- `subtitle` / `body` ≤ 140 caractères ; texte de carte ≤ 35 caractères par colonne ; chiffre de carte ≤ 7 caractères.
- Étapes : `title` ≤ 32 caractères, `sub` ≤ 32 caractères.
- Le moteur réduit le texte si besoin et le signale : raccourcir plutôt que forcer.

## Décor de couverture (IA) : pureté, pas d'or
Règle de Laurent (06/11/2026) : l'or est réservé aux accents typographiques du kit (fin des titres, libellés, bouton). Le décor photo est épuré et neutre : noirs, gris anthracite, blanc cassé, lumière naturelle douce, objets sobres et mats liés au sujet, beaucoup d'espace vide. Jamais d'objets dorés, pièces, lingots, clés anciennes, coffres, bokeh ni lumière dorée. Le décor occupe la partie basse de la couverture (y 550 à 1350), sous la grille, et le kit le désature encore légèrement. Contrôle automatique : `kit/decor_check.py`. Prompt : `docs/RUNBOOK.md`, étape 5.
