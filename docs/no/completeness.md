---
title: "Fullstendighet"
nav_order: 8
lang: "no"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Fullstendighet {#completeness}

Ingenting i en replay kastes. Det konverteren leser, går inn i tabellen og
kampdokumentet; alt annet beholdes helt i sidefilen
`<kamp>.messages.parquet`; og kampdokumentets
`selfCheck.completeness` teller hva som ble av hver type post. Dette er regelen alle
3DHeat-konvertere deler: [Konvertere beholder alt](https://holdi601.github.io/3DHeat/converters.html).

![Selvkontrollen til en syntetisk replay: hver post sett, lest, beholdt eller tapt](../assets/img/completeness.svg)

## Tellingen {#the-count}

For hver type post gir `selfCheck.completeness.types`:

| Telling | Betyr |
|---|---|
| `seen` | hvor mange replayen holder |
| `decoded` | lest helt |
| `partial` | lest delvis, og beholdt helt i sidefilen |
| `raw` | bare beholdt helt i sidefilen, ikke lest |
| `lost` | tapt: alltid `0` |

Typene er replayens egne: `block <n>` (JSON-blokkene), containerens egne byte,
`packet <type>`, og for kall på entiteter `method <entitetstype>.<nummer>` og
`property <entitetstype>.<nummer>`. `selfCheck.entities.roles` sier hvilken entitetstype
som er opptakspilotens avatar og hvilke som er skipene. En type ingen kjente til, vises
med sin telling.

## Sidefilen {#the-sidecar}

| Kolonne | Hva |
|---|---|
| `time` | replayens klokke, som i tabellen |
| `type`, `name` | typen post; hva konverteren kaller den, der den leser den |
| `entity` | skipet eller avataren den hører til, som tabellens `entity` |
| `decoded` | det som ble lest av den, som JSON |
| `payload`, `text` | dens byte, helt; JSON-blokkene, helt |
| `entityType`, `packet`, `method` | tallene |

Rader sorteres etter pakke, metode, entitet og tid. Hvilken entitet som er hvilken
spiller: kampdokumentets `entities` og `players`.

## Hva som leses, og hvordan det ble kontrollert {#what-is-read-and-how-it-was-checked}

- **Resultatene** (15.x, `results`): deres slag-ID er strømmens, og hver spiller i dem
  står i headerens deltakerliste.
- **ID-blokken** (15.x, `blockIds`): kontoen og slaget, lest som tekst slik at ingen siffer
  går tapt.
- **Stigning og rull** for hver posisjon: rullen følger svingehastigheten, slik et skip
  krenger i en sving; stigningen er nesten alltid 0.
- **Entiteter** (`entities`): når hver kom inn i klientens syn og forlot det. Ingen skip har
  en posisjon mellom at det forlot synet og at det kom tilbake.
- **Versjonen i strømmen** (`streamVersion`): den samme som headerens.

Alt annet som leses (senkinger, skade, helse, granater, torpedoer, hvor granater endte,
chat, pickle-kall, spillernes poster, posisjoner) er `partial`: i tabellen eller
kampdokumentet, og beholdt helt i sidefilen.

**Beholdt men ikke lest** (`raw`), de største typene: posisjonsoppdateringer som ikke er i
tabellen (etter at et skip sank, entiteter uten spiller), de hyppige egenskapene og metodene
uten leser, egenskapene til entitetsopprettelser, og hver annen pakke uten leser.

## Ikke tilgjengelig {#not-available}

- Det serveren aldri sendte til opptaksklienten: andre spilleres sikte, kamera og
  inndata, fiender som ikke er sett. En replay er det én klient ble fortalt.
- Navnene på entitetstyper, metoder, egenskaper og nøklene i statistikken: de står i spillets
  definisjonsfiler, ikke i replayen. Tallene beholdes.
- Skipsnavn for skipsnumrene (bruk `--ship-names`), og alt annet som krever spillets egne filer.
- Resultater fra klienter før 15.x: de finnes ikke i deres replayer.

---

Del av [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentasjon](https://holdi601.github.io/3DHeat/)). Kilde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
