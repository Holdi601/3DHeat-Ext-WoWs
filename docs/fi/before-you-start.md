---
title: Ennen aloittamista
nav_order: 2
lang: "fi"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Ennen aloittamista {#before-you-start}

Uusi komentoriviltä? Tämä sivu vie sinut nollasta toimivaan `heat3d-wows-replay`-komentoon noin
kymmenessä minuutissa. Jos käytät jo Pythonia, siirry suoraan kohtaan [Asennus](installing.md).

## 1. Asenna Python {#install-python}

1. Lataa Python **3.10 tai uudempi** osoitteesta
   [python.org/downloads](https://www.python.org/downloads/).
2. Windowsissa rastita asennusohjelman ensimmäisessä ikkunassa **Add python.exe to PATH**
   ja napsauta **Install Now**.
3. macOS:ssä ja Linuxissa Python 3 on usein jo valmiina. Kirjoita `python3` aina, kun näillä
   sivuilla lukee `python`, ja `pip3` kohtaan `pip`.

## 2. Avaa pääte {#open-a-terminal}

Pääte on ikkuna, johon kirjoitat komentoja.

- **Windows:** avaa kansio Resurssienhallinnassa, napsauta osoiteriviä, kirjoita `cmd` ja paina Enter.
  Ikkuna aukeaa valmiiksi samaan kansioon.
- **macOS:** avaa **Terminal**-sovellus. **Linux:** napsauta kansiossa hiiren oikealla ja valitse
  **Open in Terminal**.

Siirtyäksesi toiseen kansioon kirjoita `cd` ja kansion nimi:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Tarkista, että Python toimii {#check-that-python-works}

```bash
python --version
```

Sinun pitäisi nähdä `Python 3.` ja numero 10 tai suurempi, esimerkiksi `Python 3.12.4`.

## 4. Hae työkalu ja asenna se {#get-the-tool-and-install-it}

1. Avaa [työkalun GitHub-sivu](https://github.com/Holdi601/3DHeat-Ext-WoWs), napsauta vihreää
   **Code**-painiketta ja sitten **Download ZIP**, ja pura zip-tiedosto.
2. Avaa pääte puretussa kansiossa (se, jossa on `README.md`).
3. Kirjoita:

   ```bash
   pip install -e .
   ```

   Lopussa sinun pitäisi nähdä: `Successfully installed heat3d-ext-wows-0.1.0` (ehkä muitakin nimiä).
4. Tarkista asennus:

   ```bash
   heat3d-wows-replay --version
   ```

   Sinun pitäisi nähdä: `heat3d-wows-replay 0.1.0`

## Miten näillä sivuilla olevia komentoja luetaan {#how-to-read-the-commands-on-these-pages}

- Kulmasulkeissa olevat sanat, kuten `<replays>`, ovat paikanpitäjiä: kirjoita tilalle oma tiedostosi
  tai kansiosi ilman kulmasulkeita.
- Polku, jossa on välilyöntejä, tarvitsee lainausmerkit: `"C:\Program Files (x86)\Steam"`.
- Teksti `#`-merkin jälkeen on kommentti: sitä ei kirjoiteta.
- `-o out` kirjoittaa kansioon nimeltä `out` sen kansion sisään, jossa pääte on. Kansio luodaan,
  jos sitä ei ole.

## Miltä onnistuminen näyttää {#what-success-looks-like}

Komento tulostaa yhden rivin replayta kohden, esimerkiksi:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

ja päättyy poistumiskoodiin `0`. Uudet tiedostot ovat kansiossa `out`.

## Yleisiä virheitä {#common-errors}

| Näet | Mitä tehdä |
|---|---|
| `'python' is not recognized ...` tai `command not found` | Python ei ole PATHissa: asenna se uudelleen ja rastita **Add python.exe to PATH**, tai kirjoita `py` komennon `python` sijaan (Windows) |
| `'pip' is not recognized ...` | kirjoita sen sijaan `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | kirjoita `python -m heat3d_ext_wows` komennon `heat3d-wows-replay` sijaan; se tekee saman |
| `No module named heat3d_ext_wows` | et ole työkalun kansiossa tai sitä ei ole asennettu: `cd` kansioon ja aja `pip install -e .` |
| `the following arguments are required: -o/--out` | lisää komentoon `-o out` |

Seuraavaksi: [Replayjen muuntaminen](converting.md).
