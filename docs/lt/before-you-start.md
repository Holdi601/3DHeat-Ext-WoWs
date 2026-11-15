---
title: Prieš pradedant
nav_order: 2
lang: lt
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Prieš pradedant {#before-you-start}

Nesate dirbę su komandine eilute? Šis puslapis nuves jus nuo nieko iki veikiančio
`heat3d-wows-replay` per maždaug dešimt minučių. Jei jau naudojate Python, eikite tiesiai į
[Diegimą](installing.md).

## 1. Įdiekite Python {#install-python}

1. Atsisiųskite Python **3.10 ar naujesnę versiją** iš
   [python.org/downloads](https://www.python.org/downloads/).
2. Windows sistemoje pirmame diegimo lange pažymėkite **Add python.exe to PATH**, tada spauskite
   **Install Now**.
3. macOS ir Linux sistemose Python 3 dažnai jau įdiegtas. Ten, kur šiame puslapyje rašoma
   `python`, rašykite `python3`, o vietoj `pip` - `pip3`.

## 2. Atidarykite terminalą {#open-a-terminal}

Terminalas - tai langas, kuriame rašote komandas.

- **Windows:** atidarykite aplanką Failų naršyklėje, spustelėkite adreso juostą, įrašykite
  `cmd` ir paspauskite Enter. Atsidarys langas, jau aplanke, kuriame esate.
- **macOS:** atidarykite programą **Terminal**. **Linux:** dešiniuoju pelės klavišu spustelėkite
  aplanke ir pasirinkite **Open in Terminal**.

Norėdami pereiti į kitą aplanką, įrašykite `cd` ir aplanko vardą:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Patikrinkite, ar Python veikia {#check-that-python-works}

```bash
python --version
```

Turėtumėte matyti `Python 3.` ir skaičių 10 ar didesnį, pavyzdžiui
`Python 3.12.4`.

## 4. Įsidiekite ir įdiekite įrankį {#get-the-tool-and-install-it}

1. Ant [įrankio GitHub puslapio](https://github.com/Holdi601/3DHeat-Ext-WoWs) spustelėkite
   žalią mygtuką **Code**, tada **Download ZIP**, ir išskleiskite zip failą.
2. Terminale atidarykite išskleistą aplanką (tą, kuriame yra `README.md`).
3. Įrašykite:

   ```bash
   pip install -e .
   ```

   Pabaigoje turėtumėte matyti: `Successfully installed heat3d-ext-wows-0.1.0`
   (gali būti ir daugiau pavadinimų).
4. Patikrinkite:

   ```bash
   heat3d-wows-replay --version
   ```

   Turėtumėte matyti: `heat3d-wows-replay 0.1.0`

## Kaip skaityti komandas šiuose puslapiuose {#how-to-read-the-commands-on-these-pages}

- Žodžiai kampiniuose skliaustuose, pavyzdžiui `<replays>`, yra vietos žymės: vietoj jų įrašykite
  savo failo ar aplanko vardą, be skliaustų.
- Kelią su tarpais reikia rašyti kabutėse: `"C:\Program Files (x86)\Steam"`.
- Tekstas po `#` yra komentaras: jo rašyti nereikia.
- `-o out` įrašo į aplanką, vadinamą `out`, esantį tame aplanke, kuriame yra jūsų terminalas.
  Jei jo nėra, jis sukuriamas.

## Kaip atrodo sėkmė {#what-success-looks-like}

Komanda išveda po vieną eilutę kiekvienam įrašui, pavyzdžiui:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

ir baigiasi išėjimo statusu `0`. Nauji failai yra aplanke `out`.

## Dažniausios klaidos {#common-errors}

| Ką matote | Ką daryti |
|---|---|
| `'python' is not recognized ...` arba `command not found` | Python nėra PATH kelyje: įdiekite jį iš naujo, pažymėdami **Add python.exe to PATH**, arba vietoj `python` rašykite `py` (Windows) |
| `'pip' is not recognized ...` | vietoj to rašykite `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | vietoj `heat3d-wows-replay` rašykite `python -m heat3d_ext_wows` - jis daro tą patį |
| `No module named heat3d_ext_wows` | jūs nesate įrankio aplanke arba jis neįdiegtas: `cd` į jį ir paleiskite `pip install -e .` |
| `the following arguments are required: -o/--out` | pridėkite prie komandos `-o out` |

Toliau: [Įrašų konvertavimas](converting.md).
