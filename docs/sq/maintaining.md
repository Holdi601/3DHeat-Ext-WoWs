---
title: "Mirëmbajtja"
nav_order: 99
lang: "sq"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Mirëmbajtja e dokumentacionit {#maintaining-the-documentation}

Për këdo që boton një version të ri. Bëji hapat në këtë rend.

1. **Rigjenero faqet e referencës** nga kodi:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   Kjo rishkruan [Referenca e komandave](../cli-reference.md) dhe
   [Lista e kolonave](../columns.md). Këto dy nuk i ndrysho kurrë me dorë.
2. **Liston çfarë ndryshoi që nga botimi i fundit:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` është versioni i fundit i botuar (ende pa etiketë: i gjithë
   `git log --oneline`). Çdo veçori, opsion ose kolonë e re ka nevojë për faqen e vet
   dhe për një rresht te seksioni **Docs** i
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Rishikim i pavarur.** Dikush që nuk i ka shkruar faqet (një person ose
   një agjent) i lexon README-n, çdo faqe dhe çdo pamje si tre
   lexues: një fillestar që s'ka përdorur kurrë terminal, një 8-vjeçar, dhe një
   profesionist që kontrollon çdo opsion, kolonë dhe njësi me kodin.
   Ata kontrollojnë edhe diagramet me kodin, dhe që asnjë faqe nuk emërton një
   hartë, nivel, lojtar ose ndeshje të vërtetë, as jep shifra nga riluajtje të vërteta.
4. **Rregullo çfarë gjeti rishikimi.** Pastaj nise sërish hapin 1 dhe rivizato
   pamjet që ndryshuan.
5. **Përkthimet.** Çdo faqe nën `docs/<language>/` regjistron hash-in e
   faqes angleze nga e cila u përkthye. Përktheji sërish të gjitha faqet që burimi
   i tyre anglez ndryshoi, përfshirë etiketat e diagrameve. Pastaj rishiko çdo
   gjuhë: e qartë për të tre lexuesit, etiketat të sakta, dhe të njëjtat fjalë
   që përdor shikuesi 3DHeat në atë gjuhë.
6. **Botimi:** ngri `VERSION` dhe etiketo `v<VERSION>`. **Shtyje (push) vetëm pasi
   pronari të japë miratimin.**

## Përkthimet: komandat {#translations-the-commands}

Faqja është përkthyer në 40 gjuhët e shikuesit 3DHeat: anglishtja në `docs/`, çdo gjuhë tjetër
në `docs/<lang>/` me të njëjtët emra skedarësh. `tools/docs_i18n.py` mban llogaritë:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Përkthe vetëm çfarë liston `todo`: mbaj Markdown, lidhjet, kodin, emrat e skedarëve dhe kolonave siç janë,
përkthe titujt dhe përshkrimet e pamjeve, dhe përdor fjalët e vetë shikuesit 3DHeat për butonat
dhe panelet e tij (`src/i18n/locales/<lang>/`). Faqet e referencës së gjeneruar dhe pamjet e terminalit mbeten
në anglisht. Në faqe, një përkthim i vjetruar e thotë këtë dhe lidh faqen angleze; një i munguar
kthehet te anglishtja. Menyja e gjuhës në krye dhe ridrejtimi sipas gjuhës së shfletuesit në ballinë
vijnë nga `docs/_includes/`.
