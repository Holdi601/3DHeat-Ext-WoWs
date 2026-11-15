---
title: "Jak se replay čte"
nav_order: 7
lang: cs
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Jak se replay čte {#how-it-reads-a-replay}

Replay je hlavička z bloků JSON a proud paketů hry (poznámky k formátu v
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- První blok, čitelný přímo: mapa, verze klienta, hráč a loď, který nahrával, a soupiska - jméno každého hráče,
  spojenec nebo nepřítel, a číslo lodi. Novější klienti (15.x) přidávají dva bloky: prázdný a účet hráče, který
  nahrával, a id bitvy jako text, načtené do `blockIds`. Výsledky nejsou v JSON; 15.x je drží v proudu.
- Proud paketů, komprimovaný zlibem a šifrovaný Blowfishem klíčem, který hra nese; komunitní nástroje, které tyto
  soubory čtou, ho zveřejnily. Po dešifrování obsahuje:
  - aktualizace pozic enginu u každé lodi, kterou klient viděl (vlastní tým po celou dobu, nepřátelé dokud byli
    spotted nebo v blízkosti), několikrát za vteřinu, když se pohybují, a méně často, když ne;
  - vlastní loď hráče, který nahrával, v jejím vlastním paketu, asi sedmkrát za vteřinu;
  - jednou, na začátku, záznamy hráčů jako pickle seznam Pythonu. Říkají, která entita v proudu je který hráč.
    Jejich klíče jsou očíslované a čísla se mění se záplatami, takže čtečka klíče najde podle jejich hodnot: klíč,
    který drží jména ze soupisky, a klíč, který drží entity s aktualizacemi pozic;
  - volání serveru, které říká klientovi, že loď byla potopena: oběť, zabiják, příčina. Najde se podle tvaru
    (dvanáct bajtů; první dva jsou entity lodí; každá oběť se objeví jednou), ne podle čísla;
  - poškození každé lodi: pole (útočník, poškození) na každý zásah, na zasažené lodi; a její zdraví, vlastnost
    nastavená chvíli předtím;
  - každá salva granátů a torpéd, o kterých klient věděl: typ granátu, střelec, salva, a začátek a rychlost každého
    granátu nebo torpéda;
  - kde granáty skončily: střelec, typ zásahu a místo každého (u klientů 15.x s dalšími údaji o granátu v místě
    zásahu, které se přeskakují);
  - chat: odesílatel, kanál, řádek;
  - volání pickle hráči, který nahrával: jeho statistiky poškození, aktualizace záznamů hráčů, stav bitvy;
  - u klientů 15.x na konci bitvy výsledky: vlastní paket, objekt JSON s id bitvy, načtený celý do `results`
    dokumentu zápasu (seznamy hry, bez názvů: `commonList`, `privateDataList`, `playersPublicInfo` na účet, ...).

Čísla paketů a metod, která se liší mezi ověřenými verzemi (paket vlastní lodi je 43 nebo 44, volání potopení 76
nebo 83, granáty 101, 102, 126 nebo 127), se všechna najdou podle tvaru - viz
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - takže
záplata, která je přečísluje, nevyprázdní tabulku. Nalezená čísla jsou v `decoded` dokumentu zápasu.

**Pickle je nedůvěryhodná data.** Replay je soubor odkudkoli a pickle může pojmenovat kód ke spuštění. Načítá se
unpicklerem, který každé třídě nebo funkci, kterou pickle pojmenuje, předá neškodnou náhražku, takže vytvoří jen
prostá data a nic jiného. Test mu podstrčí pickle, který volá `os.system`.

**Potopení** mají přesný čas volání. Jejich místo je tam, kde byla oběť naposledy spatřena, když to bylo do pěti sekund.
**Začátek bitvy** je první okamžik, kdy se nějaká loď vůbec pohne (lodě v odpočtu stojí).

Všechno, co není řádkem tabulky, je v [dokumentu zápasu](match-document.md).

**Co bylo řečeno klientovi** je úplné pro jeho vlastní tým a částečné pro nepřátele: jejich výstřely, zásahy a zdraví
tam jsou, dokud byli v dosahu.

**Nečteno:**

- Letadla a jejich letky (volání, která je nesou, nebyla rozebrána), aktualizace viditelnosti minimapy (zabalené),
  spotting, ribbony, požáry a záplavy jako vlastní události (jejich poškození je v zásazích), spotřební materiál,
  body dobytí a skóre týmů (vlastnosti entit bez definice, podle tvaru se nedají rozlišit), zbytek vlastností lodi
  (míření, kormidlo, nastavení rychlosti...).
- Čísla klíčů záznamů hráčů a statistik poškození jako názvy: hra je číslují a čísla se mění; drží se jako čísla.
- Dodatečné údaje granátu v místě zásahu (15.x) a bajty po začátku a rychlosti granátu nebo torpéda.
- Výsledky klientů před 15.x: jejich replaye je nenesou.
- Číslo lodi jako název: názvy jsou v parametrových souborech samotné hry, ne v replayi.

## Jak bylo čtení ověřeno {#how-the-reading-was-checked}

Čtení bylo ověřeno na veřejných replayích klientů od 0.9 do 15.x, každá hodnota proti něčemu, co replay dává podruhé:

- **Pozice:** entita každé lodi se shodovala se jménem ze soupisky; kurzy souhlasí se směrem plavby do 0,1 rad;
  po svém potopení se loď pohne o méně než 0,1 jednotky. Loď, která stojí, se aktualizuje méně často.
- **Zdraví:** každá loď potopená v zorném poli klienta končí se zdravím 0. Asi polovina všech zásahů se shoduje
  s poklesem zdraví během vteřiny před nimi; zbytek spadá dohromady s opravami nebo jinými zásahy.
- **Poškození proti vlastním statistikám hry:** u nejnovějšího klienta je přečtené poškození hráče, který nahrával,
  do 0,1 % od statistik. U starších klientů jsou statistiky vyšší: klientovi nejsou posílány všechny zásahy, nebo
  statistiky počítají víc než zásahy (nevyřešeno).
- **Granáty:** granát začíná několik jednotek od poslední známé pozice své lodi (děla jsou rozložena podél trupu);
  téměř konec každého granátu následuje do minuty výstřel, který klient viděl.

Testy staví replaye ve stejném rozložení, takže v tomto repozitáři není uložen žádný skutečný replay.

**Neověřeno:** klienti před 0.9.6, klient Lesta (Mir Korabley), operace a scénáře přesahující jeden, klanové a
hodnocené bitvy, a které číslo lodi je která loď.

---

Součást [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentace](https://holdi601.github.io/3DHeat/)). Zdroj: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
