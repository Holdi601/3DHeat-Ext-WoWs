---
title: Le document de partie
nav_order: 6
lang: "fr"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Le document de partie {#the-match-document}

`<match>.match.json` contient tout ce que dit le replay et qui n'est pas une ligne de la table.
L'onglet Match du visualiseur le lit. (Le code l'appelle le résumé.)

![Le début d'un document de partie synthétique, et ses clés](../assets/img/match-document.svg)

## La bataille {#the-battle}

| Clé | Contenu |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships` ; l'identifiant de la bataille ; la carte telle que le jeu la nomme (`spaces/<map>`) et son nom affiché |
| `clientVersion`, `streamVersion` | la version du jeu d'après l'en-tête, et telle que le flux de paquets la donne |
| `recorded` | le moment où le replay a été enregistré, tel que le jeu l'écrit |
| `player`, `vehicle` | le joueur qui enregistre et son navire |
| `gameType`, `scenario` | le type de bataille (`RandomBattle`, ...) et le scénario, d'après l'en-tête |
| `duration` | la limite de temps de la bataille en secondes, d'après l'en-tête |
| `truncated` | l'enregistrement s'est arrêté tôt |
| `battleStart`, `recordingSeconds` | le début de la bataille (le premier instant où un navire bouge) et la durée de l'enregistrement, en secondes |
| `positionPacket`, `ownPositionPacket` | les numéros de paquets d'où viennent les positions : celles des autres navires, celle du joueur qui enregistre |
| `deathMethod` | le numéro de méthode où les naufrages ont été trouvés |
| `hz`, `ownHz`, `positions` | échantillons par seconde des autres navires et du navire propre ; lignes de position |
| `units` | unités du monde (15 m selon les coques, 30 m selon les portées du jeu) ; x vers l'est, y vers le haut, z vers le nord |
| `events` | le nombre de lignes de la table pour chaque événement |
| `decoded` | les numéros de méthode et de paquet trouvés pour chaque type de message |

## Joueurs et événements {#players-and-events}

| Clé | Contenu |
|---|---|
| `players` | une entrée par navire : nom, `ally` ou `enemy`, numéro et nom du navire, entité, échantillons, frags, survie ; `seen` (dégâts infligés et reçus, obus, torpilles et dernier point de vie que le client a vus) ; `header` (l'entrée de la liste) et `record` (la fiche du joueur tirée du flux, par numéro de clé) |
| `kills` | chaque naufrage : heure, victime, tueur, numéro de cause, lieu |
| `chat` | chaque ligne de chat, avec le canal et l'expéditeur |
| `damageStats` | les statistiques propres du joueur qui enregistre, telles que le jeu les tient : par arme et par genre, un compte et une quantité (le genre 0 correspond aux dégâts infligés) |
| `avatarPickles` | chaque appel pickle destiné au joueur qui enregistre, décodé, par numéro de méthode |

## En-tête, résultats et contrôles {#header-results-and-checks}

| Clé | Contenu |
|---|---|
| `header` | le premier bloc JSON, en entier sauf la liste des joueurs : mode de jeu, météo, bordure de carte, tailles des équipes et plus |
| `moreBlocks` | les blocs JSON après le premier, tels quels |
| `blockIds` | 15.x : le compte du joueur qui enregistre et l'identifiant de la bataille, lus comme du texte |
| `results` | 15.x : les résultats, que ces clients gardent dans le flux |
| `entities` | chaque entité que le flux crée : son numéro de type et son rôle, le moment où elle est entrée dans la vue du client et celui où elle en est sortie |
| `selfCheck` | le compte d'exhaustivité ([Exhaustivité](completeness.md)) et les contrôles des entités, des résultats, des identifiants et de la version |

---

Une partie de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source : [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
