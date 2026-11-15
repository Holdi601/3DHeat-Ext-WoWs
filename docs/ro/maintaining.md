---
title: Întreținerea documentației
nav_order: 99
lang: "ro"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Întreținerea documentației {#maintaining-the-documentation}

Pentru cel care lansează o versiune nouă. Faceți pașii în această ordine.

1. **Regenerează paginile de referință** din cod:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # trebuie să se încheie cu codul 0
   ```

   Aceasta rescrie [Referința comenzilor](../cli-reference.md) și
   [Lista coloanelor](../columns.md). Nu editați niciodată cele două manual.
2. **Listează ce s-a schimbat de la ultima versiune:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` este ultima versiune lansată (fără etichetă încă: tot `git log --oneline`). Fiecare funcție, opțiune sau coloană nouă are nevoie de pagina sa
   și de un rând în secțiunea **Docs** din
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Revizuire independentă.** Cineva care nu a scris paginile (o persoană sau un agent) citește README-ul, fiecare pagină și fiecare imagine
   ca trei cititori: un începător care nu a folosit niciodată un terminal, un copil de 8 ani, și un profesionist care verifică fiecare opțiune, coloană și unitate față de cod.
   Ei verifică și diagramele față de cod și că nicio pagină nu numește o hartă, un nivel, un jucător sau un meci reale, nici nu dă cifre din replay-uri reale.
4. **Reparați ce a găsit revizuirea.** Apoi rulați din nou pasul 1 și redesenează
   imaginile ale căror rezultat s-a schimbat.
5. **Traduceri.** Fiecare pagină din `docs/<language>/` înregistrează hash-ul paginii engleze din care a fost tradusă. Retraduce fiecare pagină a cărei sursă engleză s-a schimbat, inclusiv etichetele diagramelor. Apoi revizuiește fiecare limbă: clară pentru toți cei trei cititori, etichetele corecte și aceleași cuvinte pe care le folosiți vizualizatorul 3DHeat în acea limbă.
6. **Lansare:** ridicați `VERSION` și puneți eticheta `v<VERSION>`. **Trimiteți doar după acordul proprietarului.**

## Traduceri: comenzile {#translations-the-commands}

Site-ul este tradus în cele 40 de limbi ale vizualizatorului 3DHeat: engleza în `docs/`, fiecare altă limbă în `docs/<lang>/` cu aceleași nume de fișiere. `tools/docs_i18n.py` ține evidența:

```bash
python tools/docs_i18n.py hashes             # după orice schimbare în engleză: înregistrează hash-ul fiecărei pagini
python tools/docs_i18n.py svg-strings        # după orice schimbare de imagine: etichetele de tradus
python tools/docs_i18n.py status             # pe limbă: pagini actuale, învechite, lipsă
python tools/docs_i18n.py todo --lang de     # paginile în germană de (re)tradus
python tools/docs_i18n.py svg-build --lang de    # imaginile în germană din docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # marchează paginile în germană cu hash-ul lor englez
python tools/docs_i18n.py check              # iese cu 1 când hash-urile sau etichetele sunt vechi
```

Traduceți doar ce listează `todo`: păstrează Markdown-ul, linkurile, codul, numele fișierelor și al coloanelor așa cum sunt, traduceți titlurile și descrierile imaginilor, și folosiți cuvintele proprii ale vizualizatorului 3DHeat pentru butoanele și panourile sale
(`src/i18n/locales/<lang>/`). Paginile de referință generate și imaginile din terminal rămân în engleză. Pe site, o traducere învechită o spune și leagă pagina engleză; una lipsă revine la engleză. Meniul de limbă din antet și redirecționarea paginii principale după limba browserului vin din `docs/_includes/`.
