---
title: Пре почетка
nav_order: 2
lang: sr
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Пре почетка {#before-you-start}

Први пут у командној линији? Ова страница вас води од нуле до радног
`heat3d-wows-replay` за око десет минута. Ако већ користите Python, идите
право на [Инсталацију](installing.md).

## 1. Инсталирајте Python {#install-python}

1. Преузмите Python **3.10 или новији** са
   [python.org/downloads](https://www.python.org/downloads/).
2. На Windows-у означите **Add python.exe to PATH** у првом прозору
   инсталера, па кликните **Install Now**.
3. На macOS-у и Linux-у Python 3 је често већ инсталиран. Укуцајте `python3`
   где ове странице пишу `python`, и `pip3` уместо `pip`.

## 2. Отворите терминал {#open-a-terminal}

Терминал је прозор у који куцате команде.

- **Windows:** отворите фасциклу у File Explorer-у, кликните на адресну траку,
  укуцајте `cmd` и притисните Enter. Отвара се прозор, већ у тој фасцикли.
- **macOS:** отворите апликацију **Terminal**. **Linux:** десним кликом у
  фасциклу изаберите **Open in Terminal**.

Да одете у другу фасциклу, укуцајте `cd` и фасциклу:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Проверите да Python ради {#check-that-python-works}

```bash
python --version
```

Требало би да видите `Python 3.` и број 10 или већи, на пример
`Python 3.12.4`.

## 4. Преузмите алатку и инсталирајте је {#get-the-tool-and-install-it}

1. На [GitHub страници алатке](https://github.com/Holdi601/3DHeat-Ext-WoWs) кликните
   зелено дугме **Code**, па **Download ZIP**, и распакујте зип.
2. Отворите терминал у распакованој фасцикли (оној у којој је `README.md`).
3. Укуцајте:

   ```bash
   pip install -e .
   ```

   На крају треба да видите: `Successfully installed heat3d-ext-wows-0.1.0`
   (можда са још неким именима).
4. Проверите:

   ```bash
   heat3d-wows-replay --version
   ```

   Требало би да видите: `heat3d-wows-replay 0.1.0`

## Како да читате команде на овим страницама {#how-to-read-the-commands-on-these-pages}

- Речи у угаоним заградама, као `<replays>`, су места за ваше податке: на
  њих упишите своју датотеку или фасциклу, без заграда.
- Путања са размацима мора под наводнике: `"C:\Program Files (x86)\Steam"`.
- Текст иза `#` је коментар: не куцате га.
- `-o out` пише у фасциклу `out` унутар фасцикле у којој је ваш терминал.
  Ако је нема, она се прави.

## Како изгледа успех {#what-success-looks-like}

Команда исписује по један ред за сваки реплеј, на пример:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

и завршава се излазним статусом `0`. Нове датотеке су у фасцикли `out`.

## Честе грешке {#common-errors}

| Видите | Шта да урадите |
|---|---|
| `'python' is not recognized ...` или `command not found` | Python није у PATH-у: инсталирајте га поново са означеним **Add python.exe to PATH** или укуцајте `py` уместо `python` (Windows) |
| `'pip' is not recognized ...` | укуцајте `python -m pip install -e .` уместо тога |
| `'heat3d-wows-replay' is not recognized ...` | укуцајте `python -m heat3d_ext_wows` уместо `heat3d-wows-replay`; ради исто |
| `No module named heat3d_ext_wows` | нисте у фасцикли алатке, или она није инсталирана: `cd` до ње и покрените `pip install -e .` |
| `the following arguments are required: -o/--out` | додајте `-o out` команди |

Следеће: [Претварање реплеја](converting.md).
