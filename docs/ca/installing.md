---
title: Instal·lació
nav_order: 3
lang: "ca"
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Instal·lació {#installing}

No n'has fet mai servir la línia d'ordres? Llegeix primer [Abans de començar](before-you-start.md).
Cal Python 3.10 o posterior; numpy i pyarrow s'instal·len amb ell.

## Pas a pas {#step-by-step}

1. Obtén el codi: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`, o descarrega un zip des de
   [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases) i descomprimeix-lo.
2. Obre un terminal en aquesta carpeta i escriu `pip install -e .`. Això posa l'ordre
   `heat3d-wows-replay` al teu PATH.
3. Comprova-ho: `heat3d-wows-replay --version`. Hauries de veure `heat3d-wows-replay 0.1.0`.
   `heat3d-wows-replay --help` llista les opcions:

![heat3d-wows-replay --help](../assets/img/help.svg)

Sense instal·lar, `python -m heat3d_ext_wows ...` a la carpeta de l'eina fa el mateix.

El Watcher de 3DHeat executa aquesta ordre sobre les repeticions noves quan està instal·lat, i funciona
sense ella.

## Actualitzacions {#updates}

Cada inici consulta primer les versions de GitHub del projecte (com a molt una petició cada unes quantes
hores; mai no atura una conversió, estigui en línia o no). Quan hi ha una versió nova, l'ordre pregunta
abans d'instal·lar-la: un `git clone` s'actualitza amb `git pull --ff-only` (es nega si tens canvis
locals), i una còpia descarregada, des de l'arxiu de la versió. `HEAT3D_NO_UPDATE=1` desactiva la consulta
i l'actualització.

---

Part de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentació](https://holdi601.github.io/3DHeat/)). Font: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
