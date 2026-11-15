---
title: Comment le replay est lu
nav_order: 7
lang: "fr"
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Comment le replay est lu {#how-it-reads-a-replay}

Un replay est un en-tête de blocs JSON et le flux de paquets du jeu (notes sur le format dans
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)) :

- Le premier bloc, en clair : la carte, la version du client, le joueur qui enregistre et son navire, et la
  liste des joueurs - le nom de chacun, allié ou ennemi, et son numéro de navire. Les clients récents (15.x)
  ajoutent deux blocs : un vide, et le compte du joueur qui enregistre et l'identifiant de la bataille en texte,
  lus dans `blockIds`. Les résultats ne sont pas dans le JSON ; la 15.x les garde dans le flux.
- Le flux de paquets, compressé en zlib et chiffré en Blowfish avec une clé que le jeu contient, et que les
  outils communautaires qui lisent ces fichiers ont publiée. Une fois déchiffré, il contient :
  - les mises à jour de position du moteur de chaque navire que le client pouvait voir (celui de sa propre
    équipe pendant toute la bataille, les ennemis lorsqu'ils sont repérés ou à proximité), plusieurs fois par
    seconde lorsqu'ils bougent, et moins souvent lorsqu'ils ne bougent pas ;
  - le navire propre du joueur qui enregistre, dans un paquet à part, environ sept fois par seconde ;
  - une seule fois, au début, les fiches des joueurs sous forme de liste Python pickle. Elles disent quelle
    entité du flux correspond à quel joueur. Leurs clés sont numérotées, et les numéros changent avec les
    patchs ; le lecteur trouve donc les clés d'après leurs valeurs : la clé qui contient les noms de la liste,
    et la clé qui contient les entités ayant des mises à jour de position ;
  - l'appel du serveur qui indique au client qu'un navire a coulé : victime, tueur, cause. Il est trouvé par sa
    forme (douze octets ; les deux premiers sont des entités de navire ; chaque victime n'apparaît qu'une fois),
    non par son numéro ;
  - les dégâts de chaque navire : un tableau de (attaquant, dégâts) par impact, sur le navire touché ; et ses
    points de vie, une propriété fixée un instant avant ;
  - chaque salve d'obus et de torpilles dont le client a été informé : le type d'obus, le tireur, la salve, et le
    départ et la vitesse de chaque obus ou torpille ;
  - les lieux où les obus se sont arrêtés : le tireur, un type d'impact, et l'endroit de chacun (sur les clients
    15.x avec davantage d'informations sur l'obus au point d'impact, qui sont sautées) ;
  - le chat : expéditeur, canal, ligne ;
  - les appels pickle destinés au joueur qui enregistre : ses statistiques de dégâts, les mises à jour des fiches
    des joueurs, l'état de la bataille ;
  - sur les clients 15.x, les résultats de la bataille à la fin : un paquet à part, un objet JSON avec l'identifiant
    de la bataille, lu en entier dans `results` du document de match (les listes propres au jeu, sans nom :
    `commonList`, `privateDataList`, `playersPublicInfo` par compte, ...).

Les numéros de paquets et de méthodes qui diffèrent selon les versions contrôlées (le paquet du navire propre
est 43 ou 44, l'appel de naufrage 76 ou 83, les obus 101, 102, 126 ou 127) sont tous trouvés par leur forme - voir
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) -
de sorte qu'un patch qui les renumérote ne vide pas la table. Les numéros trouvés figurent dans le `decoded` du
document de match.

**Le pickle n'est pas une donnée de confiance.** Un replay est un fichier venu de n'importe où, et un pickle peut
nommer du code à exécuter. Il est chargé avec un dépickleur qui remet à chaque classe ou fonction que le pickle
nomme une coquille inerte, de sorte qu'il ne construit que des données simples, et rien d'autre. Un test lui
fournit un pickle qui appelle `os.system`.

**Les naufrages** ont l'heure exacte de l'appel. Leur lieu est l'endroit où la victime a été vue en dernier,
lorsque c'était moins de cinq secondes avant. **Le début de la bataille** est le premier instant où un navire
bouge (les navires restent immobiles pendant le compte à rebours).

Tout ce qui n'est pas une ligne de table se trouve dans [le document de match](match-document.md).

**Ce que le client a reçu** est complet pour sa propre équipe, et partiel pour les ennemis : leurs tirs, impacts
et points de vie y sont lorsqu'ils étaient à portée.

**Non lu :**

- Les avions et leurs escadrilles (les appels qui les portent n'ont pas été démontés), les mises à jour de vision
  de la minicarte (compressées), le repérage, les rubans, les incendies et les voies d'eau comme événements
  propres (leurs dégâts sont dans les impacts), les consommables, les points de capture et les scores d'équipe
  (propriétés d'entités sans définition, non distinguées par leur forme), le reste des propriétés d'un navire
  (visée, gouvernail, réglage de vitesse...).
- Les numéros des clés des fiches des joueurs et des statistiques de dégâts en noms : le jeu les numérote, et les
  numéros changent ; ils sont conservés comme des numéros.
- Les données supplémentaires d'un obus à son point d'impact (15.x) et les octets qui suivent le départ et la
  vitesse d'un obus ou d'une torpille.
- Les résultats des clients antérieurs à 15.x : leurs replays n'en contiennent aucun.
- Le numéro de navire en nom : les noms sont dans les fichiers de paramètres du jeu, non dans le replay.

## Comment la lecture a été vérifiée {#how-the-reading-was-checked}

La lecture a été vérifiée sur des replays publics de clients de la 0.9 à la 15.x, chaque valeur par rapport à
quelque chose que le replay donne une seconde fois :

- **Positions :** l'entité de chaque navire correspond à un nom de la liste ; les caps concordent avec la
  direction de déplacement à 0,1 rad près ; après son naufrage, un navire se déplace de moins de 0,1 unité. Un
  navire immobile est mis à jour moins souvent.
- **Points de vie :** chaque navire coulé dans la vue du client finit à 0 point de vie. Environ la moitié de
  tous les impacts correspondent à une baisse de points de vie dans la seconde précédente ; les autres
  coïncident avec des réparations ou d'autres impacts.
- **Dégâts par rapport aux statistiques du jeu :** sur le client le plus récent, les dégâts lus pour le joueur qui
  enregistre sont à 0,1 % près des statistiques. Sur les clients plus anciens, les statistiques sont plus hautes :
  le client ne reçoit pas chaque impact, ou les statistiques comptent davantage que des impacts (non résolu).
- **Obus :** un obus part à quelques unités de la dernière position connue de son navire (les canons sont répartis
  le long de la coque) ; presque chaque fin d'obus suit, dans la minute, un tir que le client a vu.

Les tests construisent des replays selon la même disposition, de sorte qu'aucun vrai replay n'est conservé dans
ce dépôt.

**Non vérifié :** les clients antérieurs à 0.9.6, le client Lesta (Mir Korabley), les opérations et scénarios
au-delà d'un seul, les batailles de clan et classées, et le numéro de navire qui correspond à quel navire.

---

Une partie de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source : [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
