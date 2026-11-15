---
title: Miten replay luetaan
nav_order: 7
lang: "fi"
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Miten replay luetaan {#how-it-reads-a-replay}

Replay on JSON-lohkojen otsikko ja pelin pakettivirta (formaattihuomiot:
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Ensimmäinen lohko selkokielisenä: kartta, asiakasversio, tallentava pelaaja ja alus, sekä luettelo: jokaisen
  pelaajan nimi, liittolainen tai vihollinen, ja aluksen numero. Uudemmat asiakkaat (15.x) lisäävät kaksi lohkoa:
  tyhjän, ja tallentavan pelaajan tilin sekä taistelun tunnuksen tekstinä, luettuna kenttään `blockIds`. Tulokset
  eivät ole JSON:ssa; 15.x säilyttää ne virrassa.
- Pakettivirta, zlib-pakattuna ja Blowfish-salattuna pelin mukana tulevalla avaimella, jonka replayt lukevat
  yhteisön työkalut ovat julkaisseet. Purettuna se sisältää:
  - moottorin sijaintipäivitykset jokaiselle aluksella, jonka asiakas näki (oma joukkue koko ajan, viholliset kun
    ne oli havaittu tai olivat lähellä), useita kertoja sekunnissa liikkuessa ja harvemmin, kun ne eivät liiku;
  - tallentavan pelaajan oman aluksen omassa paketissaan, noin seitsemän kertaa sekunnissa;
  - kerran alussa pelaajien tietueet pickle-muotoisena Python-listana. Ne kertovat, mikä virran kokonaisuus on mikäkin
    pelaaja. Niiden avaimet on numeroitu, ja numerot muuttuvat päivitysten mukana, joten lukija löytää avaimet niiden
    arvoista: avaimen, joka pitää luettelon nimet, ja avaimen, joka pitää kokonaisuudet, joilla on sijaintipäivityksiä;
  - palvelimen kutsun, joka kertoo asiakkaalle, että alus on upotettu: uhri, tappaja, syy. Se löydetään muodostaan
    (kaksitoista tavua; kaksi ensimmäistä ovat alus-kokonaisuuksia; jokainen uhri esiintyy kerran), ei numerostaan;
  - jokaisen aluksen vahingon: osumaa kohden taulukon (hyökkääjä, vahinko) kyseisellä osuman kohteena olevalla
    aluksella; ja sen terveyden, ominaisuuden, joka asetettiin hetkeä aiemmin;
  - jokaisen kuorisalvon ja torpedosalvon, josta asiakasta tiedotettiin: kuoren tyypin, ampujan, salvon sekä jokaisen
    kuoren tai torpedon lähtöpisteen ja nopeuden;
  - paikat, joihin kuoret päättyivät: ampujan, osumatyypin ja kunkin paikan (15.x-asiakkailla enemmän kuoresta siinä,
    missä se osui; tämä ohitetaan);
  - chatin: lähettäjä, kanava, rivi;
  - pickle-kutsut tallentavalle pelaajalle: hänen vahinkotilastonsa, pelaajien tietueiden päivitykset, taistelun tila;
  - 15.x-asiakkailla taistelun tulokset lopussa: oma paketti, JSON-olio, jossa on taistelun tunnus, luettuna kokonaisena
    ottelun asiakirjan kohtaan `results` (pelin omat luettelot ilman nimiä: `commonList`, `privateDataList`,
    `playersPublicInfo` tilikohtaisesti, ...).

Paketti- ja metodinumerot, jotka poikkeavat tarkistettujen versioiden välillä (oman aluksen paketti on 43 tai 44,
upotuskutsu 76 tai 83, kuoret 101, 102, 126 tai 127), löydetään kaikki muodon perusteella; katso
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py). Näin
uudelleennumeroiva päivitys ei tyhjennä taulukkoa. Löydetyt numerot ovat ottelun asiakirjan kohdassa `decoded`.

**Pickle on luotettamatonta dataa.** Replay on tiedosto mistä tahansa, ja pickle voi nimetä koodin, joka ajetaan.
Se ladataan purkajalla, joka antaa jokaiselle luokalle tai funktiolle, jonka pickle nimeää, toimettoman korvikkeen,
joten se rakentaa vain tavallista dataa eikä muuta. Testi syöttää sille pickle-tiedoston, joka kutsuu `os.system`-funktiota.

**Upotukset** saavat kutsun tarkan ajan. Niiden paikka on se, missä uhri nähtiin viimeksi, kun se oli viisi sekuntia
tai vähemmän sitten. **Taistelun alku** on ensimmäinen hetki, jolloin mikään alus liikkuu lainkaan (alukset ovat
paikallaan laskennassa).

Kaikki, mikä ei ole taulukon rivi, on [ottelun asiakirjassa](match-document.md).

**Mitä asiakas sai tietää**, on täydellistä oman joukkueensa osalta ja osittaista vihollisten osalta: niiden laukaukset,
osumat ja terveys ovat mukana, kun ne olivat kantaman sisällä.

**Ei luettu:**

- Lentokoneet ja niiden lentueet (kutsuja, jotka kantavat niitä, ei ole purettu), minikartan näkyvyyspäivitykset
  (pakattuja), havaitseminen, palkinnot, tulipalot ja tulvat omina tapahtumina (niiden vahinko on osumissa), kulutustavarat,
  valloituspisteet ja joukkuepisteet (ominaisuuksia kokonaisuuksista, joilla ei ole määritystä, eikä niitä erotettu
  muodon perusteella), alusten muut ominaisuudet (tähtäys, peräsin, nopeusasetus ...).
- Pelaajatietueiden ja vahinkotilastojen avainnumerot nimineen: peli numeroi ne, ja numerot muuttuvat; ne säilytetään numeroina.
- Kuoren lisätiedot siinä, missä se osui (15.x), ja tavut kuoren tai torpedon lähdön ja nopeuden jälkeen.
- Asiakkaiden 15.x edelliset versiot: niiden replayt eivät sisällä tuloksia.
- Aluksen numero nimenä: nimet ovat pelin omissa parametritiedostoissa, eivät replayssa.

## Miten lukeminen tarkistettiin {#how-the-reading-was-checked}

Lukeminen tarkistettiin julkisilla replayilla asiakasversioista 0.9 - 15.x, jokainen arvo vertaamalla johonkin,
minkä replay antaa toisen kerran:

- **Sijainnit:** jokaisen aluksen entiteetti vastasi luettelon nimeä; suunnat vastaavat liikkeen suuntaa 0,1 radiaanin
  tarkkuudella; upotuksen jälkeen alus liikkuu alle 0,1 yksikköä. Paikallaan makaava alus päivittyy harvemmin.
- **Terveys:** jokainen asiakkaan näkemä upotettu alus päättyy terveyteen 0. Noin puolet kaikista osumista vastaa
  terveyden laskua sekuntia aiemmin; loput laskevat yhdessä korjausten tai muiden osumien kanssa.
- **Vahinko pelin omia tilastoja vastaan:** uusimmalla asiakkaalla tallentavan pelaajan luettu vahinko on 0,1 %:n
  sisällä tilastoista. Vanhemmilla asiakkailla tilastot ovat korkeampia: asiakkaalle ei lähetetä jokaista osumaa, tai
  tilastot laskevat enemmän kuin osumia (ei ratkaistu).
- **Kuoret:** kuori alkaa muutaman yksikön päästä aluksen viimeksi tunnetusta paikasta (tykit ovat hajallaan rungolla);
  lähes jokaisen kuoren päättyminen seuraa minuutin sisällä laukausta, jonka asiakas näki.

Testit rakentavat replayt samaan asetteluun, joten tässä tietovarastossa ei ole yhtään oikeaa replayta.

**Ei tarkistettu:** asiakasversiot ennen 0.9.6, Lestan asiakas (Mir Korabley), operaatiot ja skenaariot, joita on useampi kuin yksi,
klaani- ja sijoitustaistelut sekä se, mikä alusnumero on mikäkin alus.

---

Osa [3DHeatiä](https://github.com/Holdi601/3DHeat) ([dokumentaatio](https://holdi601.github.io/3DHeat/)). Lähde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
