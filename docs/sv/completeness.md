---
title: "Fullständighet"
nav_order: 8
lang: "sv"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Fullständighet {#completeness}

Ingenting i en repris kastas bort. Det konverteraren läser går in i tabellen och
matchdokumentet; varje annat objekt behålls helt i sidofilen
`<match>.messages.parquet`; och matchdokumentets `selfCheck.completeness` räknar vad
som blev av varje slag av objekt. Det här är regeln alla 3DHeat-konverterare delar:
[Konverterare behåller allt](https://holdi601.github.io/3DHeat/converters.html).

![Självkontrollen för en syntetisk repris: varje objekt sett, läst, behållet eller förlorat](../assets/img/completeness.svg)

## Räkningen {#the-count}

För varje slag av objekt ger `selfCheck.completeness.types`:

| Räkning | Betyder |
|---|---|
| `seen` | hur många repriset innehåller |
| `decoded` | lästa helt |
| `partial` | lästa delvis, och behållna helt i sidofilen |
| `raw` | bara behållna helt i sidofilen, inte lästa |
| `lost` | förlorade: alltid `0` |

Slagen är repriset egna: `block <n>` (JSON-blocken), containerns egna byte, `packet <type>`,
och för anrop på entiteter `method <entity type>.<number>` och `property <entity type>.<number>`.
`selfCheck.entities.roles` säger vilken entitetstyp som är den inspelande spelarens avatar och
vilka som är fartygen. Ett slag som ingen kände till syns med sin räkning.

## Sidofilen {#the-sidecar}

| Kolumn | Vad |
|---|---|
| `time` | repriets klocka, som i tabellen |
| `type`, `name` | slaget av objekt; vad konverteraren kallar det, där den läser det |
| `entity` | fartyget eller avataren det hör till, som tabellens `entity` |
| `decoded` | vad som lästes av det, som JSON |
| `payload`, `text` | dess byte, helt; JSON-blocken, helt |
| `entityType`, `packet`, `method` | talen |

Rader sorteras efter paket, metod, entitet och tid. Vilken entitet som är vilken spelare: matchdokumentets
`entities` och `players`.

## Vad som lästes, och hur det kontrollerades {#what-is-read-and-how-it-was-checked}

- **Resultaten** (15.x, `results`): deras stridsid är strömmens, och varje spelare i dem finns i
  headerns lista.
- **Id-blocket** (15.x, `blockIds`): kontot och striden, lästa som text så att ingen siffra går förlorad.
- **Stigning och rulle** för varje position: rullen följer svängningens hastighet, eftersom ett fartyg
  krängar i en sväng; stigningen är nästan alltid 0.
- **Entiteter** (`entities`): när var och en kom in i klientens syn och lämnade den. Inget fartyg har en
  position mellan att lämna och komma tillbaka.
- **Versionen i strömmen** (`streamVersion`): samma som headerns.

Allt annat som lästs (sänkningar, skada, hälsa, granater, torpeder, var granater slutade, chatt,
inlagda anrop, spelarnas poster, positioner) är `partial`: i tabellen eller matchdokumentet, och
behållet helt i sidofilen.

**Behållet men inte läst** (`raw`), de största slagen: positionsuppdateringar som inte finns i
tabellen (efter att ett fartyg sjunkit, entiteter utan spelare), de vanliga egenskaperna och
metoderna utan läsare, egenskaperna hos entitetsskapanden, och alla andra paket utan läsare.

## Inte tillgängligt {#not-available}

- Det som servern aldrig skickade till den inspelande klienten: andra spelares sikte, kamera och
  indata, fiender när de inte är upptäckta. En repris är vad en klient fick veta.
- Namnen på entitetstyper, metoder, egenskaper och statistikens nycklar: de finns i spelets
  definitionsfiler, inte i repriset. Talen behålls.
- Fartygsnamn för fartygsnumren (använd `--ship-names`), och allt annat som kräver spelets egna filer.
- Resultat från klienter före 15.x: de finns inte i deras repriser.

---

Del av [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentation](https://holdi601.github.io/3DHeat/)). Källa: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
