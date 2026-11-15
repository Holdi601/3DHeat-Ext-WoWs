---
title: "Hogyan olvassa a visszajátszást"
nav_order: 7
lang: hu
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Hogyan olvassa a visszajátszást {#how-it-reads-a-replay}

A visszajátszás JSON-blokkok fejlécéből és a játék csomagfolyamából áll (a formátum
megjegyzései itt: [`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Az első blokk, titkosítatlanul: a térkép, a kliens verziója, a felvevő játékos és hajója, és a
  névsor – minden játékos neve, szövetséges vagy ellenség, és a hajószáma. Az újabb kliensek (15.x)
  két további blokkot tesznek hozzá: egy üreset, és a felvevő játékos fiókját és a csata
  azonosítóját szövegként, a `blockIds` mezőbe olvasva. Az eredmények nincsenek a JSON-ban; a 15.x
  a folyamban tartja őket.
- A csomagfolyam, zlib-tömörítve és a játék által hordozott kulccsal Blowfish-titkosítva, amelyet a
  közösség eszközei, amelyek ezeket a fájlokat olvassák, közzétettek. Visszafejtve tartalmazza:
  - a motor helyzetfrissítéseit minden hajóról, amelyet a kliens láthatott (a saját csapatát végig,
    az ellenségeket felderítve vagy közel), többször másodpercenként, amíg mozognak, és ritkábban,
    amikor nem;
  - a felvevő játékos saját hajóját egy saját csomagban, körülbelül másodpercenként hétszer;
  - egyszer, az elején, a játékosok rekordjait egy pickle-ölt Python-listában. Ezek megmondják, a
    folyamban melyik entitás melyik játékos. A kulcsaik számozottak, és a számok a javításokkal
    változnak, ezért az olvasó a kulcsokat az értékeik szerint találja meg: azt a kulcsot, amely a
    névsor neveit tartja, és azt, amely a helyzetfrissítésekkel rendelkező entitásokat;
  - a szerver hívása, amely a kliensnek jelzi, hogy egy hajó elsüllyedt: áldozat, gyilkos, ok. Alakja
    alapján találjuk meg (tizenkét bájt; az első kettő hajó-entitás; minden áldozat egyszer szerepel),
    nem a száma alapján;
  - minden hajó sebzése: egy (támadó, sebzés) tömb találatonként, az eltalált hajón; és az életereje, egy
    tulajdonság, amelyet egy pillanattal korábban állítanak be;
  - minden lövedék- és torpedó-salvó, amelyről a kliens értesült: a lövedék típusa, a lövő, a salvó, és
    minden lövedék vagy torpedó kezdőpontja és sebessége;
  - hová értek a lövedékek: a lövő, egy találattípus, és mindegyik helye (15.x kliensnél több adat is
    a lövedékről, ahol becsapódott, ezt kihagyjuk);
  - a chat: küldő, csatorna, sor;
  - a felvevő játékosnak szóló pickle-hívások: a sebzési statisztikái, a játékosok rekordjainak frissítései,
    a csata állapota;
  - 15.x kliensen a csata eredményei a végén: egy saját csomagban, egy JSON-objektum a csata
    azonosítójával, egészben beolvasva a meccsdokumentum `results` mezőjébe (a játék saját listái, név
    nélkül: `commonList`, `privateDataList`, `playersPublicInfo` fiókonként, ...).

A csomag- és metódusszámok, amelyek az ellenőrzött verziókban eltérnek (a saját hajó csomagja 43 vagy 44,
az elsüllyesztési hívás 76 vagy 83, a lövedékek 101, 102, 126 vagy 127) mind alakjuk alapján vannak
megtalálva – lásd [`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) –,
így egy átszámozó javítás nem üríti ki a táblázatot. A megtalált számok a meccsdokumentum `decoded` mezőjében vannak.

**A pickle nem megbízható adat.** A visszajátszás bárhonnan származó fájl, a pickle pedig futtatandó
kódot nevezhet meg. Olyan olvasóval töltjük be, amely minden osztálynak vagy függvénynek, amelyet a pickle
megnevez, egy tehetetlen helyettesítőt ad, így csak egyszerű adatot épít, mást semmit. Egy teszt olyan
pickle-lel fut, amely `os.system`-et hív.

**Az elsüllyesztések** időpontja a hívás pontos ideje. A helyük ott van, ahol az áldozatot utoljára látták,
ha ez öt másodpercen belül volt. **A csata kezdete** az első pillanat, amikor bármelyik hajó egyáltalán mozog
(a hajók a visszaszámlálás alatt állnak).

Minden, ami nem táblázatsor, a [meccsdokumentumban](match-document.md) van.

**Amit a kliens megkapott,** az a saját csapatára teljes, az ellenségekre részleges: a lövéseik, találataik és
életerejük ott vannak, amíg hatótávolságban voltak.

**Nincs olvasva:**

- A repülőgépek és rajaik (a hívások, amelyek hordozzák őket, nem lettek szétszedve), a kistérkép látási
  frissítései (tömörítve), a felderítés, a szalagok, a tüzek és az elöntések mint saját események (a sebzésük a
  találatokban van), a fogyóeszközök, a befogási pontok és a csapatok pontszámai (olyan entitások tulajdonságai,
  amelyekhez nincs definíció, és alakjuk alapján nem különböztethetők meg), a hajó többi tulajdonsága
  (célzás, kormány, sebességbeállítás...).
- A játékosrekordok és a sebzési statisztikák kulcsainak számai nevekként: a játék számozza őket, és a
  számok változnak; számként maradnak meg.
- A lövedék extra adatai azon a helyen, ahol becsapódott (15.x), és a lövedék- vagy torpedókezdet utáni bájtok.
- A 15.x előtti kliensek eredményei: a visszajátszásaikban nincsenek benne.
- A hajószám mint név: a nevek a játék saját paraméterfájljaiban vannak, nem a visszajátszásban.

## Hogyan ellenőriztük az olvasást {#how-the-reading-was-checked}

Az olvasást a 0.9-es és a 15.x közötti kliensek nyilvános visszajátszásain ellenőriztük, minden értéket
összevetve valamivel, amit a visszajátszás másodszor is megad:

- **Pozíciók:** minden hajó entitása megegyezett egy névsori névvel; az irányok a haladási iránnyal 0,1 radiánon
  belül egyeznek; elsüllyedése után egy hajó 0,1 egységnél kevesebbet mozdul. Egy álló hajó ritkábban frissül.
- **Életerő:** minden a kliens látóterében elsüllyedt hajó 0 életerővel ér véget. A találatok közel felének a
  másodperccel korábbi életerő-csökkenés felel meg; a többi a javításokkal vagy más találatokkal együtt esik.
- **Sebzés a játék saját statisztikáival összevetve:** a legújabb kliensen a felvevő játékos olvasott sebzése
  0,1%-on belül van a statisztikától. A régebbi klienseken a statisztikák magasabbak: a kliens nem kap minden
  találatot, vagy a statisztikák többet számolnak, mint a találatok (nincs feloldva).
- **Lövedékek:** egy lövedék néhány egységnyire indul az utolsó ismert hajóhelyzetétől (az ágyúk a hajótest mentén
  vannak szétosztva); szinte minden lövedék vége egy percen belül egy olyan lövést követ, amelyet a kliens látott.

A tesztek ugyanezzel az elrendezéssel építik fel a visszajátszásokat, így valódi visszajátszás nincs
megtartva ebben a tárolóban.

**Nincs ellenőrizve:** a 0.9.6 előtti kliensek, a Lesta-kliens (Mir Korabley), az egynél több művelet és
forgatókönyv, a klán- és a rangsoroló csaták, és hogy melyik hajószám melyik hajó.

---

A [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentáció](https://holdi601.github.io/3DHeat/)) része. Forrás: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
