---
title: "Перш ніж почати"
nav_order: 2
lang: uk
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Перш ніж почати {#before-you-start}

Ви ще не працювали з командним рядком? Ця сторінка проведе вас від нуля до
робочого `heat3d-wows-replay` приблизно за десять хвилин. Якщо ви вже користуєтеся
Python, одразу переходьте до [Встановлення](installing.md).

## 1. Встановіть Python {#install-python}

1. Завантажте Python **3.10 або новішої** версії з
   [python.org/downloads](https://www.python.org/downloads/).
2. У Windows у першому вікні інсталятора поставте позначку **Add python.exe to PATH**,
   потім натисніть **Install Now**.
3. У macOS і Linux Python 3 часто вже є. Там, де ці сторінки пишуть `python`,
   вводьте `python3`, а замість `pip` — `pip3`.

## 2. Відкрийте термінал {#open-a-terminal}

Термінал — це вікно, в яке ви вводите команди.

- **Windows:** відкрийте папку в Провіднику, клацніть рядок адреси, введіть
  `cmd` і натисніть Enter. Відкриється вікно, яке вже стоїть у цій папці.
- **macOS:** відкрийте програму **Terminal**. **Linux:** клацніть правою кнопкою
  миші в папці і виберіть **Open in Terminal**.

Щоб перейти в іншу папку, введіть `cd` і назву папки:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Перевірте, що Python працює {#check-that-python-works}

```bash
python --version
```

Ви маєте побачити `Python 3.` і номер 10 або більше, наприклад
`Python 3.12.4`.

## 4. Отримайте інструмент і встановіть його {#get-the-tool-and-install-it}

1. На [сторінці інструмента на GitHub](https://github.com/Holdi601/3DHeat-Ext-WoWs)
   натисніть зелену кнопку **Code**, потім **Download ZIP**, і розпакуйте архів.
2. Відкрийте термінал у розпакованій папці (тій, де лежить `README.md`).
3. Введіть:

   ```bash
   pip install -e .
   ```

   Наприкінці ви маєте побачити: `Successfully installed heat3d-ext-wows-0.1.0`
   (можливо, з більшою кількістю назв).
4. Перевірте:

   ```bash
   heat3d-wows-replay --version
   ```

   Ви маєте побачити: `heat3d-wows-replay 0.1.0`

## Як читати команди на цих сторінках {#how-to-read-the-commands-on-these-pages}

- Слова в кутових дужках, як `<replays>`, — це місця для вашого власного файлу
  або папки: введіть туди своє, без дужок.
- Шлях із пробілами потребує лапок: `"C:\Program Files (x86)\Steam"`.
- Текст після `#` — коментар: його не потрібно вводити.
- `-o out` записує в папку `out`, яка лежить у папці, де відкрито ваш термінал.
  Її буде створено, якщо її немає.

## Як виглядає успіх {#what-success-looks-like}

Команда виводить по одному рядку на повтор, наприклад:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

і завершується зі статусом `0`. Нові файли лежать у папці `out`.

## Типові помилки {#common-errors}

| Ви бачите | Що зробити |
|---|---|
| `'python' is not recognized ...` або `command not found` | Python не додано до PATH: встановіть його ще раз з позначкою **Add python.exe to PATH** або введіть `py` замість `python` (Windows) |
| `'pip' is not recognized ...` | замість цього введіть `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | замість `heat3d-wows-replay` введіть `python -m heat3d_ext_wows`; це робить те саме |
| `No module named heat3d_ext_wows` | ви не в папці інструмента або його не встановлено: перейдіть туди через `cd` і виконайте `pip install -e .` |
| `the following arguments are required: -o/--out` | додайте до команди `-o out` |

Далі: [Перетворення повторів](converting.md).
