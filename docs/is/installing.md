---
title: "Uppsetning"
nav_order: 3
lang: is
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Uppsetning {#installing}

Nýr í skipanalínunni? Lestu fyrst [Áður en þú byrjar](before-you-start.md).
Þarf Python 3.10 eða nýrra; numpy og pyarrow eru sett upp með því.

## Skref fyrir skref {#step-by-step}

1. Náðu í kóðann: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   eða sæktu zip úr [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   og pakkaðu því upp.
2. Opnaðu skipanaglugga í þeirri möppu og skrifaðu `pip install -e .`. Þetta setur
   skipunina `heat3d-wows-replay` í slóðina þína.
3. Athugaðu það: `heat3d-wows-replay --version`. Þú ættir að sjá
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` sýnir valkostina:

![heat3d-wows-replay --help](../assets/img/help.svg)

Án uppsetningar gerir `python -m heat3d_ext_wows ...` í möppu verkfærisins
það sama.

3DHeat Watcher keyrir þessa skipun á nýjum upptökum þegar hann er uppsettur,
og virkar án hennar.

## Uppfærslur {#updates}

Við hverja ræsingu er fyrst athugað með útgáfur verkefnisins á GitHub (í mesta
lagi ein beiðni á nokkurra klukkustunda fresti; það stöðvar aldrei breytingu,
hvort sem þú ert nettengdur eða ekki). Þegar nýrri útgáfa er komin spyr
skipunin áður en hún setur hana upp: `git clone` er uppfært með
`git pull --ff-only` (hafnað meðan þú ert með staðbundnar breytingar),
niðurhalað afrit úr safnskrá útgáfunnar. `HEAT3D_NO_UPDATE=1` slekkur á
athuguninni og uppfærslunni.

---

Hluti af [3DHeat](https://github.com/Holdi601/3DHeat) ([skjölun](https://holdi601.github.io/3DHeat/)). Frumkóði: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
