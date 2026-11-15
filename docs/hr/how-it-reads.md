---
title: Kako se snimka čita
nav_order: 7
lang: hr
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Kako pretvarač čita snimku {#how-it-reads-a-replay}

Snimka je zaglavlje od JSON blokova i tok paketa igre (bilješke o formatu u
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Prvi blok, otvoreno: karta, verzija klijenta, igrač koji snima i njegov brod, i popis - ime svakog igrača,
  ally ili enemy, i broj broda. Noviji klijenti (15.x) dodaju još dva bloka: prazan, i račun igrača koji snima
  i id bitke kao tekst, pročitan u `blockIds`. Rezultati nisu u JSON-u; 15.x ih čuva u toku.
- Tok paketa, zlib-komprimiran i Blowfish-šifriran ključem koji nosi igra, a koji zajednički alati za čitanje
  ovih datoteka objavljuju. Dešifriran, sadrži:
  - ažuriranja položaja motora svakog broda koji je klijent mogao vidjeti (svoj tim cijelo vrijeme, neprijatelje
    dok su uočeni ili blizu), nekoliko puta u sekundi dok se miču, a rjeđe dok stoje;
  - vlastiti brod igrača koji snima u vlastitom paketu, oko sedam puta u sekundi;
  - jednom, na početku, zapise igrača kao pickle Python listu. Oni kažu koji je entitet u toku koji igrač.
    Njihovi ključevi su numerirani, a brojevi se mijenjaju uz zakrpe, pa čitač ključeve nalazi po vrijednostima:
    ključ koji drži imena s popisa i ključ koji drži entitete s ažuriranjima položaja;
  - poziv poslužitelja koji klijentu javlja da je brod potonuo: žrtva, ubojica, uzrok. Nalazi se po obliku
    (dvanaest bajtova; prva dva su entiteti brodova; svaka žrtva se pojavi jednom), a ne po broju;
  - šteta svakog broda: niz (napadač, šteta) po pogotku, na pogođenom brodu; i njegovo zdravlje, svojstvo
    postavljeno tren prije;
  - svaka salva granata i torpeda o kojoj je klijent obaviješten: vrsta granate, strijelac, salva, i početak
    i brzina svake granate ili torpeda;
  - gdje su granate završile: strijelac, vrsta pogotka i mjesto svake (na klijentima 15.x s više podataka o
    granati na mjestu udarca, što se preskače);
  - razgovor: pošiljatelj, kanal, red;
  - pickle pozivi igraču koji snima: njegova statistika štete, ažuriranja zapisa igrača, stanje bitke;
  - na klijentima 15.x, rezultati bitke na kraju: vlastiti paket, JSON objekt s id-om bitke, pročitan cijeli u
    `results` dokumenta meča (liste same igre, bez imena: `commonList`, `privateDataList`, `playersPublicInfo`
    po računu, ...).

Brojevi paketa i metoda koji se razlikuju među provjerenim verzijama (vlastiti paket broda je 43 ili 44, poziv
potonuća 76 ili 83, granate 101, 102, 126 ili 127) svi se nalaze po obliku - vidi
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - pa
zakrpa koja ih prenumerira ne isprazni tablicu. Nađeni brojevi su u `decoded` dokumenta meča.

**Pickle nije pouzdan.** Snimka je datoteka odakle god, a pickle može imenovati kod za izvršenje. Učitava se
razvodnikom koji svakoj klasi ili funkciji koju pickle imenuje daje neaktivnu zamjenu, pa gradi obične podatke i
ništa drugo. Test mu daje pickle koji poziva `os.system`.

**Potonuća** imaju točno vrijeme poziva. Mjesto je gdje je žrtva zadnji put viđena, kad je to bilo unutar pet
sekundi. **Početak bitke** je prvi trenutak u kojem se bilo koji brod uopće pomakne (brodovi miruju tijekom
odbrojavanja).

Sve što nije redak tablice nalazi se u [dokumentu meča](match-document.md).

**Što je klijentu rečeno** potpuno je za vlastiti tim, a djelomično za neprijatelje: njihovi hici, pogoci i zdravlje
su tu dok su u dometu.

**Nije čitano:**

- Zrakoplovi i njihove eskadrile (pozivi koji ih nose nisu rastavljeni), ažuriranja vida mini-karte (pakirana),
  uočavanje, vrpce, požari i poplave kao vlastiti događaji (njihova šteta je u pogocima), potrošni predmeti,
  bodovi zauzimanja i rezultati timova (svojstva entiteta bez definicije, po obliku se ne razlikuju), ostala
  svojstva broda (cilj, kormilo, postavka brzine...).
- Ključevi zapisa igrača i statistike štete kao imena: igra ih numerira, a brojevi se mijenjaju; čuvaju se kao
  brojevi.
- Dodatni podaci granate na mjestu udarca (15.x) i bajtovi iza početka i brzine granate ili torpeda.
- Rezultati klijenata prije 15.x: njihove snimke ih nemaju.
- Broj broda kao ime: imena su u vlastitim parametarskim datotekama igre, ne u snimci.

## Kako je čitanje provjereno {#how-the-reading-was-checked}

Čitanje je provjereno na javnim snimkama klijenata od 0.9 do 15.x, svaka vrijednost prema nečemu što
snimka daje drugi put:

- **Položaji:** entitet svakog broda odgovarao je imenu s popisa; smjerovi se slažu sa smjerom kretanja unutar
  0,1 rad; nakon potonuća brod se pomakne manje od 0,1 jedinice. Brod koji stoji ažurira se rjeđe.
- **Zdravlje:** svaki brod potonut u pogledu klijenta završava sa zdravljem 0. Otprilike polovica svih pogodaka
  se poklapa s padom zdravlja u sekundi prije; ostali padaju zajedno s popravcima ili drugim pogocima.
- **Šteta prema vlastitoj statistici igre:** na najnovijem klijentu pročitana šteta igrača koji snima je unutar
  0,1 % statistike. Na starijim klijentima statistika je veća: klijentu se ne šalje svaki pogodak, ili statistika
  broji više od pogodaka (nije riješeno).
- **Granate:** granata počinje nekoliko jedinica od zadnje poznate pozicije svog broda (topovi su raspoređeni
  po trupu); gotovo kraj svake granate slijedi, unutar minute, hitac koji je klijent vidio.

Testovi grade snimke istim rasporedom, pa ni jedna prava snimka nije sačuvana u ovom repozitoriju.

**Nije provjereno:** klijenti prije 0.9.6, Lestin klijent (Mir Korabley), operacije i scenariji osim jednog, klanovske
i rangirane bitke, i koji broj pripada kojem brodu.

---

Dio [3DHeata](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Izvor: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
