---
title: Sådan læses et replay
nav_order: 7
lang: da
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Sådan læses et replay {#how-it-reads-a-replay}

Et replay er en header af JSON-blokke og spillets pakkestrøm (formatnoter i
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Den første blok, i klartekst: kortet, klientversionen, den optagende spiller og skib, og rosteren - hver
  spillers navn, allieret eller fjende, og skibsnummer. Nyere klienter (15.x) tilføjer to blokke mere: en tom,
  og den optagende spillers konto og kampens id som tekst, læst ind i `blockIds`. Resultaterne står ikke i JSON'en;
  15.x gemmer dem i strømmen.
- Pakkestrømmen, zlib-komprimeret og Blowfish-krypteret med en nøgle, spillet bærer, og som fællesskabets
  værktøjer, der læser disse filer, har offentliggjort. Dekrypteret rummer den:
  - motorens positionsopdateringer for hvert skib, klienten kunne se (dets eget hold hele tiden, fjender mens de
    er spottet eller i nærheden), flere gange i sekundet, mens de bevæger sig, og sjældnere, når de ikke gør det;
  - den optagende spillers eget skib i en pakke for sig selv, ca. syv gange i sekundet;
  - én gang, i starten, spillernes optegnelser som en indpakket Python-liste. Disse siger, hvilken entitet i
    strømmen der er hvilken spiller. Deres nøgler er nummererede, og numrene ændrer sig med patches, så læseren
    finder nøglerne ud fra deres værdier: nøglen, der holder rosterens navne, og nøglen, der holder entiteter med
    positionsopdateringer;
  - serverens kald, der fortæller klienten, at et skib er sunket: offer, dræber, årsag. Det findes ud fra sin form
    (tolv bytes; de første to er skibsentiteter; hvert offer optræder én gang), ikke ud fra sit nummer;
  - hvert skibs skade: en række af (angriber, skade) pr. træf, på det ramte skib; og dets liv, en egenskab, der
    sættes et øjeblik før;
  - hver salve af granater og torpedoer, klienten fik besked om: granattypen, skytten, salven, og hver granats eller
    torpedos start og hastighed;
  - hvor granater endte: skytten, en trætype, og stedet for hver (på 15.x-klienter med mere om granaten dér, hvor
    den ramte, hvilket springes over);
  - chatten: afsender, kanal, linje;
  - indpakkede kald til den optagende spiller: dens skadestatistik, opdateringer af spillernes optegnelser, kampens
    tilstand;
  - på 15.x-klienter, kampens resultater til sidst: en pakke for sig selv, et JSON-objekt med kampens id, læst helt
    ind i kampdokumentets `results` (spillets egne lister, uden navne: `commonList`, `privateDataList`,
    `playersPublicInfo` pr. konto, ...).

Pakke- og metodenumre, der er forskellige mellem de kontrollerede versioner (det egne skibs pakke er 43 eller 44,
søenkningskaldet 76 eller 83, granaterne 101, 102, 126 eller 127), findes alle ud fra form - se
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - så en
omnummerering i en patch tømmer ikke tabellen. De fundne tal står i kampdokumentets `decoded`.

**Den indpakkede Python-liste er ikke-betroede data.** Et replay er en fil fra hvor som helst, og en pickle kan navngive
kode, der skal køres. Den indlæses med en unpickler, der giver hver klasse eller funktion, pickle'en navngiver, en inert
placeholder, så den bygger almindelige data og intet andet. En test giver den en pickle, der kalder `os.system`.

**Søenkninger** har kaldets nøjagtige tidspunkt. Deres sted er, hvor offeret sidst blev set, når det var inden for fem
sekunder. **Kampens start** er det første øjeblik, noget skib overhovedet bevæger sig (skibe ligger stille i nedtællingen).

Alt, der ikke er en tabelrække, står i [kampdokumentet](match-document.md).

**Det, klienten fik at vide,** er fuldstændigt for sit eget hold og delvist for fjender: deres skud, træf og liv er der,
mens de er inden for rækkevidde.

**Ikke læst:**

- Fly og deres eskadriller (kaldene, der bærer dem, blev ikke skilt ad), minikortets synsopdateringer (pakket), spotting,
  bånd, brande og oversvømmelser som begivenheder for sig selv (deres skade står i træffene), forbrugsvarer,
  erobringspoint og holdscorer (egenskaber for entiteter uden en definition, ikke skilt fra hinanden på formen), resten af
  et skibs egenskaber (sigte, ror, hastighedsindstilling ...).
- Spillernes optegnelsers og skadestatistikkens nøglenumre som navne: spillet nummererer dem, og numrene ændrer sig; de
  gemmes som tal.
- En granats ekstra data dér, hvor den ramte (15.x), og bytes efter en granats eller torpedos start og hastighed.
- Resultater fra klienter før 15.x: deres replays har ingen.
- Skibsnummeret som navn: navnene står i spillets egne parameterfiler, ikke i replayet.

## Sådan blev læsningen kontrolleret {#how-the-reading-was-checked}

Læsningen blev kontrolleret på offentlige replays af klienter fra 0.9 til 15.x, hver værdi mod noget, replayet giver en
anden gang:

- **Positioner:** hvert skibs entitet matchede et rosternavn; headingerne stemmer med færdens retning inden for 0,1 rad;
  efter sin søenkning bevæger et skib sig mindre end 0,1 enheder. Et skib, der ligger stille, opdateres sjældnere.
- **Liv:** hvert skib, der blev sænket inden for klientens udsyn, ender med liv 0. Ca. halvdelen af alle træf matcher et
  fald i liv i sekundet før; resten falder sammen med reparationer eller andre træf.
- **Skade mod spillets egen statistik:** på den nyeste klient ligger den optagende spillers læste skade inden for 0,1 % af
  statistikken. På ældre klienter er statistikken højere: klienten får ikke sendt hvert træf, eller statistikken tæller
  mere end træf (ikke afklaret).
- **Granater:** en granat starter nogle få enheder fra sit skibs sidst kendte position (kanonerne er spredt langs skroget);
  næsten hver granats ende følger, inden for et minut, et skud klienten så.

Testene bygger replays efter det samme layout, så intet rigtigt replay gemmes i dette repository.

**Ikke kontrolleret:** klienter før 0.9.6, Lesta-klienten (Mir Korabley), operationer og scenarier ud over ét, klan- og
rangerede kampe, og hvilket skibsnummer der er hvilket skib.

---

Del af [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentation](https://holdi601.github.io/3DHeat/)). Kilde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
