---
title: 약관과 라이선스
nav_order: 9
lang: ko
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# 약관과 라이선스 {#terms-and-licence}

## Wargaming의 약관 {#wargamings-terms}

2026-11-07에 읽었습니다. Wargaming EULA 버전 14(2024년 4월 10일부터 시행, 현재 버전으로 게시됨). 12.3항은 월드 오브 워십 모드 정책 페이지를 가리키는데, 그 페이지는 브라우저 밖에서는 표시되지 않아서 읽지 않았습니다.

- 5.3 (b): 서면으로 허가받지 않았다면 "... decompile, disassemble, reverse engineer or otherwise make unauthorized use of the Content"(콘텐츠를 디컴파일, 디스어셈블, 리버스 엔지니어링하거나 달리 허가되지 않은 방식으로 사용하는 것)을 하면 안 됩니다.
- 12.1 (k): 금지되는 것은 "Creating, using, making available, or distributing any unauthorized software or tools, including hacks, cheats, exploits, scripts, bots, trainers, automation programs, or other software that interacts with a Product in any way and for any purpose, including intercepts, emulates, or redirects any communication between such software and Wargaming."(허가되지 않은 소프트웨어나 도구를 만들고, 쓰고, 제공하거나 배포하는 것. 해킹, 치트, 익스플로잇, 스크립트, 봇, 트레이너, 자동화 프로그램, 그리고 어떤 목적으로든 제품과 어떤 방식으로든 상호작용하는 그 밖의 소프트웨어를 포함하며, 그런 소프트웨어와 Wargaming 사이의 통신을 가로채거나, 흉내 내거나, 방향을 바꾸는 것을 포함합니다.)
- 12.1 (l): "... any software designed to modify a Product and change the user experience ("mods") unless expressly permitted by Wargaming"(Wargaming이 명시적으로 허용하지 않는 한, 제품을 수정하고 사용자 경험을 바꾸도록 설계된 모든 소프트웨어("모드")).
- 12.1 (p): "Circumventing or bypassing enforcement and security measures implemented by Wargaming"(Wargaming이 마련한 집행과 보안 조치를 우회하거나 피하는 것).

이 변환기가 하는 일: 전투가 끝난 뒤, 게임 밖에서, 게임이 쓴 파일을 읽습니다. 게임은 전혀 바꾸지 않고, 어떤 서버와도 통신하지 않고, 전투 중에는 아무것도 보여 주지 않습니다. 다만 게임의 키로 스트림을 해독하는데, 5.3 (b)와 12.1 (p)가 이것을 포함한다고 읽을 수도 있습니다. 사용은 사용자의 결정입니다. 그래서 이것은 별도의 패키지입니다.

## 라이선스와 출처 {#licence-and-sources}

MIT([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). numpy(BSD-3-Clause)와 pyarrow(Apache-2.0)가 필요합니다. 이 프로젝트를 위해 쓰였습니다. 여기의 Blowfish 암호는 자체 구현입니다. 그 표는 암호가 정의하는 대로 파이의 숫자에서 계산했습니다. 형식에 대한 사실들은 리플레이 도구들 사이에서 널리 알려진 것입니다. 단위 배율에 대한 메모는 landaire/wows-toolkit(MIT)에서 왔습니다. 다른 프로젝트의 코드는 가져오지 않았습니다.

`bigworld.py`와 `table.py`는 월드 오브 탱크 변환기([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT))와 같은 파일입니다. 둘 다 함께 바꾸세요.

---

[3DHeat](https://github.com/Holdi601/3DHeat)의 일부([문서](https://holdi601.github.io/3DHeat/)). 소스: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
