---
title: "Potpunost"
nav_order: 8
lang: bs
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Potpunost {#completeness}

Ništa iz replaya se ne baca. Ono što konverter pročita ide u
tabelu i dokument meča; svaka druga stavka čuva se cijela u sidecar datoteci
`<match>.messages.parquet`; a `selfCheck.completeness` dokumenta meča
broji šta se desilo sa svakom vrstom stavke. To je pravilo koje dijele svi
3DHeat konverteri:
[Konverteri čuvaju sve](https://holdi601.github.io/3DHeat/converters.html).

![Samoprovjera sintetičkog replaya: svaka stavka viđena, pročitana, sačuvana ili izgubljena](../assets/img/completeness.svg)

## Broj {#the-count}

Za svaku vrstu stavke, `selfCheck.completeness.types` daje:

| Broj | Znači |
|---|---|
| `seen` | koliko ih replay sadrži |
| `decoded` | pročitano cijelo |
| `partial` | pročitano djelimično i sačuvano cijelo u sidecar datoteci |
| `raw` | samo sačuvano cijelo u sidecar datoteci, nije pročitano |
| `lost` | izgubljeno: uvijek `0` |

Vrste su vlastite vrste replaya: `block <n>` (JSON blokovi), vlastiti
bajtovi kontejnera, `packet <type>`, a za pozive na entitetima
`method <entity type>.<number>` i `property <entity type>.<number>`.
`selfCheck.entities.roles` kaže koji je tip entiteta avatar
igrača koji snima, a koji su brodovi. Vrsta za koju niko nije znao pojavi se sa svojim brojem.

## Sidecar {#the-sidecar}

| Kolona | Šta |
|---|---|
| `time` | sat replaya, kao u tabeli |
| `type`, `name` | vrsta stavke; kako je konverter naziva, gdje je čita |
| `entity` | brod ili avatar kojem pripada, kao `entity` tabele |
| `decoded` | šta je od nje pročitano, kao JSON |
| `payload`, `text` | njeni bajtovi, cijeli; JSON blokovi, cijeli |
| `entityType`, `packet`, `method` | brojevi |

Redovi su sortirani po paketu, metodi, entitetu i vremenu. Koji je entitet koji
igrač: `entities` i `players` dokumenta meča.

## Šta se čita i kako je provjereno {#what-is-read-and-how-it-was-checked}

- **Rezultati** (15.x, `results`): njihov id bitke je id toka, i
  svaki igrač u njima nalazi se na spisku iz zaglavlja.
- **Blok id-ova** (15.x, `blockIds`): račun i bitka, pročitani kao
  tekst da se nijedna cifra ne izgubi.
- **Pitch i roll** svake pozicije: roll ide uz brzinu skretanja,
  jer se brod naginje u zavoju; pitch je gotovo uvijek 0.
- **Entiteti** (`entities`): kada je svaki ušao u vidokrug klijenta i izašao.
  Nijedan brod nema poziciju između izlaska i povratka.
- **Verzija u toku** (`streamVersion`): ista kao ona iz zaglavlja.

Sve ostalo pročitano (potonuća, šteta, zdravlje, granate, torpeda, gdje su
granate završile, čet, pickled pozivi, zapisi igrača, pozicije) je
`partial`: u tabeli ili dokumentu meča, i sačuvano cijelo u
sidecar datoteci.

**Sačuvano ali nepročitano** (`raw`), najveće vrste: ažuriranja pozicija koja nisu u
tabeli (poslije potonuća broda, entiteti bez igrača), česta
svojstva i metode bez čitača, svojstva stvaranja entiteta
i svaki drugi paket bez čitača.

## Nije dostupno {#not-available}

- Ono što server nikad nije poslao klijentu koji snima: nišanjenje, kamera
  i unosi drugih igrača, neprijatelji dok su neotkriveni. Replay je ono što je
  rečeno jednom klijentu.
- Imena tipova entiteta, metoda, svojstava i ključeva statistike:
  nalaze se u definicijskim datotekama igre, a ne u replayu. Brojevi
  se čuvaju.
- Imena brodova za brojeve brodova (koristite `--ship-names`), i sve ostalo
  što traži vlastite datoteke igre.
- Rezultati klijenata prije 15.x: nisu u njihovim replayevima.

---

Dio [3DHeata](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Izvor: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
