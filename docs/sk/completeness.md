---
title: "Úplnosť"
nav_order: 8
lang: "sk"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Úplnosť {#completeness}

Nič z replaye sa nevyhodí. To, čo konvertor číta, ide do tabuľky a dokumentu zápasu; každá ďalšia položka sa uchová
celá v sprievodnom súbore `<match>.messages.parquet`; a položka `selfCheck.completeness` dokumentu zápasu počíta, čo sa
stalo s každým druhom položky. Toto je pravidlo, ktoré zdieľajú všetky konvertory 3DHeat:
[Konvertory zachovávajú všetko](https://holdi601.github.io/3DHeat/converters.html).

![Samokontrola syntetického replaye: každá položka videná, prečítaná, uchovaná alebo stratená](../assets/img/completeness.svg)

## Počet {#the-count}

Pre každý druh položky dáva `selfCheck.completeness.types`:

| Počet | Znamená |
|---|---|
| `seen` | koľko ich replay obsahuje |
| `decoded` | prečítané celé |
| `partial` | prečítané čiastočne a uchované celé v sprievodnom súbore |
| `raw` | len uchované celé v sprievodnom súbore, nečítané |
| `lost` | stratené: vždy `0` |

Druhy sú replaye vlastné: `block <n>` (bloky JSON), vlastné bajty kontajnera, `packet <type>`, a pre volania na
entitách `method <entity type>.<number>` a `property <entity type>.<number>`. `selfCheck.entities.roles` hovorí,
ktorý typ entity je avatar hráča, ktorý replay nahral, a ktoré sú lode. Druh, o ktorom nikto nevedel, sa ukáže so svojím počtom.

## Sprievodný súbor {#the-sidecar}

| Stĺpec | Čo |
|---|---|
| `time` | hodiny replaye, ako v tabuľke |
| `type`, `name` | druh položky; ako ju konvertor volá, tam, kde ju číta |
| `entity` | loď alebo avatar, ktorému patrí, ako `entity` v tabuľke |
| `decoded` | čo sa z nej prečítalo, ako JSON |
| `payload`, `text` | jej bajty, celé; bloky JSON, celé |
| `entityType`, `packet`, `method` | čísla |

Riadky sú zoradené podľa paketu, metódy, entity a času. Ktorá entita je ktorý hráč:
`entities` a `players` v dokumente zápasu.

## Čo sa číta a ako sa to overilo {#what-is-read-and-how-it-was-checked}

- **Výsledky** (15.x, `results`): ich id bitky je id z toku a každý hráč v nich je v súpiske z hlavičky.
- **Blok ids** (15.x, `blockIds`): účet a bitka, čítané ako text, aby sa nestratila žiadna číslica.
- **Sklon a náklon** každej polohy: náklon ide s rýchlosťou zákruty, lebo sa loď v zákrute nakláňa; sklon je takmer vždy 0.
- **Entity** (`entities`): kedy sa každá dostala do pohľadu klienta a kedy z neho odišla. Žiadna loď nemá polohu medzi
  odchodom a návratom.
- **Verzia v toku** (`streamVersion`): rovnaká ako v hlavičke.

Všetko ostatné, čo sa číta (potopenia, poškodenie, zdravie, granáty, torpéda, miesta dopadov granátov, chat,
vyčlenené volania, záznamy hráčov, polohy), je `partial`: v tabuľke alebo v dokumente zápasu a uchované celé v
sprievodnom súbore.

**Uchované, ale nečítané** (`raw`), najväčšie druhy: aktualizácie polôh, ktoré nie sú v tabuľke (po potopení lode,
entity bez hráča), časté vlastnosti a metódy bez čítačky, vlastnosti vytvorení entít a každý ďalší paket bez čítačky.

## Nedostupné {#not-available}

- To, čo server nikdy neposlal klientovi, ktorý nahrával: mierenie, kamera a vstupy iných hráčov, nepriatelia, kým neboli
  spozorovaní. Replay je to, čo jednému klientovi bolo povedané.
- Názvy typov entít, metód, vlastností a kľúčov štatistík: sú v definičných súboroch hry, nie v replayi. Čísla sa uchovávajú.
- Názvy lodí pre čísla lodí (použite `--ship-names`) a čokoľvek iné, čo potrebuje vlastné súbory hry.
- Výsledky klientov pred 15.x: v ich replayoch nie sú.

---

Súčasť [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentácia](https://holdi601.github.io/3DHeat/)). Zdroj: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
