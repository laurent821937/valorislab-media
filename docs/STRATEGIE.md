# Stratégie éditoriale VALORISLAB (validée par Laurent le 27/10/2026, ligne éditoriale refondue le 20/11/2026)

Ce document est la référence pour toute génération automatique de contenu.
Toute modification de la stratégie passe par Laurent.
**Refonte du 20/11/2026** : la ligne éditoriale (formats, sujets, dernière slide, légende, score) vient des sections 2, 3, 6 et 7 du brief de Laurent, `docs/brief-refonte-carrousels-2026-11.md` (qui explique aussi le pourquoi, section 1, et la mesure, section 8). La charte visuelle est dans `docs/STYLE-CARROUSEL.md` (charte v7 « moderne », validée le 20/11/2026). Les règles de conformité restent inchangées.

## Positionnement
- Plateforme éducative belge francophone : Bourse, ETF, Crypto, finances personnelles.
- Cible : débutants et intermédiaires en Belgique (FR), 20–45 ans, qui veulent comprendre avant d'agir.
- Promesse : « comprendre avant d'agir ». Ton direct, pédagogique, chiffré, sans hype ni promesse de gain.
- Tutoiement. Phrases courtes. Pas de jargon non expliqué. Zéro émoji dans les visuels ; 0 à 2 émojis maximum dans une légende (de préférence aucun).
- Offre : guide gratuit « Les 20 erreurs du débutant en Bourse et en Crypto » (valorislab.be, lien en bio), puis formations Bourse et Crypto à 149 €. Le pack IA n'est plus mis en avant.
- Objectif des carrousels (brief, section 1) : faire swiper jusqu'à la dernière slide (rétention) et rendre chaque post reconnaissable comme du VALORISLAB (marque).

## Les 8 formats de rétention (brief, section 2)
Chaque semaine, la routine choisit **3 formats différents** parmi ces 8. Jamais deux fois le même format dans la même semaine. Chaque format repose sur un mécanisme qui oblige à swiper. Le format est noté dans le contenu (`format: "F1"` à `"F8"`) et affiché sur la couverture dans l'étiquette de format.

| Code | Format | Mécanisme | Couverture | Slides | Règle |
|---|---|---|---|---|---|
| F1 | La boucle ouverte | La couverture pose une question, la réponse n'arrive qu'à l'avant-dernière slide | « Une seule de ces 3 dépenses te coûte 4 000 € sur 10 ans. Laquelle ? » | Les 3 options, un indice, la révélation chiffrée, la leçon | La réponse n'est jamais devinable sur la couverture |
| F2 | Le tribunal du mythe | Une idée reçue est « jugée » : VRAI, FAUX ou ÇA DÉPEND | Tampon « VERDICT ? » et la phrase-mythe entre guillemets | L'accusation, la défense, la preuve chiffrée, le verdict (tampon), ce qu'il faut retenir | Privilégier « ÇA DÉPEND » quand c'est la réalité (expliquer des différences de démarche plutôt qu'une opposition absolue) |
| F3 | Le dossier | Un cas fictif comme un dossier d'enquête : le lecteur se demande ce qu'il ferait | « DOSSIER n° 07 · Sarah, 26 ans, 1 900 € net. Elle veut commencer à investir. Par quoi commencer ? » | La situation, les 3 options, ce qui coince dans chacune, la méthode (pas une recommandation personnelle) | Profil explicitement fictif, « Cas fictif » visible sur la couverture ; numérotation continue des dossiers (`state/series.json`) |
| F4 | Trouve l'erreur | Un document du quotidien contient une erreur coûteuse, le lecteur la cherche | « Ce relevé cache une erreur qui coûte 300 €/an. Tu la vois ? » | Le document, un indice, l'erreur entourée, le calcul, le réflexe | Document visiblement fictif : aucun logo, nom ou numéro réel, « Document fictif » sur le visuel |
| F5 | Le classement révélé | Un classement dévoilé de la dernière à la première place | « 6 façons de laisser dormir 5 000 € en Belgique. Classées de la pire à la meilleure. » | Place 6 à place 1, chacune avec le chiffre de l'année | Critère unique et explicite (ex. pouvoir d'achat après 5 ans), données officielles datées, jamais de rendements futurs |
| F6 | La facture cachée | Prix affiché contre prix réel, ligne par ligne, comme un ticket qui s'allonge | Un ticket « Prix affiché : 999 € », « Prix réel : ? » | Chaque ligne ajoutée (intérêts, frais, assurance, taxe), le total, la question à poser avant de signer | Sujets : crédit à la consommation, leasing, paiement fractionné, frais d'un fonds bancaire, carte de crédit |
| F7 | Le message suspect | Une conversation fictive façon messagerie, le lecteur repère le piège | Une bulle : « Salut ! J'ai doublé mon argent en 3 semaines, je te montre ? » | La conversation qui avance, chaque signal d'alerte surligné, ce que dit la FSMA, quoi faire | Conversation fictive, aucun nom ni plateforme réels, source FSMA citée |
| F8 | L'épisode du protagoniste | Une série : le protagoniste VALORISLAB fait une erreur que le lecteur voit venir | « Épisode 4 · Il vient de toucher sa prime de fin d'année. Il a déjà une idée. Mauvaise idée. » | La situation, la décision, la conséquence chiffrée, ce qu'il aurait dû faire, l'annonce de l'épisode suivant | Récit à la 3e personne, tiré des 20 erreurs du guide (citée sur la dernière slide) ; numérotation continue (`state/series.json`) |

## Règles de choix des sujets (brief, section 3)
1. Le sujet part d'une **situation vécue**, jamais d'une notion. « Tu viens de recevoir ta prime » plutôt que « Qu'est-ce que le précompte mobilier ».
2. Le **calendrier** compte : primes de décembre, soldes, déclaration fiscale (mai-juin), rentrée, Black Friday, 13e mois, pécule de vacances.
3. Chaque sujet est rattaché à **l'une des 20 erreurs du guide**. La dernière slide la nomme : « C'est l'erreur n° X du guide gratuit. » Numéros et intitulés : `state/guide-erreurs.json` (relevés dans le guide de Laurent le 20/11/2026 : Bourse 1 à 10, Crypto 1 à 10, bonus finances personnelles). Formulation : « C'est l'erreur Bourse n° X du guide. », « C'est l'erreur Crypto n° X du guide. », et pour un sujet budget « l'étape X du guide gratuit » (bonus finances). Champ `guide_error: {chapter, n, title}`. Ne jamais inventer un numéro.
4. **Interdit** : les sujets déjà publiés (contrôle `state/history.json`), et les sujets purement techniques sans enjeu personnel (TOB seule, domiciliation d'ETF seule, taxe Reynders seule). Ces notions peuvent apparaître à l'intérieur d'un format, jamais comme sujet principal.
5. **Répartition par semaine** : 1 sujet Bourse, 1 sujet Crypto ou arnaque, 1 sujet budget du quotidien (champ `theme` : `bourse`, `crypto` ou `arnaque`, `budget`).

## Ton humain, sujets qui concernent, accroches variées (demande de Laurent, 20/11/2026)
**But** : que chaque personne qui voit la couverture se dise « ça, c'est moi ». On parle à une personne, pas à « les investisseurs ». On explique avec des scènes de vie, pas avec des notions.

**1. Partir d'une scène de vie, jamais d'une notion.** Un moment précis (vendredi soir, jour de paie, fin du mois, Black Friday, prime de décembre, premier CDI, colocation, premier enfant, achat d'une voiture), un lieu, un montant du quotidien (un café, une livraison, un abonnement, un loyer). La notion technique (TOB, ETF, TAEG, précompte…) n'arrive qu'à l'intérieur, au moment où elle sert, traduite tout de suite en mots simples.

**2. Le test « je me sens concerné »** (les 3 réponses doivent être oui, sinon on change d'angle) :
- Un débutant belge de 20 à 45 ans se reconnaît en 1 seconde sur la couverture.
- Il a déjà vécu, pensé ou entendu ça (pas une situation rare ou réservée aux riches).
- Il repart avec un réflexe faisable en 1 minute (vérifier, comparer, refuser, noter), sans conseil personnalisé.

**3. Une émotion par post**, assumée et positive à la fin : surprise, gêne qui fait sourire, peur de rater, fierté, soulagement, « ah, je ne savais pas ». Jamais la honte ni la peur gratuite : on finit toujours sur une solution simple et de l'énergie.

**4. Zéro jargon sur la couverture.** Interdits sur la couverture (contrôlé par `kit/text_check.py`) : ETF, TOB, TAEG, TER, précompte, capitalisant, distribuant, CFD, levier, Reynders, domiciliation, staking, wallet, dividende, obligation, tracker, plus-value. Si la notion est le cœur du sujet, la couverture parle de la situation (« Tu achètes ta première action ? Une taxe t'attend ») et le mot arrive en slide 2, expliqué.

**5. Des personnages fictifs auxquels on s'identifie**, en rotation, toujours marqués « cas fictif » : Sarah, 26 ans, premier CDI à 1 900 € net ; Mehdi, 34 ans, deux enfants, ménage serré ; Julie, 41 ans, reprend ses finances après une séparation ; Tom, 22 ans, étudiant avec un job ; Inès et Lucas, 30 ans, qui préparent un achat ; Karim, 38 ans, indépendant. Le protagoniste VALORISLAB reste le héros des épisodes (F8).

**6. Accroches : 14 styles, en rotation.** Chaque contenu porte son style dans `hook_style` ; ses 5 variantes (`hook_variants`) couvrent au moins 3 styles différents, puis on garde la meilleure. Jamais deux fois le même style dans la même semaine (contrôlé par `text_check.py`), et on évite de reprendre le style des 3 derniers posts publiés.

| `hook_style` | Style | Exemple |
|---|---|---|
| `scene` | Scène vécue | « Vendredi, 23 h. Tu commandes encore à manger. » |
| `miroir` | Question miroir | « Toi aussi, ta prime disparaît en une semaine ? » |
| `chiffre-choc` | Chiffre concret qui surprend | « 3 000 € en 10 ans. Pour une seule dépense. » |
| `mythe` | Phrase entendue partout, à juger | « « Il faut beaucoup d'argent pour investir. » Vrai ? » |
| `defi` | Défi ou quiz | « Trouve l'erreur sur ce ticket en 5 secondes. » |
| `avant-apres` | Comparaison de deux vies | « Même salaire. Deux fins de mois très différentes. » |
| `moment` | Interpellation d'un moment du calendrier | « Ton 13e mois vient de tomber ? Lis ça avant de dépenser. » |
| `message` | Conversation ou notification | « « Je te montre comment j'ai doublé mon argent ? » » |
| `contre-intuitif` | Vérité qui va contre l'intuition (sourcée) | « Ton argent qui dort perd de la valeur chaque mois. » |
| `liste` | Liste avec tension | « 3 lignes que personne ne lit sur son relevé. » |
| `personnage` | Cas fictif auquel on s'identifie | « Sarah, 26 ans, premier salaire. Elle fait l'erreur n° 1. » |
| `episode` | Épisode du protagoniste | « Épisode 4 · Il vient de toucher sa prime. Mauvaise idée. » |
| `pov` | Point de vue (on se met dans la scène) | « POV : ton 13e mois vient de tomber. » |
| `objet` | Un montant rendu visible avec des objets du quotidien | « 52 cafés. Voilà ce que coûte ton lundi. » |

**7. Légende humaine** : ligne 1 = la scène ou l'émotion (pas la leçon) avec le mot-clé ; ligne 2 = la tension ou ce qu'on va découvrir ; ligne 3 = une seule question, personnelle (« Et toi, tu fais comment ? »). Puis la source, la mention et « Guide gratuit : lien dans ma bio. ».

**8. Stratégie réseaux sociaux (rappel)** : 1 sujet = 1 situation = 1 émotion = 1 réflexe. Couverture lisible en 1 seconde, mécanisme de rétention jusqu'à l'avant-dernière slide, réponse surprenante mais vraie, sortie positive, mot-clé recherché (référencement), une seule question pour les commentaires. Le critère « Situation » du score (20 points) ne donne le maximum que si le test « je me sens concerné » est passé et que l'émotion est claire.

## Ce que font les meilleurs comptes finance, version VALORISLAB (20/11/2026)
Inspiration de mécanismes seulement (jamais leurs visuels, leurs textes ni leurs personnages). Comptes étudiés : Humphrey Yang, Vivian Tu (Your Rich BFF), Ramit Sethi, Tiffany Aliche (The Budgetnista), Visual Capitalist, Finary, Graham Stephan. Les chiffres de performance publiés en ligne sur les carrousels ne sont pas vérifiables : on se fie à nos propres mesures (section « Mesure »).

| Mécanisme | Vu chez | Notre version (charte v7) | Où |
|---|---|---|---|
| Rendre un montant visible avec des objets | Humphrey Yang | Grille de pastilles `dots` (52 cafés, 12 abonnements dont 3 jamais ouverts), toujours « exemple fictif » ou chiffre sourcé | Slide 2 ou 3, accroche `objet` |
| Parler comme une amie qui s'y connaît, avec humour | Vivian Tu | Tutoiement, phrases courtes, une pointe d'humour sur la scène, jamais sur la personne ; accroche `pov` | Couverture et légende |
| Dépenser sans culpabilité, couper ce qu'on ne remarque plus | Ramit Sethi | Fin positive : on garde ce qu'on aime, on coupe le reste ; jamais de honte | Slide de méthode |
| Des scripts mot à mot | Ramit Sethi | Bloc `script` : la phrase exacte à se dire ou à dire (à sa banque, à un vendeur, à un inconnu qui propose un « plan ») | Avant-dernière ou slide de méthode |
| Un plan en étapes, à enregistrer | The Budgetnista | Bloc `recap` « À enregistrer » (3 lignes maximum) : c'est ce qui fait sauvegarder le post | Slide de méthode ou de révélation |
| Un seul graphique, un seul message | Visual Capitalist | Tuiles, ticket, pastilles : une donnée par slide, lisible en 1 seconde | Slides intérieures |
| Montrer l'écran réel (appli, relevé) | Finary | Fenêtre d'appli, téléphone et ticket fictifs, annotés | Formats F4, F6, F7 |
| Décortiquer un document ou une pub | Graham Stephan | Format F4 « Trouve l'erreur » et F6 « La facture cachée » | Sujets du mois |
| Un rendez-vous récurrent | Comptes en séries | Épisodes numérotés du protagoniste (F8), même jour chaque semaine | `state/series.json` |

**Règle d'adaptation** : chaque mécanisme passe par le test « je me sens concerné », le ton humain, la conformité (sources, mention, aucune promesse) et le style v7. Au moins **un mécanisme de ce tableau par carrousel**, noté dans `virality` (`mecanismes: [...]`).

## Format visuel
**Charte v7 « moderne » (validée le 20/11/2026) : `docs/STYLE-CARROUSEL.md`**, rendue par le kit (`kit/render.py`, gabarit `kit/templates/slide-v7.html.j2`), 5 à 7 slides. Les chartes v5 et antérieures ne servent plus qu'à re-rendre d'anciens contenus.

## Dernière slide et légende (brief, section 6)
- **Dernière slide** : « C'est l'erreur n° X des 20 erreurs du guide. Guide gratuit, lien dans ma bio. » Puis valorislab.be et la mention « Contenu éducatif, pas un conseil financier ».
- **Légende** : 3 lignes maximum avant le « … plus », puis la source et la mention. **Dernière ligne : « Guide gratuit : lien dans ma bio. »**
- **Supprimé** : « Commente GUIDE » et toute demande de commentaire liée à l'envoi d'un lien, tant qu'aucun envoi automatique en message privé n'est en place (la règle du 13/11/2026 est abrogée).
- **Jamais de révélation dans la légende** (règle de Laurent, 23/11/2026) : ni la réponse, ni le verdict, ni la première place, sur aucun réseau ; la légende donne envie de swiper et renvoie à la slide de la réponse. Mots interdits listés dans `spoilers` du contenu (contrôlé par `text_check.py`). Facebook publie désormais le même carrousel multi-images qu'Instagram.
- **Une seule question d'engagement** par légende, liée au format (« Tu avais trouvé l'erreur ? », « Ton verdict ? »).
- Inchangé : « Contenu éducatif, pas un conseil financier. » (+ hypothèses si un calcul est présenté, + « Performances passées… » si des performances historiques sont citées) ; 3 à 5 hashtags dont #belgique (voir « Référencement »).

Limites : Instagram ≤ 2 200 caractères ; titre TikTok ≤ 90 caractères, description TikTok ≤ 500 caractères ; Facebook sans limite pratique (rester ≤ 1 500).
Texte alternatif (alt) obligatoire pour chaque visuel.


## Référencement (SEO social et Google, règle de Laurent, 14/11/2026)
Instagram, TikTok et Facebook sont des moteurs de recherche : un post bien référencé continue d'être trouvé pendant des mois, alors qu'un post de fil disparaît en 48 h. Le levier, ce sont les **mots-clés**, pas les hashtags. Le contrôle `kit/seo_check.py` est bloquant.

**1 contenu = 1 mot-clé principal**, formulé comme un débutant belge le tape dans la barre de recherche (« investir en bourse », « ETF », « TOB », « précompte mobilier », « compte d'épargne », « arnaque crypto »…), plus 2 à 3 mots-clés secondaires, dans `seo: {keyword, secondary[], cluster}`. Recherche sans invention : suggestions de la barre de recherche Instagram/TikTok/Google quand elles sont accessibles, vocabulaire de Wikifin et de la FSMA, questions des commentaires. Ne jamais citer de volume de recherche inventé.

**Où le placer** (langage naturel, jamais de bourrage) :
- **Texte à l'écran** (lu par TikTok et Instagram) : dans le titre, le sous-titre ou le surtitre de la couverture, ou dans le titre de la slide 2. L'accroche reste prioritaire : si le mot-clé casse l'accroche, le mettre dans le sous-titre.
- **Légende Instagram** : dans les 125 premiers caractères (ligne visible avant « plus »), puis une seconde fois plus bas ; les secondaires une fois chacun ; phrase complète et naturelle, idéalement sous forme de question recherchée (« C'est quoi la TOB ? »).
- **Légendes TikTok et Facebook** : dans les 150 premiers caractères.
- **Titre TikTok** : contient le mot-clé, de préférence au début.
- **Texte alternatif** (global et par slide) : description concrète qui contient le mot-clé (indexé par Instagram et Google).
- **Hashtags** : 3 à 5 par légende (Instagram en limite 5) : 1 large (#bourse, #crypto, #investir), 1 à 2 de niche liés au mot-clé (#etf, #tob, #arnaquecrypto), toujours #belgique. Jamais de hashtags en masse ni sans rapport.
- **Ancrage belge** : « en Belgique » ou « belge » dans la légende quand le sujet s'y prête (recherches locales).

**Grappes thématiques** (devenir la référence sur un sujet ; chaque contenu en renforce une, noter `seo.cluster`) :
- `investir-debutant` : investir en bourse, ETF, investir chaque mois, intérêts composés, diversification.
- `frais-et-fiscalite` : frais bancaires, frais de fonds, TOB, précompte mobilier, compte-titres, taxe sur les comptes-titres.
- `epargne-belgique` : compte d'épargne réglementé, garantie des dépôts, inflation, compte à vue.
- `crypto-securite` : arnaque crypto, phrase de récupération, wallet, faux support, plateformes agréées.
- `arnaques-finance` : faux courtier, clone FSMA, arnaque sentimentale, fraude à l'investissement.
Alterner les grappes et, dans chaque grappe, couvrir les questions voisines au fil des semaines.

**Profils (à régler à la main par Laurent, la routine n'y a pas accès)** : le champ **Nom** d'Instagram est indexé séparément du @ et pèse lourd dans la recherche.
- Instagram, nom : « VALORISLAB · Bourse & Crypto Belgique ». Bio : « Investir en bourse et en crypto sans erreurs de débutant 🇧🇪 · ETF, frais, fiscalité belge, arnaques » + lien.
- TikTok, nom : « Valorislab · Bourse Crypto Belgique » ; bio sur le même modèle.
- Facebook, page : catégorie « Éducation » ou « Services financiers », section « À propos » avec les mêmes mots-clés.

## Règles de fiabilité (non négociables)
- **Tout calcul est fait en Python** dans le run, jamais de tête. Hypothèses affichées (taux, durée, « avant frais et impôts », « rendement non garanti »).
- **Données belges ou réglementaires** (taux, plafonds, montants d'exonération, fiscalité) : vérifier sur une source officielle de l'année en cours (SPF Finances, FSMA, BNB, Wikifin, FEBELFIN). Si une donnée ne peut pas être vérifiée → changer d'angle ; ne jamais publier un chiffre douteux.
- Pas de recommandation d'achat ou de vente d'un titre, d'une crypto ou d'un produit nommé ; pas de prédiction de prix ; pas de promesse de rendement ; pas de « rendement garanti ».
- **Images (décision de Laurent du 29/10/2026, adaptée à la charte v6 le 20/11/2026)** : les slides sont rendues par le kit (texte et chiffres exacts), jamais générées par IA. Charte v6 : une couverture sur deux montre le visage du protagoniste (photos photo-réalistes de Laurent, `kit/assets/scenes/`, jamais détourées), l'autre l'élément visuel du format, dessiné par le kit (tampon, ticket, bulle, dossier, document). Le décor IA (OpenAI via Make 8230680) n'est plus généré par défaut : seulement si un format en a vraiment besoin, dans les budgets du RUNBOOK. Pas de logo de marque tierce, pas de capture d'écran d'un produit tiers.
- Les sources sont listées dans le fichier de contenu (`sources`) et mentionnées en légende quand un chiffre externe est cité.
- Si un contenu ne passe pas ces règles → le remplacer par un autre sujet de la banque ci-dessous.

## Score de viralité (avant publication, obligatoire ; brief, section 7)
Chaque contenu reçoit une note sur 100, calculée et justifiée dans le champ `virality` du fichier de contenu. **Seuil : 70/100.** Sous 70 : retravailler (couverture, mécanisme) puis renoter ; le critère conformité est éliminatoire.
| Critère | Poids | Ce qui donne le maximum |
|---|---|---|
| Rétention (`retention`) | 25 | Mécanisme de rétention clair et tenu jusqu'à l'avant-dernière slide |
| Couverture (`couverture`) | 20 | Lisible en 1 seconde sur un téléphone : titre ≤ 12 mots, chiffre visible |
| Situation (`situation`) | 20 | Situation vécue par un débutant, et non une notion ; test « je me sens concerné » passé, émotion claire, zéro jargon en couverture |
| Différence (`difference`) | 15 | Différent des 3 derniers posts publiés (format, fond, visuel) |
| Erreur du guide (`guide`) | 10 | Lien explicite avec une erreur du guide |
| Conformité (`conformite`) | 10 | Sources, mention, pas de promesse. **Éliminatoire si absent** (0 = contenu refusé) |

## Mesure (brief, section 8)
- Toutes les 2 semaines : portée moyenne et taux de swipe jusqu'à la dernière slide par format (via Buffer), clics sur le lien en bio par réseau. Rapport `reports/perf-formats-<AAAA>-W<ss>.md`.
- Après 4 semaines (vers le 18/12/2026) : on garde les 4 formats les plus performants et on retire les autres (décision de Laurent).

## Analyse de performance (après publication, à chaque exécution)
- Récupérer les statistiques Buffer des posts publiés depuis 28 jours, posts natifs compris (vues, portée, taux d'engagement, enregistrements, partages, commentaires ; temps de visionnage pour les vidéos). Ignorer les posts de moins de 48 h (statistiques incomplètes).
- Comparer chaque post à la médiane de son réseau. Identifier le top 3 et le flop 3, puis ce qui les distingue : format (F1 à F8), thème, fond de couverture (sombre ou clair), visage ou élément de format, jour et heure, carrousel automatique ou vidéo native.
- Appliquer les enseignements à la semaine suivante : favoriser les formats et les couvertures gagnants, mais garder au moins 1 contenu sur 3 en exploration pour continuer à apprendre.
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

## Sources officielles belges
FSMA (fsma.be), Wikifin (wikifin.be), SPF Finances (finances.belgium.be), Banque nationale (nbb.be), Statbel (statbel.fgov.be), SPF Économie (economie.fgov.be), Febelfin (febelfin.be). Utiliser WebFetch sur ces sites ; si l'accès est bloqué, WebSearch avec `allowed_domains` limité à ces domaines. Si aucun chiffre n'est vérifiable, garder l'ancrage belge avec un sujet sans chiffre volatil (obligation, procédure, mécanisme de protection : déclaration d'un compte étranger au Point de contact central de la BNB, liste d'avertissements de la FSMA, garantie des dépôts…), plutôt que de le remplacer par un autre pilier.

## Banque de sujets (situations vécues, point de départ, à enrichir)
**Budget du quotidien** : la prime de fin d'année qui arrive · payer en 3 ou 4 fois pendant les soldes · le leasing de la voiture neuve · la carte de crédit et son solde reporté · l'abonnement oublié · le 13e mois · le pécule de vacances · le premier salaire · emménager seul(e) · épargne de précaution : combien de mois ?
**Bourse** : premier achat d'ETF avec 50 € par mois · le prix d'une action « pas chère » · vendre dans la panique après une baisse · le fonds proposé par le conseiller de la banque · copier un ami qui a « tout gagné » · attendre le « bon moment » pour commencer · l'épargne-pension de fin d'année
**Crypto ou arnaque** : le message d'un inconnu qui a « doublé son argent » · le faux support · la plateforme non agréée · l'adresse de portefeuille copiée-collée · le « match » qui parle de crypto · le placement « garanti » à 12 % · l'influenceur qui vend une formation trading
