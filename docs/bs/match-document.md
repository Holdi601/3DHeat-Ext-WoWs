---
title: "Dokument meča"
nav_order: 6
lang: "bs"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Dokument meča {#the-match-document}

`<match>.match.json` sadrži sve što replay kaže a nije red
tabele. Kartica Meč preglednika ga čita. (Kod ga naziva sažetkom.)

![Početak sintetičkog dokumenta meča i njegovi ključevi](../assets/img/match-document.svg)

## Bitka {#the-battle}

| Ključ | Šta |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; id bitke; mapa kako je igra imenuje (`spaces/<map>`) i njeno prikazano ime |
| `clientVersion`, `streamVersion` | verzija igre iz zaglavlja, i kako je kaže tok paketa |
| `recorded` | kada je replay snimljen, kako ga igra piše |
| `player`, `vehicle` | igrač koji snima i njegov brod |
| `gameType`, `scenario` | tip bitke (`RandomBattle`, ...) i scenarij, iz zaglavlja |
| `duration` | vremensko ograničenje bitke u sekundama, iz zaglavlja |
| `truncated` | snimanje je stalo prije vremena |
| `battleStart`, `recordingSeconds` | početak bitke (prvi trenutak kad se ijedan brod pomjeri) i trajanje snimka, u sekundama |
| `positionPacket`, `ownPositionPacket` | brojevi paketa u kojima su došle pozicije: drugih brodova, igrača koji snima |
| `deathMethod` | broj metode u kojoj su pronađena potonuća |
| `hz`, `ownHz`, `positions` | uzoraka u sekundi drugih brodova i vlastitog broda; redovi pozicija |
| `units` | jedinice svijeta (15 m prema trupovima, 30 m prema dometima igre); x istok, y gore, z sjever |
| `events` | broj redova tabele za svaki događaj |
| `decoded` | metoda i brojevi paketa pronađeni za svaku vrstu poruke |

## Igrači i događaji {#players-and-events}

| Ključ | Šta |
|---|---|
| `players` | jedna stavka po brodu: ime, `ally` ili `enemy`, broj i ime broda, entitet, uzorci, ubistva, preživio; `seen` (nanesena i primljena šteta, granate, torpeda i zadnje zdravlje koje je klijent vidio); `header` (stavka spiska) i `record` (zapis igrača iz toka, po broju ključa) |
| `kills` | svako potonuće: vrijeme, žrtva, ubica, broj uzroka, mjesto |
| `chat` | svaki red četa, s kanalom i pošiljaocem |
| `damageStats` | vlastita statistika igrača koji snima kako je igra vodi: po oružju i vrsti, broj i iznos (vrsta 0 je nanesena šteta) |
| `avatarPickles` | svaki pickled poziv igraču koji snima, dekodiran, po broju metode |

## Zaglavlje, rezultati i provjere {#header-results-and-checks}

| Ključ | Šta |
|---|---|
| `header` | prvi JSON blok, sve osim spiska: način igre, vrijeme, granica mape, veličine timova i više |
| `moreBlocks` | JSON blokovi poslije prvog, kakvi jesu |
| `blockIds` | 15.x: račun igrača koji snima i id bitke, pročitani kao tekst |
| `results` | 15.x: rezultati, koje ovi klijenti čuvaju u toku |
| `entities` | svaki entitet koji tok stvara: njegov broj tipa i uloga, kada je ušao u vidokrug klijenta i kada ga je napustio |
| `selfCheck` | broj potpunosti ([Potpunost](completeness.md)) i provjere entiteta, rezultata, id-ova i verzije |

---

Dio [3DHeata](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Izvor: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
