---
title: Dokument tekme
nav_order: 6
lang: sl
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Dokument tekme {#the-match-document}

`<match>.match.json` hrani vse, kar posnetek pove in ni vrstica tabele. Zavihek Tekma v pregledovalniku ga bere.
(Koda ga imenuje povzetek.)

![Začetek sintetičnega dokumenta tekme in njegovi ključi](../assets/img/match-document.svg)

## Bitka {#the-battle}

| Ključ | Kaj |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; identifikator bitke; zemljevid, kot ga imenuje igra (`spaces/<map>`), in njegovo prikazno ime |
| `clientVersion`, `streamVersion` | različica igre iz glave in kot jo pove paketni tok |
| `recorded` | kdaj je bil posnetek narejen, kot ga zapiše igra |
| `player`, `vehicle` | igralec, ki je snemal, in njegova ladja |
| `gameType`, `scenario` | vrsta bitke (`RandomBattle`, ...) in scenarij, iz glave |
| `duration` | časovna omejitev bitke v sekundah, iz glave |
| `truncated` | snemanje se je ustavilo zgodaj |
| `battleStart`, `recordingSeconds` | začetek bitke (prvi trenutek, ko se katerakoli ladja premakne) in dolžina posnetka, v sekundah |
| `positionPacket`, `ownPositionPacket` | številke paketov, v katerih so prišli položaji: drugih ladij, igralca, ki je snemal |
| `deathMethod` | številka metode, v kateri so bile najdene potopitve |
| `hz`, `ownHz`, `positions` | vzorci na sekundo drugih ladij in lastne ladje; vrstice položajev |
| `units` | svetovne enote (15 m po trupih, 30 m po igrinih dosegih); x vzhod, y gor, z sever |
| `events` | število vrstic tabele za vsak dogodek |
| `decoded` | številke metod in paketov, najdene za vsako vrsto sporočila |

## Igralci in dogodki {#players-and-events}

| Ključ | Kaj |
|---|---|
| `players` | en vnos za ladjo: ime, `ally` ali `enemy`, številka ladje in ime, entiteta, vzorci, ubijanja, preživel; `seen` (nanesena in prejeta škoda, streli, torpedi in zadnje zdravje, ki ga je videl odjemalec); `header` (vnos s seznama) in `record` (zapis igralca iz toka, po številki ključa) |
| `kills` | vsaka potopitev: čas, žrtev, ubijalec, številka vzroka, mesto |
| `chat` | vsaka vrstica klepeta, s kanalom in pošiljateljem |
| `damageStats` | lastna statistika igralca, ki je snemal, kot jo hrani igra: po orožju in vrsti število in znesek (vrsta 0 je nanesena škoda) |
| `avatarPickles` | vsak prejeti klic igralca, ki je snemal, dekodiran, po številki metode |

## Glava, rezultati in preverjanja {#header-results-and-checks}

| Ključ | Kaj |
|---|---|
| `header` | prvi blok JSON, ves razen seznama: način igre, vreme, meja zemljevida, velikosti ekip in več |
| `moreBlocks` | bloki JSON za prvim, kot so |
| `blockIds` | 15.x: račun igralca, ki je snemal, in identifikator bitke, prebrana kot besedilo |
| `results` | 15.x: rezultati, ki jih ti odjemalci hranijo v toku |
| `entities` | vsaka entiteta, ki jo ustvari tok: njena številka tipa in vloga, kdaj je prišla v pogled odjemalca in kdaj ga je zapustila |
| `selfCheck` | število popolnosti ([Popolnost](completeness.md)) in preverjanja entitet, rezultatov, identifikatorjev in različice |

---

Del [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Vir: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
