---
title: "Tamlık"
nav_order: 8
lang: tr
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Tamlık {#completeness}

Tekrarda hiçbir şey atılmaz. Dönüştürücünün okuduğu şeyler tabloya ve maç belgesine girer; geri kalan her öge
`<match>.messages.parquet` yan dosyasında bütün olarak tutulur; maç belgesinin `selfCheck.completeness` alanı ise
her öge türüne ne olduğunu sayar. Bu, tüm 3DHeat dönüştürücülerinin ortak kuralıdır:
[Dönüştürücüler her şeyi tutar](https://holdi601.github.io/3DHeat/converters.html).

![Sentetik bir tekrarın öz denetimi: görülen, okunan, tutulan ya da kaybedilen her öge](../assets/img/completeness.svg)

## Sayım {#the-count}

Her öge türü için `selfCheck.completeness.types` şunları verir:

| Sayı | Anlamı |
|---|---|
| `seen` | tekrarın kaç tane tuttuğu |
| `decoded` | bütün olarak okunan |
| `partial` | kısmen okunan ve yan dosyada bütün olarak tutulan |
| `raw` | yalnızca yan dosyada bütün olarak tutulan, okunmayan |
| `lost` | kaybedilen: her zaman `0` |

Türler tekrarın kendi türleridir: `block <n>` (JSON blokları), kapsayıcının kendi baytları, `packet <type>`, ve
varlıklara yapılan çağrılar için `method <entity type>.<number>` ile `property <entity type>.<number>`.
`selfCheck.entities.roles` hangi varlık türünün kayıt oyuncusunun avatarı, hangilerinin gemiler olduğunu söyler.
Kimsenin bilmediği bir tür, sayısıyla birlikte görünür.

## Yan dosya {#the-sidecar}

| Sütun | Ne |
|---|---|
| `time` | tekrarın saati, tabloda olduğu gibi |
| `type`, `name` | ögenin türü; dönüştürücünün ona ne ad verdiği, nerede okuduğu |
| `entity` | ait olduğu gemi ya da avatar, tablonun `entity` sütunu gibi |
| `decoded` | okunan kısmı, JSON olarak |
| `payload`, `text` | baytları bütün olarak; JSON blokları bütün olarak |
| `entityType`, `packet`, `method` | numaralar |

Satırlar paket, yöntem, varlık ve zamana göre sıralanır. Hangi varlığın hangi oyuncu olduğu: maç belgesinin
`entities` ve `players` alanları.

## Ne okunur ve nasıl denetlendi {#what-is-read-and-how-it-was-checked}

- **Sonuçlar** (15.x, `results`): savaş kimlikleri akışınkidir ve içlerindeki her oyuncu başlığın kadrosundadır.
- **Kimlik bloğu** (15.x, `blockIds`): hesap ve savaş, hiçbir basamak kaybolmasın diye metin olarak okunur.
- Her konumun **eğimi ve yalpası**: yalpa dönüş hızıyla birlikte gider, bir gemi dönüşte yatar gibi; eğim neredeyse
  her zaman 0'dır.
- **Varlıklar** (`entities`): her biri istemcinin görüşüne ne zaman girdi ve ne zaman çıktı. Hiçbir geminin,
  çıkışı ile geri dönüşü arasında bir konumu yoktur.
- **Akıştaki sürüm** (`streamVersion`): başlıktakiyle aynı.

Okunan diğer her şey (batırmalar, hasar, can, mermiler, torpidolar, mermilerin nerede bittiği, sohbet, turşulanmış
çağrılar, oyuncuların kayıtları, konumlar) `partial`dır: tabloda ya da maç belgesinde, ve yan dosyada bütün olarak tutulur.

**Tutulan ama okunmayan** (`raw`), en büyük türler: tabloda olmayan konum güncellemeleri (bir gemi battıktan sonra,
oyuncusu olmayan varlıklar), okuyucusu olmayan sık özellikler ve yöntemler, varlık oluşturmalarının özellikleri ve
okuyucusu olmayan diğer her paket.

## Mevcut olmayanlar {#not-available}

- Sunucunun kayıt yapan istemciye hiç göndermediği şeyler: diğer oyuncuların nişanı, kamerası ve girdileri, fark
  edilmemiş düşmanlar. Bir tekrar, bir istemcinin kendisine anlatılanıdır.
- Varlık türlerinin, yöntemlerin, özelliklerin ve istatistik anahtarlarının adları: bunlar oyunun tanım dosyalarındadır,
  tekrarda değil. Numaralar tutulur.
- Gemi numaralarının gemi adları (`--ship-names` kullanın) ve oyunun kendi dosyalarını gerektiren her şey.
- 15.x öncesi istemcilerin sonuçları: tekrarlarında yoktur.

---

[3DHeat](https://github.com/Holdi601/3DHeat) parçası ([belgeler](https://holdi601.github.io/3DHeat/)). Kaynak: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
