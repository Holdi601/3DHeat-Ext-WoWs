---
title: "Суправаджэнне"
nav_order: 99
lang: be
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Суправаджэнне дакументацыі {#maintaining-the-documentation}

Для таго, хто выпускае новую версію. Рабіце крокі ў гэтым парадку.

1. **Нанава стварыце даведачныя старонкі** з кода:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   Гэта перапісвае [Даведнік каманд](../cli-reference.md) і
   [Спіс слупкоў](../columns.md). Ніколі не правце гэтыя дзве старонкі ўручную.
2. **Пералічыце, што змянілася з апошняга рэлізу:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` - апошняя выпушчаная версія (тэга яшчэ няма: увесь
   `git log --oneline`). Кожная новая магчымасць, параметр або слупок
   патрабуе сваёй старонкі і радка ў раздзеле **Docs**
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Незалежны агляд.** Той, хто не пісаў старонкі (чалавек або агент),
   чытае README, кожную старонку і кожны малюнак як трое чытачоў: новічок, які
   ніколі не карыстаўся тэрміналам, васьмігадовае дзіця і прафесіянал, які
   правярае кожны параметр, слупок і адзінку па кодзе. Яны таксама правяраюць
   схемы па кодзе і тое, што ніводная старонка не называе сапраўдную карту,
   узровень, гульца або матч і не прыводзіць лікаў з сапраўдных запісаў.
4. **Выпраўце тое, што знайшоў агляд.** Потым зноў выканайце крок 1 і
   перамалюйце малюнкі, чый вывад змяніўся.
5. **Пераклады.** Кожная старонка ў `docs/<language>/` запамінае хэш
   англійскай старонкі, з якой яна перакладзена. Перакладзіце нанава кожную
   старонку, чый англійскі зыходнік змяніўся, уключна з подпісамі схем. Потым
   праглядзіце кожную мову: зразумела для ўсіх трох чытачоў, подпісы правільныя
   і тыя ж словы, што выкарыстоўвае праглядальнік 3DHeat на гэтай мове.
6. **Рэліз:** павысьце `VERSION` і паставьце тэг `v<VERSION>`. **Пушце толькі
   пасля дазволу ўладальніка.**

## Пераклады: каманды {#translations-the-commands}

Сайт перакладзены на 40 моў праглядальніка 3DHeat: англійская ў `docs/`, кожная
іншая мова ў `docs/<lang>/` з тымі ж назвамі файлаў. `tools/docs_i18n.py` вядзе ўлік:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Перакладайце толькі тое, што пералічвае `todo`: Markdown, спасылкі, код, назвы файлаў і слупкоў
пакідайце як ёсць, перакладайце загалоўкі і апісанні малюнкаў і выкарыстоўвайце ўласныя словы
праглядальніка 3DHeat для яго кнопак і панэляў (яго `src/i18n/locales/<lang>/`). Створаныя
даведачныя старонкі і малюнкі тэрмінала застаюцца англійскімі. На сайце састарэлы пераклад кажа
пра гэта і спасылаецца на англійскую старонку; адсутны вяртаецца да англійскай. Меню мовы ў
загалоўку і перанакіраванне галоўнай старонкі па мове браўзера ідуць з `docs/_includes/`.
