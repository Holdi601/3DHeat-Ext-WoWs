---
title: 완전성
nav_order: 8
lang: ko
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# 완전성 {#completeness}

리플레이에서 버려지는 것은 없어요. 변환기가 읽는 것은 테이블과 매치 문서에 들어가요. 그 밖의 항목은 모두 사이드카 `<match>.messages.parquet`에 통째로 보관돼요. 매치 문서의 `selfCheck.completeness`는 항목 종류마다 그 항목이 어떻게 되었는지 셈해요. 이것은 모든 3DHeat 변환기가 함께 따르는 규칙이에요: [변환기는 모든 것을 보관해요](https://holdi601.github.io/3DHeat/converters.html).

![합성 리플레이의 자기 점검: 본 항목, 읽은 것, 보관한 것, 잃은 것](../assets/img/completeness.svg)

## 셈 {#the-count}

항목 종류마다 `selfCheck.completeness.types`는 다음을 줘요:

| 셈 | 뜻 |
|---|---|
| `seen` | 리플레이가 가진 개수 |
| `decoded` | 통째로 읽은 것 |
| `partial` | 일부를 읽고, 사이드카에 통째로 보관한 것 |
| `raw` | 사이드카에만 통째로 보관하고 읽지 않은 것 |
| `lost` | 잃은 것: 항상 `0` |

종류는 리플레이 자신의 것이에요: `block <n>`(JSON 블록들), 컨테이너 자체의 바이트, `packet <type>`, 그리고 엔티티에 대한 호출은 `method <entity type>.<number>`와 `property <entity type>.<number>`예요. `selfCheck.entities.roles`가 어느 엔티티 타입이 녹화한 플레이어의 아바타이고 어느 것이 함선인지 알려 줘요. 아무도 몰랐던 종류는 개수와 함께 나와요.

## 사이드카 {#the-sidecar}

| 열 | 내용 |
|---|---|
| `time` | 리플레이의 시계, 테이블과 같아요 |
| `type`, `name` | 항목의 종류; 변환기가 그것을 무엇이라 부르는지, 어디서 읽는지 |
| `entity` | 그 항목이 속한 함선 또는 아바타, 테이블의 `entity`와 같아요 |
| `decoded` | 읽은 내용, JSON으로 |
| `payload`, `text` | 바이트 전체; JSON 블록 전체 |
| `entityType`, `packet`, `method` | 번호들 |

행은 패킷, 메서드, 엔티티, 시간 순으로 정렬돼요. 어떤 엔티티가 어느 플레이어인지는 매치 문서의 `entities`와 `players`에 있어요.

## 무엇을 읽었고, 어떻게 확인했나 {#what-is-read-and-how-it-was-checked}

- **결과**(15.x, `results`): 전투 ID는 스트림의 것과 같고, 결과에 있는 모든 플레이어는 헤더의 명단에 있어요.
- **ID 블록**(15.x, `blockIds`): 계정과 전투를 문자로 읽어서 숫자가 하나도 빠지지 않아요.
- **모든 위치의 피치와 롤**: 롤은 선회율과 함께 가요. 함선이 선회할 때 기울어지는 것처럼요. 피치는 거의 항상 0이에요.
- **엔티티**(`entities`): 각각 언제 클라이언트의 시야에 들어오고 나갔는지. 어떤 함선도 나간 뒤 다시 돌아올 때까지 위치가 없어요.
- **스트림의 버전**(`streamVersion`): 헤더의 버전과 같아요.

읽은 다른 모든 것(침몰, 피해, 체력, 포탄, 어뢰, 포탄이 끝난 곳, 채팅, 피클로 된 호출, 플레이어 기록, 위치)은 `partial`이에요. 테이블이나 매치 문서에 있고, 사이드카에 통째로 보관돼요.

**보관했지만 읽지 않은 것**(`raw`)이 가장 큰 종류예요. 테이블에 없는 위치 업데이트(함선이 가라앉은 뒤, 플레이어가 없는 엔티티), 읽는 코드가 없는 자주 오는 속성과 메서드, 엔티티 생성의 속성, 그리고 읽는 코드가 없는 그 밖의 모든 패킷이에요.

## 알 수 없는 것 {#not-available}

- 서버가 녹화한 클라이언트에게 보내지 않은 것: 다른 플레이어의 조준, 카메라와 입력, 발견되지 않은 적. 리플레이는 한 클라이언트가 들은 것이에요.
- 엔티티 타입, 메서드, 속성, 그리고 통계 키의 이름: 게임의 정의 파일에 있고, 리플레이에는 없어요. 번호는 보관해요.
- 함선 번호에 대한 함선 이름(`--ship-names` 사용), 그리고 게임 자체의 파일이 필요한 그 밖의 것.
- 15.x 이전 클라이언트의 결과: 그 리플레이에는 없어요.

---

[3DHeat](https://github.com/Holdi601/3DHeat)의 일부([문서](https://holdi601.github.io/3DHeat/)). 소스: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
