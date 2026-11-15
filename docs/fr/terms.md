---
title: Termes et licence
nav_order: 9
lang: fr
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Termes et licence {#terms-and-licence}

## Les conditions de Wargaming {#wargamings-terms}

Lues le 2026-11-07, EULA de Wargaming version 14 (en vigueur le 10 avril 2024, indiquée comme la version
actuelle) ; sa section 12.3 renvoie à une politique de mods de World of Warships, dont la page ne s'est pas
affichée hors d'un navigateur et n'a pas été lue :

- 5.3 (b) : sauf autorisation écrite, vous ne devez pas « ... decompile, disassemble, reverse engineer or
  otherwise make unauthorized use of the Content ».
- 12.1 (k) : est interdit « Creating, using, making available, or distributing any unauthorized software or
  tools, including hacks, cheats, exploits, scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including intercepts, emulates, or redirects any
  communication between such software and Wargaming. »
- 12.1 (l) : « ... any software designed to modify a Product and change the user experience ("mods") unless
  expressly permitted by Wargaming ».
- 12.1 (p) : « Circumventing or bypassing enforcement and security measures implemented by Wargaming ».

Ce que fait ce convertisseur : il lit un fichier que le jeu a écrit, après la bataille, hors du jeu. Il ne
modifie rien dans le jeu, ne parle à aucun serveur, et n'affiche rien pendant une bataille. Il déchiffre
bien le flux avec la clé du jeu, ce que les points 5.3 (b) et 12.1 (p) peuvent couvrir. L'utiliser relève de la
décision de l'utilisateur ; c'est pour cela qu'il s'agit d'un paquet à part.

## Licence et sources {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Nécessite numpy
(BSD-3-Clause) et pyarrow (Apache-2.0). Écrit pour ce projet : le chiffrement Blowfish d'ici est le sien, ses
tables étant calculées à partir des chiffres de pi comme le définit le chiffrement. Les faits sur le format sont
des connaissances communes aux outils de replays ; la note sur l'échelle des unités vient de landaire/wows-toolkit
(MIT). Aucun code n'a été repris d'un autre projet.

`bigworld.py` et `table.py` sont les mêmes fichiers que dans le convertisseur de World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)) ; modifiez les deux ensemble.

---

Une partie de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source : [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
