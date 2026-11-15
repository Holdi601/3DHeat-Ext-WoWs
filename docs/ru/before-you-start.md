---
title: Перед началом
nav_order: 2
lang: "ru"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Перед началом {#before-you-start}

Впервые работаете с командной строкой? Эта страница проведёт вас от нуля до работающей
команды `heat3d-wows-replay` примерно за десять минут. Если Python вы уже используете,
сразу переходите к [Установке](installing.md).

## 1. Установите Python {#install-python}

1. Скачайте Python **3.10 или новее** со страницы
   [python.org/downloads](https://www.python.org/downloads/).
2. В Windows в первом окне установщика поставьте галочку **Add python.exe to PATH**,
   затем нажмите **Install Now**.
3. В macOS и Linux Python 3 часто уже установлен. Там, где на этих страницах написано
   `python`, вводите `python3`, а вместо `pip` — `pip3`.

## 2. Откройте терминал {#open-a-terminal}

Терминал — это окно, в котором вы вводите команды.

- **Windows:** откройте папку в проводнике, щёлкните по адресной строке, введите `cmd`
  и нажмите Enter. Откроется окно, уже находящееся в этой папке.
- **macOS:** откройте приложение **Terminal** (Терминал). **Linux:** щёлкните правой
  кнопкой мыши в папке и выберите **Open in Terminal**.

Чтобы перейти в другую папку, введите `cd` и путь к ней:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Проверьте, что Python работает {#check-that-python-works}

```bash
python --version
```

Вы должны увидеть `Python 3.` и номер 10 или выше, например `Python 3.12.4`.

## 4. Скачайте инструмент и установите его {#get-the-tool-and-install-it}

1. На [странице инструмента на GitHub](https://github.com/Holdi601/3DHeat-Ext-WoWs) нажмите
   зелёную кнопку **Code**, затем **Download ZIP**, и распакуйте архив.
2. Откройте терминал в распакованной папке (той, в которой лежит `README.md`).
3. Введите:

   ```bash
   pip install -e .
   ```

   В конце вы должны увидеть: `Successfully installed heat3d-ext-wows-0.1.0`
   (возможно, с другими названиями).
4. Проверьте установку:

   ```bash
   heat3d-wows-replay --version
   ```

   Вы должны увидеть: `heat3d-wows-replay 0.1.0`

## Как читать команды на этих страницах {#how-to-read-the-commands-on-these-pages}

- Слова в угловых скобках, например `<replays>`, — это места для подстановки: вместо них
  введите свой файл или папку, без скобок.
- Путь с пробелами нужно взять в кавычки: `"C:\Program Files (x86)\Steam"`.
- Текст после `#` — это комментарий: его вводить не нужно.
- `-o out` записывает результат в папку с именем `out` внутри папки, в которой открыт ваш
  терминал. Если её нет, она будет создана.

## Как понять, что всё получилось {#what-success-looks-like}

Команда выводит одну строку на каждый реплей, например:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

и завершается с кодом `0`. Новые файлы лежат в папке `out`.

## Частые ошибки {#common-errors}

| Что вы видите | Что делать |
|---|---|
| `'python' is not recognized ...` или `command not found` | Python не добавлен в PATH: установите его заново с включённой галочкой **Add python.exe to PATH** или введите `py` вместо `python` (Windows) |
| `'pip' is not recognized ...` | введите вместо этого `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | введите `python -m heat3d_ext_wows` вместо `heat3d-wows-replay`; это то же самое |
| `No module named heat3d_ext_wows` | вы не в папке инструмента или он не установлен: перейдите туда командой `cd` и выполните `pip install -e .` |
| `the following arguments are required: -o/--out` | добавьте в команду `-o out` |

Дальше: [Преобразование реплеев](converting.md).
