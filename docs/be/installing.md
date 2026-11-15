---
title: "Усталёўка"
nav_order: 3
lang: be
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Усталёўка {#installing}

Вы новічок у камандным радку? Спачатку прачытайце [Перад пачаткам](before-you-start.md).
Патрэбны Python 3.10 або навейшы; numpy і pyarrow усталёўваюцца разам з ім.

## Крок за крокам {#step-by-step}

1. Атрымайце код: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`
   або спампуйце zip з [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   і распакуйце яго.
2. Адкрыйце тэрмінал у гэтай папцы і ўвядзіце `pip install -e .`. Гэта
   дадае каманду `heat3d-wows-replay` у ваш шлях.
3. Праверце: `heat3d-wows-replay --version`. Вы павінны ўбачыць
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` пералічвае параметры:

![heat3d-wows-replay --help](../assets/img/help.svg)

Без усталёўкі тое ж самае робіць `python -m heat3d_ext_wows ...` у папцы
інструмента.

3DHeat Watcher запускае гэтую каманду на новых запісах, калі ён усталяваны,
і працуе без яе.

## Абнаўленні {#updates}

Кожны запуск спачатку правярае рэлізы праекта ў GitHub (не болей за адзін
запыт на некалькі гадзін; ён ніколі не спыняе канвертаванне, ці ёсць сетка,
ці няма). Калі выйшаў навейшы рэліз, каманда пытаецца перад ўсталёўкай:
`git clone` абнаўляецца праз `git pull --ff-only` (адмаўляецца, пакуль у вас
ёсць лакальныя змены), спампаваная копія - з архіва рэлізу.
`HEAT3D_NO_UPDATE=1` выключае праверку і абнаўленне.

---

Частка [3DHeat](https://github.com/Holdi601/3DHeat) ([дакументацыя](https://holdi601.github.io/3DHeat/)). Крыніца: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
