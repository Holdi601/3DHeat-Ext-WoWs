---
title: "Il-konverżjoni tar-ripetizzjonijiet"
nav_order: 4
lang: mt
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Il-konverżjoni tar-ripetizzjonijiet {#converting-replays}

## Pass b'pass {#step-by-step}

1. **Ixgħel ir-reġistrazzjoni**: `isReplayEnabled` fil-`preferences.xml` tal-logħba,
   jew is-setting proprju tal-logħba fejn ikun hemm waħda. Minn hemm 'il quddiem
   il-logħba tsejvja kull battalja fil-folder `replays` tal-installazzjoni tiegħek
   ta' World of Warships, pereżempju `C:\Games\World_of_Warships_EU\replays`.
2. **Iftaħ terminal** f'folder fejn ir-riżultati jistgħu jmorru
   ([Qabel ma tibda](before-you-start.md)).
3. **Ħaddem il-konvertitur** fuq fajls ta' ripetizzjoni, jew fuq folders li jkun fihom:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` jinħoloq fil-folder fejn ikun it-terminal tiegħek.
4. **Aqra dak li jgħid.** Għandek tara linja waħda għal kull ripetizzjoni, li
   tispiċċa bit-tabella li nkitbet.
5. **Iftaħ ir-riżultat** fid-3DHeat viewer: `out/<map>/<match>.parquet`
   fit-tab Heatmap, `<match>.match.json` fit-tab Partita. Jew aqrahom
   b'kull qarrej ta' Parquet jew JSON.

![Tħaddim fuq ripetizzjoni sintetika: konverżjoni, tħaddim mill-ġdid, fajl miksur, folder vojt](../assets/img/convert.svg)

L-istampa hija tħaddim fuq ripetizzjoni li t-testijiet jibnu fil-kodiċi (mhux ripetizzjoni vera):

- ripetizzjoni kkonvertita: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- tħaddim mill-ġdid, il-partita diġà miktuba tiġi maqbuża: `<file>: already written, <table>`;
- fajl li mhux ripetizzjoni: `<file>: not converted: <why>` (fuq il-ħruġ tal-iżbalji;
  status tal-ħruġ 1, ir-ripetizzjonijiet l-oħra jiġu kkonvertiti xorta);
- ebda ripetizzjoni ma nstabet: `no .wowsreplay files in <folders>` (status tal-ħruġ 2).

## Għażliet {#options}

| Għażla | Default | X'jagħmel |
|---|---|---|
| `replays` (waħda jew aktar) | - | fajls `.wowsreplay`, jew folders fejn jinstabu (subfolders ukoll) |
| `-o`, `--out` | meħtieġa | il-folder fejn jinkiteb: folder għal kull mappa ġewwa |
| `--force` | mitfi | jikkonverti mill-ġdid dak li diġà nkiteb |
| `--ship-names JSON` | - | fajl JSON `{"<shipId>": "<name>", ...}`: ir-ripetizzjonijiet jsemmu biss il-vapur tal-plejer li rreġistra, l-oħrajn bin-numru |
| `--version` | - | jistampa `heat3d-wows-replay <version>` u jieqaf |
| `-h`, `--help` | - | jistampa l-għażliet u jieqaf |

L-għażliet kif jistampahom il-programm: [Referenza tal-kmandi](../cli-reference.md).

## X'jinkiteb {#what-is-written}

Fajls separati biss: dan il-konvertitur ma jikteb ebda fajl `.3dheat` (il-viewer
jista' jpakkjahom f'wieħed: [Fajl wieħed għal kull partita](https://holdi601.github.io/3DHeat/container.html)).
Għal kull ripetizzjoni, f'`out/<map>/` (l-isem tal-mappa mingħajr `spaces/`):

| Fajl | X'inhu |
|---|---|
| `<match>.parquet` | it-tabella: il-pożizzjoni ta' kull vapur maż-żmien u kull avveniment fejn seħħ ([It-tabella](table.md)) |
| `<match>.match.json` | id-dokument tal-partita: mappa, verżjoni tal-klijent, plejers, għarqiet, chat u kull ħaġa oħra ([Id-dokument tal-partita](match-document.md)) |
| `<match>.messages.parquet` | is-sidecar: kull element tar-ripetizzjoni li ż-żewġ fajls ta' hawn fuq ma jżommux kollu ([Kompletezza](completeness.md)) |

`<match>` huwa l-id tal-battalja stess, jew l-isem tal-fajl meta r-reġistrazzjoni
waqfet qabel ir-riżultati.

## Status tal-ħruġ {#exit-status}

`0` meta kull ripetizzjoni ġiet ikkonvertita jew maqbuża, `1` meta xi waħda falliet
(l-oħrajn jiġu kkonvertiti xorta), `2` meta ma nstab ebda fajl ta' ripetizzjoni.

---

Parti mid-[3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentazzjoni](https://holdi601.github.io/3DHeat/)). Sors: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
