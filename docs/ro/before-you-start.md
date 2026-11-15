---
title: Înainte de început
nav_order: 2
lang: ro
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Înainte de început {#before-you-start}

Sunteți nou cu linia de comandă? Această pagină vă duce de la zero la un
`heat3d-wows-replay` funcțional în vreo zece minute. Dacă folosiți deja Python, mergeți direct la
[Instalare](installing.md).

## 1. Instalați Python {#install-python}

1. Descărcați Python **3.10 sau mai nou** de la
   [python.org/downloads](https://www.python.org/downloads/).
2. Pe Windows, bifați **Add python.exe to PATH** în prima fereastră a
   programului de instalare, apoi apăsați **Install Now**.
3. Pe macOS și Linux, Python 3 este adesea deja instalat. Scrieți `python3`
   acolo unde aceste pagini spun `python`, și `pip3` în loc de `pip`.

## 2. Deschideți un terminal {#open-a-terminal}

Un terminal este o fereastră în care scrieți comenzi.

- **Windows:** deschideți folderul în File Explorer, faceți clic pe bara de adrese, scrieți
  `cmd` și apăsați Enter. Se deschide o fereastră, deja în acel folder.
- **macOS:** deschideți aplicația **Terminal**. **Linux:** faceți clic dreapta în folder
  și alegeți **Open in Terminal**.

Ca să mergeți în alt folder, scrieți `cd` și numele folderului:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Verificați dacă Python funcționează {#check-that-python-works}

```bash
python --version
```

Ar trebui să vedeți `Python 3.` și un număr de 10 sau mai mare, de exemplu
`Python 3.12.4`.

## 4. Luați instrumentul și instalați-l {#get-the-tool-and-install-it}

1. Pe [pagina GitHub a instrumentului](https://github.com/Holdi601/3DHeat-Ext-WoWs), faceți clic pe
   butonul verde **Code**, apoi pe **Download ZIP**, și dezarhivați fișierul zip.
2. Deschideți un terminal în folderul dezarhivat (cel care are `README.md` în el).
3. Scrieți:

   ```bash
   pip install -e .
   ```

   La final ar trebui să vedeți: `Successfully installed heat3d-ext-wows-0.1.0`
   (poate cu mai multe nume).
4. Verificați:

   ```bash
   heat3d-wows-replay --version
   ```

   Ar trebui să vedeți: `heat3d-wows-replay 0.1.0`

## Cum se citesc comenzile din aceste pagini {#how-to-read-the-commands-on-these-pages}

- Cuvintele între paranteze unghiulare, precum `<replays>`, sunt locuri de completat: scrieți
  propriul dumneavoastră fișier sau folder acolo, fără paranteze.
- O cale cu spații are nevoie de ghilimele: `"C:\Program Files (x86)\Steam"`.
- Textul după `#` este un comentariu: nu îl scrieți.
- `-o out` scrie într-un folder numit `out`, din folderul în care se află terminalul.
  Se creează dacă nu există.

## Cum arată un rezultat reușit {#what-success-looks-like}

Comanda afișează câte o linie pentru fiecare replay, de exemplu:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

și se termină cu codul de ieșire `0`. Fișierele noi sunt în folderul `out`.

## Erori frecvente {#common-errors}

| Vedeți | Ce să faceți |
|---|---|
| `'python' is not recognized ...` sau `command not found` | Python nu este în PATH: instalați-l din nou cu **Add python.exe to PATH** bifat, sau scrieți `py` în loc de `python` (Windows) |
| `'pip' is not recognized ...` | scrieți în schimb `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | scrieți `python -m heat3d_ext_wows` în loc de `heat3d-wows-replay`; face același lucru |
| `No module named heat3d_ext_wows` | nu sunteți în folderul instrumentului, sau nu este instalat: `cd` acolo și rulați `pip install -e .` |
| `the following arguments are required: -o/--out` | adăugați `-o out` la comandă |

Următorul: [Convertirea replay-urilor](converting.md).
