---
title: "Prima di iniziare"
nav_order: 2
lang: "it"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Prima di iniziare {#before-you-start}

Non hai mai usato la riga di comando? Questa pagina ti porta da zero a un
`heat3d-wows-replay` funzionante in circa dieci minuti. Se usi già Python, vai direttamente a
[Installazione](installing.md).

## 1. Installa Python {#install-python}

1. Scarica Python **3.10 o successivo** da
   [python.org/downloads](https://www.python.org/downloads/).
2. Su Windows, metti la spunta su **Add python.exe to PATH** nella prima finestra del
   programma di installazione, poi clicca **Install Now**.
3. Su macOS e Linux, Python 3 è spesso già presente. Scrivi `python3`
   dove queste pagine dicono `python`, e `pip3` al posto di `pip`.

## 2. Apri un terminale {#open-a-terminal}

Un terminale è una finestra in cui scrivi i comandi.

- **Windows:** apri la cartella in Esplora file, clicca sulla barra degli indirizzi, scrivi
  `cmd` e premi Invio. Si apre una finestra, già in quella cartella.
- **macOS:** apri l'app **Terminale**. **Linux:** clic destro nella cartella
  e scegli **Apri nel terminale**.

Per andare in un'altra cartella, scrivi `cd` e la cartella:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Verifica che Python funzioni {#check-that-python-works}

```bash
python --version
```

Dovresti vedere `Python 3.` e un numero 10 o superiore, per esempio
`Python 3.12.4`.

## 4. Scarica lo strumento e installalo {#get-the-tool-and-install-it}

1. Sulla [pagina GitHub dello strumento](https://github.com/Holdi601/3DHeat-Ext-WoWs), clicca il
   pulsante verde **Code**, poi **Download ZIP**, e decomprimi lo zip.
2. Apri un terminale nella cartella decompressa (quella con dentro `README.md`).
3. Scrivi:

   ```bash
   pip install -e .
   ```

   Alla fine dovresti vedere: `Successfully installed heat3d-ext-wows-0.1.0`
   (magari con altri nomi).
4. Verificalo:

   ```bash
   heat3d-wows-replay --version
   ```

   Dovresti vedere: `heat3d-wows-replay 0.1.0`

## Come leggere i comandi di queste pagine {#how-to-read-the-commands-on-these-pages}

- Le parole tra parentesi angolari, come `<replays>`, sono segnaposto: scrivi lì il tuo
  file o la tua cartella, senza le parentesi.
- Un percorso con spazi richiede le virgolette: `"C:\Program Files (x86)\Steam"`.
- Il testo dopo `#` è un commento: non lo scrivi.
- `-o out` scrive in una cartella chiamata `out` dentro la cartella in cui si trova il terminale.
  Viene creata se non c'è.

## Come si presenta il successo {#what-success-looks-like}

Il comando stampa una riga per replay, per esempio:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

e termina con stato di uscita `0`. I nuovi file sono nella cartella `out`.

## Errori comuni {#common-errors}

| Vedi | Cosa fare |
|---|---|
| `'python' is not recognized ...` o `command not found` | Python non è nel PATH: installalo di nuovo con **Add python.exe to PATH** spuntato, oppure scrivi `py` al posto di `python` (Windows) |
| `'pip' is not recognized ...` | scrivi invece `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | scrivi `python -m heat3d_ext_wows` al posto di `heat3d-wows-replay`; fa la stessa cosa |
| `No module named heat3d_ext_wows` | non sei nella cartella dello strumento, oppure non è installato: `cd` lì ed esegui `pip install -e .` |
| `the following arguments are required: -o/--out` | aggiungi `-o out` al comando |

Avanti: [Conversione dei replay](converting.md).
