---
title: "Upptökum breytt"
nav_order: 4
lang: is
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Upptökum breytt {#converting-replays}

## Skref fyrir skref {#step-by-step}

1. **Kveiktu á upptöku**: `isReplayEnabled` í `preferences.xml` leiksins, eða
   eigin stilling leiksins þar sem hún er til. Eftir það vistar leikurinn hvern
   bardaga í möppunni `replays` í World of Warships uppsetningunni þinni, til
   dæmis `C:\Games\World_of_Warships_EU\replays`.
2. **Opnaðu skipanaglugga** í möppu þar sem niðurstöðurnar mega fara
   ([Áður en þú byrjar](before-you-start.md)).
3. **Keyrðu breytinn** á upptökuskrár, eða á möppur sem geyma þær:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` er búin til í möppunni sem skipanagluggi þinn er í.
4. **Lestu það sem hann segir.** Þú ættir að sjá eina línu fyrir hverja upptöku, sem
   endar á töflunni sem var skrifuð.
5. **Opnaðu niðurstöðuna** í 3DHeat-skoðaranum: `out/<map>/<match>.parquet`
   í flipanum Hitakort, `<match>.match.json` í flipanum Leikur. Eða lestu þær
   með hvaða Parquet- eða JSON-lesara sem er.

![Keyrsla á tilbúinni upptöku: breyting, keyrt aftur, skemmd skrá, tóm mappa](../assets/img/convert.svg)

Myndin er keyrsla á upptöku sem prófanirnar smíða í kóða (engin raunveruleg upptaka):

- upptöku breytt: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- keyrt aftur, leiknum sem þegar er skrifaður er sleppt: `<file>: already written, <table>`;
- skrá sem er ekki upptaka: `<file>: not converted: <why>` (á villuúttakinu;
  útgöngustaða 1, hinar upptökurnar eru samt breyttar);
- engin upptaka fannst: `no .wowsreplay files in <folders>` (útgöngustaða 2).

## Valkostir {#options}

| Valkostur | Sjálfgefið | Gerir |
|---|---|---|
| `replays` (ein eða fleiri) | - | `.wowsreplay` skrár, eða möppur sem er leitað í að þeim (undirmöppur líka) |
| `-o`, `--out` | nauðsynlegt | mappan sem er skrifað í: mappa fyrir hvert kort inni í henni |
| `--force` | slökkt | breyta aftur því sem er þegar skrifað |
| `--ship-names JSON` | - | JSON-skrá `{"<shipId>": "<name>", ...}`: upptökur nefna aðeins skip upptökumannsins, hin með númeri |
| `--version` | - | prenta `heat3d-wows-replay <version>` og stoppa |
| `-h`, `--help` | - | prenta valkostina og stoppa |

Valkostirnir eins og forritið prentar þá: [Skipanayfirlit](../cli-reference.md).

## Hvað er skrifað {#what-is-written}

Aðeins lausar skrár: þessi breytir skrifar enga `.3dheat` skrá (skoðarinn getur
pakkað þeim í eina: [Ein skrá á leik](https://holdi601.github.io/3DHeat/container.html)).
Fyrir hverja upptöku, í `out/<map>/` (nafn kortsins án `spaces/`):

| Skrá | Hvað |
|---|---|
| `<match>.parquet` | taflan: staða hvers skips yfir tíma og hver atburður þar sem hann gerðist ([Taflan](table.md)) |
| `<match>.match.json` | leikjaskjalið: kort, útgáfa biðlara, spilarar, sökkvanir, spjall og allt annað ([Leikjaskjalið](match-document.md)) |
| `<match>.messages.parquet` | hliðarskráin: hvert atriði upptökunnar sem skrárnar tvær hér að ofan geyma ekki í heild ([Heilleiki](completeness.md)) |

`<match>` er eigið auðkenni bardagans, eða nafn skrárinnar þegar upptakan
stöðvaðist fyrir niðurstöðurnar.

## Útgöngustaða {#exit-status}

`0` þegar allar upptökur voru breyttar eða þeim sleppt, `1` þegar einhver mistókst (hinar
eru samt breyttar), `2` þegar engin upptökuskrá fannst.

---

Hluti af [3DHeat](https://github.com/Holdi601/3DHeat) ([skjölun](https://holdi601.github.io/3DHeat/)). Frumkóði: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
