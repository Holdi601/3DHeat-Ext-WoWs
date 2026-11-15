---
title: "Εγκατάσταση"
nav_order: 3
lang: el
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Εγκατάσταση {#installing}

Αν είστε νέος στη γραμμή εντολών, διαβάστε πρώτα το [Πριν ξεκινήσετε](before-you-start.md).
Χρειάζεται Python 3.10 ή νεότερη· τα numpy και pyarrow εγκαθίστανται μαζί της.

## Βήμα προς βήμα {#step-by-step}

1. Πάρτε τον κώδικα: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   ή κατεβάστε ένα zip από τις [Κυκλοφορίες](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   και αποσυμπιέστε το.
2. Ανοίξτε ένα τερματικό σε αυτόν τον φάκελο και γράψτε `pip install -e .`. Αυτό βάζει την
   εντολή `heat3d-wows-replay` στη διαδρομή σας.
3. Ελέγξτε το: `heat3d-wows-replay --version`. Πρέπει να δείτε
   `heat3d-wows-replay 0.1.0`. Το `heat3d-wows-replay --help` δείχνει τις επιλογές:

![heat3d-wows-replay --help](../assets/img/help.svg)

Χωρίς εγκατάσταση, το `python -m heat3d_ext_wows ...` μέσα στον φάκελο του εργαλείου κάνει
το ίδιο.

Ο 3DHeat Watcher τρέχει αυτή την εντολή σε νέα replays όταν είναι εγκατεστημένος, και
λειτουργεί χωρίς αυτήν.

## Ενημερώσεις {#updates}

Κάθε εκκίνηση ελέγχει πρώτα τις κυκλοφορίες του έργου στο GitHub (το πολύ ένα αίτημα
κάθε μερικές ώρες· ποτέ δεν σταματά μια μετατροπή, online ή offline). Όταν βγει νεότερη
κυκλοφορία, η εντολή ρωτά πριν την εγκαταστήσει: ένα `git clone` ενημερώνεται με
`git pull --ff-only` (αρνείται όσο έχετε τοπικές αλλαγές), ένα κατεβασμένο αντίγραφο
από το αρχείο της κυκλοφορίας. Το `HEAT3D_NO_UPDATE=1` απενεργοποιεί τον έλεγχο και
την ενημέρωση.

---

Μέρος του [3DHeat](https://github.com/Holdi601/3DHeat) ([τεκμηρίωση](https://holdi601.github.io/3DHeat/)). Πηγή: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
