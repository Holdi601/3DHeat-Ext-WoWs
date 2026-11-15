---
title: Vedligeholdelse
nav_order: 99
lang: da
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Vedligeholdelse af dokumentationen {#maintaining-the-documentation}

Til den, der udgiver en ny version. Udfør trinene i denne rækkefølge.

1. **Genskab referencesiderne** ud fra koden:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # skal afslutte med 0
   ```

   Det omskriver [Kommandoreference](../cli-reference.md) og
   [Kolonneliste](../columns.md). Redigér aldrig de to i hånden.
2. **List hvad der er ændret siden den sidste udgivelse:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` er den sidst udgivne version (ingen tag endnu: hele `git log --oneline`). Hver ny funktion,
   valgmulighed eller kolonne skal have sin side og en række i afsnittet **Docs** i
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Uafhængig gennemgang.** Nogen, der ikke har skrevet siderne (en person eller en agent), læser README,
   hver side og hvert billede med tre læsere i tankerne: en begynder, der aldrig har brugt en terminal, en
   8-årig og en professionel, der tjekker hver valgmulighed, kolonne og enhed mod koden. De kontrollerer også
   diagrammerne mod koden, og at ingen side nævner et rigtigt kort, en rigtig bane, en rigtig spiller eller en
   rigtig kamp, eller giver tal fra rigtige replays.
4. **Ret det, gennemgangen fandt.** Kør derefter trin 1 igen og tegn de billeder om, hvis output er ændret.
5. **Oversættelser.** Hver side under `docs/<language>/` noterer hashen af den engelske side, den blev oversat
   fra. Oversæt igen hver side, hvis den engelske kilde er ændret, også diagrammernes etiketter. Gennemgå derefter
   hvert sprog: klart for alle tre læsere, etiketter rigtige, og de samme ord, som 3DHeat-vieweren bruger på det sprog.
6. **Udgivelse:** hæv `VERSION` og tag `v<VERSION>`. **Skub først, når ejeren har givet grønt lys.**

## Oversættelser: kommandoerne {#translations-the-commands}

Siden er oversat til de 40 sprog, 3DHeat-vieweren understøtter: engelsk i `docs/`, hvert andet sprog i
`docs/<lang>/` med de samme filnavne. `tools/docs_i18n.py` står for bogholderiet:

```bash
python tools/docs_i18n.py hashes             # efter enhver engelsk ændring: notér hver sides hash
python tools/docs_i18n.py svg-strings        # efter enhver billedændring: etiketterne, der skal oversættes
python tools/docs_i18n.py status             # pr. sprog: aktuelle, forældede og manglende sider
python tools/docs_i18n.py todo --lang de     # de tyske sider, der skal (gen)oversættes
python tools/docs_i18n.py svg-build --lang de    # tyske billeder ud fra docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stempl de tyske sider med deres engelske hash
python tools/docs_i18n.py check              # afslutter med 1, når hashes eller etiketter er forældede
```

Oversæt kun det, `todo` viser. Behold Markdown, links, kode, fil- og kolonnenavne som de er; oversæt titler og
billedbeskrivelser, og brug 3DHeat-vieweren egne ord for dens knapper og paneler (dens `src/i18n/locales/<lang>/`).
Genererede referencesider og terminalbilleder forbliver engelske. På siden markerer en forældet oversættelse det og
linker til den engelske side; en manglende falder tilbage til engelsk. Sprogmenuen i sidehovedet og
browsersprog-omdirigeringen på forsiden kommer fra `docs/_includes/`.
