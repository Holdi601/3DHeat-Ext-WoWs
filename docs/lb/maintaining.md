---
title: "Ënnerhalt"
nav_order: 99
lang: lb
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# D'Dokumentatioun ënnerhalen {#maintaining-the-documentation}

Fir déi, déi eng nei Versioun erausbréngen. Maach d'Schrëtt an dëser Reiefolleg.

1. **D'Referenzsäiten nei generéieren** aus dem Code:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   Dat schreift d'[Befehlsreferenz](../cli-reference.md) an d'
   [Kolonnelëscht](../columns.md) nei. Ännert déi zwou ni vun Hand.
2. **Opleeschte, wat sech zënter dem leschte Release geännert huet:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` ass déi lescht verëffentlecht Versioun (nach kee Tag: de ganze
   `git log --oneline`). All nei Fonktioun, Optioun oder Kolonn brauch seng Säit
   an eng Zeil an der **Docs**-Rubrik vum
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Onofhängeg Iwwerpréifung.** Een, deen d'Säite net geschriwwen huet (eng Persoun oder
   en Agent), liest d'README, all Säit an all Bild als dräi
   Lieser: een Ufänger, deen ni en Terminal benotzt huet, en 8-Järegt, an e
   Profi, dee jidd Optioun, Kolonn an Eenheet géint de Code préift.
   Si préifen och d'Diagrammer géint de Code, a ob keng Säit eng
   richteg Kaart, e richtege Level, Spiller oder Match nennt, oder Zuelen aus richtege Replays gëtt.
4. **Fixéieren, wat d'Iwwerpréifung fonnt huet.** Dann Schrëtt 1 nach eng Kéier maachen an d'
   Biller nei zeechnen, där hir Ausgab sech geännert huet.
5. **Iwwersetzungen.** All Säit ënner `docs/<language>/` hält den Hash vun der
   englescher Säit fest, aus där se iwwersat gouf. Iwwersetz all Säit nei, där hir
   englesch Quell sech geännert huet, Diagrammbeschrëftungen abegraff. Dann all
   Sprooch iwwerpréifen: kloer fir all dräi Lieser, Beschrëftunge richteg, an déiselwecht Wierder
   wéi den 3DHeat-Viewer an där Sprooch benotzt.
6. **Release:** `VERSION` eropsetzen an `v<VERSION>` taggen. **Nëmme pushen no der
   Zousoen vum Besëtzer.**

## Iwwersetzungen: d'Befehler {#translations-the-commands}

D'Site ass an déi 40 Sproochen vum 3DHeat-Viewer iwwersat: Englesch an `docs/`, all aner
Sprooch an `docs/<lang>/` mat de selwechten Dateinimm. `tools/docs_i18n.py` mécht d'Buchféierung:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Iwwersetz nëmmen, wat `todo` oplëscht: looss Markdown, Linken, Code, Datei- a Kolonnenimm sou, wéi se sinn,
iwwersetz Titelen a Bildbeschreiwungen, a benotz dem 3DHeat-Viewer seng eege Wierder fir seng Knäppchen
a Panelen (säi `src/i18n/locales/<lang>/`). Generéiert Referenzsäiten a Terminalbiller bleiwen
Englesch. Op der Site seet eng verrout Iwwersetzung dat a verlinkt déi englesch Säit; eng feelend
fält op Englesch zeréck. D'Sproochmenü am Header an d'Viruleedung no der Browsersprooch op der Startsäit
kommen aus `docs/_includes/`.
