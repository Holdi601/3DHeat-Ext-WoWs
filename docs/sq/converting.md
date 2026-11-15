---
title: "Konvertimi i riluajtjeve"
nav_order: 4
lang: "sq"
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Konvertimi i riluajtjeve {#converting-replays}

## Hap pas hapi {#step-by-step}

1. **Ndiz regjistrimin**: `isReplayEnabled` te `preferences.xml` e lojës,
   ose cilësimi i vetë lojës aty ku e ka. Që atëherë loja e ruan çdo betejë në
   dosjen `replays` të instalimit tënd të World of Warships, për shembull
   `C:\Games\World_of_Warships_EU\replays`.
2. **Hap një terminal** në një dosje ku mund të shkojnë rezultatet
   ([Para se të fillosh](before-you-start.md)).
3. **Nise konvertuesin** mbi skedarë riluajtjeje, ose mbi dosje që i mbajnë:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` krijohet në dosjen ku është terminali yt.
4. **Lexo çfarë thotë.** Duhet të shohësh një rresht për çdo riluajtje, që mbaron me
   tabelën që shkroi.
5. **Hape rezultatin** në shikuesin 3DHeat: `out/<map>/<match>.parquet`
   në skedën Harta e nxehtësisë, `<match>.match.json` në skedën Ndeshja. Ose lexoji
   me çdo lexues Parquet ose JSON.

![Një ekzekutim mbi një riluajtje sintetike: konvertimi, ekzekutimi i dytë, një skedar i prishur, një dosje bosh](../assets/img/convert.svg)

Pamja është një ekzekutim mbi një riluajtje që testet e ndërtojnë në kod (nuk është riluajtje e vërtetë):

- një riluajtje e konvertuar: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- kur nisen përsëri, ndeshja e shkruar tashmë anashkalohet: `<file>: already written, <table>`;
- një skedar që nuk është riluajtje: `<file>: not converted: <why>` (në daljen e
  gabimeve; statusi i daljes 1, riluajtjet e tjera konvertohen prapë);
- nuk u gjet riluajtje: `no .wowsreplay files in <folders>` (statusi i daljes 2).

## Opsionet {#options}

| Opsioni | Parazgjedhja | Çfarë bën |
|---|---|---|
| `replays` (një ose më shumë) | - | skedarë `.wowsreplay`, ose dosje ku kërkohen ata (edhe nëndosjet) |
| `-o`, `--out` | i detyrueshëm | dosja ku të shkruhet: brenda saj një dosje për çdo hartë |
| `--force` | joaktiv | konverton sërish çfarë është shkruar tashmë |
| `--ship-names JSON` | - | një skedar JSON `{"<shipId>": "<name>", ...}`: riluajtjet emërtojnë vetëm anijen e lojtarit që regjistron, të tjerat sipas numrit |
| `--version` | - | printon `heat3d-wows-replay <version>` dhe ndalon |
| `-h`, `--help` | - | printon opsionet dhe ndalon |

Opsionet siç i printon programi: [Referenca e komandave](../cli-reference.md).

## Çfarë shkruhet {#what-is-written}

Vetëm skedarë të shkëputur: ky konvertues nuk shkruan skedar `.3dheat` (shikuesi mund
t'i paketojë në një të vetëm: [Një skedar për ndeshje](https://holdi601.github.io/3DHeat/container.html)).
Për riluajtje, në `out/<map>/` (emri i hartës pa `spaces/`):

| Skedari | Çfarë |
|---|---|
| `<match>.parquet` | tabela: pozicioni i çdo anijeje me kalimin e kohës dhe çdo ngjarje aty ku ndodhi ([Tabela](table.md)) |
| `<match>.match.json` | dokumenti i ndeshjes: harta, versioni i klientit, lojtarët, fundosjet, bisedat dhe gjithçka tjetër ([Dokumenti i ndeshjes](match-document.md)) |
| `<match>.messages.parquet` | skedari anësor: çdo element i riluajtjes që dy skedarët më sipër nuk e mbajnë të plotë ([Plotësia](completeness.md)) |

`<match>` është ID e vetë betejës, ose emri i skedarit kur regjistrimi
u ndal para rezultateve.

## Statusi i daljes {#exit-status}

`0` kur çdo riluajtje u konvertua ose u anashkalua, `1` kur ndonjëra dështoi (të
tjerat konvertohen prapë), `2` kur nuk u gjet asnjë skedar riluajtjeje.

---

Pjesë e [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacioni](https://holdi601.github.io/3DHeat/)). Burimi: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
