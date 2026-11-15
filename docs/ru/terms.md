---
title: Условия и лицензия
nav_order: 9
lang: "ru"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Условия и лицензия {#terms-and-licence}

## Условия Wargaming {#wargamings-terms}

Прочитано 2026-11-07, Лицензионное соглашение Wargaming (EULA), версия 14 (действует с 10 апреля
2024, указана как текущая); его раздел 12.3 отсылает к правилам модов World of Warships, страница
которых не открылась вне браузера и не была прочитана:

- 5.3 (b): если нет письменного разрешения, нельзя "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): запрещено "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Что делает этот преобразователь: он читает файл, который записала игра, после боя, вне игры. Он
ничего не меняет в игре, не обращается ни к одному серверу и ничего не показывает во время боя.
Он расшифровывает поток ключом игры, и пункты 5.3 (b) и 12.1 (p) можно понимать так, что это под
них подпадает. Использовать его — решение пользователя; поэтому он выпущен отдельным пакетом.

## Лицензия и источники {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Нужны numpy (BSD-3-Clause) и pyarrow
(Apache-2.0). Написано для этого проекта: шифр Blowfish здесь собственный, его таблицы вычислены из
цифр числа пи, как того требует сам шифр. Сведения о формате известны всем инструментам для реплеев;
замечание о масштабе единиц взято из landaire/wows-toolkit (MIT). Код ни из какого другого проекта
не взят.

`bigworld.py` и `table.py` — те же файлы, что и в преобразователе World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); меняйте их оба вместе.

---

Часть [3DHeat](https://github.com/Holdi601/3DHeat) ([документация](https://holdi601.github.io/3DHeat/)). Исходный код: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
