---
title: "Tekrarı nasıl okur"
nav_order: 7
lang: "tr"
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Tekrarı nasıl okur {#how-it-reads-a-replay}

Bir tekrar, JSON bloklarından oluşan bir başlık ve oyunun paket akışıdır (biçim notları:
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Açık haldeki ilk blok: harita, istemci sürümü, kayıt oyuncusu ve gemisi ve kadro: her oyuncunun adı, müttefik ya da
  düşman olduğu ve gemi numarası. Yeni istemciler (15.x) iki blok daha ekler: boş bir tanesi ve kayıt oyuncusunun
  hesabı ile savaşın kimliği metin olarak, `blockIds` içine okunur. Sonuçlar JSON'da değildir; 15.x onları akışta tutar.
- Paket akışı, zlib ile sıkıştırılmış ve oyunun taşıdığı bir anahtarla Blowfish ile şifrelenmiş; bu dosyaları okuyan
  topluluk araçlarının yayımladığı. Deşifre edildiğinde şunları tutar:
  - istemcinin görebildiği her geminin konum güncellemeleri (oyun motorunun gönderdiği) (kendi takımı boyunca, düşmanlar görüldüğünde ya
    da yakınken); hareket ederken saniyede birkaç kez, etmezken daha seyrek;
  - kayıt oyuncusunun kendi gemisi, kendi paketinde, saniyede yaklaşık yedi kez;
  - başlangıçta bir kez, oyuncuların kayıtları turşulanmış bir Python listesi olarak. Bunlar akıştaki hangi varlığın
    hangi oyuncu olduğunu söyler. Anahtarları numaralıdır ve numaralar yamalarla değişir, bu yüzden okuyucu anahtarları
    değerlerinden bulur: kadronun adlarını tutan anahtar ve konum güncellemesi olan varlıkları tutan anahtar;
  - istemciye bir geminin battığını söyleyen sunucu çağrısı: kurban, öldüren, neden. Numarasıyla değil, şekliyle bulunur
    (on iki bayt; ilk ikisi gemi varlıklarıdır; her kurban bir kez görünür);
  - her geminin hasarı: isabet başına (saldıran, hasar) dizisi, vurulan gemide; ve canı, bir an önce ayarlanmış bir
    özellik kümesi;
  - istemciye haber verilen her mermi ve torpido salvosu: mermi türü, atıcı, salvo ve her merminin ya da torpidonun
    başlangıcı ve hızı;
  - mermilerin nerede bittiği: atıcı, bir isabet türü ve her birinin yeri (15.x istemcilerinde ayrıca mermi çarptığında
    atlanan daha fazla bilgi ile);
  - sohbet: gönderen, kanal, satır;
  - kayıt oyuncusuna yapılan turşulanmış çağrılar: hasar istatistikleri, oyuncuların kayıtlarındaki güncellemeler, savaşın durumu;
  - 15.x istemcilerinde, savaşın sonunda sonuçlar: kendi paketinde, savaşın kimliğini içeren bir JSON nesnesi, maç
    belgesinin `results` alanına bütün olarak okunur (oyunun kendi listeleri, adsız: `commonList`, `privateDataList`,
    hesap başına `playersPublicInfo`, ...).

Denetlenen sürümler arasında değişen paket ve yöntem numaraları (kayıt oyuncusunun gemisinin paketi 43 ya da 44,
batırma çağrısı 76 ya da 83, mermiler 101, 102, 126 ya da 127) hepsi şekline göre bulunur; bkz.
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py). Bu yüzden
numaraları değiştiren bir yama tabloyu boşaltmaz. Bulunan numaralar maç belgesinin `decoded` alanındadır.

**Turşu güvenilmeyen veridir.** Bir tekrar her yerden gelmiş bir dosyadır ve bir turşu çalıştırılacak kod adlandırabilir.
Bu yüzden, turşunun adlandırdığı her sınıfı ya da işlevi etkisiz bir vekile çeviren bir açıcıyla yüklenir; böylece yalnızca
düz veri oluşur, başka hiçbir şey. Bir test ona `os.system` çağıran bir turşu verir.

**Batırmalar**, çağrının tam zamanını taşır. Yerleri, kurbanın son görüldüğü yerdir; bu beş saniye içindeyse.
**Savaşın başlangıcı**, herhangi bir geminin hiç hareket ettiği ilk andır (gemiler geri sayımda yerinde durur).

Tablo satırı olmayan her şey [maç belgesinde](match-document.md)dir.

**İstemciye söylenen**, kendi takımı için tam, düşmanlar için kısmidir: onların atışları, isabetleri ve canı menzildeyken oradadır.

**Okunmayanlar:**

- Uçaklar ve filoları (bunları taşıyan çağrılar ayrıştırılmadı), minimap'in görüş güncellemeleri (paketli), görüş,
  ribbon'lar, yangınlar ve sular altında kalmalar kendi olayları olarak (hasarları isabetlerde), tüketilebilirler,
  ele geçirme noktaları ve takım skorları (tanımı olmayan varlıkların özellikleri, şekle göre ayırt edilemedi), bir geminin
  geri kalan özellikleri (nişan, dümen, hız ayarı...).
- Oyuncu kayıtlarının ve hasar istatistiklerinin anahtar numaraları ad olarak: oyun onları numaralandırır ve numaralar
  değişir; numara olarak tutulur.
- Bir mermi çarptığında ek verisi (15.x) ve bir mermi ya da torpidonun başlangıcından ve hızından sonraki baytlar.
- 15.x öncesi istemcilerin sonuçları: tekrarlarında hiçbiri yoktur.
- Gemi numarasının ad olarak karşılığı: adlar oyunun kendi parametre dosyalarındadır, tekrarda değil.

## Okumanın nasıl denetlendiği {#how-the-reading-was-checked}

Okuma, 0.9'dan 15.x'e kadar istemcilerin herkese açık tekrarlarında denetlendi; her değer, tekrarın ona ikinci kez verdiği
bir şeyle karşılaştırıldı:

- **Konumlar:** her geminin varlığı bir kadro adıyla eşleşti; yönler, hareket yönüyle 0,1 rad içinde uyuşur; battıktan
  sonra bir gemi 0,1 birimden az hareket eder. Yerinde duran bir gemi daha seyrek güncellenir.
- **Can:** istemcinin görüşünde batan her gemi 0 canla biter. Tüm isabetlerin yaklaşık yarısı, hemen önceki saniyedeki bir
  can düşüşüyle eşleşir; kalanlar onarımlarla ya da diğer isabetlerle birlikte düşer.
- **Oyunun kendi istatistiklerine karşı hasar:** en yeni istemcide kayıt oyuncusunun okunan hasarı istatistiklerin %0,1'i
  içindedir. Eski istemcilerde istatistikler daha yüksektir: istemciye her isabet gönderilmez ya da istatistikler isabetlerden
  fazlasını sayar (çözülmedi).
- **Mermiler:** bir mermi, geminin son bilinen konumunun birkaç birim uzağında başlar (topçular gövdeye yayılmıştır); neredeyse
  her merminin bitişi, bir dakika içinde istemcinin gördüğü bir atışı izler.

Testler tekrarları aynı düzende üretir; bu yüzden bu depoda hiçbir gerçek tekrar tutulmaz.

**Denetlenmeyenler:** 0.9.6 öncesi istemciler, Lesta istemcisi (Mir Korabley), birden fazla operasyon ve senaryolar, klan
ve dereceli savaşlar ile hangi gemi numarasının hangi gemi olduğu.

---

[3DHeat](https://github.com/Holdi601/3DHeat) parçası ([belgeler](https://holdi601.github.io/3DHeat/)). Kaynak: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
