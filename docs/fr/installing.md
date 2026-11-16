---
title: Installation
nav_order: 3
lang: "fr"
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Installation {#installing}

Vous ne connaissez pas la ligne de commande ? Lisez d'abord [Avant de commencer](before-you-start.md).
Il faut Python 3.10 ou plus récent ; numpy et pyarrow sont installés avec lui.

## Étape par étape {#step-by-step}

1. Récupérez le code : `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   ou téléchargez un zip depuis [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   et décompressez-le.
2. Ouvrez un terminal dans ce dossier et tapez `pip install -e .`. Cela place la commande
   `heat3d-wows-replay` dans votre PATH.
3. Vérifiez : `heat3d-wows-replay --version`. Vous devez voir
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` liste les options :

![heat3d-wows-replay --help](../assets/img/help.svg)

Sans installation, `python -m heat3d_ext_wows ...` dans le dossier de l'outil fait la même chose.

Le Watcher de 3DHeat lance cette commande sur les nouveaux replays lorsqu'il est installé, et
fonctionne sans elle.

## Mises à jour {#updates}

Chaque démarrage consulte d'abord les versions publiées du projet sur GitHub (au plus une
requête toutes les quelques heures ; cela n'arrête jamais une conversion, en ligne ou non).
Lorsqu'une version plus récente est disponible, la commande demande avant de l'installer : un
`git clone` est mis à jour avec `git pull --ff-only` (refusé tant que vous avez des modifications
locales), une copie téléchargée est remplacée par l'archive de la version. `HEAT3D_NO_UPDATE=1` désactive
la vérification et la mise à jour.

---

Une partie de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source : [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
