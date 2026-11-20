# Charte carrousel VALORISLAB v6 (brief de Laurent du 20/11/2026)

Remplace la charte v5 pour tout nouveau contenu (`"charte": "v6"` dans le fichier de contenu). Source : sections 4 et 5 de `docs/brief-refonte-carrousels-2026-11.md`. **Rendu : `kit/render.py` + `kit/templates/slide-v6.html.j2`**, jamais d'image IA pour les slides. Les contenus v5 (sans champ `charte`) restent rendus avec `kit/templates/slide.html.j2` ; la charte v5 est archivée en fin de document.

## Format et grille
- 1080 × 1350 (4:5), mêmes images pour Instagram et TikTok ; image unique `fb-01.jpg` pour Facebook (la couverture sans compteur, accroche du bloc `fb` si présent).
- Typographie unique **Inter**, titres en minuscules accentuées (casse de phrase), graisse 800, interlignage serré.
- Marges : 72 px à gauche, 104 px à droite (colonne de boutons TikTok). Contenu de y 170 à y 1100 ; monogramme et mention à y 1112–1172 ; **rien sous y 1190** (légende TikTok, 160 px du bas).

## Fonds : alternance d'un post à l'autre (champ `bg`)
| Rôle | Sombre (`dark`) | Clair (`light`) |
|---|---|---|
| Fond | `#141416` + halo brun chaud | ivoire `#F3EEE4` + halo blanc |
| Titre, texte | `#F6F2EA` / `#E2DDD4` | anthracite `#1F1D1A` / `#2E2B27` |
| Accent (fin de titre en `*…*`, chiffres, étiquette, flèche) | or `#E5C07B` | or foncé `#89692F` |
| Texte secondaire | `#B9B2A7` | `#5E574D` |
| Encadrés (cartes, options, ticket) | ivoire `#F3EEE4`, texte `#1C1A17`, accent `#8A6A2E` | blanc cassé `#FFFDF8`, bordure `#D9CBB0` |
| Bulles (F7) | reçues `#2A2A2E`, envoyées or | reçues blanc cassé, envoyées anthracite |

Le fil ne montre jamais deux couvertures identiques côte à côte : fond alterné d'un post à l'autre, et visage une couverture sur deux.

## Couverture (brief, section 4)
- **Étiquette de format** en haut à gauche (pastille à bord accent) : nom du format (`format` F1 à F8) ou `tag` du contenu pour les séries numérotées (« DOSSIER n° 07 », « ÉPISODE 4 »). C'est le signe de reconnaissance de la marque.
- **Compteur** « 1/6 » en haut à droite. **Monogramme** VALORISLAB (emblème rond) en bas à gauche.
- **Supprimés** : la date, la mention « Finance Belgique », le logo complet en haut.
- **Titre** : 12 mots maximum (chiffre compris), 4 lignes maximum, **corps minimum 110 px** après ajustement (rendu bloqué sinon), bloc titre sur 50 à 60 % de la hauteur.
- **Chiffre clé** (`number`) : quand il existe, c'est le plus grand élément (220 px).
- **Sous-titre** : 6 mots maximum, ou rien.
- **Visuel** (`visual.type`) :
  - `face` : photo photo-réaliste du protagoniste (`visual.photo` = scène du catalogue avec `face: true` : `portrait-bureau`, `bureau-document`, `grand-place-cafe`), jamais détourée, en bandeau haut (0 à 600 px, fondu vers le fond). **Une couverture sur deux.** `visual.bubble` ajoute une bulle de message (F7).
  - `stamp` (F2) : guillemets et tampon « VERDICT ? ».
  - `bubble` (F7 sans visage) : bulle de message au-dessus du titre.
  - `ticket` (F6) : ticket « Prix affiché / Prix réel : ? » (`visual.rows`).
  - `dossier` (F3) : mention « Cas fictif » ; `document` (F4) : mention « Document fictif ».

## Slides intérieures (brief, section 5)
- **Une seule idée par slide, 25 mots maximum** (hors bulles de conversation) : avertissement au rendu au-delà.
- **Chaque slide se termine par une raison de swiper** (`next`, en accent avec flèche : question, « La suite va te surprendre », « Le verdict »…). Obligatoire sauf sur l'avant-dernière slide (rendu bloqué sinon).
- **La révélation** (réponse, verdict, première place) est **toujours sur l'avant-dernière slide**.
- **5 à 7 slides** (rendu et `qa.py` bloquants).
- Contenu centré verticalement entre l'étiquette et la flèche.
- Types de slide (`type`) : `text` (`kicker`, `title`, `body`, `big{value,label}`, `left`/`right` pour deux colonnes chiffrées, `ticket`, `steps`, `note`, `source`), `options` (A/B/C ; `state: "out"` = éliminée, `"win"` = gagnante), `chat` (`messages[{from: "them"|"me", text, flag}]`, le `flag` surligne le signal d'alerte), `verdict` (`stamp` VRAI / FAUX / ÇA DÉPEND), `cta`.
- Corps : titres 82 px, texte 44 px, cartes 32 à 40 px ; minimum 30 px partout (`qa.py`).

## Dernière slide (brief, section 6)
« C'est l'erreur n° X des 20 erreurs du guide. » (« C'est l'une des 20 erreurs du guide. » tant que `state/guide-erreurs.json` n'a pas le numéro), « Guide gratuit, lien dans ma bio. », bouton « Lien dans ma bio → », valorislab.be, monogramme + VALORISLAB, mention « Contenu éducatif, pas un conseil financier ». Plus de « Commente GUIDE ».

## Contrôles
`render.py` (titre de couverture ≤ 12 mots, ≥ 110 px, ≤ 4 lignes ; sous-titre ≤ 6 mots ; 5 à 7 slides ; `next` ; slide du guide en dernier), puis `validate.py` et `qa.py` (zones TikTok, contraste mesuré du bon côté du texte, tailles, slides), puis relecture visuelle.

---

## Archive : charte v5 (02/11/2026)


Remplace la charte v4 (archivée sur la branche `sauvegarde-charte-v4`). **Rendu : `kit/render.py` + `kit/templates/slide.html.j2`**, jamais d'image IA pour les slides. Modèle : `kit/assets/references/carrousel-v5/slide-01.jpg` à `slide-05.jpg`.

**Règle de Laurent : ces 5 images sont une référence de STYLE uniquement** (format, design, couleurs, structure, qualité). Leur sujet (Apple, résultats trimestriels), leurs textes et leurs chiffres ne sont jamais réutilisés. Tout le reste (sujets, textes, chiffres, décor) est produit par la routine. Les défauts des images de référence ne sont pas reproduits : chevauchements du guide, du bouton et du pied de page (slide 5), filet vertical qui traverse le texte (slide 3), carte collée au filet du pied de page (slide 4).

### Format et grille
- 1080 × 1350 (4:5), mêmes images pour Instagram et TikTok ; image unique `fb-01.jpg` (même charte) pour Facebook.
- Fond anthracite `#141416`, halo chaud brun doux, **grille fine** (traits blancs à 6 % d'opacité tous les 220 px, à partir de x 96 et y 180), visible aussi sur la photo de couverture.
- Typographie unique **Inter**. Titres **en majuscules**, gras, interlignage serré. Texte aligné à gauche, marges de 96 px.
- Zones : en-tête à y 214 ; contenu de y 290 à y 1060 ; filet or du pied de page à y 1084 ; **rien sous le pied de page** (zone de la légende TikTok).

### Couleurs
| Rôle | Couleur |
|---|---|
| Fond | `#141416` (anthracite, éclairci le 06/11/2026) |
| Titre (partie blanche) | `#F4F0E8` |
| Partie or du titre, chiffres clés | `#E5C07B` (aplat, pas de dégradé) |
| Surtitre, libellés de carte, numéros | `#D4AF6A` |
| Corps de texte | `#E2DDD4` |
| Pied de page, compteur, notes | `#B0AAA1` |
| **Encadrés (cartes, étapes, listes, notes) : ivoire** (demande de Laurent, 06/11/2026) | fond `#F3EEE4`, bordure `#D9CBB0`, ombre douce, coins arrondis 18 à 22 px ; texte `#1C1A17`, texte secondaire `#5E574D`, libellés, numéros et chiffres de gauche en or foncé `#8A6A2E` |
| Bouton | `#E3BE78`, texte `#1A1612`, majuscules |

### Éléments fixes (toutes les slides)
1. En-tête : emblème rond + « VALORISLAB » (capitales espacées) + « FINANCE BELGIQUE » (or), en haut à gauche.
2. Compteur « 01 / 05 » en gris, en haut à droite.
3. Surtitre : trait or + texte or en majuscules (`kicker` de la slide ; couverture : thème · date, ex. « BOURSE · 02 NOVEMBRE 2026 »).
4. Pied de page : filet or, « valorislab.be » à gauche, « Contenu éducatif · Pas un conseil financier » à droite.

### Structure de référence (5 slides par défaut, 8 au maximum)
1. **Couverture (`cover`)** : surtitre thème · date, titre-accroche en majuscules (fin en or), sous-titre qui explique le « pourquoi » (`subtitle`), ligne or d'actualité facultative (`highlight`, ex. « X publie ses résultats aujourd'hui. »). Décor IA du sujet dans la partie basse, sous la grille.
2. **Le point essentiel (`compare` sans valeur)** : surtitre « Le point essentiel », titre (fin en or), une phrase d'explication (`body`), puis une carte à 2 colonnes : libellé or + texte (`left{label, note}`, `right{label, note}`).
3. **Exemple chiffré (`compare` avec valeurs)** : surtitre « Exemple fictif · pour comprendre » (ou « Exemple réel » avec source), titre, carte à 2 colonnes : libellé gris + grand chiffre (gauche or, droite blanc) + phrase de conclusion sous un filet (`caption`), puis une note grise (`note`, ex. « Chiffres illustratifs » ou la source).
4. **Méthode (`list`)** : surtitre « Ta méthode de débutant », titre, 4 étapes en cartes numérotées 01 à 04 ; chaque étape = 1re ligne blanche (`title`) + 2e ligne grise (`sub`).
5. **CTA (`cta`)** (règle de Laurent, 13/11/2026) : surtitre « Pour aller plus loin », titre « 20 erreurs à éviter, gratuitement. », sous-titre « Commente GUIDE et je t’envoie gratuitement les 20 erreurs à éviter. » (texte exact), maquette du guide, bouton or « COMMENTE GUIDE → ».

Pour un sujet qui le demande, ajouter 1 à 3 slides du même type (`point`, `stat`, `compare`, `list`), sans dépasser 8.

### Limites de texte (lisibilité sur téléphone)
- Titre de couverture ≤ 55 caractères ; autres titres ≤ 60 caractères ; 1 segment en or, toujours la fin.
- `subtitle` / `body` ≤ 140 caractères ; texte de carte ≤ 35 caractères par colonne ; chiffre de carte ≤ 7 caractères.
- Étapes : `title` ≤ 32 caractères, `sub` ≤ 32 caractères.
- Le moteur réduit le texte si besoin et le signale : raccourcir plutôt que forcer.

### Décor de couverture (IA) : clair, pur, sans or
Règles de Laurent (06/11 et 14/11/2026) : l'or est réservé aux accents typographiques du kit. Le décor est une photo éditoriale lumineuse et épurée (lumière naturelle douce, tons clairs à moyens : pierre claire, bois clair, blanc cassé, quelques noirs mats), sans objets dorés, pièces, lingots, bokeh ni lumière dorée. Sur la couverture, il occupe le bas de la slide (y 790 à 1350), sous le texte, avec une ombre légère seulement en haut (fondu vers le titre) et sous le pied de page : il doit rester bien visible. Contrôle automatique : `kit/decor_check.py`. Prompt : `docs/RUNBOOK.md`, étape 5.
