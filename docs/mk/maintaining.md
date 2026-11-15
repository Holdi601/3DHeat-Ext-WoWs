---
title: "Одржување"
nav_order: 99
lang: mk
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Одржување на документацијата {#maintaining-the-documentation}

За оној што објавува нова верзија. Направете ги чекорите по овој редослед.

1. **Регенерирајте ги референтните страници** од кодот:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   Ова ги препишува [Упатство за команди](../cli-reference.md) и [Список на колони](../columns.md). Никогаш не ги уредувајте тие две рачно.
2. **Наведете што се променило од последното издание:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` е последната објавена верзија (нема таг уште: целиот `git log --oneline`). Секоја нова функција, опција или колона бара своја страница и ред во делот **Docs** на [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Независен преглед.** Некој што не ги напишал страниците (човек или агент) ги чита README, секоја страница и секоја слика како три читатели: почетник што никогаш не користел терминал, осумгодишно дете и професионалец што ја проверува секоја опција, колона и единица наспроти кодот. Исто така ги проверуваат дијаграмите наспроти кодот, и дека ниту една страница не именува вистинска мапа, ниво, играч или меч, ниту дава бројки од вистински снимки.
4. **Поправете што пронашол прегледот.** Потоа пуштете го чекор 1 повторно и пребојте ги сликите чиј излез се променил.
5. **Преводи.** Секоја страница под `docs/<language>/` го запишува хешот на англиската страница од која е преведена. Преведете повторно секоја страница чиј англиски извор се променил, вклучувајќи ги ознаките на дијаграмите. Потоа прегледајте го секој јазик: јасно за сите три читатели, ознаките точни, и истите зборови што ги користи 3DHeat прегледувачот на тој јазик.
6. **Издание:** подигнете го `VERSION` и таг `v<VERSION>`. **Објавете дури по одобрение од сопственикот.**

## Преводи: командите {#translations-the-commands}

Страницата е преведена на 40-те јазика на 3DHeat прегледувачот: англиски во `docs/`, секој друг јазик во `docs/<lang>/` со исти имиња на датотеки. `tools/docs_i18n.py` води сметка:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Преведувајте само што наведува `todo`: оставете ги Markdown, врските, кодот, имињата на датотеки и колони како што се, преведете ги насловите и описите на сликите, и користете ги сопствените зборови на 3DHeat прегледувачот за неговите копчиња и панели (неговиот `src/i18n/locales/<lang>/`). Генерираните референтни страници и сликите од терминал остануваат на англиски. На страницата, застарен превод го кажува тоа и врзува кон англиската страница; недостасувачки се враќа на англиски. Менито за јазици во заглавието и пренасочувањето на почетната страница според јазикот на прелистувачот доаѓаат од `docs/_includes/`.
