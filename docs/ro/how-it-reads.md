---
title: Cum citește un replay
nav_order: 7
lang: ro
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Cum citește un replay {#how-it-reads-a-replay}

Un replay este un antet de blocuri JSON și fluxul de pachete al jocului (note de format
în [`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Primul bloc, în clar: harta, versiunea clientului, jucătorul care înregistrează și nava sa, și lista - numele fiecărui jucător, aliat sau inamic, și numărul navei. Clienții mai noi (15.x) adaugă două blocuri: unul gol, și contul jucătorului care înregistrează și id-ul bătăliei ca text, citite în `blockIds`. Rezultatele nu sunt în JSON; 15.x le păstrează în flux.
- Fluxul de pachete, comprimat zlib și criptat Blowfish cu o cheie pe care o poartă jocul, pe care instrumentele comunității care citesc aceste fișiere au publicat-o. Descifrat, conține:
  - actualizările de poziție ale motorului pentru fiecare navă pe care clientul o putea vedea (echipa sa tot timpul, inamicii cât timp sunt observați sau în apropiere), de mai multe ori pe secundă cât timp se mișcă și mai rar când nu se mișcă;
  - nava proprie a jucătorului care înregistrează, într-un pachet al ei, de aproximativ șapte ori pe secundă;
  - o singură dată, la început, înregistrările jucătorilor ca o listă Python pickle. Acestea spun ce entitate din flux este ce jucător. Cheile lor sunt numerotate, iar numerele se schimbă odată cu patch-urile, deci cititorul găsește cheile după valorile lor: cheia care ține numele din listă, și cheia care ține entitățile cu actualizări de poziție;
  - apelul serverului care îi spune clientului că o navă s-a scufundat: victima, ucigașul, cauza. Este găsit după forma sa (doisprezece octeți; primii doi sunt entități de navă; fiecare victimă apare o dată), nu după numărul său;
  - daunele fiecărei nave: un șir de (atacator, daune) pentru fiecare lovitură, pe nava lovită; și viața sa, o setare de proprietate cu un moment înainte;
  - fiecare salvă de obuze și de torpile despre care i s-a spus clientului: tipul obuzului, trăgătorul, salva, și începutul și viteza fiecărui obuz sau torpile;
  - unde s-au oprit obuzele: trăgătorul, un tip de lovitură, și locul fiecăruia (la clienții 15.x cu mai multe despre obuz acolo unde a lovit, ceea ce se sare);
  - chatul: expeditorul, canalul, linia;
  - apelurile pickle către jucătorul care înregistrează: statisticile sale de daune, actualizările înregistrărilor jucătorilor, starea bătăliei;
  - la clienții 15.x, rezultatele bătăliei la sfârșit: un pachet al său, un obiect JSON cu id-ul bătăliei, citit întreg în `results` din documentul meciului (listele jocului, nenumite: `commonList`, `privateDataList`, `playersPublicInfo` pe cont, ...).

Numerele pachetelor și ale metodelor care diferă între versiunile verificate (pachetul navei proprii este 43 sau 44, apelul de scufundare 76 sau 83, obuzele 101, 102, 126 sau 127) sunt toate găsite după formă - vedeți [`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - deci un patch care le renumerotează nu golește tabelul. Numerele găsite sunt în `decoded` din documentul meciului.

**Pickle-ul nu este sigur.** Un replay poate fi un fișier de oriunde, iar un pickle poate numi cod de rulat. Este încărcat cu un unpickler care dă fiecărei clase sau funcții pe care o numește pickle-ul un substitut inert, deci construiește date simple și nimic altceva. Un test îi dă un pickle care apelează `os.system`.

**Scufundările** au ora exactă a apelului. Locul lor este unde a fost văzută ultima oară victima, când aceasta era în cinci secunde. **Începutul bătăliei** este primul moment în care se mișcă vreo navă (navele stau nemișcate în numărătoarea inversă).

Tot ce nu este un rând de tabel este în [documentul meciului](match-document.md).

**Ce i s-a spus clientului** este complet pentru echipa sa și parțial pentru inamici: loviturile, lovitările și viața lor sunt acolo cât timp sunt în rază.

**Nu se citesc:**

- Avioanele și escadrilele lor (apelurile care le transportă nu au fost descompuse), actualizările de viziune ale hărții minime (împachetate), observarea, panglicile, incendiile și inundațiile ca evenimente proprii (daunele lor sunt în lovituri), consumabilele, punctele de capturare și scorurile echipelor (proprietăți ale entităților fără definiție, nedeosebite după formă), restul proprietăților unei nave (ținta, cârma, setarea vitezei...).
- Numerele cheilor înregistrărilor jucătorilor și ale statisticilor de daune ca nume: jocul le numerotează, iar numerele se schimbă; sunt păstrate ca numere.
- Datele suplimentare ale unui obuz acolo unde a lovit (15.x) și octeții de după începutul și viteza unui obuz sau a unei torpile.
- Rezultatele clienților dinaintea versiunii 15.x: replay-urile lor nu au niciunul.
- Numărul navei ca nume: numele sunt în fișierele de parametri ai jocului, nu în replay.

## Cum a fost verificată citirea {#how-the-reading-was-checked}

Citirea a fost verificată pe replay-uri publice ale clienților de la 0.9 la 15.x, fiecare valoare
față de ceva ce replay-ul dă a doua oară:

- **Pozițiile:** entitatea fiecărei nave a corespuns unui nume din listă; cursurile concordă cu direcția de deplasare în limita a 0,1 rad; după scufundarea sa, o navă se mișcă mai puțin de 0,1 unități. O navă nemișcată este actualizată mai rar.
- **Viața:** fiecare navă scufundată în vederea clientului se termină cu viața 0. Aproximativ jumătate din toate loviturile corespund unei scăderi de viață în secunda dinainte; restul cad împreună cu reparațiile sau alte lovituri.
- **Daunele față de statisticile proprii ale jocului:** pe cel mai nou client, daunele citite ale jucătorului care înregistrează sunt în limita a 0,1% din statistici. Pe clienții mai vechi statisticile sunt mai mari: clientul nu primește fiecare lovitură, sau statisticile numără mai mult decât loviturile (nerezolvat).
- **Obuzele:** un obuz începe la câteva unități de ultima poziție cunoscută a navei sale (tunurile sunt împrăștiate de-a lungul corpului); aproape sfârșitul fiecărui obuz urmează, în un minut, un foc pe care clientul l-a văzut.

Testele construiesc replay-uri în același aranjament, deci niciun replay real nu este păstrat în
acest depozit.

**Nu s-a verificat:** clienții dinaintea versiunii 0.9.6, clientul Lesta (Mir Korabley),
operațiunile și scenariile dincolo de unul, bătăliile de clan și cele clasate, și
ce număr de navă este ce navă.

---

Parte din [3DHeat](https://github.com/Holdi601/3DHeat) ([documentație](https://holdi601.github.io/3DHeat/)). Sursă: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
