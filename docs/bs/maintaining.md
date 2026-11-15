---
title: "Održavanje"
nav_order: 99
lang: bs
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Održavanje dokumentacije {#maintaining-the-documentation}

Za onoga ko izdaje novu verziju. Radite korake ovim redoslijedom.

1. **Ponovo generišite referentne stranice** iz koda:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   Ovo prepisuje [Referenca naredbi](../cli-reference.md) i
   [Lista kolona](../columns.md). Te dvije nikad ne uređujte ručno.
2. **Navedite šta se promijenilo od zadnjeg izdanja:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` je zadnja izdana verzija (nema još oznake: cijeli
   `git log --oneline`). Svaka nova funkcija, opcija ili kolona treba svoju stranicu
   i red u odjeljku **Docs** u
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Nezavisan pregled.** Neko ko nije pisao stranice (osoba ili
   agent) čita README, svaku stranicu i svaku sliku kao tri
   čitaoca: početnik koji nikad nije koristio terminal, osmogodišnjak i
   profesionalac koji provjerava svaku opciju, kolonu i jedinicu prema kodu.
   Također provjeravaju dijagrame prema kodu, i da nijedna stranica ne imenuje
   pravu mapu, nivo, igrača ili meč, niti daje brojke iz pravih replayeva.
4. **Ispravite šta je pregled našao.** Zatim ponovo pokrenite korak 1 i ponovo nacrtajte
   slike čiji se izlaz promijenio.
5. **Prijevodi.** Svaka stranica pod `docs/<language>/` bilježi hash
   engleske stranice iz koje je prevedena. Ponovo prevedite svaku stranicu čiji se
   engleski izvor promijenio, uključujući oznake dijagrama. Zatim pregledajte svaki
   jezik: jasno za sva tri čitaoca, oznake ispravne i iste riječi
   kakve 3DHeat preglednik koristi na tom jeziku.
6. **Izdanje:** podignite `VERSION` i označite `v<VERSION>`. **Pushajte tek poslije
   odobrenja vlasnika.**

## Prijevodi: naredbe {#translations-the-commands}

Stranica je prevedena na 40 jezika 3DHeat preglednika: engleski u `docs/`, svaki drugi
jezik u `docs/<lang>/` s istim imenima datoteka. `tools/docs_i18n.py` vodi evidenciju:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Prevodite samo ono što `todo` navodi: Markdown, linkove, kod, imena datoteka i kolona ostavite kakvi jesu,
prevedite naslove i opise slika, a za dugmad i panele koristite vlastite riječi 3DHeat preglednika
(njegov `src/i18n/locales/<lang>/`). Generisane referentne stranice i slike terminala ostaju
engleski. Na stranici, zastarjeli prijevod to kaže i povezuje englesku stranicu; nedostajući
se vraća na engleski. Izbornik jezika u zaglavlju i preusmjeravanje početne stranice prema jeziku preglednika
dolaze iz `docs/_includes/`.
