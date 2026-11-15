---
title: Namestitev
nav_order: 3
lang: sl
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Namestitev {#installing}

Ste novi v ukazni vrstici? Najprej preberite [Preden začnete](before-you-start.md). Potrebujete Python
3.10 ali novejši; numpy in pyarrow se namestita skupaj z njim.

## Korak za korakom {#step-by-step}

1. Pridobite kodo: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`, ali prenesite zip iz
   [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases) in ga razpakirajte.
2. Odprite ukazno vrstico v tej mapi in vpišite `pip install -e .`. Tako se ukaz
   `heat3d-wows-replay` doda vaši poti (PATH).
3. Preverite: `heat3d-wows-replay --version`. Videti bi morali `heat3d-wows-replay 0.1.0`.
   `heat3d-wows-replay --help` izpiše možnosti:

![heat3d-wows-replay --help](../assets/img/help.svg)

Brez namestitve enako naredi `python -m heat3d_ext_wows ...` v mapi orodja.

Watcher 3DHeat zažene ta ukaz na novih posnetkih, kadar je nameščen, in deluje tudi brez njega.

## Posodobitve {#updates}

Vsak zagon najprej preveri GitHub izdaje projekta (največ en zahtevek vsaki nekaj ur; nikoli ne
ustavi pretvorbe, ne glede na to, ali ste na spletu). Ko je na voljo novejša izdaja, ukaz pred
namestitvijo vpraša: `git clone` se posodobi z `git pull --ff-only` (zavrnjeno, dokler imate lokalne
spremembe), prenesena kopija pa iz arhiva izdaje. `HEAT3D_NO_UPDATE=1` izklopi preverjanje in
posodabljanje.

---

Del [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Vir: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
