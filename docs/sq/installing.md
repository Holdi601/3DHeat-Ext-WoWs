---
title: "Instalimi"
nav_order: 3
lang: "sq"
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Instalimi {#installing}

Je i ri me rreshtin e komandave? Lexo së pari [Para se të fillosh](before-you-start.md).
Ka nevojë për Python 3.10 ose më të ri; numpy dhe pyarrow instalohen bashkë me të.

## Hap pas hapi {#step-by-step}

1. Merr kodin: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   ose shkarko një zip nga [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   dhe shpaketoje.
2. Hap një terminal në atë dosje dhe shkruaj `pip install -e .`. Kjo e vendos
   komandën `heat3d-wows-replay` në shtegun tënd.
3. Kontrolloje: `heat3d-wows-replay --version`. Duhet të shohësh
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` liston opsionet:

![heat3d-wows-replay --help](../assets/img/help.svg)

Pa instalim, `python -m heat3d_ext_wows ...` në dosjen e mjetit bën të
njëjtën gjë.

3DHeat Watcher e nis këtë komandë mbi riluajtjet e reja kur është i instaluar,
dhe funksionon edhe pa të.

## Përditësimet {#updates}

Çdo nisje kontrollon së pari botimet e projektit në GitHub (më shumë se një kërkesë
çdo disa orë nuk bën; nuk e ndalon kurrë një konvertim, me internet apo pa). Kur ka dalë një
botim më i ri, komanda pyet përpara se ta instalojë: një `git clone` përditësohet
me `git pull --ff-only` (refuzohet derisa ke ndryshime lokale), një kopje e shkarkuar
nga arkivi i botimit. `HEAT3D_NO_UPDATE=1` e çaktivizon kontrollin dhe përditësimin.

---

Pjesë e [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacioni](https://holdi601.github.io/3DHeat/)). Burimi: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
