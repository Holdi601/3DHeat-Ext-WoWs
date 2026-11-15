---
title: "Инсталирање"
nav_order: 3
lang: mk
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Инсталирање {#installing}

Нови сте со командната линија? Прво прочитајте [Пред да започнете](before-you-start.md). Потребен е Python 3.10 или понов; numpy и pyarrow се инсталираат заедно со него.

## Чекор по чекор {#step-by-step}

1. Земете го кодот: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`, или преземете zip од [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases) и распакувајте го.
2. Отворете терминал во таа папка и напишете `pip install -e .`. Ова ја става командата `heat3d-wows-replay` на вашата патека.
3. Проверете: `heat3d-wows-replay --version`. Треба да видите `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` ги наведува опциите:

![heat3d-wows-replay --help](../assets/img/help.svg)

Без инсталирање, `python -m heat3d_ext_wows ...` во папката на алатката прави исто.

3DHeat Watcher ја стартува оваа команда врз нови снимки кога е инсталиран, а работи и без неа.

## Ажурирања {#updates}

Секој почеток прво ги проверува GitHub изданијата на проектот (најмногу едно барање на неколку часа; никогаш не го запира претворањето, со или без интернет). Кога има ново издание, командата прашува пред да го инсталира: `git clone` се ажурира со `git pull --ff-only` (одбива додека имате локални промени), а преземена копија од архивата на изданието. `HEAT3D_NO_UPDATE=1` ги исклучува проверката и ажурирањето.

---

Дел од [3DHeat](https://github.com/Holdi601/3DHeat) ([документација](https://holdi601.github.io/3DHeat/)). Извор: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
