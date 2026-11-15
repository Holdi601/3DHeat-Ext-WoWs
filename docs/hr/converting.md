---
title: Pretvaranje snimki
nav_order: 4
lang: "hr"
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Pretvaranje snimki {#converting-replays}

## Korak po korak {#step-by-step}

1. **Uključi snimanje:** `isReplayEnabled` u `preferences.xml` igre, ili postavka same igre
   gdje je ima. Od tada igra sprema svaku bitku u mapu `replays` tvoje instalacije World of
   Warshipsa, na primjer `C:\Games\World_of_Warships_EU\replays`.
2. **Otvori terminal** u mapi u kojoj rezultati smiju biti
   ([Prije početka](before-you-start.md)).
3. **Pokreni pretvarač** nad datotekama snimki ili nad mapama koje ih sadrže:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` se napravi u mapi u kojoj je tvoj terminal.
4. **Pročitaj što piše.** Trebao bi vidjeti jedan redak po snimci, koji završava
   tablicom koju je zapisao.
5. **Otvori rezultat** u 3DHeat pregledniku: `out/<map>/<match>.parquet` na kartici
   Toplinska karta, `<match>.match.json` na kartici Meč. Ili ih pročitaj bilo kojim
   čitačem Parqueta ili JSON-a.

![Pokretanje na sintetičkoj snimci: pretvaranje, ponovno pokretanje, neispravna datoteka, prazna mapa](../assets/img/convert.svg)

Slika prikazuje pokretanje na snimci koju testovi grade u kodu (nema prave snimke):

- snimka pretvorena: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- pokrenuta ponovno, već zapisani meč se preskače: `<file>: already written, <table>`;
- datoteka koja nije snimka: `<file>: not converted: <why>` (u izlazu za greške; status izlaza 1,
  ostale snimke se i dalje pretvaraju);
- nije nađena nijedna snimka: `no .wowsreplay files in <folders>` (status izlaza 2).

## Opcije {#options}

| Opcija | Zadano | Radi |
|---|---|---|
| `replays` (jedna ili više) | - | `.wowsreplay` datoteke, ili mape u kojima se traže (i podmape) |
| `-o`, `--out` | obavezno | mapa u koju se piše: mapa po karti unutar |
| `--force` | isključeno | pretvori ponovno ono što je već zapisano |
| `--ship-names JSON` | - | JSON datoteka `{"<shipId>": "<name>", ...}`: snimke imenuju samo brod igrača koji snima, a ostale brojem |
| `--version` | - | ispiši `heat3d-wows-replay <version>` i stani |
| `-h`, `--help` | - | ispiši opcije i stani |

Opcije kako ih program ispisuje: [Referenca naredbi](../cli-reference.md).

## Što se zapisuje {#what-is-written}

Samo odvojene datoteke: ovaj pretvarač ne piše datoteku `.3dheat` (preglednik ih može
spakirati u jednu: [Jedna datoteka za meč](https://holdi601.github.io/3DHeat/container.html)).
Po snimci, u `out/<map>/` (naziv karte bez njezina `spaces/`):

| Datoteka | Što |
|---|---|
| `<match>.parquet` | tablica: položaj svakog broda kroz vrijeme i svaki događaj na mjestu gdje se dogodio ([Tablica](table.md)) |
| `<match>.match.json` | dokument meča: karta, verzija klijenta, igrači, potonuća, razgovor i sve ostalo ([Dokument meča](match-document.md)) |
| `<match>.messages.parquet` | pomoćna datoteka: svaka stavka snimke koju dvije gornje datoteke ne drže cijelu ([Potpunost](completeness.md)) |

`<match>` je vlastiti id bitke, ili naziv datoteke kad je snimanje stalo prije rezultata.

## Status izlaza {#exit-status}

`0` kad je svaka snimka pretvorena ili preskočena, `1` kad je neka nije uspjela (ostale se i dalje
pretvaraju), `2` kad nije nađena nijedna datoteka snimke.

---

Dio [3DHeata](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Izvor: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
