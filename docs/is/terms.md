---
title: "Skilmálar og leyfi"
nav_order: 9
lang: "is"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Skilmálar og leyfi {#terms-and-licence}

## Skilmálar Wargaming {#wargamings-terms}

Lesið 2026-11-07, Wargaming EULA útgáfa 14 (í gildi frá 10. apríl 2024, skráð
sem núverandi); kafli 12.3 í henni vísar á reglur um viðbætur (mods) fyrir World of Warships, en sú
síða birtist ekki utan vafra og var ekki lesin:

- 5.3 (b): nema með skriflegri heimild máttu ekki "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): bannað er "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Það sem þessi umbreytir gerir: hann les skrá sem leikurinn skrifaði, eftir bardagann,
utan leiksins. Hann breytir engu í leiknum, talar við engan þjón og
sýnir ekkert meðan á bardaga stendur. Hann afkóðar strauminn með lykli leiksins,
sem hægt er að lesa 5.3 (b) og 12.1 (p) þannig að nái yfir. Notkun hans er ákvörðun
notandans; þess vegna er hann sérstakur pakki.

## Leyfi og heimildir {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Þarf numpy (BSD-3-Clause) og pyarrow
(Apache-2.0). Skrifað fyrir þetta verkefni: Blowfish dulmálið hér er eigið,
með töflur sínar reiknaðar úr tölustöfum pí eins og dulmálið skilgreinir þær.
Staðreyndir um sniðið eru almenn vitneskja meðal upptökuverkfæra; athugasemdin um
einingakvarðann er frá landaire/wows-toolkit (MIT). Enginn kóði var tekinn úr neinu
öðru verkefni.

`bigworld.py` og `table.py` eru sömu skrár og í World of Tanks
umbreytinum ([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); breyttu báðum saman.

---

Hluti af [3DHeat](https://github.com/Holdi601/3DHeat) ([skjölun](https://holdi601.github.io/3DHeat/)). Frumkóði: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
