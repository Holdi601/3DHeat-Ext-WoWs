---
title: Potpunost
nav_order: 8
lang: hr
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Potpunost {#completeness}

Ništa iz snimke se ne baca. Što pretvarač čita ide u tablicu i dokument meča; svaka druga stavka
čuva se cijela u pomoćnoj datoteci `<match>.messages.parquet`; a `selfCheck.completeness` dokumenta
meča broji što se dogodilo sa svakom vrstom stavke. Ovo je pravilo koje dijele svi pretvarači
3DHeata: [Pretvarači zadržavaju sve](https://holdi601.github.io/3DHeat/converters.html).

![Samoprovjera sintetičke snimke: svaka stavka viđena, pročitana, sačuvana ili izgubljena](../assets/img/completeness.svg)

## Brojanje {#the-count}

Za svaku vrstu stavke, `selfCheck.completeness.types` daje:

| Brojač | Znači |
|---|---|
| `seen` | koliko ih snimka sadrži |
| `decoded` | pročitano cijelo |
| `partial` | pročitano djelomično, i sačuvano cijelo u pomoćnoj datoteci |
| `raw` | samo sačuvano cijelo u pomoćnoj datoteci, nije pročitano |
| `lost` | izgubljeno: uvijek `0` |

Vrste su snimkine vlastite: `block <n>` (JSON blokovi), vlastiti bajtovi kontejnera, `packet <type>`, a za
pozive nad entitetima `method <entity type>.<number>` i `property <entity type>.<number>`.
`selfCheck.entities.roles` kaže koja vrsta entiteta je avatar igrača koji snima, a koja brodovi. Vrsta koju
nitko nije poznavao pojavi se sa svojim brojem.

## Pomoćna datoteka {#the-sidecar}

| Stupac | Što |
|---|---|
| `time` | sat snimke, kao u tablici |
| `type`, `name` | vrsta stavke; što je pretvarač zove, gdje je čita |
| `entity` | brod ili avatar kojem pripada, kao `entity` u tablici |
| `decoded` | što se od nje pročitalo, kao JSON |
| `payload`, `text` | njezini bajtovi, cijeli; JSON blokovi, cijeli |
| `entityType`, `packet`, `method` | brojevi |

Reci su poredane po paketu, metodi, entitetu i vremenu. Koji je entitet koji igrač: `entities` i `players`
dokumenta meča.

## Što se čita, i kako je provjereno {#what-is-read-and-how-it-was-checked}

- **Rezultati** (15.x, `results`): njihov id bitke je id iz toka, i svaki igrač u njima je u popisu iz zaglavlja.
- **Blok id-ova** (15.x, `blockIds`): račun i bitka, pročitani kao tekst da se nijedna znamenka ne izgubi.
- **Nagib i valjanje** svakog položaja: valjanje ide uz brzinu skretanja, kako se brod nagiba u zaokretu;
  nagib je gotovo uvijek 0.
- **Entiteti** (`entities`): kad je svaki ušao u pogled klijenta i kad je izašao. Nijedan brod nema
  položaj između odlaska i povratka.
- **Verzija u toku** (`streamVersion`): ista kao u zaglavlju.

Sve ostalo što je pročitano (potonuća, šteta, zdravlje, granate, torpeda, gdje su granate završile, razgovor,
pickle pozivi, zapisi igrača, položaji) je `partial`: u tablici ili dokumentu meča, i cijelo sačuvano u
pomoćnoj datoteci.

**Sačuvano, ali nepročitano** (`raw`), najveće vrste: ažuriranja položaja koja nisu u tablici (nakon što je
brod potonuo, entiteti bez igrača), česta svojstva i metode bez čitača, svojstva stvaranja entiteta, i svaki
drugi paket bez čitača.

## Nije dostupno {#not-available}

- Što poslužitelj nikad nije poslao klijentu koji snima: nišan, kamera i upravljanje drugih igrača,
  neprijatelji dok nisu uočeni. Snimka je ono što je jedan klijent dobio.
- Nazivi vrsta entiteta, metoda, svojstava i ključeva statistike: oni su u definicijskim datotekama igre,
  ne u snimci. Brojevi su sačuvani.
- Nazivi brodova za brojeve brodova (koristi `--ship-names`), i sve drugo što treba datoteke igre.
- Rezultati klijenata prije 15.x: u njihovim snimkama ih nema.

---

Dio [3DHeata](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Izvor: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
