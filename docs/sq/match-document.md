---
title: "Dokumenti i ndeshjes"
nav_order: 6
lang: "sq"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Dokumenti i ndeshjes {#the-match-document}

`<match>.match.json` mban gjithçka që thotë riluajtja dhe që nuk është rresht i
tabelës. Skeda Ndeshja e shikuesit e lexon. (Kodi e quan summary.)

![Fillimi i një dokumenti ndeshjeje sintetik, dhe çelësat e tij](../assets/img/match-document.svg)

## Beteja {#the-battle}

| Çelësi | Çfarë |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; ID e betejës; harta siç e emërton loja (`spaces/<map>`) dhe emri i saj i shfaqur |
| `clientVersion`, `streamVersion` | versioni i lojës nga header-i, dhe siç e thotë rrjedha e paketave |
| `recorded` | kur u regjistrua riluajtja, siç e shkruan loja |
| `player`, `vehicle` | lojtari që regjistron dhe anija e tij |
| `gameType`, `scenario` | lloji i betejës (`RandomBattle`, ...) dhe skenari, nga header-i |
| `duration` | kufiri kohor i betejës në sekonda, nga header-i |
| `truncated` | regjistrimi u ndal herët |
| `battleStart`, `recordingSeconds` | fillimi i betejës (çasti i parë kur lëviz ndonjë anije) dhe gjatësia e regjistrimit, në sekonda |
| `positionPacket`, `ownPositionPacket` | numrat e paketave në të cilat erdhën pozicionet: të anijeve të tjera, të lojtarit që regjistron |
| `deathMethod` | numri i metodës në të cilën u gjetën fundosjet |
| `hz`, `ownHz`, `positions` | mostra në sekondë të anijeve të tjera dhe të anijes së vet; rreshta pozicioni |
| `units` | njësi botërore (15 m sipas trupave, 30 m sipas rrezeve të lojës); x lindje, y lart, z veri |
| `events` | numri i rreshtave të tabelës për çdo ngjarje |
| `decoded` | metoda dhe numrat e paketave të gjetura për çdo lloj mesazhi |

## Lojtarët dhe ngjarjet {#players-and-events}

| Çelësi | Çfarë |
|---|---|
| `players` | një hyrje për anije: emri, `ally` ose `enemy`, numri dhe emri i anijes, entiteti, mostrat, vrasjet, mbijetoi; `seen` (dëmi i shkaktuar dhe i marrë, predhat, silurët dhe shëndeti i fundit që pa klienti); `header` (hyrja e listës) dhe `record` (regjistri i lojtarit nga rrjedha, sipas numrit të çelësit) |
| `kills` | çdo fundosje: koha, viktima, vrasësi, numri i shkakut, vendi |
| `chat` | çdo rresht bisede, me kanalin dhe dërguesin |
| `damageStats` | statistikat e vetë lojtarit që regjistron siç i mban loja: për armë dhe lloj, një numër dhe një sasi (lloji 0 është dëmi i shkaktuar) |
| `avatarPickles` | çdo thirrje e serializuar (pickle) për lojtarin që regjistron, e dekoduar, sipas numrit të metodës |

## Header-i, rezultatet dhe kontrollet {#header-results-and-checks}

| Çelësi | Çfarë |
|---|---|
| `header` | blloku i parë JSON, i gjithë përveç listës: mënyra e lojës, moti, kufiri i hartës, madhësitë e skuadrave e më shumë |
| `moreBlocks` | blloqet JSON pas të parit, siç janë |
| `blockIds` | 15.x: llogaria e lojtarit që regjistron dhe ID e betejës, lexuar si tekst |
| `results` | 15.x: rezultatet, që këta klientë i mbajnë në rrjedhë |
| `entities` | çdo entitet që krijon rrjedha: numri i llojit dhe roli i tij, kur hyri në pamjen e klientit dhe kur doli |
| `selfCheck` | numërimi i plotësisë ([Plotësia](completeness.md)) dhe kontrollet e entiteteve, rezultateve, ID-ve dhe versionit |

---

Pjesë e [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacioni](https://holdi601.github.io/3DHeat/)). Burimi: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
