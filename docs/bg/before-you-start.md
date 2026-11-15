---
title: Преди да започнете
nav_order: 2
lang: bg
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Преди да започнете {#before-you-start}

Нов ли сте в командния ред? Тази страница ви води от нулата до работещ
`heat3d-wows-replay` за около десет минути. Ако вече използвате Python, отидете направо на
[Инсталиране](installing.md).

## 1. Инсталирайте Python {#install-python}

1. Изтеглете Python **3.10 или по-нов** от
   [python.org/downloads](https://www.python.org/downloads/).
2. На Windows отметнете **Add python.exe to PATH** в първия прозорец на
   инсталатора, после натиснете **Install Now**.
3. На macOS и Linux Python 3 често е вече инсталиран. Напишете `python3` там, където
   страниците казват `python`, и `pip3` вместо `pip`.

## 2. Отворете терминал {#open-a-terminal}

Терминалът е прозорец, в който въвеждате команди.

- **Windows:** отворете папката в File Explorer, кликнете на адресната лента, напишете
  `cmd` и натиснете Enter. Отваря се прозорец, вече в тази папка.
- **macOS:** отворете приложението **Terminal**. **Linux:** щракнете с десния бутон в
  папката и изберете **Open in Terminal**.

За да отидете в друга папка, напишете `cd` и папката:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Проверете дали Python работи {#check-that-python-works}

```bash
python --version
```

Трябва да видите `Python 3.` и номер 10 или по-голям, например
`Python 3.12.4`.

## 4. Вземете инструмента и го инсталирайте {#get-the-tool-and-install-it}

1. На [GitHub страницата на инструмента](https://github.com/Holdi601/3DHeat-Ext-WoWs) натиснете
   зеления бутон **Code**, после **Download ZIP**, и разархивирайте файла.
2. Отворете терминал в разархивираната папка (тази, в която има `README.md`).
3. Въведете:

   ```bash
   pip install -e .
   ```

   В края трябва да видите: `Successfully installed heat3d-ext-wows-0.1.0`
   (може да има и още имена).
4. Проверете го:

   ```bash
   heat3d-wows-replay --version
   ```

   Трябва да видите: `heat3d-wows-replay 0.1.0`

## Как да четете командите на тези страници {#how-to-read-the-commands-on-these-pages}

- Думите в ъглови скоби, като `<replays>`, са местодържатели: напишете вашия собствен
  файл или папка на тяхно място, без скобите.
- Път с интервали трябва да е в кавички: `"C:\Program Files (x86)\Steam"`.
- Текстът след `#` е коментар: не го въвеждате.
- `-o out` записва в папка `out` вътре в папката, в която е вашият терминал.
  Тя се създава, ако я няма.

## Как изглежда успехът {#what-success-looks-like}

Командата извежда по един ред за всяко повторение, например:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

и завършва с код на изход `0`. Новите файлове са в папката `out`.

## Чести грешки {#common-errors}

| Какво виждате | Какво да направите |
|---|---|
| `'python' is not recognized ...` или `command not found` | Python не е в PATH: инсталирайте го отново с отметнато **Add python.exe to PATH**, или напишете `py` вместо `python` (Windows) |
| `'pip' is not recognized ...` | напишете вместо това `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | напишете `python -m heat3d_ext_wows` вместо `heat3d-wows-replay`; прави същото |
| `No module named heat3d_ext_wows` | не сте в папката на инструмента или той не е инсталиран: `cd` до там и изпълнете `pip install -e .` |
| `the following arguments are required: -o/--out` | добавете `-o out` към командата |

Следва: [Преобразуване на повторенията](converting.md).
