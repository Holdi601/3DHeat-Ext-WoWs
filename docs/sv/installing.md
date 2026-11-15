---
title: "Installera"
nav_order: 3
lang: sv
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Installera {#installing}

Ny i kommandoraden? Läs [Innan du börjar](before-you-start.md) först.
Kräver Python 3.10 eller senare; numpy och pyarrow installeras tillsammans med det.

## Steg för steg {#step-by-step}

1. Hämta koden: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   eller ladda ner en zip-fil från [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   och packa upp den.
2. Öppna en terminal i mappen och skriv `pip install -e .`. Det lägger
   kommandot `heat3d-wows-replay` på din sökväg.
3. Kontrollera det: `heat3d-wows-replay --version`. Du bör se
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` listar alternativen:

![heat3d-wows-replay --help](../assets/img/help.svg)

Utan installation gör `python -m heat3d_ext_wows ...` i verktygets mapp samma sak.

3DHeat Watcher kör det här kommandot på nya repriser när den är installerad,
och fungerar utan det.

## Uppdateringar {#updates}

Varje start kontrollerar först projektets GitHub-releaser (högst en förfrågan
var några timmar; det stoppar aldrig en konvertering, online eller inte). När en
nyare release finns frågar kommandot innan den installeras: en `git clone`
uppdateras med `git pull --ff-only` (vägras om du har lokala ändringar), en
nedladdad kopia från releasens arkiv. `HEAT3D_NO_UPDATE=1` stänger av kontrollen
och uppdateringen.

---

Del av [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentation](https://holdi601.github.io/3DHeat/)). Källa: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
