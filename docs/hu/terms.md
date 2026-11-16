---
title: "Feltételek és licenc"
nav_order: 9
lang: "hu"
source: terms.md
source_hash: "0b8a5164046e"
nav_exclude: true
search_exclude: true
---
# Feltételek és licenc {#terms-and-licence}

## Mit olvas {#what-it-reads}

A konverter azokat a visszajátszásfájlokat olvassa, amelyeket a játék a saját
számítógépedre írt, a csata után és a játékon kívül. Semmit nem változtat a
játékban, egyetlen szerverrel sem kommunikál, és csata közben semmit nem
jelenít meg. A játékból semmi nem kerül vele szállításra vagy
továbbterjesztésre: sem játékerőforrás, sem játékkód, sem DLL. Amit ír, a te
számítógépeden marad.

A 3DHeat nem áll kapcsolatban a Wargaminggel, és a Wargaming nem támogatja. A
World of Warships és a kapcsolódó nevek és védjegyek a tulajdonosaikat
illetik.

Jogtulajdonosok: nyissanak egy issue-t itt:
<https://github.com/Holdi601/3DHeat-Ext-WoWs/issues> - gyorsan válaszolunk, és
kérésre bármit eltávolítunk.

## Licenc és források {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). A numpy
(BSD-3-Clause) és a pyarrow (Apache-2.0) csomagokat használja. Ez a projekthez készült: az itteni
Blowfish-titkosítás saját, a táblázatait pedig a pi jegyeiből számoljuk, ahogy a titkosítás
előírja. A formátum tényei közismertek a visszajátszó-eszközök között; az egységmérték megjegyzése
a landaire/wows-toolkit (MIT) projektből való. Kódot más projektből nem vettünk át.

A `bigworld.py` és a `table.py` ugyanazok a fájlok, mint a World of Tanks konverterében
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); mindkettőt egyszerre módosítsd.

---

A [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentáció](https://holdi601.github.io/3DHeat/)) része. Forrás: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
