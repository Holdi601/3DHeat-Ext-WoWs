---
title: "Převod replayů"
nav_order: 4
lang: "cs"
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Převod replayů {#converting-replays}

## Krok za krokem {#step-by-step}

1. **Zapněte nahrávání**: `isReplayEnabled` v souboru `preferences.xml` hry, nebo nastavení hry, pokud ho má.
   Od té chvíle hra ukládá každou bitvu do složky `replays` vaší instalace World of
   Warships, například `C:\Games\World_of_Warships_EU\replays`.
2. **Otevřete terminál** ve složce, kam se mohou výsledky uložit
   ([Než začnete](before-you-start.md)).
3. **Spusťte převodník** nad soubory replayů, nebo nad složkami, které je drží:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` se vytvoří ve složce, ve které je váš terminál.
4. **Přečtěte si, co nástroj hlásí.** Uvidíte jeden řádek na replay, který končí
   tabulkou, kterou zapsal.
5. **Otevřete výsledek** v prohlížeči 3DHeat: `out/<map>/<match>.parquet` na záložce
   Teplotní mapa, `<match>.match.json` na záložce Zápas. Nebo je přečtěte libovolným čtenářem
   Parquet nebo JSON.

![Běh nad syntetickým replayem: převod, opakovaný běh, poškozený soubor, prázdná složka](../assets/img/convert.svg)

Obrázek ukazuje běh nad replayem, který testy vytvářejí v kódu (žádný skutečný replay):

- replay převeden: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- spuštěno znovu, zápas už zapsaný se přeskočí: `<file>: already written, <table>`;
- soubor, který není replay: `<file>: not converted: <why>` (ve výstupu chyb;
  stav ukončení 1, ostatní replaye se stále převedou);
- žádný replay nenalezen: `no .wowsreplay files in <folders>` (stav ukončení 2).

## Volby {#options}

| Volba | Výchozí | Co dělá |
|---|---|---|
| `replays` (jedna nebo více) | - | soubory `.wowsreplay`, nebo složky, ve kterých se hledají (i podsložky) |
| `-o`, `--out` | povinné | složka, do které se zapisuje: uvnitř složka pro každou mapu |
| `--force` | vypnuto | převést znovu, co už je zapsané |
| `--ship-names JSON` | - | soubor JSON `{"<shipId>": "<name>", ...}`: replaye pojmenují jen loď hráče, který nahrával, ostatní podle čísla |
| `--version` | - | vypsat `heat3d-wows-replay <version>` a skončit |
| `-h`, `--help` | - | vypsat volby a skončit |

Volby tak, jak je program vypisuje: [Přehled příkazů](../cli-reference.md).

## Co se zapisuje {#what-is-written}

Pouze samostatné soubory: tento převodník nezapisuje žádný soubor `.3dheat` (prohlížeč je dokáže
zabalit do jednoho: [Jeden soubor na zápas](https://holdi601.github.io/3DHeat/container.html)).
Na každý replay, do `out/<map>/` (název mapy bez jejího `spaces/`):

| Soubor | Co |
|---|---|
| `<match>.parquet` | tabulka: pozice každé lodi v čase a každá událost, kde se stala ([Tabulka](table.md)) |
| `<match>.match.json` | dokument zápasu: mapa, verze klienta, hráči, potopení, chat a vše ostatní ([Dokument zápasu](match-document.md)) |
| `<match>.messages.parquet` | doplněk: každá položka replaye, kterou dva výše uvedené soubory nedrží celou ([Úplnost](completeness.md)) |

`<match>` je vlastní id bitvy, nebo název souboru, když nahrávání skončilo před výsledky.

## Stav ukončení {#exit-status}

`0`, když byl každý replay převeden nebo přeskočen; `1`, když kterýkoli selhal (ostatní se
stále převedou); `2`, když nebyl nalezen žádný soubor replaye.

---

Součást [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentace](https://holdi601.github.io/3DHeat/)). Zdroj: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
