---
title: "Replays omzetten"
nav_order: 4
lang: "nl"
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Replays omzetten {#converting-replays}

## Stap voor stap {#step-by-step}

1. **Zet opnemen aan**: `isReplayEnabled` in het `preferences.xml` van het spel, of de eigen instelling van het spel waar die er is. Vanaf dan slaat het spel elk gevecht op in de map `replays` van je installatie
   van World of Warships, bijvoorbeeld `C:\Games\World_of_Warships_EU\replays`.
2. **Open een terminal** in een map waarin de resultaten mogen komen
   ([Voordat je begint](before-you-start.md)).
3. **Start de converter** op replaybestanden, of op mappen die ze bevatten:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` wordt aangemaakt in de map waarin je terminal staat.
4. **Lees wat er staat.** Je ziet één regel per replay, eindigend met de
   tabel die hij schreef.
5. **Open het resultaat** in de 3DHeat-viewer: `out/<map>/<match>.parquet`
   in het tabblad Heatmap, `<match>.match.json` in het tabblad Match. Of lees ze
   met elke Parquet- of JSON-lezer.

![Een run op een synthetische replay: omzetten, opnieuw draaien, een kapot bestand, een lege map](../assets/img/convert.svg)

De afbeelding is een run op een replay die de tests in code opbouwen (geen echte replay):

- een replay is omgezet: `<bestand>: <n> posities van <n> schepen op <snelheid> Hz (eigen <snelheid> Hz), <n> gezonken, <kaart> (<clientversie>) -> <tabel>`;
- opnieuw gedraaid, dan wordt het gevecht dat al geschreven is overgeslagen: `<bestand>: already written, <tabel>`;
- een bestand dat geen replay is: `<bestand>: not converted: <waarom>` (op de foutuitvoer;
  afsluitstatus 1, de andere replays worden wel omgezet);
- geen replay gevonden: `no .wowsreplay files in <mappen>` (afsluitstatus 2).

## Opties {#options}

| Optie | Standaard | Doet |
|---|---|---|
| `replays` (één of meer) | - | `.wowsreplay`-bestanden, of mappen waarin ernaar gezocht wordt (ook de submappen) |
| `-o`, `--out` | verplicht | de map om in te schrijven: een map per kaart erin |
| `--force` | uit | zet opnieuw om wat al geschreven is |
| `--ship-names JSON` | - | een JSON-bestand `{"<shipId>": "<naam>", ...}`: replays noemen alleen het schip van de opnemende speler bij naam, de andere bij nummer |
| `--version` | - | toon `heat3d-wows-replay <versie>` en stop |
| `-h`, `--help` | - | toon de opties en stop |

De opties zoals het programma ze toont: [Opdrachtreferentie](../cli-reference.md).

## Wat er geschreven wordt {#what-is-written}

Alleen losse bestanden: deze converter schrijft geen `.3dheat`-bestand (de viewer kan ze
in één bestand inpakken: [Eén bestand per wedstrijd](https://holdi601.github.io/3DHeat/container.html)).
Per replay, in `out/<map>/` (de naam van de kaart zonder de `spaces/`):

| Bestand | Wat |
|---|---|
| `<match>.parquet` | de tabel: de positie van elk schip door de tijd en elke gebeurtenis waar die plaatsvond ([De tabel](table.md)) |
| `<match>.match.json` | het wedstrijddocument: kaart, clientversie, spelers, zinkingen, chat en al het andere ([Het wedstrijddocument](match-document.md)) |
| `<match>.messages.parquet` | de sidecar: elk onderdeel van de replay dat de twee bestanden hierboven niet volledig bevatten ([Volledigheid](completeness.md)) |

`<match>` is het eigen id van het gevecht, of de naam van het bestand als de opname stopte
voordat de resultaten er waren.

## Afsluitstatus {#exit-status}

`0` als elke replay is omgezet of overgeslagen, `1` als er één is mislukt (de
rest wordt wel omgezet), `2` als er geen replaybestand gevonden is.

---

Onderdeel van [3DHeat](https://github.com/Holdi601/3DHeat) ([documentatie](https://holdi601.github.io/3DHeat/)). Bron: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
