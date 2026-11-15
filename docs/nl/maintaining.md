---
title: "Onderhoud"
nav_order: 99
lang: "nl"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# De documentatie onderhouden {#maintaining-the-documentation}

Voor wie een nieuwe versie uitbrengt. Doe de stappen in deze volgorde.

1. **Genereer de referentiepagina's opnieuw** uit de code:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # moet afsluiten met 0
   ```

   Dit herschrijft [Opdrachtreferentie](../cli-reference.md) en
   [Kolomlijst](../columns.md). Bewerk die twee nooit met de hand.
2. **Bekijk wat er veranderd is sinds de vorige release:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` is de laatst uitgebrachte versie (nog geen tag: het hele
   `git log --oneline`). Elke nieuwe functie, optie of kolom heeft zijn pagina
   nodig en een regel in de sectie **Docs** van
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Onafhankelijke controle.** Iemand die de pagina's niet geschreven heeft (een persoon of
   een agent) leest de README, elke pagina en elke afbeelding als drie lezers: een
   beginner die nog nooit een terminal gebruikte, een achtjarige, en een professional die
   elke optie, kolom en eenheid tegen de code controleert. Ze controleren ook de diagrammen
   tegen de code, en dat geen enkele pagina een echte kaart, level, speler of wedstrijd
   noemt, of cijfers uit echte replays geeft.
4. **Los op wat de controle vond.** Voer daarna stap 1 opnieuw uit en teken de
   afbeeldingen opnieuw waarvan de uitvoer veranderd is.
5. **Vertalingen.** Elke pagina onder `docs/<taal>/` bewaart de hash van de
   Engelse pagina waaruit ze vertaald is. Vertaal elke pagina opnieuw waarvan de
   Engelse bron veranderd is, ook de labels van de diagrammen. Controleer daarna elke
   taal: duidelijk voor alle drie de lezers, labels juist, en dezelfde woorden als
   de 3DHeat-viewer in die taal gebruikt.
6. **Uitbrengen:** verhoog `VERSION` en maak de tag `v<VERSION>`. **Push pas na
   de goedkeuring van de eigenaar.**

## Vertalingen: de commando's {#translations-the-commands}

De site is vertaald in de 40 talen van de 3DHeat-viewer: Engels in `docs/`, elke andere
taal in `docs/<lang>/` met dezelfde bestandsnamen. `tools/docs_i18n.py` houdt de
administratie bij:

```bash
python tools/docs_i18n.py hashes             # na elke wijziging in het Engels: de hash van elke pagina vastleggen
python tools/docs_i18n.py svg-strings        # na elke wijziging in een afbeelding: de labels om te vertalen
python tools/docs_i18n.py status             # per taal: actueel, verouderd, ontbrekende pagina's
python tools/docs_i18n.py todo --lang de     # de Duitse pagina's om (opnieuw) te vertalen
python tools/docs_i18n.py svg-build --lang de    # Duitse afbeeldingen uit docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # de Duitse pagina's stempelen met hun Engelse hash
python tools/docs_i18n.py check              # afsluiten met 1 als hashes of labels verouderd zijn
```

Vertaal alleen wat `todo` aangeeft: laat Markdown, links, code, bestands- en kolomnamen
zoals ze zijn, vertaal de titels en de beschrijvingen van de afbeeldingen, en gebruik de eigen
woorden van de 3DHeat-viewer voor zijn knoppen en panelen (zijn `src/i18n/locales/<lang>/`).
Gegenereerde referentiepagina's en terminalafbeeldingen blijven Engels. Op de site zegt een
verouderde vertaling dat en linkt ze naar de Engelse pagina; een ontbrekende valt terug op het
Engels. De taalmenu's in de kop en de doorverwijzing van de startpagina op basis van de
browsertaal komen uit `docs/_includes/`.
