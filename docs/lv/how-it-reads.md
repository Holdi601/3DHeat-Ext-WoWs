---
title: Kā tas nolasa atkārtojumu
nav_order: 7
lang: "lv"
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Kā tas nolasa atkārtojumu {#how-it-reads-a-replay}

Atkārtojums ir galvene ar JSON blokiem un spēles paketes straume (formāta piezīmes failā [`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Pirmais bloks, atklātā tekstā: karte, klienta versija, ierakstošais spēlētājs un kuģis, un sastāvs — katra spēlētāja vārds, sabiedrotais vai ienaidnieks, un kuģa numurs. Jaunākie klienti (15.x) pievieno vēl divus blokus: tukšu un ierakstošā spēlētāja kontu un kaujas ID kā tekstu, nolasītu `blockIds`. Rezultāti nav JSON; 15.x tos glabā straumē.
- Paketes straume, saspiesta ar zlib un šifrēta ar Blowfish, ar atslēgu, ko spēle satur un ko kopienas rīki, kas lasa šos failus, ir publicējuši. Atšifrēta tā satur:
  - dzinēja pozīciju atjauninājumus katram kuģim, ko klients varēja redzēt (savu komandu visu laiku, ienaidniekus, kamēr tie ir pamanīti vai tuvu), vairākas reizes sekundē, kamēr tie kustas, un retāk, kad nekustas;
  - ieraksta spēlētāja paša kuģi atsevišķā paketē, apmēram septiņas reizes sekundē;
  - reizi, sākumā, spēlētāju ierakstus kā pickled Python sarakstu. Tie saka, kura straumes entītija ir kurš spēlētājs. To atslēgas ir numurētas, un numuri mainās līdz ar ielāpiem, tāpēc lasītājs atrod atslēgas pēc to vērtībām: atslēgu, kas satur sastāva vārdus, un atslēgu, kas satur entītijas ar pozīciju atjauninājumiem;
  - servera izsaukumu, kas saka klientam, ka kuģis ir nogrimis: upuris, slepkava, iemesls. To atrod pēc formas (divpadsmit baiti; pirmie divi ir kuģu entītijas; katrs upuris parādās vienreiz), nevis pēc tā numura;
  - katra kuģa bojājumus: masīvs (uzbrucējs, bojājums) katram trāpījumam, uz trāpītā kuģa; un tā veselību, īpašību kopu neilgi pirms tam;
  - katru čaulu un torpēdu salvu, par ko klients tika informēts: čaulas veidu, šāvēju, salvu un katras čaulas vai torpēdas sākumu un ātrumu;
  - kur čaulas beidzās: šāvēju, trāpījuma tipu un katras vietu (15.x klientos ar vairāk informācijas par čaulu tur, kur tā trāpīja, kas tiek izlaista);
  - tērzēšanu: sūtītājs, kanāls, rinda;
  - izsaukumus, kas pārsūtīti ierakstošajam spēlētājam: tā bojājumu statistiku, spēlētāju ierakstu atjauninājumus, kaujas stāvokli;
  - 15.x klientos kaujas rezultātus beigās: savu paketi, JSON objektu ar kaujas ID, nolasītu pilnībā mača dokumenta `results` (spēles pašas sarakstus, bez nosaukumiem: `commonList`, `privateDataList`, `playersPublicInfo` katram kontam, ...).

Paketes un metožu numuri, kas atšķiras starp pārbaudītajām versijām (kuģa paketes, kas pašam kuģim ir 43 vai 44; nogrimšanas izsaukums 76 vai 83; čaulas 101, 102, 126 vai 127), visi tiek atrasti pēc formas — skat. [`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) — tāpēc numerācijas maiņas ielāps neiztukšo tabulu. Atrastie numuri ir mača dokumenta `decoded`.

**Pickle dati ir nedroši.** Atkārtojums ir fails no jebkurienes, un pickle var nosaukt kodu, ko izpildīt. To ielādē ar atšifrētāju, kas katrai klasei vai funkcijai, ko pickle nosauc, dod inertu aizstājēju, tāpēc tas veido tikai vienkāršus datus un neko citu. Tests padod tam pickle, kas izsauc `os.system`.

**Nogrimšanām** ir precīzs izsaukuma laiks. To vieta ir tur, kur upuris pēdējo reizi tika redzēts, ja tas bija piecu sekunžu robežās. **Kaujas sākums** ir pirmais brīdis, kad jebkurš kuģis vispār kustas (kuģi stāv skaitīšanas laikā).

Viss, kas nav tabulas rinda, ir [mača dokumentā](match-document.md).

**Ko klients tika pateicis,** ir pilnīgi savai komandai un daļēji ienaidniekiem: viņu šāvieni, trāpījumi un veselība ir tur, kamēr tie ir diapazonā.

**Nav nolasīts:**

- Lidmašīnas un to eskadras (izsaukumi, kas tās nes, nav izšķirti); minimapas redzamības atjauninājumi (saspiesti); izlūkošana, lentes, ugunsgrēki un plūdi kā atsevišķi notikumi (to bojājumi ir trāpījumos); patēriņa priekšmeti; kontrolpunkti un komandu punkti (entītiju īpašības bez definīcijas, nav atšķirtas pēc formas); pārējās kuģa īpašības (mērķis, stūre, ātruma iestatījums...).
- Spēlētāju ierakstu un bojājumu statistikas atslēgu numuri kā nosaukumi: spēle tos numurē, un numuri mainās; tie ir paturēti kā numuri.
- Čaulas papildu dati, kur tā trāpīja (15.x), un baiti pēc čaulas vai torpēdas sākuma un ātruma.
- Rezultāti klientiem pirms 15.x: to atkārtojumos tādu nav.
- Kuģa numurs kā nosaukums: nosaukumi ir spēles pašas parametru failos, ne atkārtojumā.

## Kā lasīšana pārbaudīta {#how-the-reading-was-checked}

Lasīšana pārbaudīta uz publiskiem klientu atkārtojumiem no 0.9 līdz 15.x; katra vērtība salīdzināta ar kaut ko, ko atkārtojums dod otrreiz:

- **Pozīcijas:** katra kuģa entītija atbilda kāda sastāva vārdam; virzieni atbilst kustības virzienam 0,1 rad robežās; pēc tā nogrimšanas kuģis pārvietojas mazāk nekā par 0,1 vienību. Kuģis, kas stāv, tiek atjaunināts retāk.
- **Veselība:** katrs kuģis, kas nogrimis klienta redzeslokā, beidzas ar veselību 0. Apmēram puse no visiem trāpījumiem atbilst veselības kritumam sekundi iepriekš; pārējie sakrīt ar remontiem vai citiem trāpījumiem.
- **Bojājumi pret spēles pašu statistiku:** jaunākajā klientā ierakstošā spēlētāja nolasītais bojājums atbilst statistikai 0,1% robežās. Vecākos klientos statistika ir augstāka: klientam netiek nosūtīts katrs trāpījums, vai statistika skaita vairāk nekā trāpījumus (nav atrisināts).
- **Čaulas:** čaula sākas dažas vienības no sava kuģa pēdējās zināmās pozīcijas (ieroči ir izkaisīti pa korpusu); gandrīz katras čaulas beigas seko, minūtes robežās, kādam šāvienam, ko klients redzēja.

Testi veido atkārtojumus tādā pašā izkārtojumā, tāpēc šajā repozitorijā nav neviena īsta atkārtojuma.

**Nav pārbaudīts:** klienti pirms 0.9.6, Lesta klients (Mir Korabley), operācijas un scenāriji, kas nav viens, klanu un rangu kaujas, un tas, kurš kuģa numurs ir kurš kuģis.

---

Daļa no [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentācija](https://holdi601.github.io/3DHeat/)). Avots: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
