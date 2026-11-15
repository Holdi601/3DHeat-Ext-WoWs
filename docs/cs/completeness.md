---
title: "Úplnost"
nav_order: 8
lang: "cs"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Úplnost {#completeness}

Nic z replaye se nezahazuje. Co převodník čte, jde do tabulky a dokumentu zápasu; každá další položka se drží celá
v doplňku `<match>.messages.parquet`; a `selfCheck.completeness` dokumentu zápasu počítá, co se stalo s každým
druhem položky. Toto je pravidlo, které sdílejí všechny převodníky 3DHeat:
[Převodníky zachovávají vše](https://holdi601.github.io/3DHeat/converters.html).

![Vlastní kontrola syntetického replaye: každá položka viděna, přečtena, ponechána nebo ztracena](../assets/img/completeness.svg)

## Počet {#the-count}

Pro každý druh položky dává `selfCheck.completeness.types`:

| Počet | Znamená |
|---|---|
| `seen` | kolik jich replay obsahuje |
| `decoded` | přečteno celé |
| `partial` | přečteno zčásti a drženo celé v doplňku |
| `raw` | drženo celé jen v doplňku, nepřečteno |
| `lost` | ztraceno: vždy `0` |

Druhy jsou vlastní druhy replaye: `block <n>` (bloky JSON), vlastní bajty kontejneru,
`packet <type>`, a u volání nad entitami `method <entity type>.<number>` a `property <entity type>.<number>`.
`selfCheck.entities.roles` říká, který typ entity je avatar hráče, který nahrával, a které jsou lodě.
Druh, o kterém nikdo nevěděl, se objeví se svým počtem.

## Doplněk {#the-sidecar}

| Sloupec | Co |
|---|---|
| `time` | hodiny replaye, jako v tabulce |
| `type`, `name` | druh položky; jak ji převodník nazývá, kde ji čte |
| `entity` | loď nebo avatar, ke kterému patří, jako `entity` v tabulce |
| `decoded` | co se z ní přečetlo, jako JSON |
| `payload`, `text` | její bajty, celé; bloky JSON, celé |
| `entityType`, `packet`, `method` | čísla |

Řádky jsou seřazeny podle paketu, metody, entity a času. Která entita je který hráč: `entities` a `players`
v dokumentu zápasu.

## Co se čte a jak bylo ověřeno {#what-is-read-and-how-it-was-checked}

- **Výsledky** (15.x, `results`): jejich id bitvy je id ze streamu a každý hráč v nich je v soupisce z hlavičky.
- **Blok id** (15.x, `blockIds`): účet a bitva, čteno jako text, aby se neztratila žádná číslice.
- **Sklon a náklon** každé pozice: náklon jde s rychlostí zatáčení, jak se loď v zatáčce naklání; sklon je téměř vždy 0.
- **Entity** (`entities`): kdy se každá dostala do zorného pole klienta a kdy z něj odešla.
  Žádná loď nemá pozici mezi odchodem a návratem.
- **Verze ve streamu** (`streamVersion`): stejná jako v hlavičce.

Vše ostatní, co se čte (potopení, poškození, zdraví, granáty, torpéda, kde granáty skončily, chat, volání
pickle, záznamy hráčů, pozice), je `partial`: v tabulce nebo v dokumentu zápasu a drženo celé v doplňku.

**Drženo, ale nečteno** (`raw`), největší druhy: aktualizace pozic, které nejsou v tabulce (po potopení lodě,
entity bez hráče), časté vlastnosti a metody bez čtečky, vlastnosti vytvoření entit a každý jiný paket bez čtečky.

## Není k dispozici {#not-available}

- Co server nikdy neposlal hráči, který nahrával: míření, kamera a vstupy ostatních hráčů, nepřátelé, dokud nejsou
  spatřeni. Replay je to, co jeden klient dostal.
- Názvy typů entit, metod, vlastností a klíčů statistik: jsou v definičních souborech hry, ne v replayi. Čísla se drží.
- Názvy lodí pro čísla lodí (použijte `--ship-names`) a cokoli jiného, co potřebuje vlastní soubory hry.
- Výsledky klientů před 15.x: v jejich replayích nejsou.

---

Součást [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentace](https://holdi601.github.io/3DHeat/)). Zdroj: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
