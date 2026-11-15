---
title: "Wéi e Replay gelies gëtt"
nav_order: 7
lang: lb
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Wéi e Replay gelies gëtt {#how-it-reads-a-replay}

E Replay ass en Header aus JSON-Blöck an dem Paketstroum vum Spill (Formatnotizen
an [`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Den éischte Block, am Kloren: d'Kaart, d'Clientversioun, den opuelende
  Spiller a säi Schëff, an d'Roster - den Numm vun all Spiller, Alliéierten oder Feind, a
  Schëffsnummer. Méi nei Clienten (15.x) setzen zwee weider Blöck derbäi: en eidelen, an
  de Kont vum opuelende Spiller an d'ID vum Gefecht als Text, gelies an
  `blockIds`. D'Resultater sinn net am JSON; 15.x hält se am Stroum.
- De Paketstroum, mat zlib komprimiert a mat Blowfish chiffréiert, mat engem Schlëssel, deen d'
  Spill mat sech dréit, dee Communautéitstools, déi dës Dateien liesen,
  verëffentlecht hunn. Dechiffréiert hält en:
  - d'Positiouns-Updates vun der Engine vun all Schëff, dat de Client konnt gesinn (säin
    eegent Team duerchgängeg, Feinde wann entdeckt oder no), e puermol d'Sekonn,
    während se sech bewegen, a méi seelen, während se dat net maachen;
  - dem opuelende Spiller säin eegent Schëff an engem Paket fir sech, ongeféier siwemol
    d'Sekonn;
  - eemol, um Ufank, d'Enregistremente vun de Spiller als gepickelt Python-Lëscht. Dës
    soen, wéi eng Entitéit am Stroum wéi ee Spiller ass. Hir Schlësselen si nummeréiert,
    an d'Nummere änneren sech mat Patchen, dofir fënnt de Reader d'Schlësselen un
    hire Wäerter: de Schlëssel, deen d'Nimm vun der Roster hält, an de Schlëssel, deen
    Entitéiten hält, déi Positiouns-Updates hunn;
  - dem Server säin Opruff, deen dem Client seet, datt e Schëff versonk ass: Affer, Killer,
    Ursaach. Et gëtt un senger Form fonnt (zwielef Bytes; déi éischt zwee sinn Schëffsentitéiten;
    all Affer erschéngt eemol), net un senger Nummer;
  - de Schued vun all Schëff: eng Array vun (Ugräifer, Schued) pro Treffer, op dem Schëff,
    dat getraff gouf; a säi Liewen, eng Propriétéit, déi e Moment virdrun gesat gëtt;
  - all Salv vu Granaten an Torpedoen, vun där de Client gesot krut: den Typ vun der Granat,
    de Schëtze, d'Salv, an de Start an d'Geschwindegkeet vun all Granat oder Torpedo;
  - wou Granaten opgehalen hunn: de Schëtze, en Treffertyp, an d'Plaz vun all (op
    15.x-Clienten mat méi iwwer d'Granat do, wou se getraff huet, wat iwwersprong gëtt);
  - de Chat: Sender, Kanal, Zeil;
  - gepickelt Opruffer un den opuelende Spiller: seng Schuedstatistiken, Updates vun den
    Enregistremente vun de Spiller, den Zoustand vum Gefecht;
  - op 15.x-Clienten, d'Resultater vum Gefecht um Enn: e Paket fir sech, e
    JSON-Objet mat der ID vum Gefecht, ganz gelies an dem Match-Dokument säi
    `results` (dem Spill seng eege Lëschten, onbenannt: `commonList`,
    `privateDataList`, `playersPublicInfo` pro Kont, ...).

Paket- a Methodennummeren, déi tëscht de gepréifte Versioune variéieren (dem
eegene Schëff säi Paket ass 43 oder 44, den Versenkungsopruff 76 oder 83, d'Granaten 101, 102,
126 oder 127), ginn all un der Form fonnt - kuck
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - sou datt e Patch, deen nei
nummeréiert, d'Tabell net eidel mécht. Déi fonnte Nummere stinn am `decoded` vum
Match-Dokument.

**De Pickle sinn onvertraut Daten.** E Replay ass eng Datei vun iwwerall, an e
Pickle kann Code nennen, deen ausgefouert gëtt. Hie gëtt mat engem Unpickler gelueden, dee jiddwer Klass
oder Funktioun, déi de Pickle nennt, duerch e inerte Platzhalter ersetzt, sou datt en einfach
Daten opbaut an näischt anescht. E Test fiddert him e Pickle, deen `os.system` opruft.

**Versenkunge** hunn déi exakt Zäit vum Opruff. Hir Plaz ass, wou d'Affer zuletzt
gesi gouf, wann dat bannent fënnef Sekonne war. **Den Ufank vum Gefecht** ass dee
Moment, wou iwwerhaapt e Schëff beweegt gëtt (Schëffer leien am Countdown roueg).

Alles, wat keng Tabellzeil ass, ass am [Match-Dokument](match-document.md).

**Wat dem Client gesot gouf**, ass komplett fir säin eegent Team a partiell fir
Feinde: hir Schëss, Treffer a Liewen sinn do, solaang se an der Reechwäit waren.

**Net gelies:**

- Fliger an hir Staffelen (d'Opruffer, déi se droen, goufen net auserneeggeholl), d'Visioun-
  Updates vun der Minikaart (gepaakt), Spotting, Bänner, Bränn a
  Iwwerschwemmunge als eege Evenementer (hire Schued ass an den Treffer), Verbrauchsgidder,
  Eroberungspunkten a Teamscoren (Propriétéite vun Entitéiten ouni
  Definitioun, net un der Form ennerscheet), de Rescht vun de Propriétéite vun engem Schëff
  (Ziel, Ruder, Geschwindegkeetsastellung...).
- D'Schlësselnummere vun de Spillerenregistremente a Schuedstatistiken als Nimm: d'Spill
  nummeréiert se, an d'Nummere änneren sech; si ginn als Zuelen behalen.
- Zousazdaten vun enger Granat do, wou se getraff huet (15.x), an d'Bytes no dem Start
  an der Geschwindegkeet vun enger Granat oder engem Torpedo.
- Resultater vu Clienten virun 15.x: hir Replays droen keng.
- D'Schëffsnummer als Numm: d'Nimm sinn an den eegene Parameterdateie vum Spill,
  net am Replay.

## Wéi d'Liese gepréift gouf {#how-the-reading-was-checked}

D'Liese gouf op ëffentleche Replays vu Clienten vun 0.9 bis 15.x gepréift, all
Wäert géint eppes, wat de Replay en zweet Kéier gëtt:

- **Positiounen:** d'Entitéit vun all Schëff huet mat engem Numm vun der Roster iwwereneestëmmt; Headings
  stëmmen bannent 0.1 rad mat der Beweegungsrichtung iwwereneen; no senger Versenkung
  beweegt sech e Schëff manner wéi 0.1 Eenheeten. E Schëff, dat roueg läit, gëtt méi seelen aktualiséiert.
- **Liewen:** all Schëff, dat am Bléck vum Client versonk ass, endet mat Liewe 0.
  Ongeféier d'Hallschent vun all Treffer passt zu engem Fall vum Liewe an der Sekonn virdrun; de
  Rescht fält zesumme mat Reparaturen oder aneren Treffer.
- **Schued géint dem Spill seng eege Statistiken:** um neiste Client ass dem
  opuelende Spiller säi gelies Schued bannent 0.1% vun de Statistiken. Op eelere
  Clienten sinn d'Statistike méi héich: dem Client gëtt net all Treffer geschéckt, oder
  d'Statistike zielen méi wéi Treffer (net geléist).
- **Granaten:** eng Granat fänkt e puer Eenheeten vun der leschter bekannter Positioun vu sengem Schëff un
  (d'Kanounen sinn iwwer de Rumpf verdeelt); bal all Enn vun enger Granat follegt,
  bannent enger Minutt, engem Schoss, deen de Client gesinn huet.

D'Tester bauen Replays an der selwechter Layout, dofir gëtt kee richtege Replay an
dësem Repository behalen.

**Net gepréift:** Clienten virun 0.9.6, de Lesta-Client (Mir Korabley),
Operatiounen a Szenarien iwwer ee eraus, Clan- a Ranked-Gefechter, a
wéi eng Schëffsnummer wéi ee Schëff ass.

---

Deel vun [3DHeat](https://github.com/Holdi601/3DHeat) ([Dokumentatioun](https://holdi601.github.io/3DHeat/)). Quell: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
