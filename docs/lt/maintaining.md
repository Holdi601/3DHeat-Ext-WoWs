---
title: Dokumentacijos palaikymas
nav_order: 99
lang: "lt"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Dokumentacijos palaikymas {#maintaining-the-documentation}

Tam, kas leidžia naują versiją. Atlikite žingsnius šia tvarka.

1. **Iš naujo sugeneruokite nuorodų puslapius** iš kodo:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   Tai perrašo [Komandų nuorodą](../cli-reference.md) ir [Stulpelių sąrašą](../columns.md). Niekada
   nekeiskite šių dviejų rankiniu būdu.
2. **Išvardykite, kas pasikeitė nuo paskutinio leidimo:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` yra paskutinė išleista versija (jei žymos dar nėra: visas `git log --oneline`). Kiekvienai naujai
   funkcijai, parametrui ar stulpeliui reikia savo puslapio ir eilutės skyriuje **Docs** [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Nepriklausoma peržiūra.** Kas nors, kas nerašė puslapių (žmogus ar agentas), perskaito README, kiekvieną puslapį
   ir kiekvieną paveikslėlį tris skaitytojų akimis: pradedantysis, kuris niekada nenaudojo terminalo, aštuonerių metų
   vaikas ir profesionalas, kuris tikrina kiekvieną parametrą, stulpelį ir vienetą pagal kodą. Jie taip pat tikrina
   diagramas pagal kodą ir tai, kad joks puslapis nenurodo tikro žemėlapio, lygio, žaidėjo ar rungtynių, ir neteikia
   skaičių iš tikrų įrašų.
4. **Ištaisykite, ką rado peržiūra.** Tada vėl atlikite 1 žingsnį ir iš naujo nupieškite paveikslėlius, kurių išvestis
   pasikeitė.
5. **Vertimai.** Kiekvienas puslapis `docs/<language>/` įrašo maišos reikšmę to angliško puslapio, iš kurio jis
   išverstas. Iš naujo išverskite kiekvieną puslapį, kurio angliškas šaltinis pasikeitė, įskaitant diagramų etiketes.
   Tada peržiūrėkite kiekvieną kalbą: aiškumas trims skaitytojams, teisingos etiketės ir tie patys žodžiai, kuriuos
   3DHeat žiūryklė naudoja toje kalboje.
6. **Leidimas:** pakelkite `VERSION` ir pažymėkite `v<VERSION>`. **Skelkite tik gavę savininko leidimą.**

## Vertimai: komandos {#translations-the-commands}

Svetainė išversta į 3DHeat žiūryklės 40 kalbų: anglų kalba - `docs/`, kiekviena kita kalba - `docs/<lang>/` su tais pačiais
failų vardais. `tools/docs_i18n.py` tvarko apskaitą:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Verskite tik tai, ką nurodo `todo`: palikite Markdown, nuorodas, kodą, failų ir stulpelių vardus kaip yra; verskite
pavadinimus ir paveikslėlių aprašymus; žiūryklės mygtukams ir skydeliams naudokite jos pačios žodžius
(jos `src/i18n/locales/<lang>/`). Sugeneruoti nuorodų puslapiai ir terminalo paveikslėliai lieka angliškai. Svetainėje
pasenusiame vertime tai nurodoma ir pateikiama nuoroda į angliško puslapio, o neturint vertimo rodomas anglų
tekstas. Kalbų meniu antraštėje ir naršyklės kalbos peradresavimas pagrindiniame puslapyje ateina iš `docs/_includes/`.
