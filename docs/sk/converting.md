---
title: "Konverzia replayov"
nav_order: 4
lang: sk
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Konverzia replayov {#converting-replays}

## Krok za krokom {#step-by-step}

1. **Zapnite nahrávanie**: `isReplayEnabled` v súbore `preferences.xml` hry, alebo vlastné nastavenie hry, ak ho má.
   Od tej chvíle hra ukladá každú bitku do priečinka `replays` vašej inštalácie World of Warships,
   napríklad `C:\Games\World_of_Warships_EU\replays`.
2. **Otvorte terminál** v priečinku, kam sa môžu uložiť výsledky ([Než začnete](before-you-start.md)).
3. **Spustite konvertor** na súbory replayov alebo na priečinky, ktoré ich obsahujú:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` sa vytvorí v priečinku, v ktorom je váš terminál.
4. **Prečítajte si, čo program hlási.** Mali by ste vidieť jeden riadok na každý replay, končiaci
   tabuľkou, ktorú zapísal.
5. **Otvorte výsledok** v 3DHeat prehliadači: `out/<map>/<match>.parquet` na karte Heatmapa,
   `<match>.match.json` na karte Zápas. Alebo ich čítajte ľubovoľnou čítačkou Parquet alebo JSON.

![Beh na syntetickom replaye: konverzia, opakovaný beh, pokazený súbor, prázdny priečinok](../assets/img/convert.svg)

Obrázok je beh na replaye, ktorý testy vytvoria v kóde (žiadny skutočný replay):

- replay prekonvertovaný: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- spustené znova, zápas, ktorý už je zapísaný, sa preskočí: `<file>: already written, <table>`;
- súbor, ktorý nie je replay: `<file>: not converted: <why>` (vo výstupe chýb; návratový stav 1, ostatné replaye sa aj tak prekonvertujú);
- nenájdený replay: `no .wowsreplay files in <folders>` (návratový stav 2).

## Možnosti {#options}

| Možnosť | Predvolené | Čo robí |
|---|---|---|
| `replays` (jeden alebo viac) | - | súbory `.wowsreplay`, alebo priečinky, v ktorých sa hľadajú (aj podpriečinky) |
| `-o`, `--out` | povinné | priečinok, do ktorého sa zapisuje: vnútri priečinok pre každú mapu |
| `--force` | vypnuté | konvertovať znova, čo je už zapísané |
| `--ship-names JSON` | - | súbor JSON `{"<shipId>": "<name>", ...}`: replaye pomenúvajú len loď hráča, ktorý replay nahral, ostatné podľa čísla |
| `--version` | - | vypísať `heat3d-wows-replay <version>` a skončiť |
| `-h`, `--help` | - | vypísať možnosti a skončiť |

Možnosti tak, ako ich program vypisuje: [Referencia príkazov](../cli-reference.md).

## Čo sa zapisuje {#what-is-written}

Len samostatné súbory: tento konvertor nezapisuje súbor `.3dheat` (prehliadač ich dokáže zabaliť do jedného:
[Jeden súbor na zápas](https://holdi601.github.io/3DHeat/container.html)).
Na každý replay, do `out/<map>/` (názov mapy bez jej `spaces/`):

| Súbor | Čo |
|---|---|
| `<match>.parquet` | tabuľka: poloha každej lode v čase a každá udalosť, pri ktorej sa stala ([Tabuľka](table.md)) |
| `<match>.match.json` | dokument zápasu: mapa, verzia klienta, hráči, potopenia, chat a všetko ostatné ([Dokument zápasu](match-document.md)) |
| `<match>.messages.parquet` | sprievodný súbor: každá položka replaye, ktorú dva vyššie uvedené súbory necelé nedržia ([Úplnosť](completeness.md)) |

`<match>` je vlastné id bitky, alebo názov súboru, keď sa nahrávanie zastavilo skôr, než vznikli výsledky.

## Návratový stav {#exit-status}

`0`, keď bol každý replay prekonvertovaný alebo preskočený; `1`, keď zlyhal aspoň jeden (ostatné
sa aj tak prekonvertujú); `2`, keď nebol nájdený žiadny súbor replaye.

---

Súčasť [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentácia](https://holdi601.github.io/3DHeat/)). Zdroj: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
