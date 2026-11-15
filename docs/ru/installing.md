---
title: Установка
nav_order: 3
lang: "ru"
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Установка {#installing}

Впервые работаете с командной строкой? Сначала прочитайте [Перед началом](before-you-start.md).
Нужен Python 3.10 или новее; numpy и pyarrow устанавливаются вместе с ним.

## Пошагово {#step-by-step}

1. Получите код: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`
   или скачайте архив из [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   и распакуйте его.
2. Откройте терминал в этой папке и введите `pip install -e .`. Команда `heat3d-wows-replay`
   появится в вашем PATH.
3. Проверьте: `heat3d-wows-replay --version`. Вы должны увидеть
   `heat3d-wows-replay 0.1.0`. Команда `heat3d-wows-replay --help` покажет параметры:

![heat3d-wows-replay --help](../assets/img/help.svg)

Без установки то же самое делает `python -m heat3d_ext_wows ...` в папке инструмента.

Watcher 3DHeat запускает эту команду для новых реплеев, если он установлен, и работает и без неё.

## Обновления {#updates}

При каждом запуске сначала проверяются релизы проекта на GitHub (не чаще одного запроса в
несколько часов; проверка никогда не останавливает преобразование, онлайн или нет). Когда
выходит новый релиз, команда спрашивает, ставить ли его. Копия из `git clone` обновляется
командой `git pull --ff-only` (отказывается работать, пока есть локальные изменения), скачанная
копия — из архива релиза. Переменная `HEAT3D_NO_UPDATE=1` выключает и проверку, и обновление.

---

Часть [3DHeat](https://github.com/Holdi601/3DHeat) ([документация](https://holdi601.github.io/3DHeat/)). Исходный код: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
