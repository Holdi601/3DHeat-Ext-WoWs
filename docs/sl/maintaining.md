---
title: Vzdrževanje dokumentacije
nav_order: 99
lang: "sl"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Vzdrževanje dokumentacije {#maintaining-the-documentation}

Za tistega, ki izda novo različico. Koraki naj se izvedejo v tem vrstnem redu.

1. **Ponovno ustvarite referenčne strani** iz kode:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # mora končati z 0
   ```

   To prepiše [Referenca ukazov](../cli-reference.md) in [Seznam stolpcev](../columns.md). Ti dve nikoli ne
   urejajte ročno.
2. **Izpišite, kaj se je spremenilo od zadnje izdaje:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` je zadnja izdana različica (oznake še ni: celoten `git log --oneline`). Vsaka nova
   funkcija, možnost ali stolpec potrebuje svojo stran in vrstico v razdelku **Docs** v
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Neodvisen pregled.** Nekdo, ki ni pisal strani (oseba ali agent), prebere README, vsako stran in
   vsako sliko kot tri bralci: začetnik, ki še nikoli ni uporabljal ukazne vrstice, osemletnik in
   strokovnjak, ki vsako možnost, stolpec in enoto preveri z kodo. Preverijo tudi diagrame glede na
   kodo in to, da nobena stran ne navaja pravega zemljevida, nivoja, igralca ali tekme ali ne daje
   številk iz pravih posnetkov.
4. **Popravite, kar je pregled našel.** Nato ponovno zaženite korak 1 in na novo narišite slike, pri
   katerih se je izhod spremenil.
5. **Prevodi.** Vsaka stran pod `docs/<jezik>/` si beleži zgoščeno vrednost angleške strani, iz katere
   je bila prevedena. Ponovno prevedite vsako stran, katere angleški vir se je spremenil, vključno z
   oznakami na diagramih. Nato pregledajte vsak jezik: jasen za vse tri bralce, oznake pravilne in
   enake besede, kot jih v tem jeziku uporablja 3DHeat pregledovalnik.
6. **Izdaja:** dvignite `VERSION` in označite `v<VERSION>`. **Potisnite šele po odobritvi lastnika.**

## Prevodi: ukazi {#translations-the-commands}

Spletna stran je prevedena v 40 jezikov 3DHeat pregledovalnika: angleščina je v `docs/`, vsak drug jezik
v `docs/<lang>/` z enakimi imeni datotek. `tools/docs_i18n.py` vodi evidenco:

```bash
python tools/docs_i18n.py hashes             # po vsaki spremembi angleščine: zabeleži zgoščeno vrednost vsake strani
python tools/docs_i18n.py svg-strings        # po vsaki spremembi slike: oznake za prevod
python tools/docs_i18n.py status             # po jezikih: aktualne, zastarele, manjkajoče strani
python tools/docs_i18n.py todo --lang de     # nemške strani za (ponovni) prevod
python tools/docs_i18n.py svg-build --lang de    # nemške slike iz docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # označi nemške strani z njihovo angleško zgoščeno vrednostjo
python tools/docs_i18n.py check              # konča z 1, ko so zgoščene vrednosti ali oznake zastarele
```

Prevedite samo tisto, kar navaja `todo`: ohranite Markdown, povezave, kodo ter imena datotek in stolpcev,
prevedite naslove in opise slik ter za gumbe in plošče pregledovalnika uporabite njegove lastne besede
(njegov `src/i18n/locales/<lang>/`). Ustvarjene referenčne strani in slike terminala ostanejo v
angleščini. Na spletni strani zastarel prevod to pove in povezuje na angleško stran; manjkajoča stran se
prikaže v angleščini. Jezikovni meni v glavi in samodejno preusmeritev domače strani na podlagi jezika
brskalnika določa `docs/_includes/`.
