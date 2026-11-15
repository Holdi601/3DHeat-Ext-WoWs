---
title: Сопровождение документации
nav_order: 99
lang: ru
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Сопровождение документации {#maintaining-the-documentation}

Для того, кто выпускает новую версию. Выполняйте шаги в этом порядке.

1. **Пересоздайте справочные страницы** из кода:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   Эта команда перезаписывает [Справку по командам](../cli-reference.md) и
   [Список столбцов](../columns.md). Эти две страницы никогда не редактируйте вручную.
2. **Посмотрите, что изменилось со времени последнего релиза:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` — последняя выпущенная версия (если тега ещё нет: весь `git log --oneline`).
   Каждой новой функции, параметру или столбцу нужны своя страница и строка в разделе **Docs**
   файла [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Независимая проверка.** Кто-то, кто не писал страницы (человек или агент), читает README,
   каждую страницу и каждую картинку тремя читателями: новичком, который никогда не пользовался
   терминалом, восьмилетним ребёнком и профессионалом, который сверяет каждый параметр, столбец и
   единицу измерения с кодом. Они также сверяют схемы с кодом и проверяют, что ни на одной странице
   не назван настоящая карта, уровень, игрок или матч и что нет цифр из настоящих реплеев.
4. **Исправьте то, что нашла проверка.** Затем снова выполните шаг 1 и перерисуйте картинки, вывод
   которых изменился.
5. **Переводы.** Каждая страница в `docs/<language>/` хранит хеш английской страницы, с которой она
   переведена. Заново переведите каждую страницу, у которой изменился английский исходник, включая
   подписи на схемах. Затем проверьте каждый язык: понятно ли всем трём читателям, верны ли подписи и
   те же ли слова, что использует просмотрщик 3DHeat на этом языке.
6. **Выпуск:** поднимите `VERSION` и поставьте тег `v<VERSION>`. **Отправляйте только с разрешения
   владельца.**

## Переводы: команды {#translations-the-commands}

Сайт переведён на 40 языков просмотрщика 3DHeat: английский — в `docs/`, каждый другой язык — в
`docs/<lang>/` с теми же именами файлов. `tools/docs_i18n.py` ведёт учёт:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Переводите только то, что показывает `todo`: разметку, ссылки, код, имена файлов и столбцов
оставляйте как есть, переводите заголовки и описания картинок, а для кнопок и панелей просмотрщика
используйте его собственные слова (его `src/i18n/locales/<lang>/`). Справочные страницы, созданные из
кода, и картинки с терминалом остаются на английском. На сайте устаревший перевод об этом сообщает и
ведёт на английскую страницу; если перевода нет, открывается английская. Меню языков в шапке и
перенаправление домашней страницы по языку браузера берутся из `docs/_includes/`.
