---
title: Paigaldamine
nav_order: 3
lang: "et"
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Paigaldamine {#installing}

Uus käsurea kasutamisel? Loe esmalt [Enne alustamist](before-you-start.md). Vajab Pythonit 3.10 või uuemat; numpy
ja pyarrow paigaldatakse koos sellega.

## Samm-sammult {#step-by-step}

1. Hangi kood: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`, või laadi zip alla lehelt
   [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases) ja paki lahti.
2. Ava terminal selles kaustas ja kirjuta `pip install -e .`. See teeb käsu `heat3d-wows-replay` kättesaadavaks.
3. Kontrolli: `heat3d-wows-replay --version`. Peaksid nägema `heat3d-wows-replay 0.1.0`.
   `heat3d-wows-replay --help` loetleb valikud:

![heat3d-wows-replay --help](../assets/img/help.svg)

Ilma paigaldamata teeb sama `python -m heat3d_ext_wows ...` tööriista kaustas.

3DHeat Watcher käivitab selle käsu uutel kordustel, kui see on paigaldatud, ja töötab ka ilma selleta.

## Uuendused {#updates}

Iga käivitamine kontrollib kõigepealt projekti GitHubi väljalaske (kõige rohkem üks päring iga paari tunni tagant;
see ei peata kunagi konverteerimist, ka siis, kui võrku ei ole). Kui on ilmunud uuem väljalase, küsib käsk enne
paigaldamist: `git clone` uuendatakse käsuga `git pull --ff-only` (keeldub, kui sul on lokaalseid muudatusi); allalaaditud koopia uuendatakse väljalaske arhiivist. `HEAT3D_NO_UPDATE=1` lülitab kontrolli ja uuendamise välja.

---

Osa [3DHeatist](https://github.com/Holdi601/3DHeat) ([dokumentatsioon](https://holdi601.github.io/3DHeat/)). Lähtekood: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
