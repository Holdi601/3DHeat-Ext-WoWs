---
title: "Πριν ξεκινήσετε"
nav_order: 2
lang: el
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Πριν ξεκινήσετε {#before-you-start}

Είστε νέος στη γραμμή εντολών; Αυτή η σελίδα σε πάει από το μηδέν σε ένα
λειτουργικό `heat3d-wows-replay` σε περίπου δέκα λεπτά. Αν ήδη χρησιμοποιείτε Python,
πηγαίνετε κατευθείαν στο [Εγκατάσταση](installing.md).

## 1. Εγκαταστήστε την Python {#install-python}

1. Κατεβάστε την Python **3.10 ή νεότερη** από το
   [python.org/downloads](https://www.python.org/downloads/).
2. Στα Windows, επιλέξτε **Add python.exe to PATH** στο πρώτο παράθυρο του
   εγκαταστάτη, και μετά πατήστε **Install Now**.
3. Σε macOS και Linux, η Python 3 είναι συχνά ήδη εκεί. Γράψτε `python3` όπου
   αυτές οι σελίδες λένε `python`, και `pip3` αντί για `pip`.

## 2. Ανοίξτε ένα τερματικό {#open-a-terminal}

Το τερματικό είναι ένα παράθυρο όπου πληκτρολογείτε εντολές.

- **Windows:** ανοίξτε τον φάκελο στον Εξερευνητή αρχείων, κάντε κλικ στη γραμμή
  διεύθυνσης, γράψτε `cmd` και πατήστε Enter. Ανοίγει ένα παράθυρο, ήδη μέσα σε
  αυτόν τον φάκελο.
- **macOS:** ανοίξτε την εφαρμογή **Terminal**. **Linux:** κάντε δεξί κλικ μέσα
  στον φάκελο και διαλέξτε **Open in Terminal**.

Για να πάτε σε άλλο φάκελο, γράψτε `cd` και τον φάκελο:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Ελέγξτε ότι η Python δουλεύει {#check-that-python-works}

```bash
python --version
```

Πρέπει να δείτε `Python 3.` και έναν αριθμό 10 ή μεγαλύτερο, για παράδειγμα
`Python 3.12.4`.

## 4. Πάρτε το εργαλείο και εγκαταστήστε το {#get-the-tool-and-install-it}

1. Στη [σελίδα GitHub του εργαλείου](https://github.com/Holdi601/3DHeat-Ext-WoWs), πατήστε
   το πράσινο κουμπί **Code**, και μετά **Download ZIP**, και αποσυμπιέστε το zip.
2. Ανοίξτε ένα τερματικό μέσα στον αποσυμπιεσμένο φάκελο (αυτόν με το `README.md`).
3. Γράψτε:

   ```bash
   pip install -e .
   ```

   Στο τέλος πρέπει να δείτε: `Successfully installed heat3d-ext-wows-0.1.0`
   (ίσως με περισσότερα ονόματα).
4. Ελέγξτε το:

   ```bash
   heat3d-wows-replay --version
   ```

   Πρέπει να δείτε: `heat3d-wows-replay 0.1.0`

## Πώς διαβάζονται οι εντολές σε αυτές τις σελίδες {#how-to-read-the-commands-on-these-pages}

- Οι λέξεις μέσα σε γωνιακές αγκύλες, όπως `<replays>`, είναι θέσεις: γράψτε εκεί το
  δικό σας αρχείο ή φάκελο, χωρίς τις αγκύλες.
- Μια διαδρομή με κενά χρειάζεται εισαγωγικά: `"C:\Program Files (x86)\Steam"`.
- Το κείμενο μετά από `#` είναι σχόλιο: δεν το πληκτρολογείτε.
- Το `-o out` γράφει μέσα σε έναν φάκελο που λέγεται `out` και βρίσκεται μέσα στον
  φάκελο όπου είναι το τερματικό σας. Δημιουργείται αν δεν υπάρχει.

## Πώς είναι η επιτυχία {#what-success-looks-like}

Η εντολή τυπώνει μία γραμμή για κάθε replay, για παράδειγμα:

```text
example.wowsreplay: 904 θέσεις από 3 πλοία στα 6,99 Hz, ... -> out/<map>/<match>.parquet
```

και τελειώνει με κωδικό εξόδου `0`. Τα νέα αρχεία είναι στον φάκελο `out`.

## Συνηθισμένα σφάλματα {#common-errors}

| Βλέπετε | Τι να κάνετε |
|---|---|
| `'python' is not recognized ...` ή `command not found` | Η Python δεν είναι στο PATH: εγκαταστήστε την ξανά με το **Add python.exe to PATH** επιλεγμένο, ή γράψτε `py` αντί για `python` (Windows) |
| `'pip' is not recognized ...` | γράψτε `python -m pip install -e .` αντί γι' αυτό |
| `'heat3d-wows-replay' is not recognized ...` | γράψτε `python -m heat3d_ext_wows` αντί για `heat3d-wows-replay`· κάνει το ίδιο |
| `No module named heat3d_ext_wows` | δεν είστε στον φάκελο του εργαλείου, ή δεν είναι εγκατεστημένο: `cd` εκεί και τρέξτε `pip install -e .` |
| `the following arguments are required: -o/--out` | προσθέστε `-o out` στην εντολή |

Επόμενο: [Μετατροπή replay](converting.md).
