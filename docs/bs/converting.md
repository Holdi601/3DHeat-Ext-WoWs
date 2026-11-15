---
title: "Pretvaranje replayeva"
nav_order: 4
lang: "bs"
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Pretvaranje replayeva {#converting-replays}

## Korak po korak {#step-by-step}

1. **Uključite snimanje**: `isReplayEnabled` u `preferences.xml` igre,
   ili vlastita postavka igre gdje je ima. Od tada
   igra sprema svaku bitku u folder `replays` vaše World of
   Warships instalacije, na primjer
   `C:\Games\World_of_Warships_EU\replays`.
2. **Otvorite terminal** u folderu u koji rezultati smiju ići
   ([Prije nego počnete](before-you-start.md)).
3. **Pokrenite konverter** nad replay datotekama ili folderima s njima:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` se pravi u folderu u kojem je vaš terminal.
4. **Pročitajte šta ispiše.** Trebali biste vidjeti jedan red po replayu, koji završava
   tabelom koju je napisao.
5. **Otvorite rezultat** u 3DHeat pregledniku: `out/<map>/<match>.parquet`
   u kartici Toplotna mapa, `<match>.match.json` u kartici Meč. Ili ih pročitajte
   bilo kojim čitačem Parqueta ili JSON-a.

![Pokretanje na sintetičkom replayu: pretvaranje, ponovno pokretanje, pokvarena datoteka, prazan folder](../assets/img/convert.svg)

Slika prikazuje pokretanje na replayu koji testovi grade u kodu (nije pravi replay):

- pretvoren replay: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- pokrenuto ponovo, već napisan meč se preskače: `<file>: already written, <table>`;
- datoteka koja nije replay: `<file>: not converted: <why>` (na izlazu za greške;
  izlazni status 1, ostali replayevi se i dalje pretvaraju);
- replay nije pronađen: `no .wowsreplay files in <folders>` (izlazni status 2).

## Opcije {#options}

| Opcija | Zadano | Šta radi |
|---|---|---|
| `replays` (jedan ili više) | - | `.wowsreplay` datoteke ili folderi u kojima se traže (i podfolderi) |
| `-o`, `--out` | obavezno | folder u koji se piše: unutra folder po mapi |
| `--force` | isključeno | ponovo pretvori ono što je već napisano |
| `--ship-names JSON` | - | JSON datoteka `{"<shipId>": "<name>", ...}`: replayevi imenuju samo brod igrača koji snima, ostale brojem |
| `--version` | - | ispiši `heat3d-wows-replay <version>` i stani |
| `-h`, `--help` | - | ispiši opcije i stani |

Opcije onako kako ih program ispisuje: [Referenca naredbi](../cli-reference.md).

## Šta se piše {#what-is-written}

Samo odvojene datoteke: ovaj konverter ne piše `.3dheat` datoteku (preglednik ih može
spakirati u jednu: [Jedna datoteka po meču](https://holdi601.github.io/3DHeat/container.html)).
Po replayu, u `out/<map>/` (ime mape bez njenog `spaces/`):

| Datoteka | Šta |
|---|---|
| `<match>.parquet` | tabela: pozicija svakog broda kroz vrijeme i svaki događaj na mjestu gdje se desio ([Tabela](table.md)) |
| `<match>.match.json` | dokument meča: mapa, verzija klijenta, igrači, potonuća, čet i sve ostalo ([Dokument meča](match-document.md)) |
| `<match>.messages.parquet` | sidecar: svaka stavka replaya koju gornje dvije datoteke ne drže cijelu ([Potpunost](completeness.md)) |

`<match>` je vlastiti id bitke, ili ime datoteke kada se snimanje
zaustavilo prije rezultata.

## Izlazni status {#exit-status}

`0` kada je svaki replay pretvoren ili preskočen, `1` kada je neki propao (ostali se
i dalje pretvaraju), `2` kada nije pronađena nijedna replay datoteka.

---

Dio [3DHeata](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Izvor: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
