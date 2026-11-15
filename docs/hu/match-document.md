---
title: "A meccsdokumentum"
nav_order: 6
lang: hu
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# A meccsdokumentum {#the-match-document}

A `<match>.match.json` mindent tartalmaz, amit a visszajátszás elmond, és ami nem a táblázat egy
sora. A megjelenítő Meccs fülje ezt olvassa. (A kód összefoglalónak nevezi.)

![Egy szintetikus meccsdokumentum eleje és kulcsai](../assets/img/match-document.svg)

## A csata {#the-battle}

| Kulcs | Mi |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; a csata azonosítója; a térkép a játék nevével (`spaces/<map>`) és a megjelenő neve |
| `clientVersion`, `streamVersion` | a játék verziója a fejlécből, és ahogy a csomagfolyam megadja |
| `recorded` | mikor lett a visszajátszás rögzítve, ahogy a játék írja |
| `player`, `vehicle` | a felvevő játékos és a hajójuk |
| `gameType`, `scenario` | a csata típusa (`RandomBattle`, ...) és forgatókönyve, a fejlécből |
| `duration` | a csata időkorlátja másodpercben, a fejlécből |
| `truncated` | a felvétel korán megállt |
| `battleStart`, `recordingSeconds` | a csata kezdete (az első pillanat, amikor bármelyik hajó mozog) és a felvétel hossza másodpercben |
| `positionPacket`, `ownPositionPacket` | a csomagszámok, amelyekben a pozíciók érkeztek: a többi hajóé, a felvevő játékosé |
| `deathMethod` | a metódusszám, amelyben az elsüllyesztéseket megtaláltuk |
| `hz`, `ownHz`, `positions` | minta másodpercenként a többi hajóról és a saját hajóról; pozíciósorok |
| `units` | világegységek (a hajótestek szerint 15 m, a játék hatótávolságai szerint 30 m); x kelet, y fel, z észak |
| `events` | minden eseményfajta táblázatbeli sorainak száma |
| `decoded` | minden üzenetfajtához megtalált metódus- és csomagszámok |

## Játékosok és események {#players-and-events}

| Kulcs | Mi |
|---|---|
| `players` | egy bejegyzés hajónként: név, `ally` vagy `enemy`, hajószám és név, entitás, minták, ölések, túlélte-e; `seen` (a kliens által látott okozott és kapott sebzés, lövedékek, torpedók és utolsó életerő); `header` (a névsor bejegyzése) és `record` (a játékos rekordja a folyamból, a kulcs száma szerint) |
| `kills` | minden elsüllyesztés: idő, áldozat, gyilkos, az ok száma, hely |
| `chat` | minden chat-sor, csatornával és küldővel |
| `damageStats` | a felvevő játékos saját statisztikái, ahogy a játék vezeti: fegyverenként és fajtánként darabszám és összeg (a 0-s fajta az okozott sebzés) |
| `avatarPickles` | minden pickle-hívás a felvevő játékosnak, dekódolva, metódusszám szerint |

## Fejléc, eredmények és ellenőrzések {#header-results-and-checks}

| Kulcs | Mi |
|---|---|
| `header` | az első JSON-blokk, a névsor kivételével: játékmód, időjárás, pályahatár, csapatméretek és más |
| `moreBlocks` | az első utáni JSON-blokkok, változtatás nélkül |
| `blockIds` | 15.x: a felvevő játékos fiókja és a csata azonosítója, szövegként olvasva |
| `results` | 15.x: az eredmények, amelyeket ezek a kliensek a folyamban tartanak |
| `entities` | minden entitás, amelyet a folyam létrehoz: típusszáma és szerepe, mikor került a kliens látóterébe, és mikor távozott onnan |
| `selfCheck` | a teljességi számlálás ([Teljesség](completeness.md)), és az entitások, az eredmények, az azonosítók és a verzió ellenőrzései |

---

A [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentáció](https://holdi601.github.io/3DHeat/)) része. Forrás: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
