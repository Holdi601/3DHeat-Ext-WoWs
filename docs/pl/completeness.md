---
title: Kompletność
nav_order: 8
lang: pl
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Kompletność {#completeness}

Nic z replaya nie jest wyrzucane. To, co odczytuje konwerter, trafia do
tabeli i dokumentu meczu; każdy inny element jest zachowany w całości w pliku
towarzyszącym `<match>.messages.parquet`; a `selfCheck.completeness` w dokumencie
meczu liczy, co stało się z każdym rodzajem elementu. To zasada, którą dzielą wszystkie konwertery 3DHeat:
[Konwertery zachowują wszystko](https://holdi601.github.io/3DHeat/converters.html).

![Samosprawdzenie syntetycznego replaya: każdy element widziany, odczytany, zachowany lub stracony](../assets/img/completeness.svg)

## Liczniki {#the-count}

Dla każdego rodzaju elementu `selfCheck.completeness.types` podaje:

| Licznik | Znaczy |
|---|---|
| `seen` | ile replay zawiera |
| `decoded` | odczytane w całości |
| `partial` | odczytane częściowo i zachowane w całości w pliku towarzyszącym |
| `raw` | tylko zachowane w całości w pliku towarzyszącym, nieodczytane |
| `lost` | stracone: zawsze `0` |

Rodzaje są własne dla replaya: `block <n>` (bloki JSON), własne bajty
kontenera, `packet <type>`, a dla wywołań obiektów `method <entity type>.<number>`
i `property <entity type>.<number>`.
`selfCheck.entities.roles` mówi, który typ obiektu to awatar nagrywającego gracza,
a który okręty. Rodzaj, o którym nikt nie wiedział, pojawia się z własnym licznikiem.

## Plik towarzyszący {#the-sidecar}

| Kolumna | Co to jest |
|---|---|
| `time` | zegar replaya, jak w tabeli |
| `type`, `name` | rodzaj elementu; jak nazywa go konwerter, tam gdzie go czyta |
| `entity` | okręt albo awatar, do którego należy, jak `entity` w tabeli |
| `decoded` | co z niego odczytano, jako JSON |
| `payload`, `text` | jego bajty w całości; bloki JSON w całości |
| `entityType`, `packet`, `method` | liczby |

Wiersze są posortowane wg pakietu, metody, obiektu i czasu. Który obiekt to który
gracz: `entities` i `players` w dokumencie meczu.

## Co jest odczytywane i jak to sprawdzono {#what-is-read-and-how-it-was-checked}

- **Wyniki** (15.x, `results`): ich identyfikator bitwy jest taki jak w strumieniu, a
  każdy gracz w nich jest na liście graczy z nagłówka.
- **Blok identyfikatorów** (15.x, `blockIds`): konto i bitwa, odczytane jako tekst,
  więc żadna cyfra się nie gubi.
- **Pochylenie i przechył** każdej pozycji: przechył idzie z szybkością skrętu,
  bo okręt przechyla się w zakręcie; pochylenie jest prawie zawsze 0.
- **Obiekty** (`entities`): kiedy każdy wszedł do widoku klienta i kiedy z niego wyszedł.
  Żaden okręt nie ma pozycji między wyjściem a powrotem.
- **Wersja w strumieniu** (`streamVersion`): taka sama jak w nagłówku.

Wszystko inne odczytane (zatopienia, obrażenia, zdrowie, pociski, torpedy, miejsca,
w których zakończyły lot pociski, czat, zakodowane wywołania, rekordy graczy, pozycje) jest
`partial`: w tabeli lub dokumencie meczu, a w całości w pliku towarzyszącym.

**Zachowane, ale nieodczytane** (`raw`), największe rodzaje: aktualizacje pozycji, których nie ma w tabeli (po zatonięciu okrętu, obiekty bez gracza),
częste właściwości i metody bez czytnika, właściwości tworzenia obiektów
oraz każdy inny pakiet bez czytnika.

## Niedostępne {#not-available}

- To, czego serwer nigdy nie wysłał nagrywającemu klientowi: celowanie innych graczy,
  kamera i sterowanie, wrogowie, dopóki nie zostali wypatrzeni. Replay to to, co jeden klient
  został poinformowany.
- Nazwy typów obiektów, metod, właściwości i kluczy statystyk: są w plikach definicji gry,
  a nie w replayu. Liczby są zachowane.
- Nazwy okrętów dla numerów okrętów (użyj `--ship-names`) oraz wszystko inne,
  co wymaga plików własnych gry.
- Wyniki klientów sprzed 15.x: nie ma ich w ich replayach.

---

Część [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacja](https://holdi601.github.io/3DHeat/)). Źródło: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
