---
title: Jak czytany jest replay
nav_order: 7
lang: pl
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Jak czytany jest replay {#how-it-reads-a-replay}

Replay to nagłówek z bloków JSON i strumień pakietów gry (uwagi o formacie w
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Pierwszy blok, jawnie: mapa, wersja klienta, nagrywający gracz i jego okręt oraz lista graczy – nazwa każdego gracza, sojusznik lub wróg,
  i numer okrętu. Nowsze klienty (15.x) dodają dwa bloki więcej: pusty oraz
  konto nagrywającego gracza i identyfikator bitwy jako tekst, odczytane do
  `blockIds`. Wyniki nie są w JSON; 15.x trzyma je w strumieniu.
- Strumień pakietów, skompresowany zlib i zaszyfrowany Blowfishem kluczem, który dołącza gra,
  a który narzędzia społeczności czytające te pliki opublikowały. Po odszyfrowaniu
  zawiera:
  - aktualizacje pozycji silnika każdego okrętu, jaki klient mógł zobaczyć (własna drużyna
    przez cały czas, wrogowie, gdy byli wypatrzeni lub w pobliżu), kilka razy na
    sekundę, gdy się poruszają, i rzadziej, gdy stoją;
  - własny okręt nagrywającego gracza w osobnym pakiecie, około siedem razy na sekundę;
  - raz, na początku, rekordy graczy jako lista Pythona zapisana pickle. Mówią one, który obiekt w strumieniu
    to który gracz. Ich klucze są ponumerowane, a numery zmieniają się wraz z łatami, więc czytnik znajduje klucze
    po ich wartościach: klucz trzymający nazwy z listy graczy i klucz trzymający
    obiekty, które mają aktualizacje pozycji;
  - wywołanie serwera, które mówi klientowi, że okręt zatonął: ofiara, zabójca,
    przyczyna. Znajduje się je po kształcie (dwanaście bajtów; dwa pierwsze to obiekty okrętów; każda ofiara pojawia się raz),
    a nie po numerze;
  - obrażenia każdego okrętu: tablica (atakujący, obrażenia) na każde trafienie w trafiony okręt; oraz jego zdrowie, właściwość ustawiana chwilę wcześniej;
  - każdą salwę pocisków i torped, o jakich klient został poinformowany: typ pocisku, strzelec, salwa oraz początek i prędkość każdego pocisku lub torpedy;
  - miejsca, w których zakończyły lot pociski: strzelec, rodzaj trafienia i miejsce każdego (u klientów 15.x z dodatkowymi danymi o pocisku w miejscu uderzenia, które są pomijane);
  - czat: nadawca, kanał, linia;
  - wywołania pickle do nagrywającego gracza: jego statystyki obrażeń, aktualizacje
    rekordów graczy, stan bitwy;
  - u klientów 15.x wyniki bitwy na końcu: osobny pakiet, obiekt JSON z identyfikatorem bitwy, odczytany w całości do
    `results` dokumentu meczu (listy gry, bez nazw: `commonList`,
    `privateDataList`, `playersPublicInfo` na konto, ...).

Numery pakietów i metod, które różnią się między sprawdzonymi wersjami (pakiet własnego
okrętu to 43 lub 44, wywołanie zatonięcia 76 lub 83, pociski 101, 102,
126 lub 127), są wszystkie znajdowane po kształcie – zob.
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) – więc łatka
przenumerowująca je nie opróżnia tabeli. Znalezione liczby są w `decoded`
dokumentu meczu.

**Pickle to dane niezaufane.** Replay to plik skądkolwiek, a pickle może nazwać kod do uruchomienia.
Jest ładowany czytnikiem, który każdej klasie i funkcji, jaką pickle nazywa, podaje bezwładny zastępnik, więc
buduje tylko zwykłe dane i nic więcej. Test podaje mu pickle, które wywołuje `os.system`.

**Zatonięcia** mają dokładny czas wywołania. Ich miejsce to miejsce, w którym ofiarę widziano
ostatnio, gdy było to w ciągu pięciu sekund. **Początek bitwy** to pierwsza chwila, w której
jakikolwiek okręt się rusza (okręty stoją w miejscu podczas odliczania).

Wszystko, co nie jest wierszem tabeli, jest w [dokumencie meczu](match-document.md).

**To, co dostał klient**, jest kompletne dla własnej drużyny, a częściowe dla
wrogów: ich strzały, trafienia i zdrowie są tam, gdy byli w zasięgu.

**Nieodczytane:**

- Samoloty i ich eskadry (wywołania, które je niosą, nie zostały rozłożone), aktualizacje
  widzenia z minimapy (upakowane), wykrywanie, odznaczenia, pożary i zalania jako osobne zdarzenia (ich obrażenia są w trafieniach), wyposażenie,
  punkty przechwytu i wyniki drużyn (właściwości obiektów bez definicji, nie odróżnione po kształcie), reszta
  właściwości okrętu (celowanie, ster, ustawienie prędkości...).
- Klucze numeryczne rekordów graczy i statystyk obrażeń jako nazwy: gra je ponumerowała, a numery się zmieniają; są zachowane jako liczby.
- Dodatkowe dane pocisku w miejscu uderzenia (15.x) i bajty po początku oraz prędkości pocisku lub torpedy.
- Wyniki klientów sprzed 15.x: ich replaye ich nie niosą.
- Numer okrętu jako nazwa: nazwy są w plikach parametrów samej gry, a nie w replayu.

## Jak sprawdzono odczyt {#how-the-reading-was-checked}

Odczyt sprawdzono na publicznych replayach klientów od 0.9 do 15.x, każdą
wartość względem czegoś, co replay podaje drugi raz:

- **Pozycje:** obiekt każdego okrętu pasował do nazwy z listy graczy; kursy zgadzają się z kierunkiem ruchu w granicach 0,1 rad;
  po zatonięciu okręt przesuwa się o mniej niż 0,1 jednostki. Okręt stojący w miejscu jest aktualizowany rzadziej.
- **Zdrowie:** każdy okręt zatopiony w zasięgu widoku klienta kończy ze zdrowiem 0.
  Około połowa wszystkich trafień pasuje do spadku zdrowia w sekundzie wcześniej; reszta
  zbiega się z naprawami lub innymi trafieniami.
- **Obrażenia względem własnych statystyk gry:** u najnowszego klienta odczyt obrażeń nagrywającego gracza mieści się w granicach 0,1%
  statystyk. U starszych klientów statystyki są wyższe: klient nie dostaje każdego
  trafienia albo statystyki liczą więcej niż trafienia (nierozstrzygnięte).
- **Pociski:** pocisk zaczyna się kilka jednostek od ostatniej znanej pozycji swojego okrętu
  (działa są rozłożone wzdłuż kadłuba); niemal koniec każdego pocisku następuje w ciągu minuty po
  strzale, który klient widział.

Testy budują replaye w tym samym układzie, więc żaden prawdziwy replay nie jest
przechowywany w tym repozytorium.

**Nie sprawdzono:** klientów przed 0.9.6, klienta Lesta (Mir Korabley),
operacji i scenariuszy poza jednym, bitew klanowych i rankingowych oraz
tego, który numer okrętu to który okręt.

---

Część [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacja](https://holdi601.github.io/3DHeat/)). Źródło: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
