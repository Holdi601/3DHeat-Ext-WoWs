---
title: "Встановлення"
nav_order: 3
lang: "uk"
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Встановлення {#installing}

Ви ще не працювали з командним рядком? Спочатку прочитайте
[Перш ніж почати](before-you-start.md).
Потрібен Python 3.10 або новіший; numpy і pyarrow встановлюються разом із ним.

## Крок за кроком {#step-by-step}

1. Отримайте код: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   або завантажте архів із [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   і розпакуйте його.
2. Відкрийте термінал у цій папці і введіть `pip install -e .`. Після цього команда
   `heat3d-wows-replay` працює з будь-якої папки.
3. Перевірте: `heat3d-wows-replay --version`. Ви маєте побачити
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` показує опції:

![heat3d-wows-replay --help](../assets/img/help.svg)

Без встановлення те саме робить `python -m heat3d_ext_wows ...` у папці інструмента.

Watcher 3DHeat запускає цю команду для нових повторів, коли вона встановлена, і
працює без неї.

## Оновлення {#updates}

Під час кожного запуску спочатку перевіряються релізи проєкту на GitHub (не
частіше ніж раз на кілька годин; це ніколи не зупиняє перетворення, онлайн чи
офлайн). Коли новіший реліз готовий, команда питає, чи встановлювати його:
`git clone` оновлюється через `git pull --ff-only` (відмовляє, поки є ваші
локальні зміни), завантажена копія — з архіву релізу. `HEAT3D_NO_UPDATE=1`
вимикає перевірку і оновлення.

---

Частина [3DHeat](https://github.com/Holdi601/3DHeat) ([документація](https://holdi601.github.io/3DHeat/)). Джерело: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
