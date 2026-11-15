---
title: "Manutenzjoni"
nav_order: 99
lang: "mt"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Manutenzjoni tad-dokumentazzjoni {#maintaining-the-documentation}

Għal min joħroġ verżjoni ġdida. Agħmel il-passi f'dan l-ordni.

1. **Erġa' ġenera l-paġni ta' referenza** mill-kodiċi:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   Dan jikteb mill-ġdid [Referenza tal-kmandi](../cli-reference.md) u
   [Lista tal-kolonni](../columns.md). Qatt ma tbiddel dawn it-tnejn bl-idejn.
2. **Elenka x'inbidel mill-aħħar release:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` hija l-aħħar verżjoni maħruġa (għad m'hemm l-ebda tag: l-`git log --oneline`
   kollu). Kull feature, għażla jew kolonna ġdida teħtieġ il-paġna tagħha u ringiela fit-taqsima
   **Docs** ta' [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Reviżjoni indipendenti.** Xi ħadd li ma kitibx il-paġni (persuna jew aġent) jaqra
   r-README, kull paġna u kull stampa bħala tliet qarrejja: bidu li qatt ma użat terminal,
   tifel ta' 8 snin, u professjonist li jiċċekkja kull għażla, kolonna u unità mal-kodiċi.
   Jiċċekkjaw ukoll id-dijagrammi mal-kodiċi, u li l-ebda paġna ma ssemmi mappa, livell,
   plejer jew partita vera, jew ma tagħti figuri minn ripetizzjonijiet veri.
4. **Sewwi dak li sabet ir-reviżjoni.** Imbagħad erġa' agħmel il-pass 1 u erġa' rasam
   l-istampi li nbidel il-ħruġ tagħhom.
5. **Traduzzjonijiet.** Kull paġna taħt `docs/<language>/` tirreġistra l-hash tal-paġna
   Ingliża li minnha ġiet tradotta. Ittraduċi mill-ġdid kull paġna li s-sors Ingliż tagħha
   inbidel, it-tikketti tad-dijagrammi inklużi. Imbagħad irrevedi kull lingwa: ċara għat-tliet
   qarrejja, tikketti ġusti, u l-istess kliem bħal dak li juża l-viewer tad-3DHeat f'dik il-lingwa.
6. **Release:** għolli `VERSION` u agħmel tag `v<VERSION>`. **Agħmel push biss wara
   l-ewwel li s-sid jagħti l-ok.**

## Traduzzjonijiet: il-kmandi {#translations-the-commands}

Is-sit huwa tradott fit-40 lingwa tad-3DHeat viewer: Ingliż f'`docs/`, kull lingwa oħra
f'`docs/<lang>/` bl-istess ismijiet ta' fajls. `tools/docs_i18n.py` iżomm il-kontijiet:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Ittraduċi biss dak li jelenka `todo`: żomm Markdown, links, kodiċi, ismijiet ta' fajls u
kolonni kif inhuma, ittraduċi t-titli u d-deskrizzjonijiet tal-istampi, u uża l-kliem proprju
tad-3DHeat viewer għall-buttuni u l-pannelli tiegħu (`src/i18n/locales/<lang>/` tiegħu). Il-paġni
ta' referenza ġġenerati u l-istampi tat-terminal jibqgħu bl-Ingliż. Fuq is-sit, traduzzjoni
skaduta tgħid hekk u tgħaqqad mal-paġna Ingliża; waħda neqsa terġa' lura għall-Ingliż. Il-menu
tal-lingwa fil-header u r-redirect tal-lingwa tal-browser tal-paġna ewlenija ġejjin minn `docs/_includes/`.
