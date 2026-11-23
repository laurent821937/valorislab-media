# Charte carrousel VALORISLAB v7 « moderne » (validée définitivement par Laurent le 20/11/2026, en vigueur pour tous les posts)

Inspiration : style des carrousels « studio » modernes envoyés par Laurent (référence de STYLE uniquement : aucune de leurs images, aucun texte, aucune couleur de marque reprise). Gabarit `kit/templates/slide-v7.html.j2`, contenu `"charte": "v7"`, rendu par `kit/render.py` (même chaîne que la v6). Maquette de départ : `reports/maquettes/maquette-v7-moderne.jpg`, prototype `kit/prototypes/v7-moderne.py`. Le brief (`docs/brief-refonte-carrousels-2026-11.md`, sections 2 à 7) reste la règle éditoriale.

## Identité
- Fond ivoire chaud `#F7F2EC` (`bg: "light"`) ou champagne `#EFE5D6` (`bg: "champagne"`), halo blanc doux. Jamais de fond sombre en pleine page.
- **Titre** : Inter 800, CAPITALES, interlettrage serré (−0,045 em), 116 px en couverture (110 px minimum, contrôlé), 90 px à l'intérieur, 84 px sur la dernière slide.
- **Mot fort** : le passage entre `*…*` du titre devient une **étiquette en dégradé vert → or** (`#1E8C78 → #5DA66A → #C8963A`), Plus Jakarta Sans 800, texte blanc, légèrement penchée (−2°). Une seule par titre.
- **Pastille de rubrique** (`kicker` + `icon`) : pastille noire arrondie, pastille ronde en dégradé à gauche (« 1 SIGNAL 1 », « ? LES 3 SUSPECTS », « ✓ CE QUE DIT LA FSMA »). C'est le fil rouge du carrousel.
- **Sous-texte** (`body`) : Inter 38 px gris chaud, **gras** = noir pour le passage important.
- **Bouton de swipe** (`next`) : pilule en dégradé « la suite → » avec rond noir et flèche, en bas à droite (au-dessus des 160 px TikTok, à gauche de la colonne de boutons TikTok). Couverture : « je te montre → ».
- Monogramme « VALORISLAB » + « Contenu éducatif, pas un conseil financier » en petit, en haut à droite des slides intérieures. Couverture : étiquette de format en haut à gauche (« LE MESSAGE SUSPECT », « LE TRIBUNAL DU MYTHE »…), compteur « 1/6 » en haut à droite.

## Visuels réalistes (un par slide intérieure, champ dédié)
- `phone` + `messages[]` : téléphone avec conversation (bulle `flag: true` cerclée d'or = le piège). Toujours « Conversation fictive ».
- `app` : fenêtre d'appli fictive (`title`, `label`, `value`, `chip`, `chart`).
- `receipt` : ticket de caisse (lignes, total dans une étiquette en dégradé).
- `options[]` (cartes A/B/C, `state: out|win`), `steps[]` (cartes numérotées), `tiles[]` (tuiles d'appli de bourse fictives), `big` (chiffre géant), verdict (`type: "verdict"`, tampon).
- `dots` `{count, on, cols, label}` : grille de pastilles (objets du quotidien rendus visibles, `on` en dégradé).
- `script` `{head, lines[]}` : la phrase exacte à se dire ou à dire, entre guillemets.
- `recap` `{head, items[]}` : « À enregistrer », 3 lignes maximum (incite à sauvegarder).
- `ann[]` : **annotations** = pilules noires avec flèche en dégradé, posées à cheval sur le bord droit du visuel, jamais sur son texte (contrôlé). Saut de ligne : `\n`.

## Protagoniste : ne jamais le modifier (Laurent, 20/11/2026)
Référence unique `kit/assets/protagonist/ref-sweat-noir.jpg` (voir `kit/assets/protagonist/README.md`) : carrure athlétique et musclée, cheveux courts texturés en pointes avec reflets blonds, dégradé très court, barbe courte, yeux bleu-gris, regard intense, tenue noire (sweat à capuche ou chemise) et montre noire. Le prompt commence par « EXACTEMENT le MÊME homme que sur l'image de référence, sans rien changer à son physique » et décrit ces traits ; seule la scène change (lumineuse). Image qui dérive (visage plus doux, carrure plus fine, autre tenue) = rejetée. Les vraies photos de Laurent ne servent jamais de référence IA.

## Couverture
- **Photo façon selfie** du protagoniste (une couverture sur deux) : gros plan face caméra, mur clair en haut pour le titre, expression vivante (sourcil levé, main levée, sourire stupéfait). Image IA neuve via Make avec `reference_url` (RUNBOOK, étape 5), style `v7-moderne-selfie`. Bulle de message (`visual.bubble`), mention fictive (`subtitle` → pastille), chiffre clé (`number`) au-dessus du titre.
- **Couverture graphique** (l'autre sur deux) : titre-mythe entre « », tuiles du format (`visual.tiles`), tampon « VERDICT ? » (`visual.stamp`).

## Dernière slide
- Photo lumineuse du protagoniste (`cta_photo`, différente de la couverture), titre « C'est l'une des 20 erreurs *du guide.* » (« l'erreur n° X » dès que la liste numérotée est fournie), bandeau sombre en bas : « Guide gratuit | LIEN EN BIO », phrase, « valorislab.be · Contenu éducatif, pas un conseil financier ».

## Légendes
- Instagram et TikTok : une question, renvoi à la slide de la réponse (avant-dernière), dernière ligne « Guide gratuit : lien dans ma bio. ».
- Facebook reçoit le même carrousel multi-images qu'Instagram (décision de Laurent du 23/11/2026) : même logique de légende, renvoi à la slide de la réponse autorisé.
- **Aucune légende ne révèle la réponse, le verdict ni la première place** : le contenu liste ces mots dans `spoilers` ; `text_check.py` bloque s'ils apparaissent dans la légende Facebook (alerte pour Instagram et TikTok).

## Contrôles (bloquants)
`render.py` (CLIP_JS_V7) : rien hors de la zone (40 px de marge, 160 px en bas), rien de coupé, bulles dans l'écran, rien sous le bouton de swipe, le monogramme ou la bulle de couverture, annotations jamais sur un texte, titre de couverture ≥ 110 px sur 4 lignes maximum, 25 mots maximum par slide (chiffres non comptés). Puis `text_check.py`, `seo_check.py`, `qa.py` (contraste, zones TikTok, grille Instagram), `validate.py`.

---

# Archive : charte v6 (brief de Laurent du 20/11/2026)

Remplace la charte v5 pour tout nouveau contenu (`"charte": "v6"` dans le fichier de contenu). Source : sections 4 et 5 de `docs/brief-refonte-carrousels-2026-11.md`. **Rendu : `kit/render.py` + `kit/templates/slide-v6.html.j2`**, jamais d'image IA pour les slides. Les contenus v5 (sans champ `charte`) restent rendus avec `kit/templates/slide.html.j2` ; la charte v5 est archivée en fin de document.

## Format et grille
- 1080 × 1350 (4:5), mêmes images sur Instagram, TikTok et Facebook (carrousel multi-images depuis le 23/11/2026).
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

## Finition premium (demande de Laurent, 20/11/2026)
- **Titres en Playfair Display** (600, casse de phrase, fin en *italique* accent or) ; texte, étiquettes et chiffres de carte en Inter ; grands chiffres en Playfair.
- **Filets or fins** : cadre intérieur de 1 px (à 36 px du bord, il s'arrête au-dessus de la zone TikTok), trait devant l'étiquette de format et les surtitres, trait après la raison de swiper.
- Étiquette de format et surtitres en petites capitales espacées (0,24 em) ; compteur « 1/6 » en Playfair italique ; monogramme + VALORISLAB en bas à gauche sur toutes les slides.
- Cartes sobres : bord fin, coins de 18 px, ombre diffuse ; lettres d'option et numéros en Playfair italique cerclés d'or.
- Dernière slide : maquette du guide (`kit/assets/guide-mockup.jpg`), bouton « Lien dans ma bio », valorislab.be en italique.

## Couverture photo IA (`visual.type: "photo"`, 20/11/2026)
- Image pleine page 1080 × 1350 générée pour le contenu (Make 8230680, entrée `reference_url`) : **le protagoniste à partir de sa photo de référence** (`kit/assets/protagonist/ref-portrait.jpg` ou `ref-pensif.jpg`, même visage, nouvelle scène liée au sujet), ou une nature morte premium pour les couvertures sans visage (alternance du brief : visage une couverture sur deux).
- Le sujet occupe la moitié haute ; un dégradé vers le fond (sombre ou ivoire) porte le titre dans la moitié basse (contenu de y 500 à y 1088).
- `visual.stamp` (tampon) et `visual.bubble` (bulle) se combinent avec la photo.
- Contrôle : relecture visuelle (aucun texte, logo, chiffre ni objet doré, visage fidèle) ; `decor_check.py` ne s'applique qu'aux décors sans personne (la peau et la lumière chaude le font échouer à tort).

## Lumière, vie et réalisme (demande de Laurent, 20/11/2026, prime sur l'alternance sombre/clair du brief)
- **Pas de post sombre** : les fonds alternent entre **ivoire** (`bg: "light"`, `#F3EEE4`) et **champagne** (`bg: "champagne"`, `#EDE2CF`, accent texte `#6B501F`). Le fond sombre (`dark`) reste disponible mais n'est plus utilisé par défaut.
- **Images IA lumineuses et enthousiastes** : lumière naturelle du matin, tons crème, bois miel, vert sauge, protagoniste souriant, vif, confiant (jamais l'air sombre ou inquiet), scènes réalistes de la vie quotidienne liées au sujet ; moitié basse claire pour le titre.
- **Éléments réalistes propres à la niche** dans les slides intérieures : téléphone avec conversation (`chat` + `phone: {contact, status, time}`), ticket de caisse (`receipt: {title, rows, total, foot}`), tuiles d'appli d'investissement fictives (`tiles: [{name, price, change, gain, sub}]`). Toujours marqués fictifs.
- Bulle « moi » dorée, bulle reçue blanche ; signaux d'alerte surlignés d'or.
- **Contrôles bloquants** : `kit/text_check.py` (cohérence slides ↔ légendes : chiffres, renvoi à la slide de révélation, une seule question, fin « Guide gratuit : lien dans ma bio. », mention), et dans `render.py` la mesure des éléments coupés ou collés au bord (bulles, cartes, tampon, ticket, tuiles, téléphone), du texte coupé et du texte réduit sous 90 %.

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
