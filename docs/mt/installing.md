---
title: "Installazzjoni"
nav_order: 3
lang: mt
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Installazzjoni {#installing}

Ġdid mal-linja tal-kmandi? Aqra [Qabel ma tibda](before-you-start.md) l-ewwel.
Teħtieġ Python 3.10 jew aktar ġdid; numpy u pyarrow jiġu installati miegħu.

## Pass b'pass {#step-by-step}

1. Ġib il-kodiċi: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   jew niżżel zip minn [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   u ħollu.
2. Iftaħ terminal f'dak il-folder u ikteb `pip install -e .`. Dan ipoġġi l-kmand
   `heat3d-wows-replay` fil-path tiegħek.
3. Iċċekkjah: `heat3d-wows-replay --version`. Għandek tara
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` jelenka l-għażliet:

![heat3d-wows-replay --help](../assets/img/help.svg)

Mingħajr installazzjoni, `python -m heat3d_ext_wows ...` fil-folder tal-għodda
jagħmel l-istess.

Id-3DHeat Watcher iħaddem dan il-kmand fuq ripetizzjonijiet ġodda meta jkun
installat, u jaħdem mingħajru.

## Aġġornamenti {#updates}

Kull bidu l-ewwel jiċċekkja r-releases tal-proġett fuq GitHub (l-iktar talba
waħda kull ftit sigħat; qatt ma twaqqaf konverżjoni, online jew le). Meta toħroġ
release ġdida, il-kmand jistaqsi qabel jinstallaha: `git clone` jiġi aġġornat
b'`git pull --ff-only` (miċħud waqt li jkollok bidliet lokali), kopja niżżelta
mill-arkivju tar-release. `HEAT3D_NO_UPDATE=1` ixolji ċ-ċekk u l-aġġornament.

---

Parti mid-[3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentazzjoni](https://holdi601.github.io/3DHeat/)). Sors: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
