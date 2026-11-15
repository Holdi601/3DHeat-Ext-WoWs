---
title: Konvertering af replays
nav_order: 4
lang: da
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Konvertering af replays {#converting-replays}

## Trin for trin {#step-by-step}

1. **Slå optagelse til:** `isReplayEnabled` i spillets `preferences.xml`, eller spillets egen indstilling, hvor der
   findes en. Fra da af gemmer spillet hver kamp i mappen `replays` i din World of Warships-installation,
   for eksempel `C:\Games\World_of_Warships_EU\replays`.
2. **Åbn en terminal** i en mappe, hvor resultaterne må ligge
   ([Før du går i gang](before-you-start.md)).
3. **Kør konverteren** på replay-filer, eller på mapper, der indeholder dem:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` oprettes i den mappe, din terminal står i.
4. **Læs hvad der står.** Du bør se én linje pr. replay, som ender med den tabel, den skrev.
5. **Åbn resultatet** i 3DHeat-vieweren: `out/<map>/<match>.parquet` på Heatmap-fanen,
   `<match>.match.json` på Kamp-fanen. Eller læs dem med en hvilken som helst Parquet- eller JSON-læser.

![En kørsel på et syntetisk replay: konvertering, ny kørsel, en ødelagt fil, en tom mappe](../assets/img/convert.svg)

Billedet viser en kørsel på et replay, som testene bygger i kode (intet rigtigt replay):

- et replay konverteret: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- kørt igen, springes den kamp, der allerede er skrevet, over: `<file>: already written, <table>`;
- en fil, der ikke er et replay: `<file>: not converted: <why>` (på fejloutputtet; afslutningsstatus 1, de
  andre replays konverteres stadig);
- intet replay fundet: `no .wowsreplay files in <folders>` (afslutningsstatus 2).

## Valgmuligheder {#options}

| Valg | Standard | Gør |
|---|---|---|
| `replays` (en eller flere) | - | `.wowsreplay`-filer, eller mapper, der søges i efter dem (også undermapper) |
| `-o`, `--out` | påkrævet | mappen at skrive i: en mappe pr. kort indeni |
| `--force` | fra | konverter igen det, der allerede er skrevet |
| `--ship-names JSON` | - | en JSON-fil `{"<shipId>": "<name>", ...}`: replays navngiver kun den optagende spillers skib, de andre efter nummer |
| `--version` | - | skriv `heat3d-wows-replay <version>` og stop |
| `-h`, `--help` | - | skriv valgmulighederne og stop |

Valgmulighederne, som programmet viser dem: [Kommandoreference](../cli-reference.md).

## Hvad der skrives {#what-is-written}

Kun løse filer: denne konverter skriver ingen `.3dheat`-fil (vieweren kan pakke dem i én:
[En fil pr. kamp](https://holdi601.github.io/3DHeat/container.html)).
Pr. replay, i `out/<map>/` (kortets navn uden dets `spaces/`):

| Fil | Indhold |
|---|---|
| `<match>.parquet` | tabellen: hvert skibs position over tid og hver begivenhed, hvor den skete ([Tabellen](table.md)) |
| `<match>.match.json` | kampdokumentet: kort, klientversion, spillere, søenkninger, chat og alt det øvrige ([Kampdokumentet](match-document.md)) |
| `<match>.messages.parquet` | sidecaren: hvert element i replayet, de to filer ovenfor ikke rummer helt ([Fuldstændighed](completeness.md)) |

`<match>` er kampens eget id, eller filens navn, når optagelsen stoppede, før resultaterne kom.

## Afslutningsstatus {#exit-status}

`0`, når hvert replay blev konverteret eller sprunget over, `1`, når et af dem fejlede (de
øvrige konverteres stadig), `2`, når ingen replay-fil blev fundet.

---

Del af [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentation](https://holdi601.github.io/3DHeat/)). Kilde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
