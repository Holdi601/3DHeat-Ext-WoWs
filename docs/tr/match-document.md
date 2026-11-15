---
title: "Maç belgesi"
nav_order: 6
lang: tr
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Maç belgesi {#the-match-document}

`<match>.match.json` tekrarın, tablonun bir satırı olmayan her şeyini tutar. Görüntüleyicinin Maç sekmesi
onu okur. (Kod buna özet der.)

![Sentetik bir maç belgesinin başı ve anahtarları](../assets/img/match-document.svg)

## Savaş {#the-battle}

| Anahtar | Ne |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; savaşın kimliği; haritanın oyunun adlandırdığı hali (`spaces/<map>`) ve görünen adı |
| `clientVersion`, `streamVersion` | başlıktan oyun sürümü ve paket akışının söylediği biçimde |
| `recorded` | tekrarın ne zaman kaydedildiği, oyunun yazdığı gibi |
| `player`, `vehicle` | kayıt oyuncusu ve gemisi |
| `gameType`, `scenario` | savaşın türü (`RandomBattle`, ...) ve senaryosu, başlıktan |
| `duration` | savaşın saniye cinsinden zaman sınırı, başlıktan |
| `truncated` | kayıt erken durdu |
| `battleStart`, `recordingSeconds` | savaşın başlangıcı (herhangi bir geminin hareket ettiği ilk an) ve kaydın saniye cinsinden uzunluğu |
| `positionPacket`, `ownPositionPacket` | konumların geldiği paket numaraları: diğer gemilerin, kayıt oyuncusunun |
| `deathMethod` | batırmaların bulunduğu yöntem numarası |
| `hz`, `ownHz`, `positions` | diğer gemilerin ve kendi geminin saniyedeki örnekleri; konum satırları |
| `units` | dünya birimleri (gövdelere göre 15 m, oyunun menzil değerlerine göre 30 m); x doğu, y yukarı, z kuzey |
| `events` | her olay türünün tablo satırı sayısı |
| `decoded` | her ileti türü için bulunan yöntem ve paket numaraları |

## Oyuncular ve olaylar {#players-and-events}

| Anahtar | Ne |
|---|---|
| `players` | bir gemi başına bir giriş: ad, `ally` ya da `enemy`, gemi numarası ve adı, varlık, örnekler, öldürmeler, hayatta kalma; `seen` (istemcinin gördüğü verilen ve alınan hasar, mermiler, torpidolar ve son can); `header` (kadro girişi) ve `record` (akıştaki oyuncu kaydı, anahtar numarasıyla) |
| `kills` | her batırma: zaman, kurban, öldüren, neden numarası, yer |
| `chat` | her sohbet satırı, kanal ve gönderenle |
| `damageStats` | kayıt oyuncusunun oyunun tuttuğu kendi istatistikleri: silah ve türe göre, bir sayı ve bir miktar (tür 0 verilen hasardır) |
| `avatarPickles` | kayıt oyuncusuna yapılan her turşulanmış çağrı, çözülmüş, yöntem numarasına göre |

## Başlık, sonuçlar ve denetimler {#header-results-and-checks}

| Anahtar | Ne |
|---|---|
| `header` | ilk JSON bloğu, kadro dışında hepsi: oyun modu, hava, harita sınırı, takım büyüklükleri ve daha fazlası |
| `moreBlocks` | ilk bloktan sonraki JSON blokları, olduğu gibi |
| `blockIds` | 15.x: kayıt oyuncusunun hesabı ve savaşın kimliği, metin olarak okunmuş |
| `results` | 15.x: sonuçlar; bu istemciler onları akışta tutar |
| `entities` | akışın oluşturduğu her varlık: tür numarası ve rolü, istemcinin görüşüne ne zaman girdiği ve ne zaman çıktığı |
| `selfCheck` | tamlık sayımı ([Tamlık](completeness.md)) ve varlıkların, sonuçların, kimliklerin ve sürümün denetimleri |

---

[3DHeat](https://github.com/Holdi601/3DHeat) parçası ([belgeler](https://holdi601.github.io/3DHeat/)). Kaynak: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
