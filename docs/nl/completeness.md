---
title: "Volledigheid"
nav_order: 8
lang: nl
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Volledigheid {#completeness}

Niets in een replay wordt weggegooid. Wat de converter leest, gaat in de tabel
en het wedstrijddocument; elk ander onderdeel wordt volledig bewaard in de sidecar
`<match>.messages.parquet`; en `selfCheck.completeness` van het wedstrijddocument telt wat er
van elke soort onderdeel geworden is. Dit is de regel die alle 3DHeat-converters delen:
[Converters bewaren alles](https://holdi601.github.io/3DHeat/converters.html).

![De zelfcontrole van een synthetische replay: elk onderdeel gezien, gelezen, bewaard of verloren](../assets/img/completeness.svg)

## De telling {#the-count}

Voor elke soort onderdeel geeft `selfCheck.completeness.types`:

| Telling | Betekent |
|---|---|
| `seen` | hoeveel de replay er bevat |
| `decoded` | volledig gelezen |
| `partial` | gedeeltelijk gelezen, en volledig bewaard in de sidecar |
| `raw` | alleen volledig bewaard in de sidecar, niet gelezen |
| `lost` | verloren: altijd `0` |

De soorten zijn die van de replay zelf: `block <n>` (de JSON-blokken), de eigen bytes van de
container, `packet <type>`, en voor aanroepen op entiteiten `method <entiteitstype>.<nummer>`
en `property <entiteitstype>.<nummer>`. `selfCheck.entities.roles` zegt welk entiteitstype de
avatar van de opnemende speler is en welke de schepen. Een soort die niemand kende, verschijnt
met zijn telling.

## De sidecar {#the-sidecar}

| Kolom | Wat |
|---|---|
| `time` | de klok van de replay, zoals in de tabel |
| `type`, `name` | de soort onderdeel; hoe de converter het noemt, waar hij het leest |
| `entity` | het schip of de avatar waar het bij hoort, als `entity` in de tabel |
| `decoded` | wat ervan gelezen is, als JSON |
| `payload`, `text` | de bytes, volledig; de JSON-blokken, volledig |
| `entityType`, `packet`, `method` | de nummers |

Rijen zijn gesorteerd op pakket, methode, entiteit en tijd. Welke entiteit welke
speler is: de `entities` en `players` van het wedstrijddocument.

## Wat er gelezen wordt, en hoe het gecontroleerd is {#what-is-read-and-how-it-was-checked}

- **De resultaten** (15.x, `results`): hun gevecht-id is dat van de stroom, en elke speler erin staat
  in de deelnemerslijst van de kop.
- **Het blok met id's** (15.x, `blockIds`): het account en het gevecht, als tekst gelezen zodat geen cijfer verloren gaat.
- **Helling en rol** van elke positie: de rol hangt samen met de draaisnelheid, want een schip helt over in een bocht;
  de helling is bijna altijd 0.
- **Entiteiten** (`entities`): wanneer elk in het zicht van de client kwam en wegging. Geen enkel schip
  heeft een positie tussen het weggaan en het terugkomen.
- **De versie in de stroom** (`streamVersion`): gelijk aan die van de kop.

Al het andere dat gelezen wordt (zinkingen, schade, gezondheid, granaten, torpedo's, waar granaten
eindigden, chat, gepickelde aanroepen, de records van de spelers, posities) is `partial`: in de tabel
of het wedstrijddocument, en volledig bewaard in de sidecar.

**Bewaard maar niet gelezen** (`raw`), de grootste soorten: positie-updates die niet in de
tabel staan (na het zinken van een schip, entiteiten zonder speler), de veelvoorkomende
eigenschappen en methoden zonder lezer, de eigenschappen van entiteitscreaties,
en elk ander pakket zonder lezer.

## Niet beschikbaar {#not-available}

- Wat de server de opnemende client nooit stuurde: de richting, camera en besturing van andere spelers,
  vijanden zolang ze niet gespot waren. Een replay is wat één client te horen kreeg.
- De namen van entiteitstypen, methoden, eigenschappen en de sleutels van de statistieken: die staan in de
  definitiebestanden van het spel, niet in de replay. De nummers worden bewaard.
- De namen van schepen bij de schipnummers (gebruik `--ship-names`), en alles andere dat de eigen
  bestanden van het spel nodig heeft.
- Resultaten van clients vóór 15.x: die staan niet in hun replays.

---

Onderdeel van [3DHeat](https://github.com/Holdi601/3DHeat) ([documentatie](https://holdi601.github.io/3DHeat/)). Bron: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
