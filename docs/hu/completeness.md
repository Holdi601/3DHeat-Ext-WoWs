---
title: "Teljesség"
nav_order: 8
lang: hu
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Teljesség {#completeness}

A visszajátszásból semmi sem vész el. Amit a konvertáló beolvas, az a táblázatba és a
meccsdokumentumba kerül; minden más tételt egészben megtart a `<match>.messages.parquet`
kísérőfájl; a meccsdokumentum `selfCheck.completeness` mezője pedig számolja, mi lett
minden tételfajtával. Ez az a szabály, amelyet minden 3DHeat-konverter közösen követ:
[A konverterek mindent megtartanak](https://holdi601.github.io/3DHeat/converters.html).

![A szintetikus visszajátszás önellenőrzése: minden látott, beolvasott, megtartott vagy elveszett tétel](../assets/img/completeness.svg)

## A számlálás {#the-count}

Tételfajtánként a `selfCheck.completeness.types` a következőket adja:

| Számláló | Jelentése |
|---|---|
| `seen` | hány van a visszajátszásban |
| `decoded` | egészben beolvasva |
| `partial` | részben beolvasva, és egészben megtartva a kísérőfájlban |
| `raw` | csak egészben megtartva a kísérőfájlban, nincs beolvasva |
| `lost` | elveszett: mindig `0` |

A fajták a visszajátszás saját fajtái: `block <n>` (a JSON-blokkok), a tároló saját bájtjai,
`packet <type>`, és az entitásokon végzett hívásoknál `method <entity type>.<number>` és
`property <entity type>.<number>`. A `selfCheck.entities.roles` megmondja, melyik entitástípus a
felvevő játékos avatarja és melyik a hajók. Egy fajta, amelyről senki nem tudott, a darabszámával
együtt jelenik meg.

## A kísérőfájl {#the-sidecar}

| Oszlop | Mi |
|---|---|
| `time` | a visszajátszás órája, mint a táblázatban |
| `type`, `name` | a tétel fajtája; a konverter hogyan nevezi, ahol olvassa |
| `entity` | a hajó vagy avatar, amelyhez tartozik, mint a táblázat `entity` mezője |
| `decoded` | ami beolvasva belőle, JSON-ként |
| `payload`, `text` | a bájtjai egészben; a JSON-blokkok egészben |
| `entityType`, `packet`, `method` | a számok |

A sorok csomag, metódus, entitás és idő szerint vannak rendezve. Hogy melyik entitás melyik játékos:
a meccsdokumentum `entities` és `players` mezője.

## Mi van beolvasva, és hogyan ellenőriztük {#what-is-read-and-how-it-was-checked}

- **Az eredmények** (15.x, `results`): azonosítójuk a folyamé, és minden bennük szereplő játékos benne van a
  fejléc névsorában.
- **Az azonosító-blokk** (15.x, `blockIds`): a fiók és a csata, szövegként olvasva, így egyetlen számjegy sem vész el.
- **Minden pozíció dőlése és billenése**: a billenés a fordulás sebességével jár, ahogy egy hajó egy
  fordulóban dől; a dőlés szinte mindig 0.
- **Entitások** (`entities`): mikor kerültek a kliens látóterébe, és mikor távoztak onnan. Egyetlen
  hajónak sincs helye az eltűnése és visszatérése között.
- **A folyam verziója** (`streamVersion`): ugyanaz, mint a fejlécé.

Minden más beolvasott adat (elsüllyesztések, sebzés, életerő, lövedékek, torpedók, a lövedékek
végpontja, chat, pickle-hívások, a játékosok rekordjai, pozíciók) `partial`: a táblázatban vagy a
meccsdokumentumban van, és egészben megtartva a kísérőfájlban.

**Megtartva, de nincs beolvasva** (`raw`), a legnagyobb fajták: a táblázatban nem szereplő
helyzetfrissítések (miután egy hajó elsüllyedt, a játékos nélküli entitások), a gyakori
tulajdonságok és metódusok olvasó nélkül, az entitás-létrehozások tulajdonságai, és minden más
csomag, amelyhez nincs olvasó.

## Nem elérhető {#not-available}

- Ami a szerver soha nem küldött a felvevő kliensnek: más játékosok célzása, kamerája és
  bemenetei, az ellenségek, amíg nem voltak felfedezve. A visszajátszás azt tartalmazza, amit
  egy kliens megkapott.
- Az entitástípusok, metódusok, tulajdonságok és a statisztikák kulcsainak nevei: ezek a játék
  definíciós fájljaiban vannak, nem a visszajátszásban. A számok megmaradnak.
- A hajónevek a hajószámokhoz (a `--ship-names` kapcsolóval adhatók meg), és minden más, ami a
  játék saját fájljaiból kell.
- A 15.x előtti kliensek eredményei: a visszajátszásaikban nincsenek benne.

---

A [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentáció](https://holdi601.github.io/3DHeat/)) része. Forrás: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
