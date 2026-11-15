---
title: "Ako sa replay číta"
nav_order: 7
lang: "sk"
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Ako sa replay číta {#how-it-reads-a-replay}

Replay je hlavička z blokov JSON a tok paketov hry (poznámky k formátu
v [`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Prvý blok, čitateľný bez šifry: mapa, verzia klienta, hráč a loď, ktorí replay nahrali, a súpiska – meno každého
  hráča, spojenec alebo nepriateľ, a číslo lode. Novšie klienty (15.x) pridávajú ešte dva bloky: prázdny a účet hráča,
  ktorý replay nahral, a id bitky ako text, čítané do `blockIds`. Výsledky nie sú v JSON; 15.x ich drží v toku.
- Tok paketov, komprimovaný zlibom a šifrovaný Blowfishom s kľúčom, ktorý hra nesie; komunitné nástroje, ktoré tieto
  súbory čítajú, ho zverejnili. Po dešifrovaní obsahuje:
  - aktualizácie polohy enginu každej lode, ktorú klient mohol vidieť (jeho vlastný tím po celý čas, nepriatelia,
    kým sú spozorovaní alebo v blízkosti), niekoľkokrát za sekundu, keď sa pohybujú, a zriedkavejšie, keď nie;
  - loď hráča, ktorý replay nahral, v svojom vlastnom pakete, asi sedemkrát za sekundu;
  - raz, na začiatku, záznamy hráčov ako vyčlenený zoznam Python. Hovoria, ktorá entita v toku je ktorý hráč.
    Ich kľúče sú očíslované a čísla sa menia s patchmi, takže čítačka kľúče nájde podľa ich hodnôt: kľúč, ktorý drží
    mená zo súpisky, a kľúč, ktorý drží entity s aktualizáciami polohy;
  - volanie servera, ktoré hovorí klientovi, že loď sa potopila: obeť, vrah, príčina. Nájde sa podľa svojho tvaru
    (dvanásť bajtov; prvé dva sú entity lodí; každá obeť sa objaví raz), nie podľa čísla;
  - poškodenie každej lode: pole (útočník, poškodenie) na každý zásah, na zasiahnutej lodi; a jej zdravie, vlastnosť
    nastavená chvíľu predtým;
  - každú salvu granátov a torpéd, o ktorých klient vedel: typ strely, strelec, salva, a začiatok a rýchlosť každého
    granátu alebo torpéda;
  - kam granáty dopadli: strelec, typ zásahu a miesto každého (na klientoch 15.x s ďalšími údajmi o granáte v mieste
    zásahu, ktoré sa preskakujú);
  - chat: odosielateľ, kanál, riadok;
  - vyčlenené volania hráčovi, ktorý replay nahral: jeho štatistiky poškodenia, aktualizácie záznamov hráčov, stav bitky;
  - na klientoch 15.x výsledky bitky na konci: vlastný paket, objekt JSON s id bitky, prečítaný celý do `results`
    dokumentu zápasu (zoznamy hry, bez pomenovania: `commonList`, `privateDataList`, `playersPublicInfo` pre každý účet, ...).

Čísla paketov a volaní, ktoré sa líšia medzi overenými verziami (vlastný paket lode je 43 alebo 44, volanie potopenia 76
alebo 83, granáty 101, 102, 126 alebo 127), sa všetky nájdu podľa tvaru – pozri
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) – takže
oprava, ktorá ich prečísluje, nevyprázdni tabuľku. Nájdené čísla sú v `decoded` dokumentu zápasu.

**Vyčlenený zoznam je nedôveryhodné dáta.** Replay je súbor odkiaľkoľvek a vyčlenený zoznam môže pomenúvať kód na spustenie.
Načítava sa čítačkou, ktorá každej triede alebo funkcii, ktorú zoznam pomenúva, dá neaktívnu náhradu, takže vytvorí
len obyčajné dáta a nič iné. Jeden test mu podsunie vyčlenený zoznam, ktorý volá `os.system`.

**Potopenia** majú presný čas volania. Ich miesto je tam, kde bola obeť naposledy videná, keď to bolo do päť sekúnd.
**Začiatok bitky** je prvý okamih, keď sa niektorá loď vôbec pohne (lode v odpočítavaní stoja).

Všetko, čo nie je riadkom tabuľky, je v [dokumente zápasu](match-document.md).

**Čo bolo klientovi povedané** je úplné pre jeho vlastný tím a čiastočné pre nepriateľov: ich výstrely, zásahy a zdravie
sú tam, kým sú v dosahu.

**Nečítané:**

- Lietadlá a ich eskadry (volania, ktoré ich nesú, neboli rozobrané), aktualizácie videnia z minimapy (zabalené),
  spozorovanie, stuhy, požiare a záplavy ako vlastné udalosti (ich poškodenie je v zásahoch), spotrebný materiál,
  body dobytia a skóre tímov (vlastnosti entít bez definície, tvarom sa nerozlíšia), ostatné vlastnosti lode
  (miereni, kormidlo, nastavenie rýchlosti ...).
- Kľúčové čísla záznamov hráčov a štatistík poškodenia ako názvy: hra ich čísluje a čísla sa menia; sú uchované ako čísla.
- Dodatočné údaje granátu v mieste zásahu (15.x) a bajty po začiatku a rýchlosti granátu alebo torpéda.
- Výsledky klientov pred 15.x: ich replaye ich nenesú.
- Číslo lode ako názov: názvy sú v parametrových súboroch hry, nie v replayi.

## Ako sa čítanie overilo {#how-the-reading-was-checked}

Čítanie sa overilo na verejných replayoch klientov od 0.9 po 15.x, každá hodnota oproti niečomu, čo replay dáva druhýkrát:

- **Polohy:** entita každej lode sa zhodovala s menom zo súpisky; smery sa zhodujú so smerom pohybu do 0,1 rad; po jej
  potopení sa loď pohne menej než o 0,1 jednotky. Loď, ktorá stojí, sa aktualizuje zriedkavejšie.
- **Zdravie:** každá loď potopená v dohľade klienta skončí so zdravím 0. Asi polovica všetkých zásahov sa zhoduje s poklesom
  zdravia v sekunde pred nimi; zvyšok padne spolu s opravami alebo inými zásahmi.
- **Poškodenie oproti štatistikám hry:** na najnovšom klientovi je prečítané poškodenie hráča, ktorý replay nahral, do
  0,1 % štatistík. Na starších klientoch sú štatistiky vyššie: klientovi sa neposiela každý zásah, alebo štatistiky
  počítajú viac než zásahy (nevyriešené).
- **Granáty:** granát začína niekoľko jednotiek od poslednej známej polohy svojej lode (delá sú rozložené pozdĺž trupu);
  takmer každý koniec granátu nasleduje do minúty výstrel, ktorý klient videl.

Testy skladajú replaye do rovnakého rozloženia, takže v tomto repozitári nie je uložený žiadny skutočný replay.

**Neoverené:** klienty pred 0.9.6, klient Lesta (Mir Korabley), operácie a scenáre nad jeden, klanové a rankové bitky
a to, ktoré číslo lode je ktorá loď.

---

Súčasť [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentácia](https://holdi601.github.io/3DHeat/)). Zdroj: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
