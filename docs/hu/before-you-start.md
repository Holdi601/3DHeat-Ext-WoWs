---
title: "Mielőtt elkezded"
nav_order: 2
lang: "hu"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Mielőtt elkezded {#before-you-start}

Új vagy a parancssorban? Ez az oldal a semmiből egy működő `heat3d-wows-replay`
parancsig visz, körülbelül tíz perc alatt. Ha már használod a Pythont, menj
egyenesen a [Telepítés](installing.md) oldalra.

## 1. Telepítsd a Pythont {#install-python}

1. Töltsd le a Python **3.10 vagy újabb** verzióját innen:
   [python.org/downloads](https://www.python.org/downloads/).
2. Windowson a telepítő első ablakában pipáld be a **Add python.exe to PATH**
   (Python.exe hozzáadása a PATH-hoz) lehetőséget, majd kattints az **Install Now**
   (Telepítés most) gombra.
3. macOS-en és Linuxon a Python 3 gyakran már megvan. Ahol ezek az oldalak
   `python`-t írnak, írd be helyette a `python3`-at, a `pip` helyett pedig a `pip3`-at.

## 2. Nyiss egy terminált {#open-a-terminal}

A terminál egy ablak, ahová parancsokat gépelsz.

- **Windows:** nyisd meg a mappát a Fájlkezelőben, kattints a címsorra, írd be a
  `cmd`-t, és nyomj Entert. Egy ablak nyílik, amely már abban a mappában van.
- **macOS:** nyisd meg a **Terminal** (Terminál) alkalmazást. **Linux:** kattints
  jobb gombbal a mappában, és válaszd az **Open in Terminal** (Megnyitás terminálban)
  lehetőséget.

Másik mappába a `cd` és a mappa nevét írva jutsz:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Ellenőrizd, hogy a Python működik {#check-that-python-works}

```bash
python --version
```

A kimenetben `Python 3.` és 10 vagy annál nagyobb szám szerepel, például
`Python 3.12.4`.

## 4. Szerezd meg az eszközt, és telepítsd {#get-the-tool-and-install-it}

1. A [az eszköz GitHub-oldalán](https://github.com/Holdi601/3DHeat-Ext-WoWs)
   kattints a zöld **Code** (Kód) gombra, majd a **Download ZIP** (ZIP letöltése)
   lehetőségre, és csomagold ki a zip fájlt.
2. Nyiss egy terminált a kicsomagolt mappában (abban, amelyben a `README.md` van).
3. Írd be:

   ```bash
   pip install -e .
   ```

   A végén ezt kell látnod: `Successfully installed heat3d-ext-wows-0.1.0`
   (lehet, hogy további nevekkel együtt).
4. Ellenőrizd:

   ```bash
   heat3d-wows-replay --version
   ```

   Ezt kell látnod: `heat3d-wows-replay 0.1.0`

## Hogyan olvasd ezeken az oldalakon a parancsokat {#how-to-read-the-commands-on-these-pages}

- A szögletes zárójelbe tett szavak, például `<replays>`, helyőrzők: írd be ide
  a saját fájlodat vagy mappádat, a zárójelek nélkül.
- Szóközt tartalmazó útvonalat idézőjelbe kell tenni: `"C:\Program Files (x86)\Steam"`.
- A `#` utáni szöveg megjegyzés: nem kell beírnod.
- Az `-o out` a terminálod mappájában lévő, `out` nevű mappába ír. Ha nincs ilyen,
  létrejön.

## Mi jelzi a sikert {#what-success-looks-like}

A parancs soronként egy üzenetet ír ki minden visszajátszáshoz, például:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

és `0` kilépési állapottal fejeződik be. Az új fájlok az `out` mappában vannak.

## Gyakori hibák {#common-errors}

| Ezt látod | Mit tegyél |
|---|---|
| `'python' is not recognized ...` vagy `command not found` | a Python nincs a PATH-ban: telepítsd újra a **Add python.exe to PATH** bejelölésével, vagy Windowson `py`-t írj a `python` helyett |
| `'pip' is not recognized ...` | írd be helyette: `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | a `heat3d-wows-replay` helyett írd be: `python -m heat3d_ext_wows`; ugyanezt csinálja |
| `No module named heat3d_ext_wows` | nem az eszköz mappájában vagy, vagy nincs telepítve: menj oda a `cd` paranccsal, és futtasd a `pip install -e .`-t |
| `the following arguments are required: -o/--out` | tedd a parancs végére: `-o out` |

Következő: [Visszajátszások konvertálása](converting.md).
