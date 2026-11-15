---
title: Pirms sākat
nav_order: 2
lang: lv
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Pirms sākat {#before-you-start}

Jauns komandrindā? Šī lappuse ved no nulles līdz darbojošamies `heat3d-wows-replay` apmēram desmit minūtēs. Ja jau lieto Python, dodies tieši uz [Uzstādīšana](installing.md).

## 1. Uzstādi Python {#install-python}

1. Lejupielādē Python **3.10 vai jaunāku** no [python.org/downloads](https://www.python.org/downloads/).
2. Windows sistēmā atzīmē **Add python.exe to PATH** instalētāja pirmajā logā un tad noklikšķini **Install Now**.
3. macOS un Linux sistēmā Python 3 bieži jau ir. Kur šīs lappuses raksta `python`, raksti `python3`, un `pip` vietā raksti `pip3`.

## 2. Atver termināli {#open-a-terminal}

Termināls ir logs, kurā raksti komandas.

- **Windows:** atver mapi File Explorer, noklikšķini adreses joslā, ieraksti `cmd` un nospied Enter. Atveras logs, jau šajā mapē.
- **macOS:** atver lietotni **Terminal**. **Linux:** ar peles labo pogu klikšķini mapē un izvēlies **Open in Terminal**.

Lai pārietu uz citu mapi, ieraksti `cd` un mapes nosaukumu:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Pārbaudi, vai Python darbojas {#check-that-python-works}

```bash
python --version
```

Jābūt redzamam `Python 3.` un skaitlim 10 vai lielākam, piemēram `Python 3.12.4`.

## 4. Iegūsti rīku un uzstādi to {#get-the-tool-and-install-it}

1. Rīka GitHub lapā ([rīka GitHub lapa](https://github.com/Holdi601/3DHeat-Ext-WoWs)) noklikšķini zaļo pogu **Code**, tad **Download ZIP**, un izpako zip failu.
2. Atver termināli izpakotajā mapē (tajā, kurā ir `README.md`).
3. Ieraksti:

   ```bash
   pip install -e .
   ```

   Beigās vajadzētu redzēt: `Successfully installed heat3d-ext-wows-0.1.0` (varbūt ar vēl dažiem nosaukumiem).
4. Pārbaudi:

   ```bash
   heat3d-wows-replay --version
   ```

   Vajadzētu redzēt: `heat3d-wows-replay 0.1.0`

## Kā lasīt šajās lappusēs esošās komandas {#how-to-read-the-commands-on-these-pages}

- Vārdi leņķa iekavās, piemēram `<replays>`, ir vietturi: ieraksti savu failu vai mapi tur, bez iekavām.
- Ceļš ar atstarpēm prasa pēdiņas: `"C:\Program Files (x86)\Steam"`.
- Teksts aiz `#` ir komentārs: to neraksti.
- `-o out` raksta mapē `out`, kas atrodas mapē, kurā ir tavs termināls. Ja tās nav, tā tiek izveidota.

## Kā izskatās veiksme {#what-success-looks-like}

Komanda izdrukā vienu rindu katram atkārtojumam, piemēram:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

un beidzas ar izejas statusu `0`. Jaunie faili ir mapē `out`.

## Biežākās kļūdas {#common-errors}

| Ko redzi | Ko darīt |
|---|---|
| `'python' is not recognized ...` vai `command not found` | Python nav PATH: uzstādi to vēlreiz, atzīmējot **Add python.exe to PATH**, vai raksti `py` `python` vietā (Windows) |
| `'pip' is not recognized ...` | raksti `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | raksti `python -m heat3d_ext_wows` `heat3d-wows-replay` vietā; tas dara to pašu |
| `No module named heat3d_ext_wows` | tu neesi rīka mapē vai tas nav uzstādīts: `cd` uz to un palaid `pip install -e .` |
| `the following arguments are required: -o/--out` | pievieno komandai `-o out` |

Tālāk: [Atkārtojumu pārvēršana](converting.md).
