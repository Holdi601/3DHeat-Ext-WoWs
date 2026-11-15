---
title: Instalare
nav_order: 3
lang: ro
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Instalare {#installing}

Sunteți nou cu linia de comandă? Citiți mai întâi [Înainte de început](before-you-start.md).
Are nevoie de Python 3.10 sau mai nou; numpy și pyarrow se instalează odată cu el.

## Pas cu pas {#step-by-step}

1. Luați codul: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   sau descărcați un zip din [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   și dezarhivați-l.
2. Deschideți un terminal în acel folder și scrieți `pip install -e .`. Aceasta pune
   comanda `heat3d-wows-replay` în calea dumneavoastră de căutare.
3. Verificați: `heat3d-wows-replay --version`. Ar trebui să vedeți
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` listează opțiunile:

![heat3d-wows-replay --help](../assets/img/help.svg)

Fără instalare, `python -m heat3d_ext_wows ...` în folderul instrumentului face
același lucru.

Watcher-ul 3DHeat rulează această comandă pe replay-urile noi când este instalat,
și funcționează și fără ea.

## Actualizări {#updates}

Fiecare pornire verifică mai întâi versiunile publicate ale proiectului pe GitHub (cel mult o cerere
la câteva ore; nu oprește niciodată o conversie, fie că sunteți online, fie că nu). Când apare o versiune mai nouă,
comanda întreabă înainte de a o instala: un `git clone` se actualizează cu `git pull --ff-only` (refuzat cât timp aveți
modificări locale), o copie descărcată din arhiva versiunii. `HEAT3D_NO_UPDATE=1` oprește
verificarea și actualizarea.

---

Parte din [3DHeat](https://github.com/Holdi601/3DHeat) ([documentație](https://holdi601.github.io/3DHeat/)). Sursă: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
