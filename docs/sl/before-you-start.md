---
title: Preden začnete
nav_order: 2
lang: "sl"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Preden začnete {#before-you-start}

Ste novi v ukazni vrstici? Ta stran vas v približno desetih minutah pripelje od začetka do delujočega
`heat3d-wows-replay`. Če že uporabljate Python, pojdite naravnost na [Namestitev](installing.md).

## 1. Namestite Python {#install-python}

1. Prenesite Python **3.10 ali novejši** s strani
   [python.org/downloads](https://www.python.org/downloads/).
2. V Windows v prvem oknu namestitve obkljukajte **Add python.exe to PATH**, nato kliknite
   **Install Now**.
3. Na macOS in Linux je Python 3 pogosto že nameščen. Tam, kjer te strani pišejo `python`,
   napišite `python3`, namesto `pip` pa `pip3`.

## 2. Odprite ukazno vrstico {#open-a-terminal}

Ukazna vrstica je okno, v katerem vpisujete ukaze.

- **Windows:** v Raziskovalcu odprite mapo, kliknite naslovno vrstico, vpišite `cmd` in
  pritisnite Enter. Odpre se okno, ki je že v tej mapi.
- **macOS:** odprite aplikacijo **Terminal**. **Linux:** z desno tipko kliknite v mapi in
  izberite **Open in Terminal**.

Če želite v drugo mapo, vpišite `cd` in mapo:

```bash
cd "C:\Users\vi\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Preverite, ali Python deluje {#check-that-python-works}

```bash
python --version
```

Videti bi morali `Python 3.` in število 10 ali več, na primer `Python 3.12.4`.

## 4. Pridobite orodje in ga namestite {#get-the-tool-and-install-it}

1. Na [GitHub strani orodja](https://github.com/Holdi601/3DHeat-Ext-WoWs) kliknite zeleni gumb
   **Code**, nato **Download ZIP**, in razpakirajte zip.
2. Odprite ukazno vrstico v razpakirani mapi (tisti, v kateri je `README.md`).
3. Vpišite:

   ```bash
   pip install -e .
   ```

   Na koncu bi morali videti: `Successfully installed heat3d-ext-wows-0.1.0` (morda z več imeni).
4. Preverite:

   ```bash
   heat3d-wows-replay --version
   ```

   Videti bi morali: `heat3d-wows-replay 0.1.0`

## Kako brati ukaze na teh straneh {#how-to-read-the-commands-on-these-pages}

- Besede v oglatih oklepajih, kot je `<replays>`, so mesta za vaše vrednosti: na to mesto vpišite
  svojo datoteko ali mapo, brez oklepajev.
- Pot s presledki potrebuje narekovaje: `"C:\Program Files (x86)\Steam"`.
- Besedilo za `#` je komentar: ga ne vpisujete.
- `-o out` zapiše v mapo `out` znotraj mape, v kateri je vaša ukazna vrstica. Če je ni, se ustvari.

## Kako izgleda uspeh {#what-success-looks-like}

Ukaz izpiše eno vrstico za vsak posnetek, na primer:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

in se konča s končnim stanjem `0`. Nove datoteke so v mapi `out`.

## Pogoste napake {#common-errors}

| Kaj vidite | Kaj storiti |
|---|---|
| `'python' is not recognized ...` ali `command not found` | Python ni v PATH: namestite ga znova z obkljukano možnostjo **Add python.exe to PATH** ali v Windows napišite `py` namesto `python` |
| `'pip' is not recognized ...` | namesto tega vpišite `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | namesto `heat3d-wows-replay` vpišite `python -m heat3d_ext_wows`; naredi isto |
| `No module named heat3d_ext_wows` | niste v mapi orodja ali ni nameščeno: pojdite tja z `cd` in zaženite `pip install -e .` |
| `the following arguments are required: -o/--out` | dodajte `-o out` k ukazu |

Naprej: [Pretvorba posnetkov](converting.md).
