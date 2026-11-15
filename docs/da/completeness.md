---
title: Fuldstændighed
nav_order: 8
lang: "da"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Fuldstændighed {#completeness}

Intet i et replay bliver smidt væk. Det konverteren læser, går ind i tabellen og kampdokumentet;
hvert andet element gemmes helt i sidecaren `<match>.messages.parquet`; og kampdokumentets
`selfCheck.completeness` tæller, hvad der blev af hver slags element. Dette er reglen, alle
3DHeat-konvertere deler: [Konvertere bevarer alt](https://holdi601.github.io/3DHeat/converters.html).

![Selvkontrollen af et syntetisk replay: hvert element set, læst, gemt eller tabt](../assets/img/completeness.svg)

## Tællingen {#the-count}

For hver slags element giver `selfCheck.completeness.types`:

| Tælling | Betyder |
|---|---|
| `seen` | hvor mange replayet indeholder |
| `decoded` | læst helt |
| `partial` | læst delvist, og gemt helt i sidecaren |
| `raw` | kun gemt helt i sidecaren, ikke læst |
| `lost` | tabt: altid `0` |

Slagene er replayets egne: `block <n>` (JSON-blokkene), containerens egne bytes, `packet <type>`, og for
kald på entiteter `method <entity type>.<number>` og `property <entity type>.<number>`.
`selfCheck.entities.roles` siger, hvilken entitetstype der er den optagende spillers avatar, og hvilke der er
skibene. En slags, ingen kendte til, dukker op med sin tælling.

## Sidecaren {#the-sidecar}

| Kolonne | Hvad |
|---|---|
| `time` | replayets ur, som i tabellen |
| `type`, `name` | slags element; hvad konverteren kalder det, hvor den læser det |
| `entity` | skibet eller avataren, det hører til, som tabellens `entity` |
| `decoded` | det, der blev læst af det, som JSON |
| `payload`, `text` | dets bytes, helt; JSON-blokkene, helt |
| `entityType`, `packet`, `method` | tallene |

Rækkerne sorteres efter pakke, metode, entitet og tid. Hvilken entitet der er hvilken spiller: kampdokumentets
`entities` og `players`.

## Hvad der læses, og hvordan det blev kontrolleret {#what-is-read-and-how-it-was-checked}

- **Resultaterne** (15.x, `results`): deres kamp-id er strømmens, og hver spiller i dem står i headerens rosterliste.
- **Id-blokken** (15.x, `blockIds`): konto og kamp, læst som tekst, så intet ciffer går tabt.
- **Hældning og rulning** for hver position: rulningen følger drejehastigheden, da et skib krænger i en
  drejning; hældningen er næsten altid 0.
- **Entiteter** (`entities`): hvornår hver kom ind i klientens udsyn, og hvornår den forlod det.
  Intet skib har en position mellem at forlade og komme tilbage.
- **Versionen i strømmen** (`streamVersion`): den samme som headerens.

Alt det øvrige, der læses (søenkninger, skade, liv, granater, torpedoer, hvor granater endte, chat, afkodede
kald, spillernes optegnelser, positioner), er `partial`: i tabellen eller kampdokumentet, og gemt helt i sidecaren.

**Gemt, men ikke læst** (`raw`), de største slags: positionsopdateringer, der ikke er i tabellen (efter et skib
er sunket, entiteter uden en spiller), de hyppige egenskaber og metoder uden en læser, egenskaberne ved
entitetsoprettelser, og hver anden pakke uden en læser.

## Ikke tilgængeligt {#not-available}

- Det, serveren aldrig sendte til den optagende klient: andre spilleres sigte, kamera og input, fjender,
  mens de ikke er opdaget. Et replay er det, én klient blev fortalt.
- Navnene på entitetstyper, metoder, egenskaber og statistikkens nøgler: de står i spillets definitionsfiler, ikke
  i replayet. Tallene gemmes.
- Skibsnavne til skibsnumrene (brug `--ship-names`), og alt andet, der kræver spillets egne filer.
- Resultater fra klienter før 15.x: de findes ikke i deres replays.

---

Del af [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentation](https://holdi601.github.io/3DHeat/)). Kilde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
