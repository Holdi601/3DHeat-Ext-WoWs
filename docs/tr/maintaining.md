---
title: "Bakım"
nav_order: 99
lang: tr
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Belgelerin bakımı {#maintaining-the-documentation}

Yeni bir sürüm yayımlayan kişi içindir. Adımları bu sırayla yapın.

1. **Başvuru sayfalarını koddan yeniden üretin:**

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # 0 ile çıkmalı
   ```

   Bu, [Komut başvurusu](../cli-reference.md) ve [Sütun listesi](../columns.md) sayfalarını yeniden yazar. Bu ikisini
   asla elle düzenlemeyin.
2. **Son sürümden beri neyin değiştiğini listeleyin:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>`, son yayımlanan sürümdür (henüz etiket yoksa tüm `git log --oneline`). Her yeni özelliğin, seçeneğin
   ya da sütunun kendi sayfası ve
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md) dosyasının **Docs** bölümünde
   bir satırı olmalı.
3. **Bağımsız inceleme.** Sayfaları yazmamış biri (bir kişi ya da bir ajan) README'yi, her sayfayı ve her resmi üç
   okuyucu gibi okur: hiç terminal kullanmamış bir yeni başlayan, 8 yaşında bir çocuk ve her seçeneği, sütunu ve
   birimi koda karşı denetleyen bir uzman. Ayrıca diyagramları koda karşı denetlerler ve hiçbir sayfanın gerçek bir
   harita, seviye, oyuncu ya da maç adını anmadığını, gerçek tekrarlardan rakam vermediğini doğrularlar.
4. **İncelemenin bulduklarını düzeltin.** Sonra 1. adımı yeniden çalıştırın ve çıktısı değişen resimleri yeniden çizin.
5. **Çeviriler.** `docs/<dil>/` altındaki her sayfa, hangi İngilizce sayfadan çevrildiğinin karmasını kaydeder.
   İngilizce kaynağı değişen her sayfayı yeniden çevirin; diyagram etiketleri de dahil. Sonra her dili inceleyin:
   üç okuyucu için de açık, etiketler doğru ve 3DHeat görüntüleyicisinin o dilde kullandığı sözcüklerle aynı.
6. **Yayın:** `VERSION` değerini yükseltin ve `v<VERSION>` etiketi koyun. **Yalnızca sahibin onayından sonra gönderin.**

## Çeviriler: komutlar {#translations-the-commands}

Site, 3DHeat görüntüleyicisinin 40 diline çevrilmiştir: İngilizcesi `docs/` içinde, diğer her dil aynı dosya adlarıyla
`docs/<lang>/` içinde. `tools/docs_i18n.py` kayıtları tutar:

```bash
python tools/docs_i18n.py hashes             # İngilizce bir değişiklikten sonra: her sayfanın karmasını kaydet
python tools/docs_i18n.py svg-strings        # bir resim değişikliğinden sonra: çevrilecek etiketler
python tools/docs_i18n.py status             # dil başına: güncel, eski ve eksik sayfalar
python tools/docs_i18n.py todo --lang de     # (yeniden) çevrilecek Almanca sayfalar
python tools/docs_i18n.py svg-build --lang de    # docs/assets/i18n/svg/de.json dosyasından Almanca resimler
python tools/docs_i18n.py finish --lang de   # Almanca sayfalara İngilizce karmayı damgala
python tools/docs_i18n.py check              # karmalar ya da etiketler eskiyse 1 ile çıkar
```

Yalnızca `todo`nun listelediğini çevirin: Markdown'ı, bağlantıları, kodu, dosya ve sütun adlarını olduğu gibi bırakın;
başlıkları ve resim açıklamalarını çevirin; düğmeler ve paneller için 3DHeat görüntüleyicisinin kendi sözcüklerini
kullanın (`src/i18n/locales/<lang>/`). Üretilmiş başvuru sayfaları ve terminal resimleri İngilizce kalır. Sitede eski
bir çeviri bunu söyler ve İngilizce sayfaya bağlanır; eksik bir çeviri İngilizceye döner. Üstbilgideki dil menüsü ve
ana sayfanın tarayıcı diline göre yönlendirmesi `docs/_includes/` içinden gelir.
