---
title: "Telepítés"
nav_order: 3
lang: hu
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Telepítés {#installing}

Új vagy a parancssorban? Olvasd el előbb a [Mielőtt elkezded](before-you-start.md) oldalt.
Python 3.10 vagy újabb kell hozzá; a numpy és a pyarrow vele együtt települ.

## Lépésről lépésre {#step-by-step}

1. Szerezd meg a kódot: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   vagy töltsd le a zip-et a [Kiadások](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   oldalról, és csomagold ki.
2. Nyiss egy terminált ebben a mappában, és írd be: `pip install -e .`. Ez a
   `heat3d-wows-replay` parancsot teszi elérhetővé a PATH-odon.
3. Ellenőrizd: `heat3d-wows-replay --version`. Ezt kell látnod:
   `heat3d-wows-replay 0.1.0`. A `heat3d-wows-replay --help` felsorolja a kapcsolókat:

![heat3d-wows-replay --help](../assets/img/help.svg)

Telepítés nélkül az eszköz mappájában a `python -m heat3d_ext_wows ...` ugyanezt csinálja.

A 3DHeat Watcher ezt a parancsot futtatja az új visszajátszásokon, ha telepítve van,
és enélkül is működik.

## Frissítések {#updates}

Minden indításkor először ellenőrzi a projekt GitHub-kiadásait (legfeljebb néhány óránként
egy kérés; soha nem állítja le a konvertálást, online vagy offline). Ha újabb kiadás van,
a parancs a telepítés előtt megkérdezi: a `git clone` másolatot a `git pull --ff-only`
paranccsal frissíti (megtagadja, ha van helyi módosításod), a letöltött másolatot pedig a
kiadás archívumából. A `HEAT3D_NO_UPDATE=1` kikapcsolja az ellenőrzést és a frissítést.

---

A [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentáció](https://holdi601.github.io/3DHeat/)) része. Forrás: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
