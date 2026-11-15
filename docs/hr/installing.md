---
title: Instalacija
nav_order: 3
lang: hr
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Instalacija {#installing}

Nikad nisi koristio naredbeni redak? Prvo pročitaj [Prije početka](before-you-start.md).
Treba Python 3.10 ili noviji; numpy i pyarrow se instaliraju uz njega.

## Korak po korak {#step-by-step}

1. Preuzmi kod: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   ili preuzmi zip s [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   i raspakiraj ga.
2. Otvori terminal u toj mapi i upiši `pip install -e .`. Ovo stavlja naredbu
   `heat3d-wows-replay` na tvoj put (PATH).
3. Provjeri: `heat3d-wows-replay --version`. Trebao bi vidjeti
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` ispisuje opcije:

![heat3d-wows-replay --help](../assets/img/help.svg)

Bez instalacije isto radi `python -m heat3d_ext_wows ...` u mapi alata.

Watcher 3DHeata pokreće ovu naredbu nad novim snimkama kad je instaliran,
a radi i bez nje.

## Ažuriranja {#updates}

Svako pokretanje prvo provjerava GitHub izdanja projekta (najviše jedan zahtjev svakih nekoliko
sati; nikad ne zaustavlja pretvaranje, online ili offline). Kad je izašlo novije izdanje,
naredba pita prije instaliranja: `git clone` se ažurira s `git pull --ff-only` (odbija se dok imaš
lokalne promjene), a preuzeta kopija iz arhive izdanja. `HEAT3D_NO_UPDATE=1` isključuje
provjeru i ažuriranje.

---

Dio [3DHeata](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Izvor: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
