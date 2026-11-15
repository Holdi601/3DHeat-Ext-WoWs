---
title: Dokument meča
nav_order: 6
lang: hr
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Dokument meča {#the-match-document}

`<match>.match.json` drži sve što snimka kaže, a što nije redak tablice. Kartica Meč
preglednika ga čita. (Kod ga zove sažetak.)

![Početak sintetičkog dokumenta meča, i njegovi ključevi](../assets/img/match-document.svg)

## Bitka {#the-battle}

| Ključ | Što |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; id bitke; karta kako je igra imenuje (`spaces/<map>`) i njezin prikazni naziv |
| `clientVersion`, `streamVersion` | verzija igre iz zaglavlja, i kako ju kaže tok paketa |
| `recorded` | kad je snimka zabilježena, kako je igra zapisuje |
| `player`, `vehicle` | igrač koji snima i njegov brod |
| `gameType`, `scenario` | vrsta bitke (`RandomBattle`, ...) i scenarij, iz zaglavlja |
| `duration` | vremensko ograničenje bitke u sekundama, iz zaglavlja |
| `truncated` | snimanje je stalo rano |
| `battleStart`, `recordingSeconds` | početak bitke (prvi trenutak kad se bilo koji brod pomakne) i trajanje snimanja, u sekundama |
| `positionPacket`, `ownPositionPacket` | brojevi paketa u kojima su došli položaji: tuđih brodova, igračeva |
| `deathMethod` | broj metode u kojoj su potonuća nađena |
| `hz`, `ownHz`, `positions` | uzoraka u sekundi tuđih brodova i vlastitog broda; redci položaja |
| `units` | jedinice svijeta (15 m po trupovima, 30 m po dometima igre); x istok, y gore, z sjever |
| `events` | broj redaka tablice za svaki događaj |
| `decoded` | brojevi metoda i paketa nađeni za svaku vrstu poruke |

## Igrači i događaji {#players-and-events}

| Ključ | Što |
|---|---|
| `players` | jedan unos po brodu: ime, `ally` ili `enemy`, broj i naziv broda, entitet, uzorci, ubojstva, preživljeno; `seen` (nanesena i primljena šteta, granate, torpeda i zadnje zdravlje koje je klijent vidio); `header` (unos iz popisa) i `record` (zapis igrača iz toka, po broju ključa) |
| `kills` | svako potonuće: vrijeme, žrtva, ubojica, broj uzroka, mjesto |
| `chat` | svaki red razgovora, s kanalom i pošiljateljem |
| `damageStats` | vlastita statistika igrača koji snima kako je igra vodi: po oružju i vrsti, broj i iznos (vrsta 0 je nanesena šteta) |
| `avatarPickles` | svaki pickle poziv igraču koji snima, dekodiran, po broju metode |

## Zaglavlje, rezultati i provjere {#header-results-and-checks}

| Ključ | Što |
|---|---|
| `header` | prvi JSON blok, cijeli osim popisa: način igre, vremenske prilike, granica karte, veličine timova i još |
| `moreBlocks` | JSON blokovi iza prvog, kakvi jesu |
| `blockIds` | 15.x: račun igrača koji snima i id bitke, pročitani kao tekst |
| `results` | 15.x: rezultati, koje ti klijenti čuvaju u toku |
| `entities` | svaki entitet koji tok stvara: njegov broj vrste i uloga, kad je ušao u pogled klijenta i kad je izašao |
| `selfCheck` | brojanje potpunosti ([Potpunost](completeness.md)) i provjere entiteta, rezultata, id-ova i verzije |

---

Dio [3DHeata](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Izvor: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
