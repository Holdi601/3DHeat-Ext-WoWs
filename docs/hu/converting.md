---
title: "Visszajátszások konvertálása"
nav_order: 4
lang: hu
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Visszajátszások konvertálása {#converting-replays}

## Lépésről lépésre {#step-by-step}

1. **Kapcsold be a felvételt**: az `isReplayEnabled` beállítás a játék `preferences.xml`
   fájljában, vagy a játék saját beállítása, ahol van ilyen. Ettől kezdve a játék minden csatát a
   World of Warships telepítésed `replays` (visszajátszások) mappájába ment, például
   `C:\Games\World_of_Warships_EU\replays`.
2. **Nyiss egy terminált** abban a mappában, ahová az eredmények kerülhetnek
   ([Mielőtt elkezded](before-you-start.md)).
3. **Futtasd a konvertert** visszajátszás-fájlokra, vagy az ezeket tartalmazó mappákra:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   Az `out` a terminálod mappájában jön létre.
4. **Olvasd el, mit ír ki.** Visszajátszásonként egy sort kell látnod, a végén a táblázattal,
   amelyet írt.
5. **Nyisd meg az eredményt** a 3DHeat megjelenítőben: az `out/<map>/<match>.parquet` a Hőtérkép
   fülön, a `<match>.match.json` a Meccs fülön. Vagy olvasd be bármely Parquet- vagy JSON-olvasóval.

![Futtatás szintetikus visszajátszáson: konvertálás, újrafuttatás, egy sérült fájl, egy üres mappa](../assets/img/convert.svg)

A kép egy olyan visszajátszáson készült futtatást mutat, amelyet a tesztek kódban hoznak létre
(valódi visszajátszás nélkül):

- egy visszajátszás konvertálva: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- újrafuttatáskor a már megírt meccs kimarad: `<file>: already written, <table>`;
- egy fájl, amely nem visszajátszás: `<file>: not converted: <why>` (a hibakimenetre; kilépési állapot 1,
  a többi visszajátszás attól még konvertálódik);
- nincs visszajátszás: `no .wowsreplay files in <folders>` (kilépési állapot 2).

## Kapcsolók {#options}

| Kapcsoló | Alapértelmezés | Mit tesz |
|---|---|---|
| `replays` (egy vagy több) | - | `.wowsreplay` fájlok, vagy mappák, amelyekben ezeket keresi (az almappákban is) |
| `-o`, `--out` | kötelező | az a mappa, ahová ír: bennük mappa minden térképhez |
| `--force` | ki | újra konvertálja, ami már meg van írva |
| `--ship-names JSON` | - | egy JSON-fájl `{"<shipId>": "<name>", ...}` alakban: a visszajátszások csak a felvevő játékos hajóját nevezik meg, a többit számmal |
| `--version` | - | kiírja a `heat3d-wows-replay <version>` szöveget, és leáll |
| `-h`, `--help` | - | kiírja a kapcsolókat, és leáll |

A kapcsolók ahogy a program kiírja: [Parancsreferencia](../cli-reference.md).

## Mi íródik ki {#what-is-written}

Csak külön fájlok: ez a konverter nem ír `.3dheat` fájlt (a megjelenítő egybe csomagolhatja:
[Egy fájl egy meccshez](https://holdi601.github.io/3DHeat/container.html)).
Visszajátszásonként, az `out/<map>/` mappába (a térkép nevéből a `spaces/` nélkül):

| Fájl | Mi |
|---|---|
| `<match>.parquet` | a táblázat: minden hajó helyzete időben, és minden esemény, ahol történt ([A táblázat](table.md)) |
| `<match>.match.json` | a meccsdokumentum: térkép, kliensverzió, játékosok, elsüllyesztések, chat és minden más ([A meccsdokumentum](match-document.md)) |
| `<match>.messages.parquet` | a kísérőfájl: a visszajátszás minden olyan tétele, amelyet a fenti két fájl nem tart meg egészben ([Teljesség](completeness.md)) |

A `<match>` a csata saját azonosítója, vagy a fájl neve, ha a felvétel az eredmények előtt állt le.

## Kilépési állapot {#exit-status}

`0`, ha minden visszajátszás konvertálódott vagy kimaradt; `1`, ha bármelyik nem sikerült (a többit
attól még konvertálja); `2`, ha nem találtunk visszajátszás-fájlt.

---

A [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentáció](https://holdi601.github.io/3DHeat/)) része. Forrás: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
