---
title: Utrzymanie
nav_order: 99
lang: pl
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Utrzymanie dokumentacji {#maintaining-the-documentation}

Dla tego, kto wydaje nową wersję. Wykonuj kroki w tej kolejności.

1. **Wygeneruj ponownie strony z opisami** z kodu:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   To przepisuje [Opis poleceń](../cli-reference.md) i
   [Lista kolumn](../columns.md). Nigdy nie edytuj tych dwóch ręcznie.
2. **Wypisz, co się zmieniło od ostatniego wydania:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` to ostatnio wydana wersja (jeszcze bez tagu: cały
   `git log --oneline`). Każda nowa funkcja, opcja lub kolumna potrzebuje swojej strony
   i wiersza w sekcji **Docs** w
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Niezależny przegląd.** Ktoś, kto nie pisał stron (osoba albo agent), czyta README, każdą stronę
   i każdy obrazek jako trzech czytelników: początkującego, który nigdy nie używał terminala, ośmiolatka
   i profesjonalistę, który sprawdza każdą opcję, kolumnę i jednostkę względem kodu.
   Sprawdzają też diagramy względem kodu oraz to, czy żadna strona nie nazywa
   prawdziwej mapy, poziomu, gracza ani meczu i nie podaje liczb z prawdziwych replayów.
4. **Napraw to, co wykazał przegląd.** Potem uruchom krok 1 ponownie i narysuj na nowo
   obrazki, których wynik się zmienił.
5. **Tłumaczenia.** Każda strona w `docs/<language>/` zapisuje skrót (hash)
   angielskiej strony, z której została przetłumaczona. Przetłumacz ponownie każdą stronę, której
   angielskie źródło się zmieniło, łącznie z podpisami diagramów. Potem przejrzyj każdy język: czy jest
   jasny dla wszystkich trzech czytelników, czy etykiety są poprawne i czy używa tych samych słów
   co przeglądarka 3DHeat w tym języku.
6. **Wydanie:** podnieś `VERSION` i oznacz tag `v<VERSION>`. **Wysyłaj na serwer dopiero po zgodzie
   właściciela.**

## Tłumaczenia: polecenia {#translations-the-commands}

Strona jest tłumaczona na 40 języków przeglądarki 3DHeat: angielski w `docs/`, każdy inny język w
`docs/<lang>/` o tych samych nazwach plików. `tools/docs_i18n.py` prowadzi ewidencję:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Tłumacz tylko to, co wypisuje `todo`: zachowaj Markdown, linki, kod, nazwy plików i kolumn tak jak są,
tłumacz tytuły i opisy obrazków, a przyciski i panele przeglądarki nazywaj jej własnymi słowami
(z `src/i18n/locales/<lang>/`). Wygenerowane strony z opisami i obrazki z terminala zostają
po angielsku. Na stronie nieaktualne tłumaczenie to mówi i linkuje stronę angielską; brakujące
przechodzi na angielski. Menu języków w nagłówku i przekierowanie strony głównej wg języka przeglądarki
pochodzą z `docs/_includes/`.
