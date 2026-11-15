---
title: 매치 문서
nav_order: 6
lang: ko
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# 매치 문서 {#the-match-document}

`<match>.match.json`에는 리플레이가 테이블의 행이 아닌 것으로 말하는 모든 것이 들어 있어요. 뷰어의 매치 탭이 이 파일을 읽어요. (코드에서는 이것을 요약이라고 불러요.)

![합성 매치 문서의 시작 부분과 그 키들](../assets/img/match-document.svg)

## 전투 {#the-battle}

| 키 | 내용 |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; 전투의 ID; 게임이 부르는 대로의 맵(`spaces/<map>`)과 그 표시 이름 |
| `clientVersion`, `streamVersion` | 헤더의 게임 버전, 그리고 패킷 스트림이 말하는 버전 |
| `recorded` | 리플레이를 녹화한 시각, 게임이 쓴 그대로 |
| `player`, `vehicle` | 녹화한 플레이어와 그 함선 |
| `gameType`, `scenario` | 헤더의 전투 유형(`RandomBattle`, ...)과 시나리오 |
| `duration` | 헤더에서 가져온 전투의 제한 시간(초) |
| `truncated` | 녹화가 일찍 멈춘 것 |
| `battleStart`, `recordingSeconds` | 전투의 시작(어떤 함선이라도 처음 움직인 순간)과 녹화의 길이(초) |
| `positionPacket`, `ownPositionPacket` | 위치가 온 패킷 번호: 다른 함선의 것, 녹화한 플레이어의 것 |
| `deathMethod` | 침몰이 발견된 메서드 번호 |
| `hz`, `ownHz`, `positions` | 다른 함선과 자기 함선의 초당 샘플 수; 위치 행 |
| `units` | 세계 단위(선체 기준 15 m, 게임의 사거리 기준 30 m); x 동, y 위, z 북 |
| `events` | 이벤트마다 테이블 행의 수 |
| `decoded` | 메시지 종류마다 찾은 메서드와 패킷 번호 |

## 플레이어와 이벤트 {#players-and-events}

| 키 | 내용 |
|---|---|
| `players` | 함선 하나당 항목 하나: 이름, `ally`(아군) 또는 `enemy`(적군), 함선 번호와 이름, 엔티티, 샘플 수, 처치, 생존 여부. `seen`(클라이언트가 본 준 피해와 받은 피해, 포탄, 어뢰, 마지막 체력); `header`(명단의 항목)와 `record`(스트림의 플레이어 기록, 키 번호별) |
| `kills` | 모든 침몰: 시각, 피해자, 공격자, 원인 번호, 위치 |
| `chat` | 모든 채팅 줄, 채널과 보낸 사람 포함 |
| `damageStats` | 게임이 보관하는 녹화한 플레이어 자신의 통계: 무기와 종류별로 횟수와 양(종류 0은 준 피해) |
| `avatarPickles` | 녹화한 플레이어에게 간 모든 피클된 호출, 해독한 것, 메서드 번호별 |

## 헤더, 결과와 확인 {#header-results-and-checks}

| 키 | 내용 |
|---|---|
| `header` | 첫 JSON 블록 전체(명단은 뺌): 게임 모드, 날씨, 맵 경계, 팀 크기 등 |
| `moreBlocks` | 첫 블록 뒤의 JSON 블록들, 그대로 |
| `blockIds` | 15.x: 녹화한 플레이어의 계정과 전투 ID, 문자로 읽은 것 |
| `results` | 15.x: 결과. 이 클라이언트들은 결과를 스트림에 보관해요 |
| `entities` | 스트림이 만드는 모든 엔티티: 타입 번호와 역할, 클라이언트 시야에 들어온 때와 나간 때 |
| `selfCheck` | 완전성 셈([완전성](completeness.md))과 엔티티, 결과, ID, 버전의 확인 |

---

[3DHeat](https://github.com/Holdi601/3DHeat)의 일부([문서](https://holdi601.github.io/3DHeat/)). 소스: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
