---
title: Pojmovi i licenca
nav_order: 9
lang: "hr"
source: terms.md
source_hash: "0b8a5164046e"
nav_exclude: true
search_exclude: true
---
# Pojmovi i licenca {#terms-and-licence}

## Što čita {#what-it-reads}

Pretvarač čita datoteke snimki koje je igra zapisala na vašem vlastitom
računalu, nakon bitke i izvan igre. Ne mijenja ništa u igri, ne komunicira ni
s jednim poslužiteljem i ne prikazuje ništa tijekom bitke. Ništa iz igre ne
isporučuje se niti dalje distribuira s njim: nema resursa igre, koda igre ni
DLL-ova. Ono što zapiše ostaje na vašem računalu.

3DHeat nije povezan s Wargamingom niti ga Wargaming podržava. World of
Warships i povezani nazivi i zaštitni znakovi pripadaju svojim vlasnicima.

Nositelji prava: otvorite issue na
<https://github.com/Holdi601/3DHeat-Ext-WoWs/issues> - brzo odgovaramo i na
zahtjev uklanjamo bilo što.

## Licenca i izvori {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Treba numpy (BSD-3-Clause) i pyarrow
(Apache-2.0). Napisano za ovaj projekt: Blowfish šifra ovdje je vlastita, s tablicama izračunatim iz znamenki broja pi
kako ih šifra definira. Činjenice o formatu su opće poznate među alatima za snimke; bilješka o mjerilu jedinica
je iz landaire/wows-toolkit (MIT). Nijedan kod nije uzet iz nekog drugog projekta.

`bigworld.py` i `table.py` su iste datoteke kao u pretvaraču za World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); mijenjaj ih oba zajedno.

---

Dio [3DHeata](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Izvor: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
