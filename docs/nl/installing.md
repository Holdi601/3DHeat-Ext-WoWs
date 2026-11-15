---
title: "Installeren"
nav_order: 3
lang: nl
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Installeren {#installing}

Nieuw met de opdrachtregel? Lees eerst [Voordat je begint](before-you-start.md).
Je hebt Python 3.10 of nieuwer nodig; numpy en pyarrow worden er automatisch bij geïnstalleerd.

## Stap voor stap {#step-by-step}

1. Haal de code op: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   of download een zip-bestand via [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   en pak het uit.
2. Open een terminal in die map en typ `pip install -e .`. Dit zet de opdracht
   `heat3d-wows-replay` op je pad.
3. Controleer het: `heat3d-wows-replay --version`. Je ziet
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` laat de opties zien:

![heat3d-wows-replay --help](../assets/img/help.svg)

Zonder installeren doet `python -m heat3d_ext_wows ...` in de map van de tool
hetzelfde.

De 3DHeat Watcher draait deze opdracht op nieuwe replays als hij geïnstalleerd is,
en werkt ook zonder hem.

## Updates {#updates}

Bij elke start wordt eerst de GitHub-release van het project gecontroleerd (hooguit
één verzoek per paar uur; het stopt nooit een omzetting, online of offline). Is er een
nieuwere release, dan vraagt de opdracht eerst of hij die mag installeren: een
`git clone` wordt bijgewerkt met `git pull --ff-only` (geweigerd zolang je lokale
wijzigingen hebt), een gedownloade kopie uit het archief van de release.
`HEAT3D_NO_UPDATE=1` zet de controle en de update uit.

---

Onderdeel van [3DHeat](https://github.com/Holdi601/3DHeat) ([documentatie](https://holdi601.github.io/3DHeat/)). Bron: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
