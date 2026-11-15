---
title: "Kurulum"
nav_order: 3
lang: tr
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Kurulum {#installing}

Komut satırına yeni misiniz? Önce [Başlamadan önce](before-you-start.md) sayfasını okuyun.
Python 3.10 veya daha yeni bir sürüm gerekir; numpy ve pyarrow onunla birlikte kurulur.

## Adım adım {#step-by-step}

1. Kodu alın: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`, ya da
   [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases) sayfasından bir zip
   indirip açın.
2. Bu klasörde bir terminal açın ve `pip install -e .` yazın. Bu, `heat3d-wows-replay`
   komutunu yolunuza koyar.
3. Denetleyin: `heat3d-wows-replay --version`. `heat3d-wows-replay 0.1.0` görmelisiniz.
   `heat3d-wows-replay --help` seçenekleri listeler:

![heat3d-wows-replay --help](../assets/img/help.svg)

Kurmadan: aracın klasöründe `python -m heat3d_ext_wows ...` aynısını yapar.

3DHeat Watcher kuruluysa yeni tekrarlarda bu komutu çalıştırır, ama bu komut olmadan da çalışır.

## Güncellemeler {#updates}

Her başlatmada önce projenin GitHub sürümleri denetlenir (en fazla birkaç saatte bir istek;
dönüştürmeyi hiçbir zaman durdurmaz, çevrimiçi ya da çevrimdışı). Yeni bir sürüm çıktığında
komut kurmadan önce sorar: `git clone` ile alınmış kopya `git pull --ff-only` ile güncellenir
(yerel değişiklikleriniz varsa reddedilir), indirilmiş kopya ise sürümün arşivinden.
`HEAT3D_NO_UPDATE=1` bu denetimi ve güncellemeyi kapatır.

---

[3DHeat](https://github.com/Holdi601/3DHeat) parçası ([belgeler](https://holdi601.github.io/3DHeat/)). Kaynak: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
