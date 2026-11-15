---
title: "Hvernig upptaka er lesin"
nav_order: 7
lang: is
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Hvernig upptaka er lesin {#how-it-reads-a-replay}

Upptaka er haus úr JSON-blokkum og pakkastraumur leiksins (sniðathugasemdir
í [`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Fyrsta blokkin, ódulkóðuð: kortið, útgáfa biðlarans, upptökumaðurinn
  og skip hans, og listinn yfir þátttakendur - nafn hvers spilara, bandamaður eða óvinur, og
  skipanúmer. Nýrri biðlarar (15.x) bæta við tveimur blokkum til viðbótar: tómri, og
  reikningi upptökumannsins og auðkenni bardagans sem texta, lesið í
  `blockIds`. Niðurstöðurnar eru ekki í JSON; 15.x geymir þær í straumnum.
- Pakkastraumurinn, zlib-þjappaður og Blowfish-dulkóðaður með lykli sem
  leikurinn ber með sér, og samfélagsverkfærin sem lesa þessar skrár hafa
  birt. Afkóðaður geymir hann:
  - stöðuuppfærslur vélarinnar fyrir hvert skip sem biðlarinn gat séð (eigið
    lið allan tímann, óvini meðan þeir voru sénir eða nálægir), nokkrum sinnum á
    sekúndu meðan þau hreyfast og sjaldnar meðan þau gera það ekki;
  - eigið skip upptökumannsins í eigin pakka, um sjö sinnum
    á sekúndu;
  - einu sinni, í upphafi, skrár spilaranna sem pickled Python-lista. Þær
    segja hver eining í straumnum er hvaða spilari. Lyklar þeirra eru númeraðir,
    og númerin breytast með uppfærslum, svo lesarinn finnur lyklana eftir
    gildum þeirra: lykillinn sem geymir nöfn listans yfir þátttakendur, og lykillinn sem geymir
    einingar sem hafa stöðuuppfærslur;
  - kall þjónsins sem segir biðlaranum að skip hafi sokkið: fórnarlamb, drápsmaður,
    orsök. Það er fundið eftir lögun sinni (tólf bæti; fyrstu tvö eru skipseiningar;
    hvert fórnarlamb birtist einu sinni), ekki eftir númeri;
  - skaða hvers skips: fylki af (árásarmaður, skaði) fyrir hvert högg, á skipinu
    sem varð fyrir því; og heilsu þess, eiginleika sem er stilltur augnabliki áður;
  - hverja skothríð (salvo) af skeljum og tundurskeytum sem biðlaranum var sagt frá: gerð
    skeljar, skyttan, skothríðin, og upphaf og hraði hverrar skeljar eða tundurskeytis;
  - hvar skeljar enduðu: skyttan, högggerð, og staður hverrar (á
    15.x biðlurum með meira um skelina þar sem hún hitti, sem er sleppt);
  - spjallið: sendandi, rás, lína;
  - pickled köll til upptökumannsins: skaðatölfræði hans, uppfærslur á
    skrám spilaranna, ástand bardagans;
  - á 15.x biðlurum, niðurstöður bardagans í lokin: eigin pakki, JSON-hlutur
    með auðkenni bardagans, lesinn í heild í `results` í leikjaskjalinu (eigin listar
    leiksins, ónefndir: `commonList`,
    `privateDataList`, `playersPublicInfo` á reikning, ...).

Pakka- og aðferðarnúmer sem eru ólík milli útgáfnanna sem voru athugaðar (pakki
eigin skips er 43 eða 44, sökkvunarkallið 76 eða 83, skeljarnar 101, 102,
126 eða 127) eru öll fundin eftir lögun - sjá
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - svo uppfærsla sem
endurnúmerar tæmir ekki töfluna. Númerin sem fundust eru í `decoded` í
leikjaskjalinu.

**Pickle er ótraust gögn.** Upptaka er skrá hvaðan sem er, og
pickle getur nefnt kóða til að keyra. Það er hlaðið með unpickler sem gefur hverjum
flokki eða falli sem pickle nefnir óvirkan staðgengil, svo það smíðar venjuleg
gögn og ekkert annað. Próf gefur því pickle sem kallar á `os.system`.

**Sökkvanir** hafa nákvæman tíma kallsins. Staður þeirra er þar sem fórnarlambið sást
síðast, þegar það var innan fimm sekúndna. **Upphaf bardagans** er
fyrsta stund sem nokkurt skip hreyfist yfirleitt (skip liggja kyrr í niðurtalningunni).

Allt sem er ekki taflaröð er í [leikjaskjalinu](match-document.md).

**Það sem biðlaranum var sagt** er fullkomið fyrir eigið lið og hlutfallslegt fyrir
óvini: skot þeirra, högg og heilsa eru til staðar meðan þeir eru innan sviðs.

**Ekki lesið:**

- Flugvélar og flugsveitir þeirra (köllin sem bera þær voru ekki
  tekin í sundur), sjónuppfærslur smákortsins (pakkaðar), kortlagning (spotting), borðar (ribbons), eldar og
  flóð sem eigin atburðir (skaði þeirra er í höggunum), birgðir (consumables),
  handtökupunktar og stig liða (eiginleikar eininga án
  skilgreiningar, ekki greindir í sundur eftir lögun), restin af eiginleikum skips
  (miðun, stýri, hraðastilling...).
- Lyklanúmer skráa spilaranna og skaðatölfræðinnar sem nöfn: leikurinn
  númerar þau, og númerin breytast; þau eru geymd sem tölur.
- Aukagögn skeljar þar sem hún hitti (15.x) og bætin á eftir upphafi og hraða skeljar
  eða tundurskeytis.
- Niðurstöður biðlara fyrir 15.x: upptökur þeirra bera engar.
- Skipanúmerið sem nafn: nöfnin eru í eigin breytuskrám leiksins,
  ekki í upptökunni.

## Hvernig lesturinn var athugaður {#how-the-reading-was-checked}

Lesturinn var athugaður á opinberum upptökum biðlara frá 0.9 til 15.x, hvert
gildi gegn einhverju sem upptakan gefur í annað sinn:

- **Stöður:** eining hvers skips passaði við nafn á listanum; stefnur stemma
  við stefnu ferðar innan 0,1 rad; eftir sökkvun hreyfist skip
  minna en 0,1 einingar. Skip sem liggur kyrrt er uppfært sjaldnar.
- **Heilsa:** hvert skip sem sökk innan sjónsviðs biðlarans endar með heilsu 0.
  Um helmingur allra högga passar við fall í heilsu sekúndunni á undan; afgangurinn
  fellur saman við viðgerðir eða önnur högg.
- **Skaði gegn eigin tölfræði leiksins:** á nýjasta biðlaranum er skaði
  upptökumannsins sem er lesinn innan 0,1% frá tölfræðinni. Á eldri
  biðlurum er tölfræðin hærri: biðlaranum eru ekki send öll högg, eða
  tölfræðin telur fleira en högg (óleyst).
- **Skeljar:** skel byrjar nokkrar einingar frá síðustu þekktu stöðu skips síns
  (byssurnar dreifast eftir skrokknum); endir nær hverrar skeljar kemur
  innan mínútu á eftir skoti sem biðlarinn sá.

Prófanirnar smíða upptökur í sama útliti, svo engin raunveruleg upptaka er geymd í
þessari geymslu.

**Ekki athugað:** biðlarar fyrir 0.9.6, Lesta biðlarinn (Mir Korabley),
aðgerðir (operations) og sviðsmyndir umfram eina, ættar- og ranked-bardagar, og
hvaða skipanúmer er hvaða skip.

---

Hluti af [3DHeat](https://github.com/Holdi601/3DHeat) ([skjölun](https://holdi601.github.io/3DHeat/)). Frumkóði: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
