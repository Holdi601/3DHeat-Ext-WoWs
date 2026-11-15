---
title: "Başlamadan önce"
nav_order: 2
lang: tr
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Başlamadan önce {#before-you-start}

Komut satırına yeni misiniz? Bu sayfa sizi yaklaşık on dakikada hiçbir şeyden,
çalışan bir `heat3d-wows-replay` komutuna götürür. Python'u zaten kullanıyorsanız
doğrudan [Kurulum](installing.md) sayfasına geçin.

## 1. Python'u kurun {#install-python}

1. [python.org/downloads](https://www.python.org/downloads/) adresinden Python **3.10 veya
   daha yeni** sürümünü indirin.
2. Windows'ta kurucunun ilk penceresinde **Add python.exe to PATH** kutusunu işaretleyin,
   sonra **Install Now** düğmesine tıklayın.
3. macOS ve Linux'ta Python 3 genellikle zaten yüklüdür. Bu sayfalarda `python` yazan
   yerlere `python3`, `pip` yazan yerlere `pip3` yazın.

## 2. Bir terminal açın {#open-a-terminal}

Terminal, komutları yazdığınız bir penceredir.

- **Windows:** klasörü Dosya Gezgini'nde açın, adres çubuğuna tıklayın, `cmd` yazıp Enter'a basın.
  Pencere açılır ve zaten o klasördedir.
- **macOS:** **Terminal** uygulamasını açın. **Linux:** klasörde sağ tıklayıp
  **Open in Terminal** seçin.

Başka bir klasöre geçmek için `cd` ve klasörü yazın:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Python'un çalıştığını denetleyin {#check-that-python-works}

```bash
python --version
```

`Python 3.` ile başlayan ve 10 ya da daha büyük bir sayı görmelisiniz, örneğin
`Python 3.12.4`.

## 4. Aracı alın ve kurun {#get-the-tool-and-install-it}

1. [Aracın GitHub sayfasında](https://github.com/Holdi601/3DHeat-Ext-WoWs) yeşil **Code**
   düğmesine, sonra **Download ZIP** seçeneğine tıklayın ve zip dosyasını açın.
2. Açılan klasörde (içinde `README.md` olan klasörde) bir terminal açın.
3. Yazın:

   ```bash
   pip install -e .
   ```

   Sonunda şunu görmelisiniz: `Successfully installed heat3d-ext-wows-0.1.0`
   (yanında başka adlar da olabilir).
4. Denetleyin:

   ```bash
   heat3d-wows-replay --version
   ```

   Şunu görmelisiniz: `heat3d-wows-replay 0.1.0`

## Bu sayfalardaki komutları nasıl okursunuz {#how-to-read-the-commands-on-these-pages}

- `<replays>` gibi köşeli parantez içindeki sözcükler yer tutuculardır. Kendi dosya ya da
  klasörünüzü parantezsiz yazın.
- Boşluk içeren bir yol tırnak işareti ister: `"C:\Program Files (x86)\Steam"`.
- `#` işaretinden sonraki metin bir açıklamadır: onu yazmazsınız.
- `-o out`, terminalinizin bulunduğu klasörün içinde `out` adlı bir klasöre yazar.
  Klasör yoksa oluşturulur.

## Başarı neye benzer {#what-success-looks-like}

Komut her tekrar için bir satır yazdırır, örneğin:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

ve çıkış durumu `0` ile biter. Yeni dosyalar `out` klasöründedir.

## Sık görülen hatalar {#common-errors}

| Gördüğünüz | Ne yapmalısınız |
|---|---|
| `'python' is not recognized ...` ya da `command not found` | Python PATH üzerinde değil: **Add python.exe to PATH** işaretli olarak yeniden kurun ya da `python` yerine `py` yazın (Windows) |
| `'pip' is not recognized ...` | bunun yerine `python -m pip install -e .` yazın |
| `'heat3d-wows-replay' is not recognized ...` | `heat3d-wows-replay` yerine `python -m heat3d_ext_wows` yazın; aynısını yapar |
| `No module named heat3d_ext_wows` | aracın klasöründe değilsiniz ya da kurulu değil: oraya `cd` yapın ve `pip install -e .` çalıştırın |
| `the following arguments are required: -o/--out` | komuta `-o out` ekleyin |

Sonraki: [Tekrarları çevirme](converting.md).
