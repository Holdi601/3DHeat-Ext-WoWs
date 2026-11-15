---
title: Täydellisyys
nav_order: 8
lang: "fi"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Täydellisyys {#completeness}

Replayssa ei heitetä mitään pois. Se, minkä muunnin lukee, menee taulukkoon ja ottelun asiakirjaan; jokainen
muu kohta säilytetään kokonaisena sivutiedostossa `<match>.messages.parquet`; ja ottelun asiakirjan
`selfCheck.completeness` laskee, mitä kullekin kohtatyypille tapahtui. Tämä on sääntö, jonka kaikki 3DHeat-muuntimet
jakavat: [Muuntimet säilyttävät kaiken](https://holdi601.github.io/3DHeat/converters.html).

![Synteettisen replayn itsetarkistus: jokainen kohta nähty, luettu, säilytetty tai menetetty](../assets/img/completeness.svg)

## Laskuri {#the-count}

Jokaiselle kohtatyypille `selfCheck.completeness.types` antaa:

| Laskuri | Tarkoittaa |
|---|---|
| `seen` | kuinka monta replay sisältää |
| `decoded` | luettu kokonaisena |
| `partial` | luettu osittain, ja säilytetty kokonaisena sivutiedostossa |
| `raw` | vain säilytetty kokonaisena sivutiedostossa, ei luettu |
| `lost` | menetetty: aina `0` |

Tyypit ovat replayn omia: `block <n>` (JSON-lohkot), säiliön omat tavut, `packet <type>`, ja kokonaisuuksiin
kohdistuville kutsuille `method <entity type>.<number>` ja `property <entity type>.<number>`.
`selfCheck.entities.roles` kertoo, mikä kokonaisuustyyppi on tallentavan pelaajan avatar ja mitkä ovat alukset.
Tyyppi, josta kukaan ei tiennyt, näkyy laskurinsa kanssa.

## Sivutiedosto {#the-sidecar}

| Sarake | Mitä se on |
|---|---|
| `time` | replayn kello, kuten taulukossa |
| `type`, `name` | kohdetyyppi; sen nimi muuntimessa, siellä missä se luetaan |
| `entity` | alus tai avatar, johon se kuuluu, kuten taulukon `entity` |
| `decoded` | siitä luettu, JSON-muodossa |
| `payload`, `text` | sen tavut kokonaisina; JSON-lohkot kokonaisina |
| `entityType`, `packet`, `method` | numerot |

Rivit on lajiteltu paketin, metodin, kokonaisuuden ja ajan mukaan. Se, mikä kokonaisuus on mikäkin pelaaja:
ottelun asiakirjan `entities` ja `players`.

## Mitä luetaan, ja miten se tarkistettiin {#what-is-read-and-how-it-was-checked}

- **Tulokset** (15.x, `results`): niiden taistelutunnus on virran tunnus, ja jokainen niissä oleva pelaaja on otsikon
  luettelossa.
- **Tunnuslohko** (15.x, `blockIds`): tili ja taistelu, luettuina tekstinä, joten yhtäkään numeroa ei menetetä.
- **Kallistus ja roll** jokaisesta sijainnista: roll kulkee kääntymisen nopeuden mukana, kuten alus kallistuu
  käännöksessä; kallistus on lähes aina 0.
- **Kokonaisuudet** (`entities`): milloin kukin tuli asiakkaan näkyviin ja poistui sieltä. Yksikään alus ei ole
  sijainnissa poistumisen ja paluun välillä.
- **Version virrassa** (`streamVersion`): sama kuin otsikon.

Kaikki muu luettu (upotukset, vahinko, terveys, kuoret, torpedot, kuorten päättymispaikat, chat, pickle-muotoiset kutsut,
pelaajien tietueet, sijainnit) on `partial`: taulukossa tai ottelun asiakirjassa, ja säilytettynä kokonaisena
sivutiedostossa.

**Säilytetty mutta ei luettu** (`raw`), suurimmat tyypit: sijaintipäivitykset, joita ei ole taulukossa (upotetun aluksen
jälkeen, kokonaisuudet ilman pelaajaa), usein toistuvat ominaisuudet ja metodit, joilla ei ole lukijaa, kokonaisuuksien
luomisen ominaisuudet sekä jokainen muu paketti, jolla ei ole lukijaa.

## Ei saatavilla {#not-available}

- Mitä palvelin ei koskaan lähettänyt tallentavalle asiakkaalle: muiden pelaajien tähtäys, kamera ja syötteet,
  viholliset, kun niitä ei ole nähty. Replay on se, mitä yksi asiakas sai tietää.
- Kokonaisuustyyppien, metodien, ominaisuuksien ja tilastojen avainten nimet: ne ovat pelin määritystiedostoissa,
  eivät replayssa. Numerot säilytetään.
- Aluksen nimet alusnumeroille (käytä `--ship-names`-valintaa) ja kaikki muu, mikä vaatii pelin omat tiedostot.
- Asiakkaiden 15.x edellisten versioiden tulokset: niitä ei ole niiden replayissa.

---

Osa [3DHeatiä](https://github.com/Holdi601/3DHeat) ([dokumentaatio](https://holdi601.github.io/3DHeat/)). Lähde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
