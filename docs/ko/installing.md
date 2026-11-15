---
title: 설치
nav_order: 3
lang: "ko"
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# 설치 {#installing}

명령줄이 처음이라면 먼저 [시작하기 전에](before-you-start.md)를 읽어 주세요. Python 3.10 이상이 필요합니다. numpy와 pyarrow도 함께 설치됩니다.

## 단계별 설치 {#step-by-step}

1. 코드를 받으세요: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`. 또는 [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)에서 zip을 받아 압축을 푸세요.
2. 그 폴더에서 터미널을 열고 `pip install -e .`을 입력하세요. 이렇게 하면 `heat3d-wows-replay` 명령이 경로에 들어갑니다.
3. 확인하세요: `heat3d-wows-replay --version`. `heat3d-wows-replay 0.1.0`이 보이면 됩니다. `heat3d-wows-replay --help`는 옵션 목록을 보여 줍니다:

![heat3d-wows-replay --help](../assets/img/help.svg)

설치하지 않고 쓰려면 도구 폴더에서 `python -m heat3d_ext_wows ...`를 실행하면 같은 일을 합니다.

3DHeat Watcher는 이것이 설치되어 있으면 새 리플레이에 이 명령을 실행합니다. 없어도 Watcher는 작동합니다.

## 업데이트 {#updates}

실행할 때마다 먼저 이 프로젝트의 GitHub 릴리스를 확인합니다(최대 몇 시간에 한 번씩 요청합니다). 인터넷이 없어도 변환은 멈추지 않습니다. 새 릴리스가 나오면 명령이 설치 전에 먼저 물어봅니다. `git clone`으로 받은 것은 `git pull --ff-only`로 업데이트하고(로컬 변경이 있으면 거부합니다), 내려받은 복사본은 릴리스의 압축 파일로 업데이트합니다. `HEAT3D_NO_UPDATE=1`로 확인과 업데이트를 모두 끌 수 있습니다.

---

[3DHeat](https://github.com/Holdi601/3DHeat)의 일부([문서](https://holdi601.github.io/3DHeat/)). 소스: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
