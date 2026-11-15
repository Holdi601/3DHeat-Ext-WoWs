---
title: "安裝"
nav_order: 3
lang: "zh-Hant"
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# 安裝 {#installing}

第一次使用命令列嗎？請先閱讀[開始之前](before-you-start.md)。
需要 Python 3.10 或更新版本；安裝時會一併安裝 numpy 與 pyarrow。

## 逐步說明 {#step-by-step}

1. 取得程式碼：`git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`，或從 [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases) 下載 zip 檔並解壓縮。
2. 在該資料夾中開啟終端機，輸入 `pip install -e .`。這會讓 `heat3d-wows-replay` 指令出現在你的 PATH 中。
3. 檢查安裝：`heat3d-wows-replay --version`。你應該會看到 `heat3d-wows-replay 0.1.0`。`heat3d-wows-replay --help` 會列出所有選項：

![heat3d-wows-replay --help](../assets/img/help.svg)

不安裝也可以：在工具的資料夾中執行 `python -m heat3d_ext_wows ...`，效果相同。

3DHeat Watcher 安裝後會對新的回放執行此指令；沒有它，Watcher 也能運作。

## 更新 {#updates}

每次啟動時，都會先檢查專案的 GitHub Releases（最多每幾小時一次請求；無論是否連上網路，都不會中斷轉換）。若有較新的版本，指令會在安裝前詢問：用 `git clone` 取得的副本會以 `git pull --ff-only` 更新（若你有本機變更則會拒絕），下載的副本則從該版本的封存檔更新。設定 `HEAT3D_NO_UPDATE=1` 可關閉檢查與更新。

---

屬於 [3DHeat](https://github.com/Holdi601/3DHeat)（[說明文件](https://holdi601.github.io/3DHeat/)）的一部分。來源：[3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs)。
