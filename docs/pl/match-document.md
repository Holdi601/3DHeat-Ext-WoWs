---
title: Dokument meczu
nav_order: 6
lang: pl
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Dokument meczu {#the-match-document}

`<match>.match.json` zawiera wszystko, co replay mówi, a co nie jest wierszem
tabeli. Karta Mecz w przeglądarce czyta właśnie ten plik. (W kodzie nazywa się go podsumowaniem.)

![Początek syntetycznego dokumentu meczu i jego klucze](../assets/img/match-document.svg)

## Bitwa {#the-battle}

| Klucz | Co to jest |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; identyfikator bitwy; mapa tak, jak nazywa ją gra (`spaces/<map>`) i jej nazwa wyświetlana |
| `clientVersion`, `streamVersion` | wersja gry z nagłówka i taka, jaką podaje strumień pakietów |
| `recorded` | kiedy replay został nagrany, tak jak zapisuje to gra |
| `player`, `vehicle` | nagrywający gracz i jego okręt |
| `gameType`, `scenario` | typ bitwy (`RandomBattle`, ...) i scenariusz, z nagłówka |
| `duration` | limit czasu bitwy w sekundach, z nagłówka |
| `truncated` | nagrywanie zatrzymało się wcześniej |
| `battleStart`, `recordingSeconds` | początek bitwy (pierwsza chwila, w której rusza jakikolwiek okręt) i długość nagrania, w sekundach |
| `positionPacket`, `ownPositionPacket` | numery pakietów, w których przyszły pozycje: innych okrętów, nagrywającego gracza |
| `deathMethod` | numer metody, w której znaleziono zatonięcia |
| `hz`, `ownHz`, `positions` | próbki na sekundę innych okrętów i własnego okrętu; wiersze pozycji |
| `units` | jednostki świata (15 m wg kadłubów, 30 m wg zasięgów gry); x na wschód, y w górę, z na północ |
| `events` | liczba wierszy tabeli każdego zdarzenia |
| `decoded` | numery metod i pakietów znalezione dla każdego rodzaju komunikatu |

## Gracze i zdarzenia {#players-and-events}

| Klucz | Co to jest |
|---|---|
| `players` | jeden wpis na okręt: nazwa, `ally` lub `enemy`, numer i nazwa okrętu, obiekt, próbki, zabójstwa, przeżycie; `seen` (zadane i otrzymane obrażenia, pociski, torpedy i ostatnie zdrowie, jakie widział klient); `header` (wpis z listy graczy) i `record` (rekord gracza ze strumienia, wg numeru klucza) |
| `kills` | każde zatonięcie: czas, ofiara, zabójca, numer przyczyny, miejsce |
| `chat` | każda linia czatu, z kanałem i nadawcą |
| `damageStats` | własne statystyki nagrywającego gracza, tak jak prowadzi je gra: wg broni i rodzaju, liczba i kwota (rodzaj 0 to zadane obrażenia) |
| `avatarPickles` | każde zakodowane wywołanie do nagrywającego gracza, odczytane, wg numeru metody |

## Nagłówek, wyniki i sprawdzenia {#header-results-and-checks}

| Klucz | Co to jest |
|---|---|
| `header` | pierwszy blok JSON, w całości poza listą graczy: tryb gry, pogoda, granica mapy, wielkości drużyn i więcej |
| `moreBlocks` | bloki JSON po pierwszym, takie, jakie są |
| `blockIds` | 15.x: konto nagrywającego gracza i identyfikator bitwy, odczytane jako tekst |
| `results` | 15.x: wyniki, które te klienty trzymają w strumieniu |
| `entities` | każdy obiekt, który tworzy strumień: jego numer typu i rola, kiedy wszedł do widoku klienta i kiedy z niego wyszedł |
| `selfCheck` | licznik kompletności ([Kompletność](completeness.md)) oraz sprawdzenia obiektów, wyników, identyfikatorów i wersji |

---

Część [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacja](https://holdi601.github.io/3DHeat/)). Źródło: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
