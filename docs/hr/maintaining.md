---
title: Održavanje dokumentacije
nav_order: 99
lang: hr
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Održavanje dokumentacije {#maintaining-the-documentation}

Za onoga tko objavljuje novu verziju. Napravi korake ovim redom.

1. **Ponovno generiraj stranice referenci** iz koda:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # mora završiti sa statusom 0
   ```

   Ovo ponovno piše [Referencu naredbi](../cli-reference.md) i [Popis stupaca](../columns.md).
   Nikad ih ne uređuj ručno.
2. **Popiši što se promijenilo od zadnjeg izdanja:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` je zadnja objavljena verzija (bez oznake: cijeli `git log --oneline`). Svaka nova
   značajka, opcija ili stupac treba svoju stranicu i redak u odjeljku **Docs** u
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Neovisni pregled.** Netko tko nije pisao stranice (osoba ili agent) čita README, svaku
   stranicu i svaku sliku kao tri čitatelja: početnika koji nikad nije koristio terminal, osmogodišnjaka
   i profesionalca koji provjerava svaku opciju, stupac i jedinicu prema kodu. Također provjeravaju
   dijagrame prema kodu i to da nijedna stranica ne imenuje pravu kartu, razinu, igrača ili meč niti
   daje brojke iz pravih snimki.
4. **Popravi što je pregled našao.** Zatim ponovi korak 1 i ponovno nacrtaj slike čiji se
   izlaz promijenio.
5. **Prijevodi.** Svaka stranica pod `docs/<language>/` bilježi hash engleske stranice iz koje je
   prevedena. Ponovno prevedi svaku stranicu čiji se engleski izvor promijenio, uključujući
   oznake na dijagramima. Zatim pregledaj svaki jezik: jasno za sva tri čitatelja, oznake točne, i iste
   riječi kakve koristi 3DHeat preglednik na tom jeziku.
6. **Izdanje:** podigni `VERSION` i označi `v<VERSION>`. **Objavi tek nakon odobrenja
   vlasnika.**

## Prijevodi: naredbe {#translations-the-commands}

Stranica je prevedena na 40 jezika 3DHeat preglednika: engleski je u `docs/`, svaki drugi jezik u
`docs/<lang>/` s istim nazivima datoteka. `tools/docs_i18n.py` vodi evidenciju:

```bash
python tools/docs_i18n.py hashes             # nakon bilo koje engleske promjene: zabilježi hash svake stranice
python tools/docs_i18n.py svg-strings        # nakon bilo koje promjene slike: oznake za prijevod
python tools/docs_i18n.py status             # po jeziku: aktualno, zastarjelo, nedostajuće stranice
python tools/docs_i18n.py todo --lang de     # njemačke stranice za (ponovni) prijevod
python tools/docs_i18n.py svg-build --lang de    # njemačke slike iz docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # označi njemačke stranice engleskim hashom
python tools/docs_i18n.py check              # izlaz 1 kad su hashevi ili oznake zastarjeli
```

Prevodi samo ono što `todo` navodi: zadrži Markdown, poveznice, kod, nazive datoteka i stupaca,
prevedi naslove i opise slika, a za gumbe i panele 3DHeat preglednika koristi njegove vlastite
riječi (njegov `src/i18n/locales/<lang>/`). Generirane stranice referenci i terminalne slike ostaju
na engleskom. Na webu zastarjeli prijevod to kaže i poveznicom vodi na englesku stranicu; nedostajuća
se prikazuje na engleskom. Izbornik jezika u zaglavlju i preusmjeravanje na početnoj stranici prema
jeziku preglednika dolaze iz `docs/_includes/`.
