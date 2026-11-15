---
title: "Пред да започнете"
nav_order: 2
lang: "mk"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Пред да започнете {#before-you-start}

Нови сте со командната линија? Оваа страница ве води од ништо до работен `heat3d-wows-replay` за околу десет минути. Ако веќе користите Python, одете директно на [Инсталирање](installing.md).

## 1. Инсталирајте Python {#install-python}

1. Преземете Python **3.10 или понов** од [python.org/downloads](https://www.python.org/downloads/).
2. На Windows, штиклирајте **Add python.exe to PATH** во првиот прозорец на инсталерот, па кликнете **Install Now**.
3. На macOS и Linux, Python 3 често веќе е инсталиран. Пишувајте `python3` секаде каде што овие страници кажуваат `python`, и `pip3` наместо `pip`.

## 2. Отворете терминал {#open-a-terminal}

Терминалот е прозорец во кој пишувате команди.

- **Windows:** отворете ја папката во File Explorer, кликнете на адресната лента, напишете `cmd` и притиснете Enter. Се отвора прозорец веќе во таа папка.
- **macOS:** отворете ја апликацијата **Terminal**. **Linux:** кликнете десно во папката и изберете **Open in Terminal**.

За да одите во друга папка, напишете `cd` и папката:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Проверете дали Python работи {#check-that-python-works}

```bash
python --version
```

Треба да видите `Python 3.` и број 10 или повеќе, на пример `Python 3.12.4`.

## 4. Земете ја алатката и инсталирајте ја {#get-the-tool-and-install-it}

1. На [GitHub страницата на алатката](https://github.com/Holdi601/3DHeat-Ext-WoWs) кликнете на зеленото копче **Code**, па **Download ZIP**, и распакувајте го zip-от.
2. Отворете терминал во распакуваната папка (онаа во која е `README.md`).
3. Напишете:

   ```bash
   pip install -e .
   ```

   На крајот треба да видите: `Successfully installed heat3d-ext-wows-0.1.0` (можеби со повеќе имиња).
4. Проверете:

   ```bash
   heat3d-wows-replay --version
   ```

   Треба да видите: `heat3d-wows-replay 0.1.0`

## Како да ги читате командите на овие страници {#how-to-read-the-commands-on-these-pages}

- Зборовите во аголни загради, како `<replays>`, се места за пополнување: впишете своја датотека или папка таму, без заградите.
- Патека со празни места бара наводници: `"C:\Program Files (x86)\Steam"`.
- Текстот по `#` е коментар: не го пишувате.
- `-o out` пишува во папка наречена `out` внатре во папката во која е вашиот терминал. Се создава ако ја нема.

## Како изгледа успехот {#what-success-looks-like}

Командата печати по една линија за секоја снимка, на пример:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

и завршува со излезен статус `0`. Новите датотеки се во папката `out`.

## Чести грешки {#common-errors}

| Што гледате | Што да направите |
|---|---|
| `'python' is not recognized ...` или `command not found` | Python не е во PATH: инсталирајте го повторно со штиклирано **Add python.exe to PATH**, или напишете `py` наместо `python` (Windows) |
| `'pip' is not recognized ...` | напишете `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | напишете `python -m heat3d_ext_wows` наместо `heat3d-wows-replay`; прави исто |
| `No module named heat3d_ext_wows` | не сте во папката на алатката, или не е инсталирана: направете `cd` таму и пуштете `pip install -e .` |
| `the following arguments are required: -o/--out` | додајте `-o out` на командата |

Следно: [Претворање на снимки](converting.md).
