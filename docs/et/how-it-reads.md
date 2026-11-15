---
title: Kuidas tööriist kordust loeb
nav_order: 7
lang: "et"
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Kuidas tööriist kordust loeb {#how-it-reads-a-replay}

Kordus on JSON-plokkide päis ja mängu paketivoog (formaadi märkused leheküljel
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Esimene plokk, lahtiselt: kaart, kliendi versioon, salvestajamängija ja tema laev ning nimekiri - iga mängija
  nimi, liitlane või vastane, ja laevanumber. Uuemad kliendid (15.x) lisavad veel kaks plokki: tühja ja
  salvestajamängija konto ning lahingu ID tekstina, loetud `blockIds`-i. Tulemused ei ole JSON-is; 15.x hoiab need voos.
- Paketivoog, zlib-pakitud ja Blowfishiga šifreeritud mängu kaasasoleva võtmega, mille on avaldanud kogukonna
  tööriistad, mis neid faile loevad. Dešifreerituna sisaldab see:
  - mootori asukohauuendused igale laevale, mida klient nägi (oma meeskond kogu aeg, vaenlased, kui neid nähti või
    need olid lähedal), mitu korda sekundis, kui nad liiguvad, ja harvemini, kui ei liigu;
  - salvestajamängija oma laev omaette paketis, umbes seitse korda sekundis;
  - algusest üks kord mängijate kirjed pickle'itud Pythoni nimekirjana. Need ütlevad, milline olem voos on milline
    mängija. Nende võtmed on nummerdatud ja numbrid muutuvad paikadega, nii et lugeja leiab võtmed nende väärtuste
    järgi: võtme, mis hoiab nimekirja nimesid, ja võtme, mis hoiab olemeid, millel on asukohauuendusi;
  - serveri kutse, mis ütleb kliendile, et laev on uppunud: ohver, tapja, põhjus. See leitakse selle kuju järgi
    (kaksteist baiti; esimesed kaks on laevaolemid; iga ohver ilmub üks kord), mitte numbri järgi;
  - iga laeva kahju: massiiv (ründaja, kahju) iga tabamuse kohta tabatud laeval; ja tema tervis, omadus, mis
    määratakse hetk varem;
  - iga salve kestadest ja torpeedodest, millest klient teada sai: mürsu tüüp, laskja, salv, ja iga kesta või
    torpeedo algus ja kiirus;
  - kohad, kus mürsud lõppesid: laskja, tabamuse tüüp ja iga koha asukoht (15.x klientidel veel rohkem mürsu kohta,
    kus see tabas, mida jäetakse vahele);
  - vestlus: saatja, kanal, rida;
  - pickle'itud kutsed salvestajamängijale: tema kahjustusstatistika, mängijate kirjete uuendused, lahingu seisund;
  - 15.x klientidel lahingu tulemused lõpus: paketi oma, JSON-objekt lahingu ID-ga, loetud tervena mängu dokumendi
    `results`-i (mängu enda nimekirjad, nimetamata: `commonList`, `privateDataList`, `playersPublicInfo` konto kohta, ...).

Paketi ja meetodi numbrid, mis erinevad kontrollitud versioonides (salvestajamängija laeva pakett on 43 või 44,
uppumise kutse 76 või 83, kestad 101, 102, 126 või 127), leitakse kõik kuju järgi - vt
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) -
nii et ümbernummerdamise paranduse korral ei tühjene tabel. Leitud numbrid on mängu dokumendi `decoded`-is.

**Pickle on usaldamatu andmed.** Kordus on fail kustahes, ja pickle võib nimetada koodi, mida käivitada. Seda
laetakse lugejaga, mis annab iga klassi või funktsiooni, mida pickle nimetab, inertse asendaja, nii et see ehitab
ainult lihtsaid andmeid ja mitte midagi muud. Test annab sellele pickle'i, mis kutsub `os.system`.

**Uppumised** on täpse kutse ajaga. Nende koht on see, kus ohvrit viimati nähti, kui see oli viie sekundi piires.
**Lahingu algus** on esimene hetk, kui mõni laev üldse liigub (laevad seisavad loenduses paigal).

Kõik, mis ei ole tabeli rida, on [mängu dokumendis](match-document.md).

**Mida klient teada sai,** on täielik oma meeskonna jaoks ja osaline vaenlaste jaoks: nende lasud, tabamused ja
tervis on seal, kui nad olid ulatuses.

**Ei loeta:**

- Lennukid ja nende eskadrillid (kutsed, mis neid kannavad, ei olnud lahti võetud), minikaardi nägemise
  uuendused (pakitud), märkamine, autasud, tulekahjud ja üleujutused eraldi sündmustena (nende kahju on tabamustes),
  kulumaterjalid, vallutuspunktid ja meeskonna skoorid (olemite omadused ilma definitsioonita, kuju järgi
  eristamata), laeva ülejäänud omadused (siht, roolid, kiiruse seade...).
- Mängijakirjete ja kahjustusstatistika võtmete numbrid nimedena: mäng nummerdab need, ja numbrid muutuvad; need
  on hoitud numbritena.
- Mürsu lisaandmed kohas, kus see tabas (15.x), ja baidid pärast mürsu või torpeedo algust ja kiirust.
- Enne 15.x klientide tulemused: nende kordustes neid ei ole.
- Laevanumber nimena: nimed on mängu enda parameetrifailides, mitte kordusses.

## Kuidas lugemist kontrolliti {#how-the-reading-was-checked}

Lugemist kontrolliti avalikel kordustel klientidest 0.9 kuni 15.x, iga väärtust võrreldes sellega, mida kordus annab
teist korda:

- **Asukohad:** iga laeva olem sobitus mõne nimekirja nimega; suunad kokkulangevad sõidusuunaga 0,1 radiaani
  täpsusega; pärast uppumist liigub laev vähem kui 0,1 ühikut. Paigal seisev laev uuendatakse harvemini.
- **Tervis:** iga klienti vaatevälja jäänud uppunud laev lõpeb tervisega 0. Umbes pool kõigist tabamustest vastab
  tervise langusele sekundi jooksul enne seda; ülejäänud langevad kokku remondide või muude tabamustega.
- **Kahju mängu enda statistika vastu:** uusimal kliendil on salvestajamängija loetud kahju 0,1% piires statistikast.
  Vanematel klientidel on statistika kõrgem: klient ei saa iga tabamust kätte, või statistika loeb rohkem kui
  tabamusi (ei ole lahendatud).
- **Mürsud:** kest algab mõne ühiku kaugusel laeva viimasest teadaolevast asukohast (relvad on laeva kere peale
  laiali); peaaegu iga kesta lõpp järgneb minuti jooksul lasule, mida klient nägi.

Testid koostavad kordused samale paigutusele, nii et ühtegi päris kordust ei hoita selles hoidlas.

**Ei ole kontrollitud:** kliendid enne 0.9.6, Lesta klient (Mir Korabley), operatsioonid ja stsenaariumid peale ühe,
klaani- ja reitinglahingud ning see, milline laevanumber on milline laev.

---

Osa [3DHeatist](https://github.com/Holdi601/3DHeat) ([dokumentatsioon](https://holdi601.github.io/3DHeat/)). Lähtekood: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
