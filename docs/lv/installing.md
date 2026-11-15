---
title: Uzstādīšana
nav_order: 3
lang: lv
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Uzstādīšana {#installing}

Jauns komandrindā? Vispirms izlasiet [Pirms sākat](before-you-start.md). Nepieciešams Python 3.10 vai jaunāks; numpy un pyarrow tiek uzstādīti kopā ar to.

## Soli pa solim {#step-by-step}

1. Iegūstiet kodu: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`, vai lejupielādējiet zip failu no [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases) un izpakojiet to.
2. Atveriet termināli šajā mapē un ierakstiet `pip install -e .`. Tas padara komandu `heat3d-wows-replay` pieejamu jūsu ceļā.
3. Pārbaudiet: `heat3d-wows-replay --version`. Vajadzētu redzēt `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` parāda iespējas:

![heat3d-wows-replay --help](../assets/img/help.svg)

Bez uzstādīšanas `python -m heat3d_ext_wows ...` rīka mapē dara to pašu.

3DHeat Watcher palaiž šo komandu jaunajiem atkārtojumiem, ja tas ir uzstādīts, un darbojas arī bez tā.

## Atjauninājumi {#updates}

Katrs starts vispirms pārbauda projekta GitHub izlaidumus (ne vairāk kā vienu pieprasījumu ik pēc dažām stundām; tas nekad nepārtrauc konvertēšanu, ar internetu vai bez tā). Kad ir jaunāks izlaidums, komanda pirms uzstādīšanas jautā: `git clone` kopiju atjauno ar `git pull --ff-only` (atsakās, ja ir vietējas izmaiņas), lejupielādētu kopiju — no izlaiduma arhīva. `HEAT3D_NO_UPDATE=1` izslēdz pārbaudi un atjaunināšanu.

---

Daļa no [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentācija](https://holdi601.github.io/3DHeat/)). Avots: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
