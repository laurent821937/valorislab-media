# Brief de refonte des carrousels automatiques VALORISLAB

Version 2026-11-20. Remplace la ligne éditoriale et la charte de couverture actuelles de la routine « Caroussel ». Les règles de conformité existantes restent inchangées (sources officielles, chiffres calculés en Python, mention « Contenu éducatif, pas un conseil financier », jamais de promesse de gain).

## 1. Pourquoi on change

Constat du 17 au 20/11/2026 (Buffer) :

* Carrousels automatiques : portée de 0 à 14 personnes par post.
* Vidéos où Laurent parle : 200 à 300 personnes par post, soit environ 20 fois plus.
* Zéro commentaire sur « Commente GUIDE » : aucun message automatique n'envoie le lien.
* Couvertures toutes identiques (fond noir, titre en haut, photo d'objet en bas) : elles ressemblent à une publicité de banque et ne stoppent pas le scroll.

Objectif de la refonte : faire swiper jusqu'à la dernière slide (rétention) et rendre chaque post reconnaissable comme du VALORISLAB (marque).

## 2. Les 8 formats de rétention

Chaque semaine, la routine choisit 3 formats différents parmi ces 8. Jamais deux fois le même format dans la même semaine. Chaque format repose sur un mécanisme qui oblige à swiper.

### F1. La boucle ouverte

* Mécanisme : la couverture pose une question, la réponse n'arrive qu'à l'avant-dernière slide.
* Couverture : « Une seule de ces 3 dépenses te coûte 4 000 € sur 10 ans. Laquelle ? »
* Slides : les 3 options, un indice, la révélation chiffrée, la leçon.
* Règle : la réponse ne doit jamais être devinable sur la couverture.

### F2. Le tribunal du mythe

* Mécanisme : une idée reçue est « jugée » et reçoit un verdict : VRAI, FAUX ou ÇA DÉPEND.
* Couverture : un tampon visuel « VERDICT ? » et la phrase-mythe entre guillemets. Ex. : « Il faut beaucoup d'argent pour investir. »
* Slides : l'accusation, la défense, la preuve chiffrée, le verdict (tampon), ce qu'il faut retenir.
* Règle : privilégier « ÇA DÉPEND » quand c'est la réalité, conformément à la règle « expliquer des différences de démarche plutôt qu'une opposition absolue ».

### F3. Le dossier

* Mécanisme : un cas fictif comme un dossier d'enquête. Le lecteur se demande ce qu'il ferait.
* Couverture : « DOSSIER n° 07 · Sarah, 26 ans, 1 900 € net. Elle veut commencer à investir. Par quoi commencer ? »
* Slides : la situation, les 3 options possibles, ce qui coince dans chacune, la méthode (pas une recommandation personnelle).
* Règle : profil explicitement fictif, mention « Cas fictif » visible sur la couverture. Numérotation continue des dossiers : la série crée un rendez-vous.

### F4. Trouve l'erreur

* Mécanisme : un document du quotidien contient une erreur coûteuse, le lecteur la cherche.
* Couverture : « Ce relevé cache une erreur qui coûte 300 €/an. Tu la vois ? »
* Slides : le document (relevé de frais, simulation de crédit, ordre de bourse), un indice, l'erreur entourée, le calcul, le réflexe à prendre.
* Règle : document visiblement fictif (aucun logo, nom ou numéro réel, mention « Document fictif » sur le visuel).

### F5. Le classement révélé

* Mécanisme : un classement qui se dévoile de la dernière à la première place. La première place est sur la dernière slide.
* Couverture : « 6 façons de laisser dormir 5 000 € en Belgique. Classées de la pire à la meilleure. »
* Slides : place 6 à place 1, chacune avec le chiffre de l'année (inflation, taux du compte d'épargne réglementé, etc.).
* Règle : critère de classement unique et explicite (ex. pouvoir d'achat après 5 ans). Données officielles datées. Pas de classement sur des rendements futurs.

### F6. La facture cachée

* Mécanisme : le prix affiché contre le prix réel, ligne par ligne, comme un ticket de caisse qui s'allonge.
* Couverture : un ticket avec « Prix affiché : 999 € » et « Prix réel : ? »
* Slides : chaque ligne qui s'ajoute (intérêts, frais, assurance, taxe), le total, la question à poser avant de signer.
* Sujets : crédit à la consommation, leasing, paiement fractionné, frais d'un fonds bancaire, carte de crédit.

### F7. Le message suspect

* Mécanisme : une conversation fictive façon messagerie, le lecteur repère le piège.
* Couverture : une bulle de message : « Salut ! J'ai doublé mon argent en 3 semaines, je te montre ? »
* Slides : la conversation qui avance, chaque signal d'alerte surligné, ce que dit la FSMA, quoi faire.
* Règle : conversation fictive, aucun nom réel ni plateforme réelle. Source FSMA citée.

### F8. L'épisode du protagoniste

* Mécanisme : une série. Le protagoniste VALORISLAB vit une situation d'argent, épisode après épisode, et fait une erreur que le lecteur voit venir.
* Couverture : « Épisode 4 · Il vient de toucher sa prime de fin d'année. Il a déjà une idée. Mauvaise idée. »
* Slides : la situation, la décision, la conséquence chiffrée, ce qu'il aurait dû faire, l'annonce de l'épisode suivant.
* Règle : récit à la 3e personne, tiré des 20 erreurs du guide (l'erreur correspondante est citée sur la dernière slide). C'est la passerelle naturelle vers le guide.

## 3. Règles de choix des sujets

1. Le sujet part d'une situation vécue, jamais d'une notion. « Tu viens de recevoir ta prime » plutôt que « Qu'est-ce que le précompte mobilier ».
2. Le calendrier compte : primes de décembre, soldes, déclaration fiscale (mai-juin), rentrée, Black Friday, 13e mois, pécule de vacances.
3. Chaque sujet est rattaché à l'une des 20 erreurs du guide. La dernière slide la nomme : « C'est l'erreur n° X du guide gratuit. »
4. Interdit : les sujets déjà publiés (contrôle `state/history.json`), et les sujets purement techniques sans enjeu personnel (TOB seule, domiciliation d'ETF seule, taxe Reynders seule). Ces notions peuvent apparaître à l'intérieur d'un format, jamais comme sujet principal.
5. Répartition par semaine : 1 sujet Bourse, 1 sujet Crypto ou arnaque, 1 sujet budget du quotidien.

## 4. Charte de couverture (nouveau rendu)

* Titre : 50 à 60 % de la hauteur, 4 lignes maximum, 12 mots maximum. Corps minimum 110 px sur 1080 de large.
* Chiffre clé : quand il existe, il est le plus grand élément de la couverture.
* Sous-titre : 6 mots maximum, ou rien.
* Visage : le protagoniste (rendu photo-réaliste, jamais détouré) apparaît sur une couverture sur deux. Les autres couvertures utilisent l'élément visuel du format (tampon VERDICT, ticket, bulle de message, dossier).
* Alternance des fonds : sombre (noir chaud, comme aujourd'hui) et clair (ivoire `#F3EEE4`, texte anthracite, accent or foncé `#89692F`), en alternance d'un post à l'autre. Le fil ne doit jamais montrer deux couvertures identiques côte à côte.
* Supprimé : la date, la mention « Finance Belgique », le logo complet en haut. Conservé : un petit monogramme VALORISLAB en bas à gauche, le compteur « 1/6 ».
* Marqueur de format : une petite étiquette en haut à gauche avec le nom du format (« DOSSIER n° 07 », « LE TRIBUNAL DU MYTHE », « ÉPISODE 4 »). C'est le signe de reconnaissance de la marque.
* Zone de sécurité TikTok inchangée : rien dans les 160 px du bas.

## 5. Règles des slides intérieures

* Une seule idée par slide, 25 mots maximum.
* Chaque slide se termine par une raison de swiper : question, « La suite va te surprendre », flèche, compteur.
* La révélation (réponse, verdict, première place) est toujours sur l'avant-dernière slide.
* Entre 5 et 7 slides.

## 6. Dernière slide et légende

* Dernière slide : « C'est l'erreur n° X des 20 erreurs du guide. Guide gratuit, lien dans ma bio. » Puis valorislab.be et la mention « Contenu éducatif, pas un conseil financier ».
* Légende : 3 lignes maximum avant le « … plus », puis la source et la mention. Dernière ligne : « Guide gratuit : lien dans ma bio. »
* Supprimé : « Commente GUIDE » et toute demande de commentaire liée à l'envoi d'un lien, tant qu'aucun envoi automatique en message privé n'est en place.
* Une seule question d'engagement par légende, liée au format (« Tu avais trouvé l'erreur ? », « Ton verdict ? »).

## 7. Score de viralité : nouveaux critères

Remplacer la grille actuelle par ces critères, seuil maintenu à 70/100 :

* Mécanisme de rétention clair et tenu jusqu'à l'avant-dernière slide : 25
* Couverture lisible en 1 seconde sur un téléphone (titre ≤ 12 mots, chiffre visible) : 20
* Situation vécue par un débutant (et non une notion) : 20
* Différent des 3 derniers posts publiés (format, fond, visuel) : 15
* Lien explicite avec une erreur du guide : 10
* Conformité (sources, mention, pas de promesse) : 10, éliminatoire si absent

## 8. Mesure

* Toutes les 2 semaines : portée moyenne et taux de swipe jusqu'à la dernière slide par format (via Buffer), clics sur le lien en bio par réseau.
* Après 4 semaines : on garde les 4 formats les plus performants et on retire les autres.
