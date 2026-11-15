---
title: "Údržba dokumentace"
nav_order: 99
lang: cs
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Údržba dokumentace {#maintaining-the-documentation}

Pro toho, kdo vydává novou verzi. Kroky dělejte v tomto pořadí.

1. **Znovu vygenerujte referenční stránky** z kódu:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # musí skončit stavem 0
   ```

   Tím se přepíšou [Přehled příkazů](../cli-reference.md) a [Seznam sloupců](../columns.md). Tyto dvě stránky
   nikdy neupravujte ručně.
2. **Vypište, co se změnilo od poslední verze:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` je poslední vydaná verze (zatím bez tagu: celý `git log --oneline`). Každá nová funkce, volba
   nebo sloupec potřebuje svou stránku a řádek v sekci **Docs** v
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Nezávislá kontrola.** Někdo, kdo stránky nenapsal (člověk nebo agent), přečte README, každou stránku
   a každý obrázek ze tří pohledů čtenáře: začátečník, který nikdy nepoužil terminál, osmiletý žák, a odborník,
   který každou volbu, sloupec a jednotku ověří proti kódu. Zkontrolují také diagramy proti kódu a to, že žádná
   stránka nejmenuje skutečnou mapu, úroveň, hráče ani zápas a neuvádí čísla ze skutečných replayů.
4. **Opravte, co kontrola našla.** Pak znovu proveďte krok 1 a překreslete obrázky, jejichž výstup se změnil.
5. **Překlady.** Každá stránka pod `docs/<language>/` zaznamenává hash anglické stránky, ze které byla přeložena.
   Znovu přeložte každou stránku, jejíž anglický zdroj se změnil, včetně popisků diagramů. Potom zkontrolujte
   každý jazyk: srozumitelnost pro všechny tři čtenáře, správné popisky a stejná slova, jaká prohlížeč 3DHeat
   v tom jazyce používá.
6. **Vydání:** zvyšte `VERSION` a označte `v<VERSION>`. **Odeslat pouze se souhlasem vlastníka.**

## Překlady: příkazy {#translations-the-commands}

Web je přeložen do 40 jazyků prohlížeče 3DHeat: angličtina v `docs/`, každý další jazyk v `docs/<lang>/` se
stejnými názvy souborů. `tools/docs_i18n.py` vede evidenci:

```bash
python tools/docs_i18n.py hashes             # po každé anglické změně: zaznamenat hash každé stránky
python tools/docs_i18n.py svg-strings        # po každé změně obrázku: popisky k překladu
python tools/docs_i18n.py status             # pro každý jazyk: aktuální, zastaralé, chybějící stránky
python tools/docs_i18n.py todo --lang de     # německé stránky k (novému) překladu
python tools/docs_i18n.py svg-build --lang de    # německé obrázky z docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # označit německé stránky anglickým hashem
python tools/docs_i18n.py check              # konec se stavem 1, když jsou hashe nebo popisky zastaralé
```

Překládejte jen to, co vypíše `todo`: Markdown, odkazy, kód, názvy souborů a sloupců ponechte beze změny,
překládejte nadpisy a popisy obrázků a pro tlačítka a panely prohlížeče používejte jeho vlastní slova (ve
složce `src/i18n/locales/<lang>/`). Vygenerované referenční stránky a obrázky terminálu zůstávají anglicky.
Na webu zastaralý překlad to řekne a odkáže na anglickou stránku; chybějící se vrátí k angličtině. Nabídku
jazyků v záhlaví a přesměrování domovské stránky podle jazyka prohlížeče berou ze složky `docs/_includes/`.
