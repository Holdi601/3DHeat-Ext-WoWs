---
title: "Kako čita replay"
nav_order: 7
lang: bs
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Kako čita replay {#how-it-reads-a-replay}

Replay je zaglavlje JSON blokova i tok paketa igre (bilješke o formatu
u [`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Prvi blok, otvoreno: mapa, verzija klijenta, igrač koji snima
  i brod, te spisak - ime svakog igrača, saveznik ili neprijatelj i
  broj broda. Noviji klijenti (15.x) dodaju još dva bloka: prazan, i
  račun igrača koji snima i id bitke kao tekst, pročitan u
  `blockIds`. Rezultati nisu u JSON-u; 15.x ih čuva u toku.
- Tok paketa, zlib-komprimiran i Blowfish-šifriran ključem koji
  igra nosi, a koji su zajednički alati što čitaju ove datoteke
  objavili. Dešifriran, sadrži:
  - ažuriranja pozicija engine-a za svaki brod koji je klijent mogao vidjeti (njegov
    vlastiti tim cijelo vrijeme, neprijatelji dok su otkriveni ili blizu), nekoliko puta u
    sekundi dok se kreću, a rjeđe dok se ne kreću;
  - brod igrača koji snima u vlastitom paketu, oko sedam puta
    u sekundi;
  - jednom, na početku, zapise igrača kao pickled Python listu. Ti zapisi
    kažu koji je entitet u toku koji igrač. Njihovi ključevi su numerirani,
    a brojevi se mijenjaju s patchevima, pa čitač nalazi ključeve po
    njihovim vrijednostima: ključ koji drži imena sa spiska i ključ koji drži
    entitete koji imaju ažuriranja pozicija;
  - poziv servera koji klijentu javlja da je brod potonuo: žrtva, ubica,
    uzrok. Nalazi se po svom obliku (dvanaest bajtova; prva dva su
    entiteti brodova; svaka žrtva se pojavljuje jednom), a ne po broju;
  - štetu svakog broda: niz (napadač, šteta) po pogotku, na pogođenom
    brodu; i njegovo zdravlje, svojstvo postavljeno trenutak prije;
  - svaki plotun granata i torpeda o kojem je klijent obaviješten: tip
    granate, strijelac, plotun, te početak i brzina svake granate ili torpeda;
  - gdje su granate završile: strijelac, tip pogotka i mjesto svake (na
    klijentima 15.x s više podataka o granati tamo gdje je udarila, što se preskače);
  - čet: pošiljalac, kanal, red;
  - pickled pozive igraču koji snima: njegova statistika štete, ažuriranja
    zapisa igrača, stanje bitke;
  - na klijentima 15.x, rezultate bitke na kraju: vlastiti paket, JSON
    objekt s id-om bitke, pročitan cijeli u `results` dokumenta meča
    (vlastite liste igre, neimenovane: `commonList`,
    `privateDataList`, `playersPublicInfo` po računu, ...).

Brojevi paketa i metoda koji se razlikuju među provjerenim verzijama (paket
vlastitog broda je 43 ili 44, poziv potonuća 76 ili 83, granate 101, 102,
126 ili 127) svi se nalaze po obliku - vidi
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - pa patch
koji renumeriše ne ispraznuje tabelu. Pronađeni brojevi su u `decoded`
dokumenta meča.

**Pickle su nepouzdani podaci.** Replay je datoteka odakle god, a
pickle može imenovati kod za pokretanje. Učitava se unpicklerom koji svakoj
klasi ili funkciji koju pickle imenuje daje inertnu zamjenu, pa gradi obične
podatke i ništa drugo. Test mu daje pickle koji poziva `os.system`.

**Potonuća** imaju tačno vrijeme poziva. Njihovo mjesto je ono gdje je žrtva
zadnji put viđena, kad je to bilo unutar pet sekundi. **Početak bitke** je
prvi trenutak kad se ijedan brod uopće pomjeri (brodovi miruju tokom odbrojavanja).

Sve što nije red tabele nalazi se u [dokumentu meča](match-document.md).

**Ono što je rečeno klijentu** potpuno je za njegov vlastiti tim, a djelimično za
neprijatelje: njihovi hici, pogoci i zdravlje tu su dok su u dometu.

**Ne čita se:**

- Avioni i njihove eskadrile (pozivi koji ih nose nisu rastavljeni),
  ažuriranja vidljivosti minimape (pakirana), otkrivanje, ribboni, požari i
  poplave kao vlastiti događaji (njihova šteta je u pogocima), potrošni materijal,
  tačke zauzimanja i rezultati timova (svojstva entiteta bez
  definicije, ne razlikuju se po obliku), ostatak svojstava broda
  (nišanjenje, kormilo, postavka brzine...).
- Brojevi ključeva zapisa igrača i statistike štete kao imena: igra
  ih numeriše, a brojevi se mijenjaju; čuvaju se kao brojevi.
- Dodatni podaci granate tamo gdje je udarila (15.x) i bajtovi poslije početka i brzine
  granate ili torpeda.
- Rezultati klijenata prije 15.x: njihovi replayevi ih ne nose.
- Broj broda kao ime: imena su u vlastitim datotekama parametara
  igre, a ne u replayu.

## Kako je čitanje provjereno {#how-the-reading-was-checked}

Čitanje je provjereno na javnim replayevima klijenata od 0.9 do 15.x, svaka
vrijednost prema nečemu što replay daje drugi put:

- **Pozicije:** entitet svakog broda uparen je s imenom sa spiska; headinzi se slažu
  sa smjerom kretanja unutar 0,1 rad; poslije potonuća brod
  se pomjera manje od 0,1 jedinice. Brod koji miruje ažurira se rjeđe.
- **Zdravlje:** svaki brod potonuo unutar vidokruga klijenta završava sa zdravljem 0.
  Oko polovine svih pogodaka odgovara padu zdravlja u prethodnoj sekundi; ostali
  padaju zajedno s popravcima ili drugim pogocima.
- **Šteta prema vlastitoj statistici igre:** na najnovijem klijentu
  pročitana šteta igrača koji snima je unutar 0,1% statistike. Na starijim
  klijentima je statistika veća: klijentu se ne šalje svaki pogodak, ili
  statistika broji više od pogodaka (nije razriješeno).
- **Granate:** granata počinje nekoliko jedinica od zadnje poznate pozicije svog broda
  (topovi su raspoređeni duž trupa); kraj gotovo svake granate slijedi,
  unutar minute, hitac koji je klijent vidio.

Testovi grade replayeve u istom rasporedu, pa se nijedan pravi replay ne čuva u
ovom repozitoriju.

**Nije provjereno:** klijenti prije 0.9.6, Lesta klijent (Mir Korabley),
operacije i scenariji osim jednog, klanske i rangirane bitke, i
koji broj broda je koji brod.

---

Dio [3DHeata](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Izvor: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
