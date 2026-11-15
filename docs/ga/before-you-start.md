---
title: Sula dtosaíonn tú
nav_order: 2
lang: "ga"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Sula dtosaíonn tú {#before-you-start}

Nua leis an líne ordaithe? Tógann an leathanach seo thú ó rud ar bith go dtí `heat3d-wows-replay` atá ag obair, i gceann deich nóiméad nó mar sin. Má úsáideann tú Python cheana, téigh díreach go [Suiteáil](installing.md).

## 1. Suiteáil Python {#install-python}

1. Íoslódáil Python **3.10 nó níos déanaí** ó [python.org/downloads](https://www.python.org/downloads/).
2. Ar Windows, cuir tic i **Add python.exe to PATH** i gcéad fhuinneog an suiteálaí, ansin cliceáil **Install Now**.
3. Ar macOS agus Linux, bíonn Python 3 ann go minic cheana. Clóscríobh `python3` san áit a ndeir na leathanaigh seo `python`, agus `pip3` in ionad `pip`.

## 2. Oscail teirminéal {#open-a-terminal}

Is fuinneog é teirminéal inar clóscríobhann tú orduithe.

- **Windows:** oscail an fillteán in File Explorer, cliceáil ar an mbarra seoltaí, clóscríobh `cmd` agus brúigh Enter. Osclaíonn fuinneog atá sa fhillteán sin cheana.
- **macOS:** oscail an app **Terminal**. **Linux:** cliceáil ar dheis sa fhillteán agus roghnaigh **Open in Terminal**.

Chun dul go fillteán eile, clóscríobh `cd` agus an fillteán:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Seiceáil go n-oibríonn Python {#check-that-python-works}

```bash
python --version
```

Ba cheart duit `Python 3.` a fheiceáil agus uimhir 10 nó níos mó, mar shampla `Python 3.12.4`.

## 4. Faigh an uirlis agus suiteáil í {#get-the-tool-and-install-it}

1. Ar [leathanach GitHub na huirlise](https://github.com/Holdi601/3DHeat-Ext-WoWs), cliceáil ar an gcnaipe glas **Code**, ansin **Download ZIP**, agus díphacáil an zip.
2. Oscail teirminéal sa fhillteán díphacáilte (an ceann a bhfuil `README.md` ann).
3. Clóscríobh:

   ```bash
   pip install -e .
   ```

   Ba cheart duit a fheiceáil ag an deireadh: `Successfully installed heat3d-ext-wows-0.1.0` (b'fhéidir le tuilleadh ainmneacha).
4. Seiceáil é:

   ```bash
   heat3d-wows-replay --version
   ```

   Ba cheart duit a fheiceáil: `heat3d-wows-replay 0.1.0`

## Conas na horduithe ar na leathanaigh seo a léamh {#how-to-read-the-commands-on-these-pages}

- Is áitchoinneálaithe iad focail idir lúibíní uillinneacha, mar `<replays>`: clóscríobh do chomhad nó d'fhillteán féin ansin, gan na lúibíní.
- Teastaíonn comharthaí athfhriotail ó chonair a bhfuil spásanna inti: `"C:\Program Files (x86)\Steam"`.
- Is nóta é an téacs i ndiaidh `#`: ní chlóscríobhann tú é.
- Scríobhann `-o out` isteach i bhfillteán darb ainm `out` laistigh den fhillteán a bhfuil do theirminéal ann. Déantar é mura bhfuil sé ann.

## Cén chuma atá ar rath {#what-success-looks-like}

Priontálann an t-ordú líne amháin do gach athsheinm, mar shampla:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

agus críochnaíonn sé le stádas scoir `0`. Tá na comhaid nua san fhillteán `out`.

## Earráidí coitianta {#common-errors}

| Cad a fheiceann tú | Cad atá le déanamh |
|---|---|
| `'python' is not recognized ...` nó `command not found` | Níl Python ar an PATH: suiteáil arís é agus tic i **Add python.exe to PATH**, nó clóscríobh `py` in ionad `python` (Windows) |
| `'pip' is not recognized ...` | clóscríobh `python -m pip install -e .` ina áit |
| `'heat3d-wows-replay' is not recognized ...` | clóscríobh `python -m heat3d_ext_wows` in ionad `heat3d-wows-replay`; déanann sé an rud céanna |
| `No module named heat3d_ext_wows` | níl tú i bhfillteán na huirlise, nó níl sí suiteáilte: déan `cd` ann agus rith `pip install -e .` |
| `the following arguments are required: -o/--out` | cuir `-o out` leis an ordú |

Ar aghaidh: [Athsheinmeanna a thiontú](converting.md).
