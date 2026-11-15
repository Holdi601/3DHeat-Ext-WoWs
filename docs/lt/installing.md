---
title: Diegimas
nav_order: 3
lang: "lt"
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Diegimas {#installing}

Nesate dirbę su komandine eilute? Pirma perskaitykite [Prieš pradedant](before-you-start.md).
Reikia Python 3.10 ar naujesnės versijos; numpy ir pyarrow įdiegiami kartu su juo.

## Žingsnis po žingsnio {#step-by-step}

1. Gaukite kodą: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`
   arba atsisiųskite zip failą iš [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   ir išskleiskite.
2. Atidarykite terminalą tame aplanke ir įrašykite `pip install -e .`. Tai įdeda komandą
   `heat3d-wows-replay` į jūsų kelią (PATH).
3. Patikrinkite: `heat3d-wows-replay --version`. Turėtumėte matyti
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` išvardija parametrus:

![heat3d-wows-replay --help](../assets/img/help.svg)

Be diegimo tą patį daro `python -m heat3d_ext_wows ...` įrankio aplanke.

3DHeat Watcher paleidžia šią komandą naujiems įrašams, kai jis įdiegtas, ir veikia be jos.

## Atnaujinimai {#updates}

Kiekvieno paleidimo metu pirmiausia tikrinami projekto GitHub leidimai (ne dažniau kaip kartą per
kelias valandas; tai niekada nesustabdo konvertavimo, prisijungus ar neprisijungus). Kai išleidžiama
naujesnė versija, komanda prieš diegdama klausia: `git clone` kopija atnaujinama su
`git pull --ff-only` (atsisakoma, jei turite vietinių pakeitimų), atsisiųsta kopija - iš leidimo
archyvo. `HEAT3D_NO_UPDATE=1` išjungia ir tikrinimą, ir atnaujinimą.

---

Dalis [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Šaltinis: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
