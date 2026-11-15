---
title: "Умови і ліцензія"
nav_order: 9
lang: uk
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Умови і ліцензія {#terms-and-licence}

## Умови Wargaming {#wargamings-terms}

Прочитано 2026-11-07, Wargaming EULA версії 14 (чинна з 10 квітня 2024 року, назва
як поточна). Її розділ 12.3 посилається на правила модифікацій World of Warships; ця
сторінка поза браузером не відобразилася, тож її не прочитано:

- 5.3 (b): без письмового дозволу не можна "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): заборонено "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Що робить цей конвертер: він читає файл, який записала гра, після бою, поза грою.
Він нічого не змінює в грі, не розмовляє з жодним сервером і нічого не показує під
час бою. Він дешифрує потік ключем гри, і пункти 5.3 (b) і 12.1 (p) можна прочитати
так, що вони це охоплюють. Користуватися ним — рішення користувача; тому він
окремий пакет.

## Ліцензія і джерела {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Потрібні numpy (BSD-3-Clause) і pyarrow
(Apache-2.0). Написано для цього проєкту: шифр Blowfish тут власний, а його таблиці
обчислено з цифр числа пі, як того вимагає сам шифр. Відомості про формат —
загальновідомі серед інструментів для повторів; примітка про масштаб одиниць
походить із landaire/wows-toolkit (MIT). Код з жодного іншого проєкту не взято.

`bigworld.py` і `table.py` — ті самі файли, що й у конвертері World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); змінюйте їх разом.

---

Частина [3DHeat](https://github.com/Holdi601/3DHeat) ([документація](https://holdi601.github.io/3DHeat/)). Джерело: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
