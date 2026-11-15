---
title: "Konvertera repriser"
nav_order: 4
lang: "sv"
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Konvertera repriser {#converting-replays}

## Steg för steg {#step-by-step}

1. **Slå på inspelning:** `isReplayEnabled` i spelets `preferences.xml`, eller spelets egen
   inställning där en finns. Från och med då sparar spelet varje strid i mappen `replays` i din
   World of Warships-installation, till exempel `C:\Games\World_of_Warships_EU\replays`.
2. **Öppna en terminal** i en mapp dit resultaten får skrivas
   ([Innan du börjar](before-you-start.md)).
3. **Kör konverteraren** på repriserfiler, eller på mappar som innehåller dem:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` skapas i mappen din terminal står i.
4. **Läs vad den skriver.** Du bör se en rad per repris, som slutar med tabellen
   den skrev.
5. **Öppna resultatet** i 3DHeat-visaren: `out/<map>/<match>.parquet` på
   Värmekarta-fliken, `<match>.match.json` på Match-fliken. Eller läs dem med
   valfri Parquet- eller JSON-läsare.

![En körning på en syntetisk repris: konvertering, ny körning, en trasig fil, en tom mapp](../assets/img/convert.svg)

Bilden är en körning på en repris som testerna bygger i kod (ingen riktig repris):

- en repris konverterad: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- körd igen, hoppas matchen som redan skrivits över: `<file>: already written, <table>`;
- en fil som inte är en repris: `<file>: not converted: <why>` (på felutdata; exitstatus 1,
  de andra repriserna konverteras ändå);
- ingen repris hittad: `no .wowsreplay files in <folders>` (exitstatus 2).

## Alternativ {#options}

| Alternativ | Standard | Gör |
|---|---|---|
| `replays` (en eller flera) | - | `.wowsreplay`-filer, eller mappar som söks efter sådana (även undermappar) |
| `-o`, `--out` | krävs | mappen att skriva till: en mapp per karta inuti |
| `--force` | av | konvertera det som redan är skrivet igen |
| `--ship-names JSON` | - | en JSON-fil `{"<shipId>": "<name>", ...}`: repriser namnger bara den inspelande spelarens fartyg, de andra efter nummer |
| `--version` | - | skriv `heat3d-wows-replay <version>` och stanna |
| `-h`, `--help` | - | skriv alternativen och stanna |

Alternativen så som programmet skriver dem: [Kommandoreferens](../cli-reference.md).

## Vad som skrivs {#what-is-written}

Bara lösa filer: den här konverteraren skriver ingen `.3dheat`-fil (visaren kan
packa dem till en: [En fil per match](https://holdi601.github.io/3DHeat/container.html)).
Per repris, i `out/<map>/` (kartans namn utan dess `spaces/`):

| Fil | Vad |
|---|---|
| `<match>.parquet` | tabellen: varje fartygs position över tid och varje händelse där den skedde ([Tabellen](table.md)) |
| `<match>.match.json` | matchdokumentet: karta, klientversion, spelare, sänkningar, chatt och allt annat ([Matchdokumentet](match-document.md)) |
| `<match>.messages.parquet` | sidofilen: varje del av repriset som de två filerna ovan inte håller helt ([Fullständighet](completeness.md)) |

`<match>` är stridens eget id, eller filens namn när inspelningen stoppade före
resultaten.

## Exitstatus {#exit-status}

`0` när varje repris konverterades eller hoppades över, `1` när någon misslyckades (de
övriga konverteras ändå), `2` när ingen repris-fil hittades.

---

Del av [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentation](https://holdi601.github.io/3DHeat/)). Källa: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
