---
title: "Vedlikeholde dokumentasjonen"
nav_order: 99
lang: no
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Vedlikeholde dokumentasjonen {#maintaining-the-documentation}

For den som gir ut en ny versjon. Gjør stegene i denne rekkefølgen.

1. **Regenerer referansesidene** fra koden:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # må avslutte med 0
   ```

   Dette skriver om [Kommandoreferanse](../cli-reference.md) og
   [Kolonneliste](../columns.md). Rediger aldri disse to for hånd.
2. **List hva som er endret siden forrige utgivelse:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` er den sist utgitte versjonen (uten tagg ennå: hele
   `git log --oneline`). Hver ny funksjon, hvert nytt valg eller hver ny kolonne
   trenger sin side og en rad i **Docs**-delen i
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Uavhengig gjennomgang.** Noen som ikke skrev sidene (en person eller en
   agent) leser README, hver side og hvert bilde som tre lesere: en nybegynner
   som aldri har brukt en terminal, en åtteåring, og en profesjonell som sjekker
   hvert valg, hver kolonne og hver enhet mot koden. De sjekker også diagrammene
   mot koden, og at ingen side nevner et ekte kart, nivå, en spiller eller et
   slag, eller gir tall fra ekte replayer.
4. **Rett det gjennomgangen fant.** Kjør deretter steg 1 igjen og tegn på nytt
   bildene der utdataene er endret.
5. **Oversettelser.** Hver side under `docs/<språk>/` lagrer hashen til den
   engelske siden den ble oversatt fra. Oversett på nytt hver side der den
   engelske kilden er endret, også tekst i diagrammene. Gjennomgå deretter hvert
   språk: tydelig for alle tre lesere, riktige navn, og de samme ordene som
   3DHeat-visningsprogrammet bruker på det språket.
6. **Utgivelse:** øk `VERSION` og lag taggen `v<VERSION>`. **Publiser først etter
   eierens grønne lys.**

## Oversettelser: kommandoene {#translations-the-commands}

Nettstedet er oversatt til 3DHeat-visningsprogrammets 40 språk: engelsk i `docs/`, hvert
annet språk i `docs/<språk>/` med de samme filnavnene. `tools/docs_i18n.py` står for
bokføringen:

```bash
python tools/docs_i18n.py hashes             # etter enhver endring i engelsk: lagre hashen til hver side
python tools/docs_i18n.py svg-strings        # etter enhver endring i et bilde: tekstene som skal oversettes
python tools/docs_i18n.py status             # per språk: oppdatert, utdatert, manglende sider
python tools/docs_i18n.py todo --lang de     # de tyske sidene som skal (over)oversettes
python tools/docs_i18n.py svg-build --lang de    # tyske bilder fra docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # merk de tyske sidene med deres engelske hash
python tools/docs_i18n.py check              # avslutter med 1 når hasher eller tekster er utdaterte
```

Oversett bare det `todo` lister: behold Markdown, lenker, kode, fil- og kolonnenavn
som de er, oversett titler og bildebeskrivelser, og bruk 3DHeat-visningsprogrammets egne
ord for knapper og paneler (dets `src/i18n/locales/<språk>/`). Genererte
referansesider og terminalbilder forblir engelske. På nettstedet sier en utdatert
oversettelse fra, og lenker til den engelske siden; en manglende faller tilbake til
engelsk. Språkmenyen i hodet og nettleserspråk-omdirigeringen på hjemmesiden kommer
fra `docs/_includes/`.
