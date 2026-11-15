---
title: "Перад пачаткам"
nav_order: 2
lang: be
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Перад пачаткам {#before-you-start}

Вы новічок у камандным радку? Гэтая старонка правядзе вас ад нуля да
працоўнага `heat3d-wows-replay` прыкладна за дзесяць хвілін. Калі вы ўжо
карыстаецеся Python, адразу ідзіце да [Усталёўкі](installing.md).

## 1. Усталюйце Python {#install-python}

1. Спампуйце Python **3.10 або навейшы** на
   [python.org/downloads](https://www.python.org/downloads/).
2. У Windows у першым акне ўсталёўшчыка адзначце **Add python.exe to PATH**,
   потым націсніце **Install Now**.
3. У macOS і Linux Python 3 часта ўжо ёсць. Там, дзе на гэтых старонках
   напісана `python`, уводзьце `python3`, а замест `pip` - `pip3`.

## 2. Адкрыйце тэрмінал {#open-a-terminal}

Тэрмінал - гэта акно, у якім уводзяць каманды.

- **Windows:** адкрыйце папку ў Правадыру, пстрыкніце ў адрасным радку,
  увядзіце `cmd` і націсніце Enter. Адкрыецца акно, якое адразу знаходзіцца ў
  гэтай папцы.
- **macOS:** адкрыйце праграму **Terminal**. **Linux:** пстрыкніце ў папцы
  правай кнопкай і абярыце **Open in Terminal**.

Каб перайсці ў іншую папку, увядзіце `cd` і папку:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Праверце, што Python працуе {#check-that-python-works}

```bash
python --version
```

Вы павінны ўбачыць `Python 3.` і лік 10 або болей, напрыклад
`Python 3.12.4`.

## 4. Атрымайце інструмент і ўсталюйце яго {#get-the-tool-and-install-it}

1. На [старонцы інструмента ў GitHub](https://github.com/Holdi601/3DHeat-Ext-WoWs)
   націсніце зялёную кнопку **Code**, потым **Download ZIP** і распакуйце
   архіў.
2. Адкрыйце тэрмінал у распакаванай папцы (у той, дзе ёсць `README.md`).
3. Увядзіце:

   ```bash
   pip install -e .
   ```

   У канцы вы павінны ўбачыць: `Successfully installed heat3d-ext-wows-0.1.0`
   (магчыма, з большай колькасцю імёнаў).
4. Праверце:

   ```bash
   heat3d-wows-replay --version
   ```

   Вы павінны ўбачыць: `heat3d-wows-replay 0.1.0`

## Як чытаць каманды на гэтых старонках {#how-to-read-the-commands-on-these-pages}

- Словы ў вуглавых дужках, як `<replays>`, - гэта запаўняльнікі: уводзьце
  туды свой файл або папку, без дужак.
- Шлях з прабеламі патрабуе двукоссяў: `"C:\Program Files (x86)\Steam"`.
- Тэкст пасля `#` - каментарый: яго не ўводзяць.
- `-o out` піша ў папку з назвай `out` усярэдзіне папкі, у якой знаходзіцца
  ваш тэрмінал. Калі яе няма, яна ствараецца.

## Як выглядае поспех {#what-success-looks-like}

Каманда выводзіць па адным радку на кожны запіс, напрыклад:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

і завяршаецца са статусам выхаду `0`. Новыя файлы ляжаць у папцы `out`.

## Частыя памылкі {#common-errors}

| Што вы бачыце | Што рабіць |
|---|---|
| `'python' is not recognized ...` або `command not found` | Python няма ў PATH: усталюйце яго зноў з адзнакай **Add python.exe to PATH** або ўвядзіце `py` замест `python` (Windows) |
| `'pip' is not recognized ...` | увядзіце замест гэтага `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | увядзіце `python -m heat3d_ext_wows` замест `heat3d-wows-replay`; гэта робіць тое ж самае |
| `No module named heat3d_ext_wows` | вы не ў папцы інструмента, або ён не ўсталяваны: перайдзіце туды праз `cd` і выканайце `pip install -e .` |
| `the following arguments are required: -o/--out` | дадайце `-o out` да каманды |

Далей: [Канвертаванне запісаў](converting.md).
