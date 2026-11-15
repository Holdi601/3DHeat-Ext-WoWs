---
title: Dokumentācijas uzturēšana
nav_order: 99
lang: "lv"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Dokumentācijas uzturēšana {#maintaining-the-documentation}

Tiem, kas izlaiž jaunu versiju. Veiciet soļus šādā secībā.

1. **Atjaunojiet atsauces lappuses** no koda:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # jābeidzas ar 0
   ```

   Tas pārraksta [Komandu atsauci](../cli-reference.md) un [Kolonnu sarakstu](../columns.md). Nekad nerediģējiet šīs divas ar roku.
2. **Uzskaitiet, kas mainījies kopš pēdējā izlaiduma:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` ir pēdējā izlaistā versija (ja tagu vēl nav: viss `git log --oneline`). Katrai jaunai funkcijai, iespējai vai kolonnai nepieciešama sava lappuse un rinda sadaļā **Docs** [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Neatkarīga pārskatīšana.** Kāds, kas nav rakstījis lappuses (cilvēks vai aģents), izlasa README, katru lappusi un katru attēlu kā trīs lasītāji: iesācējs, kurš nekad nav lietojis termināli; astoņgadnieks; un profesionālis, kurš pārbauda katru iespēju, kolonnu un mērvienību pret kodu. Viņi pārbauda arī diagrammas pret kodu un to, ka neviena lappuse nenosauc reālu karti, līmeni, spēlētāju vai maču, un nedod ciparus no reāliem atkārtojumiem.
4. **Izlabojiet, ko atrada pārskatīšana.** Tad atkārtojiet 1. soli un pārzīmējiet attēlus, kuru izvade mainījusies.
5. **Tulkojumi.** Katra lappuse `docs/<valoda>/` ieraksta to angļu lappuses jaucējkodu, no kuras tā tulkota. Atkārtoti tulkojiet katru lappusi, kuras angļu avots mainījies, arī diagrammu uzrakstus. Tad pārskatiet katru valodu: skaidri visiem trim lasītājiem, pareizi uzraksti un tie paši vārdi, ko 3DHeat skatītājs lieto šajā valodā.
6. **Izlaidums:** paaugstiniet `VERSION` un atzīmējiet `v<VERSION>`. **Pārsūtiet tikai pēc īpašnieka atļaujas.**

## Tulkojumi: komandas {#translations-the-commands}

Vietne tulkota 3DHeat skatītāja 40 valodās: angļu `docs/`, katra cita valoda `docs/<lang>/` ar tiem pašiem failu nosaukumiem. `tools/docs_i18n.py` veic uzskaiti:

```bash
python tools/docs_i18n.py hashes             # pēc jebkuras angļu izmaiņas: ierakstiet katras lappuses jaucējkodu
python tools/docs_i18n.py svg-strings        # pēc jebkuras attēla izmaiņas: uzraksti, ko tulkot
python tools/docs_i18n.py status             # pa valodām: aktuālās, novecojušās, trūkstošās lappuses
python tools/docs_i18n.py todo --lang de     # vācu lappuses, kas jātulko (vai jātulko vēlreiz)
python tools/docs_i18n.py svg-build --lang de    # vācu attēli no docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # apzīmo vācu lappuses ar to angļu jaucējkodu
python tools/docs_i18n.py check              # izejas kods 1, ja jaucējkodi vai uzraksti ir novecojuši
```

Tulkojiet tikai to, ko `todo` saraksta: saglabājiet Markdown, saites, kodu, failu un kolonnu nosaukumus kā tie ir; tulkojiet virsrakstus un attēlu aprakstus, un izmantojiet 3DHeat skatītāja pašu vārdus tā pogām un paneļiem (`src/i18n/locales/<lang>/`). Ģenerētās atsauces lappuses un termināla attēli paliek angliski. Vietnē novecojis tulkojums to saka un saista ar angļu lappusi; trūkstoša lappuse atkrīt uz angļu valodu. Galvenes valodu izvēlni un mājas lappuses pārvirzīšanu pēc pārlūka valodas nodrošina `docs/_includes/`.

