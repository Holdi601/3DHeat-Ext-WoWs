---
title: Инсталиране
nav_order: 3
lang: bg
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Инсталиране {#installing}

Нов ли сте в командния ред? Първо прочетете [Преди да започнете](before-you-start.md).
Нужен е Python 3.10 или по-нов; numpy и pyarrow се инсталират заедно с него.

## Стъпка по стъпка {#step-by-step}

1. Вземете кода: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   или изтеглете zip от [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   и го разархивирайте.
2. Отворете терминал в тази папка и напишете `pip install -e .`. Това поставя
   командата `heat3d-wows-replay` в пътя ви.
3. Проверете: `heat3d-wows-replay --version`. Трябва да видите
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` показва опциите:

![heat3d-wows-replay --help](../assets/img/help.svg)

Без инсталиране `python -m heat3d_ext_wows ...` в папката на инструмента върши
същото.

Watcher на 3DHeat пуска тази команда върху новите повторения, когато е инсталиран,
и работи и без нея.

## Обновявания {#updates}

При всеки старт първо се проверяват GitHub изданията на проекта (най-много една заявка
на няколко часа; никога не спира преобразуването, онлайн или офлайн). Когато има по-ново
издание, командата пита, преди да го инсталира: `git clone` се обновява с
`git pull --ff-only` (отказва, докато имате локални промени), а изтеглено копие – от
архива на издането. `HEAT3D_NO_UPDATE=1` изключва проверката и обновяването.

---

Част от [3DHeat](https://github.com/Holdi601/3DHeat) ([документация](https://holdi601.github.io/3DHeat/)). Източник: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
