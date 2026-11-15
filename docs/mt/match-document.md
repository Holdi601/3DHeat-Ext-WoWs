---
title: "Id-dokument tal-partita"
nav_order: 6
lang: mt
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Id-dokument tal-partita {#the-match-document}

`<match>.match.json` iżomm dak kollu li r-ripetizzjoni tgħid li mhuwiex ringiela
tat-tabella. It-tab Partita tal-viewer taqrah. (Il-kodiċi jsejjaħlu s-sommarju.)

![Il-bidu ta' dokument tal-partita sintetiku, u ċ-ċwievet tiegħu](../assets/img/match-document.svg)

## Il-battalja {#the-battle}

| Ċavetta | X'inhi |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; l-id tal-battalja; il-mappa kif tisimha l-logħba (`spaces/<map>`) u l-isem tagħha li jidher |
| `clientVersion`, `streamVersion` | il-verżjoni tal-logħba mill-header, u kif tgħidha l-fluss tal-pakketti |
| `recorded` | meta ġiet irreġistrata r-ripetizzjoni, kif jikteb il-logħba |
| `player`, `vehicle` | il-plejer li rreġistra u l-vapur tiegħu |
| `gameType`, `scenario` | it-tip tal-battalja (`RandomBattle`, ...) u l-iskenarju, mill-header |
| `duration` | il-limitu tal-ħin tal-battalja f'sekondi, mill-header |
| `truncated` | ir-reġistrazzjoni waqfet kmieni |
| `battleStart`, `recordingSeconds` | il-bidu tal-battalja (l-ewwel mument li xi vapur jiċċaqlaq) u t-tul tar-reġistrazzjoni, f'sekondi |
| `positionPacket`, `ownPositionPacket` | in-numri tal-pakketti li fihom waslu l-pożizzjonijiet: ta' vapuri oħra, tal-plejer li rreġistra |
| `deathMethod` | in-numru tal-metodu li fih instabu l-għarqiet |
| `hz`, `ownHz`, `positions` | kampjuni fit-tieni ta' vapuri oħra u tal-vapur proprju; ringieli ta' pożizzjoni |
| `units` | unitajiet tad-dinja (15 m skont l-iskossijiet, 30 m skont il-firxiet tal-logħba); x lvant, y 'il fuq, z tramuntana |
| `events` | in-numru ta' ringieli tat-tabella għal kull avveniment |
| `decoded` | il-metodu u n-numri tal-pakketti misjuba għal kull tip ta' messaġġ |

## Plejers u avvenimenti {#players-and-events}

| Ċavetta | X'inhi |
|---|---|
| `players` | daħla għal kull vapur: isem, `ally` jew `enemy`, numru u isem tal-vapur, entità, kampjuni, qtil, baqa' ħaj; `seen` (ħsara magħmula u riċevuta, qxur, torpidnijiet u l-aħħar saħħa li ra l-klijent); `header` (id-daħla tar-roster) u `record` (ir-record tal-plejer mill-fluss, bin-numru taċ-ċavetta) |
| `kills` | kull għerq: ħin, vittma, qattiel, numru tal-kawża, post |
| `chat` | kull linja taċ-chat, bil-kanal u min bagħat |
| `damageStats` | l-istatistika proprja tal-plejer li rreġistra kif iżommha l-logħba: għal kull arma u tip, għadd u ammont (tip 0 huwa ħsara magħmula) |
| `avatarPickles` | kull sejħa pickled lill-plejer li rreġistra, deċifrata, bin-numru tal-metodu |

## Header, riżultati u kontrolli {#header-results-and-checks}

| Ċavetta | X'inhi |
|---|---|
| `header` | l-ewwel blokk JSON, kollu ħlief ir-roster: modalità tal-logħba, temp, tarf tal-mappa, daqsijiet tat-timijiet u aktar |
| `moreBlocks` | il-blokok JSON wara l-ewwel, kif inhuma |
| `blockIds` | 15.x: il-kont tal-plejer li rreġistra u l-id tal-battalja, moqrija bħala test |
| `results` | 15.x: ir-riżultati, li dawn il-klijenti jżommu fil-fluss |
| `entities` | kull entità li l-fluss joħloq: in-numru tat-tip u r-rwol, meta daħlet fil-vista tal-klijent u meta ħarġet |
| `selfCheck` | l-għadd tal-kompletezza ([Kompletezza](completeness.md)) u l-kontrolli tal-entitajiet, tar-riżultati, tal-ids u tal-verżjoni |

---

Parti mid-[3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentazzjoni](https://holdi601.github.io/3DHeat/)). Sors: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
