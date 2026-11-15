---
title: "Karbantartás"
nav_order: 99
lang: "hu"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# A dokumentáció karbantartása {#maintaining-the-documentation}

Annak, aki új verziót ad ki. A lépéseket ebben a sorrendben végezd el.

1. **A referenciaoldalak újragenerálása** a kódból:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   Ez újraírja a [Parancsreferencia](../cli-reference.md) és az [Oszloplista](../columns.md)
   oldalt. Ez a két oldal soha nem szerkeszthető kézzel.
2. **Listázd, mi változott az utolsó kiadás óta:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   A `<VERSION>` az utoljára kiadott verzió (ha még nincs címke: a teljes
   `git log --oneline`). Minden új funkciónak, kapcsolónak vagy oszlopnak kell az oldala,
   és egy sor a [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md)
   **Docs** (Dokumentáció) szakaszában.
3. **Független átnézés.** Valaki, aki nem írta az oldalakat (egy személy vagy egy ügynök),
   három olvasóként végigolvassa a README-t, minden oldalt és minden képet: egy kezdőt, aki
   még sosem használt terminált, egy nyolcévest, és egy szakembert, aki minden kapcsolót,
   oszlopot és mértékegységet ellenőriz a kóddal szemben. Ellenőrzik az ábrákat is a kóddal
   szemben, és azt, hogy egyik oldal sem nevez meg valódi térképet, pályát, játékost vagy
   meccset, és nem közöl valódi visszajátszásokból származó számokat.
4. **Javítsd ki, amit az átnézés talált.** Aztán futtasd újra az 1. lépést, és rajzold újra
   azokat a képeket, amelyek kimenete megváltozott.
5. **Fordítások.** Minden `docs/<language>/` alatti oldal rögzíti annak az angol oldalnak
   a hash-ét, amelyből fordították. Fordítsd újra minden olyan oldalt, amelynek az angol forrása
   megváltozott, az ábrák feliratait is beleértve. Aztán nézd át minden nyelvet: mindhárom
   olvasónak érthető, a feliratok helyesek, és ugyanazokat a szavakat használja, mint a
   3DHeat megjelenítő abban a nyelvben.
6. **Kiadás:** emeld meg a `VERSION` értékét, és készíts `v<VERSION>` címkét. **Csak a
   tulajdonos jóváhagyása után tolj.**

## Fordítások: a parancsok {#translations-the-commands}

Az oldal a 3DHeat megjelenítő 40 nyelvére van lefordítva: az angol a `docs/` mappában van, minden
más nyelv a `docs/<lang>/` mappában, ugyanazokkal a fájlnevekkel. A `tools/docs_i18n.py`
végzi a nyilvántartást:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Csak azt fordítsd, amit a `todo` listáz: tartsd meg a Markdownt, a linkeket, a kódot, a fájl- és
oszlopneveket úgy, ahogy vannak; fordítsd a címeket és a képleírásokat, és a 3DHeat megjelenítő saját
szavait használd a gombjaihoz és paneljeihez (a `src/i18n/locales/<lang>/` alatt). A generált
referenciaoldalak és a terminálképek angol nyelven maradnak. Az oldalon egy elavult fordítás ezt
jelzi, és az angol oldalra linkel; a hiányzó oldal visszaesik angolra. A fejléc nyelvi menüje és
a kezdőlap böngészőnyelv-átirányítása a `docs/_includes/` mappából jön.
