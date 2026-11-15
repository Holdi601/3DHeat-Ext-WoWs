---
title: "Installere"
nav_order: 3
lang: no
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Installere {#installing}

Ny på kommandolinjen? Les [Før du starter](before-you-start.md) først.
Krever Python 3.10 eller nyere; numpy og pyarrow installeres sammen med det.

## Steg for steg {#step-by-step}

1. Hent koden: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   eller last ned en zip fra [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   og pakk den ut.
2. Åpne en terminal i den mappen og skriv `pip install -e .`. Dette legger
   kommandoen `heat3d-wows-replay` på din PATH.
3. Sjekk det: `heat3d-wows-replay --version`. Du bør se
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` lister valgene:

![heat3d-wows-replay --help](../assets/img/help.svg)

Uten å installere gjør `python -m heat3d_ext_wows ...` i verktøyets mappe det samme.

3DHeat Watcher kjører denne kommandoen på nye replayer når den er installert,
og fungerer uten den.

## Oppdateringer {#updates}

Hver oppstart sjekker først prosjektets GitHub-utgivelser (høyst én forespørsel
hvert par timer; den stopper aldri en konvertering, enten du er på nett eller
ikke). Når en nyere utgivelse finnes, spør kommandoen før den installeres: en
`git clone` oppdateres med `git pull --ff-only` (avvist mens du har lokale
endringer), en nedlastet kopi fra utgivelsens arkiv. `HEAT3D_NO_UPDATE=1` slår
av sjekken og oppdateringen.

---

Del av [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentasjon](https://holdi601.github.io/3DHeat/)). Kilde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
