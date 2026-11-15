---
title: "Instalace"
nav_order: 3
lang: cs
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Instalace {#installing}

Nikdy jste nepracovali s příkazovým řádkem? Nejdříve si přečtěte [Než začnete](before-you-start.md).
Potřebuje Python 3.10 nebo novější; numpy a pyarrow se nainstalují spolu s ním.

## Krok za krokem {#step-by-step}

1. Získejte kód: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   nebo stáhněte zip z [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   a rozbalte ho.
2. Otevřete terminál v té složce a napište `pip install -e .`. Tím se příkaz
   `heat3d-wows-replay` dostane na vaši cestu (PATH).
3. Ověřte to: `heat3d-wows-replay --version`. Měli byste vidět
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` vypíše volby:

![heat3d-wows-replay --help](../assets/img/help.svg)

Bez instalace dělá totéž `python -m heat3d_ext_wows ...` ve složce nástroje.

Watcher 3DHeat spouští tento příkaz nad novými replayi, když je nainstalovaný,
a funguje i bez něj.

## Aktualizace {#updates}

Každé spuštění nejdřív zkontroluje GitHub vydání projektu (nejvýš jeden dotaz každých pár hodin; převod nikdy
nezastaví, ať je online, nebo ne). Když je vydána novější verze, příkaz se před instalací zeptá: `git clone` se
aktualizuje příkazem `git pull --ff-only` (odmítne se, pokud máte lokální změny), stažená kopie z archivu vydání.
`HEAT3D_NO_UPDATE=1` kontrolu i aktualizaci vypne.

---

Součást [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentace](https://holdi601.github.io/3DHeat/)). Zdroj: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
