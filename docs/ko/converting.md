---
title: 리플레이 변환하기
nav_order: 4
lang: ko
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# 리플레이 변환하기 {#converting-replays}

## 단계별 안내 {#step-by-step}

1. **녹화를 켜요.** 게임의 `preferences.xml`에 있는 `isReplayEnabled`, 또는 그 설정이 있는 경우 게임 자체의 설정으로요. 그 뒤로 게임은 전투마다 월드 오브 워십 설치 폴더의 `replays` 폴더에 저장해요. 예: `C:\Games\World_of_Warships_EU\replays`.
2. **터미널을 열어요.** 결과물을 써도 되는 폴더에서 열어 주세요([시작하기 전에](before-you-start.md)).
3. **변환기를 실행해요.** 리플레이 파일이나, 그런 파일이 든 폴더에 실행해요:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out`은 터미널이 있는 폴더 안에 만들어져요.
4. **출력된 내용을 읽어요.** 리플레이마다 한 줄씩 보여야 하고, 그 줄은 쓴 테이블로 끝나요.
5. **결과를 열어요.** 3DHeat 뷰어에서 히트맵 탭의 `out/<map>/<match>.parquet`, 매치 탭의 `<match>.match.json`을 열어요. 또는 Parquet나 JSON을 읽는 아무 도구로 읽으세요.

![합성 리플레이 실행: 변환, 다시 실행, 깨진 파일, 빈 폴더](../assets/img/convert.svg)

그림은 테스트가 코드로 만든 합성 리플레이에 대한 실행 결과예요(실제 리플레이는 쓰지 않았어요).

- 리플레이가 변환된 경우: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- 다시 실행하면 이미 쓴 매치는 건너뛰어요: `<file>: already written, <table>`;
- 리플레이가 아닌 파일: `<file>: not converted: <why>`(오류 출력에; 종료 상태 1, 나머지 리플레이는 계속 변환돼요);
- 리플레이를 찾지 못한 경우: `no .wowsreplay files in <folders>`(종료 상태 2).

## 옵션 {#options}

| 옵션 | 기본값 | 역할 |
|---|---|---|
| `replays`(하나 이상) | - | `.wowsreplay` 파일, 또는 그것을 찾을 폴더(하위 폴더도 포함) |
| `-o`, `--out` | 필수 | 쓸 폴더: 그 안에 맵마다 폴더가 만들어져요 |
| `--force` | 꺼짐 | 이미 쓴 것도 다시 변환해요 |
| `--ship-names JSON` | - | `{"<shipId>": "<name>", ...}` 형식의 JSON 파일: 리플레이는 녹화한 플레이어의 함선만 이름으로 적고, 나머지는 번호로 적어요 |
| `--version` | - | `heat3d-wows-replay <버전>`을 출력하고 멈춰요 |
| `-h`, `--help` | - | 옵션을 출력하고 멈춰요 |

프로그램이 출력하는 옵션: [명령 참조](../cli-reference.md).

## 무엇이 쓰이나 {#what-is-written}

낱개 파일만 써요. 이 변환기는 `.3dheat` 파일을 쓰지 않아요(뷰어가 하나로 묶을 수 있어요: [매치 하나를 담은 파일](https://holdi601.github.io/3DHeat/container.html)). 리플레이마다, `out/<map>/` 안에 다음을 써요(맵 이름은 `spaces/` 없이):

| 파일 | 내용 |
|---|---|
| `<match>.parquet` | 테이블: 모든 함선의 시간에 따른 위치와, 그 위치에서 일어난 모든 이벤트([테이블](table.md)) |
| `<match>.match.json` | 매치 문서: 맵, 클라이언트 버전, 플레이어, 침몰, 채팅과 그 밖의 모든 것([매치 문서](match-document.md)) |
| `<match>.messages.parquet` | 사이드카: 위의 두 파일이 통째로 담지 않는 리플레이의 모든 항목([완전성](completeness.md)) |

`<match>`는 전투 자신의 ID예요. 결과가 나오기 전에 녹화가 멈췄다면 파일 이름을 써요.

## 종료 상태 {#exit-status}

모든 리플레이가 변환되었거나 건너뛰어졌으면 `0`, 하나라도 실패하면 `1`(나머지는 계속 변환돼요), 리플레이 파일을 찾지 못하면 `2`예요.

---

[3DHeat](https://github.com/Holdi601/3DHeat)의 일부([문서](https://holdi601.github.io/3DHeat/)). 소스: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
