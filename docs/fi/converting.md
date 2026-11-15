---
title: Replayjen muuntaminen
nav_order: 4
lang: fi
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Replayjen muuntaminen {#converting-replays}

## Vaihe vaiheelta {#step-by-step}

1. **Kytke tallennus päälle:** `isReplayEnabled` pelin `preferences.xml`-tiedostossa, tai pelin oma asetus,
   jos sellainen on. Siitä lähtien peli tallentaa jokaisen taistelun World of Warships -asennuksesi
   `replays`-kansioon, esimerkiksi `C:\Games\World_of_Warships_EU\replays`.
2. **Avaa pääte** kansioon, johon tulokset saa kirjoittaa ([Ennen aloittamista](before-you-start.md)).
3. **Aja muunnin** replay-tiedostoille tai niitä sisältäville kansioille:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` luodaan kansioon, jossa pääte on.
4. **Lue, mitä se sanoo.** Näet yhden rivin replayta kohden, ja se päättyy taulukkoon, jonka se kirjoitti.
5. **Avaa tulos** 3DHeat-katselimessa: `out/<map>/<match>.parquet` Lämpökartta-välilehdellä,
   `<match>.match.json` Ottelu-välilehdellä. Tai lue ne millä tahansa Parquet- tai JSON-lukijalla.

![Ajo synteettisellä replaylla: muunnos, uudelleenajo, rikkinäinen tiedosto, tyhjä kansio](../assets/img/convert.svg)

Kuva on ajo replaylla, jonka testit rakentavat koodissa (ei oikeaa replayta):

- replay muunnettu: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- ajettu uudelleen, jo kirjoitettu ottelu ohitetaan: `<file>: already written, <table>`;
- tiedosto, joka ei ole replay: `<file>: not converted: <why>` (virhetulosteessa; poistumiskoodi 1, muut replayt muunnetaan silti);
- replayta ei löydy: `no .wowsreplay files in <folders>` (poistumiskoodi 2).

## Valinnat {#options}

| Valinta | Oletus | Tekee |
|---|---|---|
| `replays` (yksi tai useampi) | - | `.wowsreplay`-tiedostoja tai kansioita, joista niitä etsitään (myös alikansioista) |
| `-o`, `--out` | pakollinen | kansio, johon kirjoitetaan: kansio kartaa kohden sen sisällä |
| `--force` | pois | muunna uudelleen se, mikä on jo kirjoitettu |
| `--ship-names JSON` | - | JSON-tiedosto `{"<shipId>": "<name>", ...}`: replayt nimeävät vain tallentavan pelaajan aluksen, muut numeron mukaan |
| `--version` | - | tulosta `heat3d-wows-replay <version>` ja lopeta |
| `-h`, `--help` | - | tulosta valinnat ja lopeta |

Valinnat sellaisina kuin ohjelma ne tulostaa: [Komentoviite](../cli-reference.md).

## Mitä kirjoitetaan {#what-is-written}

Vain erillisiä tiedostoja: tämä muunnin ei kirjoita `.3dheat`-tiedostoa (katselin voi pakata ne yhteen:
[Yksi tiedosto ottelua kohden](https://holdi601.github.io/3DHeat/container.html)). Jokaisesta replayta
kohden kansioon `out/<map>/` (kartan nimi ilman `spaces/`-osaa):

| Tiedosto | Mitä se on |
|---|---|
| `<match>.parquet` | taulukko: jokaisen aluksen sijainti ajan yli ja jokainen tapahtuma siinä, missä se tapahtui ([Taulukko](table.md)) |
| `<match>.match.json` | ottelun asiakirja: kartta, asiakasversio, pelaajat, upotukset, chat ja kaikki muu ([Ottelun asiakirja](match-document.md)) |
| `<match>.messages.parquet` | sivutiedosto: jokainen replayn kohta, jota kaksi yllä olevaa tiedostoa eivät säilytä kokonaisena ([Täydellisyys](completeness.md)) |

`<match>` on taistelun oma tunnus, tai tiedoston nimi, jos tallennus päättyi ennen tuloksia.

## Poistumiskoodi {#exit-status}

`0`, kun jokainen replay muunnettiin tai ohitettiin; `1`, kun jokin epäonnistui (muut muunnetaan
silti); `2`, kun replay-tiedostoa ei löytynyt.

---

Osa [3DHeatiä](https://github.com/Holdi601/3DHeat) ([dokumentaatio](https://holdi601.github.io/3DHeat/)). Lähde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
