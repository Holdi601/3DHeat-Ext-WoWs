---
title: "Viðhald skjölunar"
nav_order: 99
lang: is
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Viðhald skjölunar {#maintaining-the-documentation}

Fyrir þann sem gefur út nýja útgáfu. Gerðu skrefin í þessari röð.

1. **Búðu til tilvísunarsíðurnar aftur** úr kóðanum:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   Þetta endurskrifar [Skipanayfirlit](../cli-reference.md) og
   [Dálkalisti](../columns.md). Breyttu þessum tveimur aldrei í höndunum.
2. **Taktu saman hvað breyttist frá síðustu útgáfu:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` er síðasta útgefna útgáfa (engin tag enn: allt
   `git log --oneline`). Hver nýr eiginleiki, valkostur eða dálkur þarf sína síðu
   og röð í hlutanum **Docs** í
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Óháð yfirferð.** Einhver sem skrifaði ekki síðurnar (manneskja eða
   agent) les README, hverja síðu og hverja mynd sem þrír lesendur: byrjandi sem hefur aldrei notað
   skipanalínu, átta ára barn, og atvinnumaður sem ber hvern valkost, dálk og einingu saman við kóðann.
   Þeir athuga líka skýringarmyndirnar gegn kóðanum, og að engin síða nefni
   raunverulegt kort, borð, spilara eða leik, né gefi tölur úr raunverulegum upptökum.
4. **Lagaðu það sem yfirferðin fann.** Keyrðu svo skref 1 aftur og teiknaðu
   upp myndirnar þar sem úttakið breyttist.
5. **Þýðingar.** Hver síða undir `docs/<language>/` skráir tætigildi (hash) ensku
   síðunnar sem hún var þýdd úr. Þýddu aftur hverja síðu þar sem enski frumtextinn
   breyttist, merkimiða skýringarmynda meðtalda. Farðu svo yfir hvert
   tungumál: skýrt fyrir alla þrjá lesendurna, merkimiðar réttir, og sömu orð
   og 3DHeat-skoðarinn notar á því tungumáli.
6. **Útgáfa:** hækkaðu `VERSION` og merktu `v<VERSION>`. **Ýttu (push) aðeins eftir
   samþykki eigandans.**

## Þýðingar: skipanirnar {#translations-the-commands}

Vefurinn er þýddur á 40 tungumál 3DHeat-skoðarans: enska í `docs/`, hvert annað
tungumál í `docs/<lang>/` með sömu skráarnöfnum. `tools/docs_i18n.py` sér um bókhaldið:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Þýddu aðeins það sem `todo` telur upp: haltu Markdown, tenglum, kóða, skráar- og dálkanöfnum eins og þau eru,
þýddu titla og myndlýsingar, og notaðu eigin orð 3DHeat-skoðarans fyrir hnappa hans
og spjöld (`src/i18n/locales/<lang>/`). Búnar til tilvísunarsíður og skipanalínumyndir haldast
á ensku. Á vefnum segir úrelt þýðing frá því og tengir á ensku síðuna; vantandi þýðing
fellur aftur á ensku. Tungumálavalmynd hausins og tilvísun heimasíðunnar eftir tungumáli vafrans
koma úr `docs/_includes/`.
