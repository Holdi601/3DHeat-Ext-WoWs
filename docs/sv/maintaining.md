---
title: "Underhåll av dokumentationen"
nav_order: 99
lang: sv
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Underhåll av dokumentationen {#maintaining-the-documentation}

För den som släpper en ny version. Gör stegen i den här ordningen.

1. **Skapa om referenssidorna** från koden:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # måste avslutas med 0
   ```

   Det skriver om [Kommandoreferens](../cli-reference.md) och
   [Kolumnlista](../columns.md). Redigera aldrig dessa två för hand.
2. **Lista vad som ändrats sedan den senaste releasen:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` är den senast släppta versionen (ingen tagg än: hela
   `git log --oneline`). Varje ny funktion, varje alternativ eller kolumn behöver sin
   sida och en rad i avsnittet **Docs** i
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Oberoende granskning.** Någon som inte skrev sidorna (en person eller en agent)
   läser README, varje sida och varje bild som tre läsare: en nybörjare som aldrig
   använt en terminal, en åttaåring, och en proffs som kontrollerar varje alternativ,
   kolumn och enhet mot koden. De kontrollerar också att diagrammen stämmer med
   koden, och att ingen sida nämner en verklig karta, nivå, spelare eller match, eller
   anger siffror från verkliga repriser.
4. **Åtgärda det granskningen hittade.** Kör sedan steg 1 igen och rita om bilderna
   vars utdata ändrats.
5. **Översättningar.** Varje sida under `docs/<språk>/` registrerar hashen för den
   engelska sida den översattes från. Översätt om varje sida vars engelska källa
   ändrats, inklusive diagrammens etiketter. Granska sedan varje språk: tydligt för
   alla tre läsarna, etiketterna rätt, och samma ord som 3DHeat-visaren använder på
   det språket.
6. **Release:** höj `VERSION` och tagga `v<VERSION>`. **Publicera först efter ägarens
   godkännande.**

## Översättningar: kommandona {#translations-the-commands}

Webbplatsen är översatt till 3DHeat-visarens 40 språk: engelska i `docs/`, varje annat
språk i `docs/<lang>/` med samma filnamn. `tools/docs_i18n.py` sköter bokföringen:

```bash
python tools/docs_i18n.py hashes             # efter varje engelsk ändring: registrera varje sidas hash
python tools/docs_i18n.py svg-strings        # efter varje bildändring: etiketterna att översätta
python tools/docs_i18n.py status             # per språk: aktuella, inaktuella och saknade sidor
python tools/docs_i18n.py todo --lang de     # de tyska sidorna att (över)översätta
python tools/docs_i18n.py svg-build --lang de    # tyska bilder från docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stämpla de tyska sidorna med deras engelska hash
python tools/docs_i18n.py check              # avslutas med 1 när hashar eller etiketter är inaktuella
```

Översätt bara det `todo` listar: behåll Markdown, länkar, kod, fil- och kolumnnamn
som de är, översätt titlar och bildbeskrivningar, och använd 3DHeat-visarens egna
ord för dess knappar och paneler (dess `src/i18n/locales/<lang>/`). Genererade
referenssidor och terminalbilder förblir engelska. På webbplatsen säger en inaktuell
översättning det och länkar den engelska sidan; en saknad faller tillbaka på engelska.
Språkmenyn i sidhuvudet och startsidans omdirigering efter webbläsarspråk kommer från
`docs/_includes/`.
