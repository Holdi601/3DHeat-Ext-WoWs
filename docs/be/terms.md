---
title: "Умовы і ліцэнзія"
nav_order: 9
lang: "be"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Умовы і ліцэнзія {#terms-and-licence}

## Умовы Wargaming {#wargamings-terms}

Прачытана 2026-11-07, EULA Wargaming версіі 14 (дзейнічае з 10 красавіка 2024,
пазначана як бягучая); яе раздзел 12.3 спасылаецца на палітыку модаў World of
Warships, старонка якой не адлюстроўвалася па-за браўзерам і не была прачытана:

- 5.3 (b): калі няма пісьмовага дазволу, нельга "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): забаронена "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Што робіць гэты канвертар: ён чытае файл, які запісала гульня, пасля бою, па-за
гульнёй. Ён нічога не змяняе ў гульні, не звяртаецца да ніводнага сервера і
нічога не паказвае падчас бою. Ён расшыфроўвае струмень ключом гульні, што
5.3 (b) і 12.1 (p) можна прачытаць як ахопленае. Карыстацца ім - рашэнне
карыстальніка; таму гэта асобны пакет.

## Ліцэнзія і крыніцы {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Патрабуе numpy (BSD-3-Clause) і pyarrow
(Apache-2.0). Напісана для гэтага праекта: шыфр Blowfish тут уласны,
з табліцамі, вылічанымі з лічбаў пі так, як шыфр іх вызначае. Факты пра фармат -
агульныя веды сярод інструментаў запісаў; заўвага пра маштаб адзінак - з
landaire/wows-toolkit (MIT). Код з іншых праектаў не браўся.

`bigworld.py` і `table.py` - тыя ж файлы, што ў канвертары World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); мяняйце абодва разам.

---

Частка [3DHeat](https://github.com/Holdi601/3DHeat) ([дакументацыя](https://holdi601.github.io/3DHeat/)). Крыніца: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
