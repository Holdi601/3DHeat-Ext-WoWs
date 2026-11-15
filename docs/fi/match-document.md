---
title: Ottelun asiakirja
nav_order: 6
lang: fi
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Ottelun asiakirja {#the-match-document}

`<match>.match.json` sisältää kaiken, minkä replay kertoo ja joka ei ole taulukon rivi. Katselimen Ottelu-välilehti
lukee sen. (Koodi kutsuu sitä yhteenvedoksi.)

![Synteettisen ottelun asiakirjan alku ja sen avaimet](../assets/img/match-document.svg)

## Taistelu {#the-battle}

| Avain | Mitä se on |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; taistelun tunnus; kartta sellaisena kuin peli sen nimeää (`spaces/<map>`) ja sen näyttönimi |
| `clientVersion`, `streamVersion` | pelin versio otsikosta, ja sellaisena kuin paketti­virta sen kertoo |
| `recorded` | milloin replay tallennettiin, sellaisena kuin peli sen kirjoittaa |
| `player`, `vehicle` | tallentava pelaaja ja hänen aluksensa |
| `gameType`, `scenario` | taistelun tyyppi (`RandomBattle`, ...) ja skenaario, otsikosta |
| `duration` | taistelun aikaraja sekunteina, otsikosta |
| `truncated` | tallennus pysähtyi aikaisin |
| `battleStart`, `recordingSeconds` | taistelun alku (ensimmäinen hetki, jolloin mikään alus liikkuu) ja tallennuksen pituus sekunteina |
| `positionPacket`, `ownPositionPacket` | paketin numerot, joissa sijainnit tulivat: muiden alusten, tallentavan pelaajan |
| `deathMethod` | metodin numero, josta upotukset löydettiin |
| `hz`, `ownHz`, `positions` | muiden alusten ja oman aluksen näytteet sekunnissa; sijaintirivit |
| `units` | maailman yksiköt (15 m aluksen rungon mukaan, 30 m pelin kantamien mukaan); x itään, y ylös, z pohjoiseen |
| `events` | jokaisen tapahtuman taulukkorivien määrä |
| `decoded` | jokaiselle viestityypille löydetyt metodi- ja pakettinumerot |

## Pelaajat ja tapahtumat {#players-and-events}

| Avain | Mitä se on |
|---|---|
| `players` | yksi merkintä alusta kohden: nimi, `ally` tai `enemy`, aluksen numero ja nimi, kokonaisuus, näytteet, tapot, selviytyi; `seen` (vahinko annettu ja saatu, kuoret, torpedot ja viimeisin terveys, jonka asiakas näki); `header` (luettelon merkintä) ja `record` (pelaajan tietue virrasta, avaimen numeron mukaan) |
| `kills` | jokainen upotus: aika, uhri, tappaja, syynumero, paikka |
| `chat` | jokainen chat-rivi kanavan ja lähettäjän kanssa |
| `damageStats` | tallentavan pelaajan omat tilastot, sellaisina kuin peli ne pitää: aseittain ja tyypeittäin, lukumäärä ja summa (tyyppi 0 on aiheutettu vahinko) |
| `avatarPickles` | jokainen pickle-kutsu tallentavalle pelaajalle, dekoodattuna, metodinumeron mukaan |

## Otsikko, tulokset ja tarkistukset {#header-results-and-checks}

| Avain | Mitä se on |
|---|---|
| `header` | ensimmäinen JSON-lohko kokonaisuudessaan paitsi luettelo: pelimuoto, sää, kartan rajat, joukkueiden koot ja muuta |
| `moreBlocks` | JSON-lohkot ensimmäisen jälkeen sellaisinaan |
| `blockIds` | 15.x: tallentavan pelaajan tili ja taistelun tunnus, luettuina tekstinä |
| `results` | 15.x: tulokset, jotka nämä asiakkaat säilyttävät virrassa |
| `entities` | jokainen virran luoma kokonaisuus: sen tyyppinumero ja rooli, milloin se tuli asiakkaan näkyviin ja milloin se poistui |
| `selfCheck` | täydellisyyslaskuri ([Täydellisyys](completeness.md)) ja kokonaisuuksien, tulosten, tunnusten ja version tarkistukset |

---

Osa [3DHeatiä](https://github.com/Holdi601/3DHeat) ([dokumentaatio](https://holdi601.github.io/3DHeat/)). Lähde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
