---
title: 문서 관리
nav_order: 99
lang: "ko"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# 문서 관리 {#maintaining-the-documentation}

새 버전을 내는 사람을 위한 페이지입니다. 아래 순서대로 하세요.

1. **참조 페이지를 코드에서 다시 만드세요:**

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # 종료 코드 0이어야 합니다
   ```

   이 명령은 [명령 참조](../cli-reference.md)와 [열 목록](../columns.md)을 다시 씁니다. 이 두 페이지는 손으로 고치지 마세요.
2. **마지막 릴리스 이후 바뀐 것을 보세요:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>`은 마지막으로 릴리스된 버전입니다(아직 태그가 없으면 `git log --oneline` 전체). 새 기능, 옵션, 열마다 그것을 설명하는 페이지와 [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md)의 **Docs** 섹션에 줄이 하나씩 필요합니다.
3. **독립적인 검토.** 페이지를 쓰지 않은 사람(사람이나 에이전트)이 README와 모든 페이지, 모든 그림을 세 가지 독자의 눈으로 읽습니다. 터미널을 써 본 적이 없는 초보자, 여덟 살 아이, 모든 옵션, 열, 단위를 코드와 대조하는 전문가입니다. 그림이 코드와 맞는지도 확인하고, 실제 맵, 레벨, 플레이어, 매치의 이름이나 실제 리플레이의 수치를 쓴 페이지가 없는지 확인하세요.
4. **검토에서 나온 것을 고치세요.** 그다음 1단계를 다시 실행하고, 출력이 바뀐 그림을 다시 그리세요.
5. **번역.** `docs/<언어>/`의 모든 페이지는 번역의 바탕이 된 영어 페이지의 해시를 기록합니다. 영어 원문이 바뀐 페이지는 모두 다시 번역하세요. 그림의 라벨도 포함합니다. 그다음 각 언어를 검토하세요: 세 독자 모두에게 명확한지, 라벨이 맞는지, 그리고 3DHeat 뷰어가 그 언어에서 쓰는 말과 같은지.
6. **릴리스:** `VERSION`을 올리고 `v<VERSION>` 태그를 붙이세요. **소유자의 승인을 받은 뒤에만 푸시하세요.**

## 번역: 명령 {#translations-the-commands}

사이트는 3DHeat 뷰어의 40개 언어로 번역됩니다. 영어는 `docs/`에, 다른 언어는 같은 파일 이름으로 `docs/<lang>/`에 있습니다. `tools/docs_i18n.py`가 관리 작업을 합니다:

```bash
python tools/docs_i18n.py hashes             # 영어가 바뀐 뒤: 페이지마다 해시를 기록
python tools/docs_i18n.py svg-strings        # 그림이 바뀐 뒤: 번역할 라벨 목록
python tools/docs_i18n.py status             # 언어별: 최신, 오래됨, 없는 페이지
python tools/docs_i18n.py todo --lang de     # 번역(다시 번역)할 독일어 페이지
python tools/docs_i18n.py svg-build --lang de    # docs/assets/i18n/svg/de.json으로 독일어 그림 만들기
python tools/docs_i18n.py finish --lang de   # 독일어 페이지에 영어 해시를 찍기
python tools/docs_i18n.py check              # 해시나 라벨이 오래되었으면 종료 코드 1
```

`todo`가 나열한 것만 번역하세요. Markdown, 링크, 코드, 파일과 열 이름은 그대로 두세요. 제목과 그림 설명은 번역하세요. 뷰어의 버튼과 패널은 뷰어 자신의 말을 쓰세요(`src/i18n/locales/<lang>/`). 생성된 참조 페이지와 터미널 그림은 영어로 둡니다. 사이트에서 오래된 번역에는 그렇다는 표시가 나오고 영어 페이지로 연결됩니다. 없는 번역은 영어로 대신합니다. 헤더의 언어 메뉴와 홈 페이지의 브라우저 언어 자동 이동은 `docs/_includes/`에서 옵니다.
