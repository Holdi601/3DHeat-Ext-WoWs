---
title: 시작하기 전에
nav_order: 2
lang: ko
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# 시작하기 전에 {#before-you-start}

명령줄이 처음입니까? 이 페이지는 아무것도 없는 상태에서 `heat3d-wows-replay`가 작동하기까지 약 10분 정도를 안내합니다. 이미 Python을 쓰고 있다면 바로 [설치](installing.md)로 가세요.

## 1. Python 설치하기 {#install-python}

1. [python.org/downloads](https://www.python.org/downloads/)에서 Python **3.10 이상**을 내려받으세요.
2. Windows에서는 설치 프로그램의 첫 화면에서 **Add python.exe to PATH**에 체크한 뒤 **Install Now**를 누르세요.
3. macOS와 Linux에는 Python 3이 이미 설치되어 있는 경우가 많습니다. 이 페이지에서 `python`이라고 쓴 곳에 `python3`을, `pip`이라고 쓴 곳에 `pip3`을 입력하세요.

## 2. 터미널 열기 {#open-a-terminal}

터미널은 명령을 입력하는 창입니다.

- **Windows:** 파일 탐색기에서 폴더를 열고, 주소 표시줄을 클릭해서 `cmd`를 입력한 뒤 Enter를 누르세요. 그 폴더로 이동된 창이 열립니다.
- **macOS:** **터미널** 앱을 여세요. **Linux:** 폴더에서 마우스 오른쪽 버튼을 누르고 **터미널에서 열기**를 고르세요.

다른 폴더로 가려면 `cd`와 폴더 경로를 입력하세요.

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Python이 작동하는지 확인하기 {#check-that-python-works}

```bash
python --version
```

`Python 3.`과 10 이상의 숫자가 보이면 됩니다. 예를 들어 `Python 3.12.4`처럼 보입니다.

## 4. 도구 받아서 설치하기 {#get-the-tool-and-install-it}

1. [도구의 GitHub 페이지](https://github.com/Holdi601/3DHeat-Ext-WoWs)에서 초록색 **Code** 버튼을 누른 다음 **Download ZIP**을 눌러 zip 파일을 받고, 압축을 푸세요.
2. 압축을 푼 폴더(`README.md`가 있는 폴더)에서 터미널을 여세요.
3. 다음을 입력하세요.

   ```bash
   pip install -e .
   ```

   끝에 `Successfully installed heat3d-ext-wows-0.1.0`(다른 이름이 더 붙을 수도 있습니다)이 보이면 성공입니다.
4. 확인하세요.

   ```bash
   heat3d-wows-replay --version
   ```

   `heat3d-wows-replay 0.1.0`이 보이면 됩니다.

## 이 페이지의 명령 읽는 법 {#how-to-read-the-commands-on-these-pages}

- `<replays>`처럼 꺾쇠 괄호 안에 든 말은 자리표시자입니다. 괄호는 빼고, 그 자리에 여러분의 파일이나 폴더 이름을 입력하세요.
- 공백이 있는 경로는 따옴표로 감싸야 합니다. 예: `"C:\Program Files (x86)\Steam"`.
- `#` 뒤의 글은 설명입니다. 입력하지 않습니다.
- `-o out`은 터미널이 있는 폴더 안에 `out`이라는 폴더를 만들어 그곳에 씁니다. 폴더가 없으면 새로 만듭니다.

## 제대로 되었는지 확인하기 {#what-success-looks-like}

명령이 리플레이마다 한 줄씩 출력합니다. 예를 들면 다음과 같습니다.

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

마지막은 종료 상태 `0`으로 끝납니다. 새 파일은 `out` 폴더에 있습니다.

## 자주 보이는 오류 {#common-errors}

| 보이는 메시지 | 할 일 |
|---|---|
| `'python' is not recognized ...` 또는 `command not found` | Python이 PATH에 없습니다. **Add python.exe to PATH**에 체크하고 다시 설치하거나, Windows에서는 `python` 대신 `py`를 입력하세요 |
| `'pip' is not recognized ...` | 대신 `python -m pip install -e .`을 입력하세요 |
| `'heat3d-wows-replay' is not recognized ...` | `heat3d-wows-replay` 대신 `python -m heat3d_ext_wows`를 입력하세요. 같은 일을 합니다 |
| `No module named heat3d_ext_wows` | 도구 폴더에 있지 않거나 설치되지 않았습니다. 그 폴더로 `cd`한 뒤 `pip install -e .`을 실행하세요 |
| `the following arguments are required: -o/--out` | 명령에 `-o out`을 추가하세요 |

다음: [리플레이 변환하기](converting.md).
