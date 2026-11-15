---
title: "Údržba dokumentácie"
nav_order: 99
lang: sk
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Údržba dokumentácie {#maintaining-the-documentation}

Pre toho, kto vydáva novú verziu. Kroky robte v tomto poradí.

1. **Obnovte referenčné stránky** z kódu:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # musí skončiť s 0
   ```

   Tento príkaz prepíše [Referencia príkazov](../cli-reference.md) a [Zoznam stĺpcov](../columns.md).
   Tieto dve stránky nikdy neupravujte ručne.
2. **Vypíšte, čo sa zmenilo od poslednej verzie:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` je posledná vydaná verzia (zatiaľ bez značky: celý `git log --oneline`). Každá nová funkcia, možnosť
   alebo stĺpec potrebuje svoju stránku a riadok v sekcii **Docs** v
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Nezávislá kontrola.** Niekto, kto stránky nenapísal (človek alebo agent), prečíta README, každú stránku a každý obrázok
   ako tri čitatelia: začiatočník, ktorý nikdy nepoužil terminál, osemročné dieťa a profesionál, ktorý kontroluje každú
   možnosť, stĺpec a jednotku oproti kódu. Kontrolujú aj diagramy oproti kódu a to, že žiadna stránka nepomenúva
   skutočnú mapu, level, hráča ani zápas, ani neuvádza čísla zo skutočných replayov.
4. **Opravte, čo kontrola našla.** Potom znova spustite krok 1 a prekreslite obrázky, ktorých výstup sa zmenil.
5. **Preklady.** Každá stránka pod `docs/<jazyk>/` zaznamenáva hash anglickej stránky, z ktorej bola preložená. Znova
   preložte každú stránku, ktorej anglický zdroj sa zmenil, vrátane popisov diagramov. Potom skontrolujte každý jazyk:
   zrozumiteľnosť pre všetkých troch čitateľov, správne popisky a tie isté slová, aké používa 3DHeat prehliadač v tomto jazyku.
6. **Vydanie:** zvýšte `VERSION` a označte `v<VERSION>`. **Odosielajte len po súhlase vlastníka.**

## Preklady: príkazy {#translations-the-commands}

Stránky sú preložené do 40 jazykov prehliadača 3DHeat: angličtina v `docs/`, každý ďalší jazyk v `docs/<lang>/`
s rovnakými názvami súborov. `tools/docs_i18n.py` vedie evidenciu:

```bash
python tools/docs_i18n.py hashes             # po každej zmene angličtiny: zapíše hash každej stránky
python tools/docs_i18n.py svg-strings        # po každej zmene obrázka: popisky na preklad
python tools/docs_i18n.py status             # pre každý jazyk: aktuálne, zastarané, chýbajúce stránky
python tools/docs_i18n.py todo --lang de     # nemecké stránky na (znovu)preloženie
python tools/docs_i18n.py svg-build --lang de    # nemecké obrázky z docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # označí nemecké stránky hashom anglickej verzie
python tools/docs_i18n.py check              # skončí s 1, keď sú hashe alebo popisky zastarané
```

Prekladajte len to, čo vypíše `todo`: Markdown, odkazy, kód, názvy súborov a stĺpcov nechajte tak, ako sú; preložte
nadpisy a popisy obrázkov a pre tlačidlá a panely prehliadača používajte jeho vlastné slová (jeho
`src/i18n/locales/<lang>/`). Generované referenčné stránky a obrázky terminálu zostávajú v angličtine. Na stránke
zastaraný preklad to povie a odkáže na anglickú stránku; chýbajúci spadne na angličtinu. Ponuku jazykov v hlavičke
a presmerovanie na domovskú stránku podľa jazyka prehliadača berú z `docs/_includes/`.
