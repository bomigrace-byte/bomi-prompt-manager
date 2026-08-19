# 📌 나만의 프롬프트 관리자 (Prompt Manager)

> 파편화된 프롬프트를 한곳에서 저장, 조회, 검색, 즐겨찾기하고 관리할 수 있는 파이썬 콘솔 기반 프로그램입니다.
> 

---

## 1. 📖 프로젝트 개요

개발 목적: 다양한 GenAI 도구를 사용하며 흩어진 프롬프트를 체계적으로 정리하고 다룰 수 있는 나만의 프롬프트 집(House)을 구축합니다.

- 학습 목표:
    - 파이썬(Python)의 기본 데이터 구조(List, Dictionary), 제어문(if, while), 함수 분리를 활용해 동작하는 콘솔 프로그램을 구현합니다.
    - Git을 통해 기능 단위 커밋, 브랜치 관리(`checkout`, `merge`) 및 GitHub 버전 관리 워크플로우를 체계적으로 적용합니다.

---

## 2. ⚙️ 개발 환경 (Environment)

- OS: [ Windows / macOS ]
- Editor: Visual Studio Code (Python Extension, Korean Language Pack)
- Language: Python 3.10+ (외부 라이브러리 없는 파이썬 표준 라이브러리 기반)
- Version Control: Git & GitHub

---

## 3. ✨ 주요 기능 목록 (Features)

본 프로그램은 순수 파이썬 기본 문법과 기능별 함수 분리 구조로 작성되었습니다.

| 메뉴 번호 | 주요 기능 | 설명 및 담당 함수 |
| --- | --- | --- |
| 0 | 프로그램 종료 | 루프를 종료하고 프로그램을 안전하게 마칩니다. |
| 1 | 프롬프트 추가 | 제목, 내용, 카테고리를 입력받아 신규 등록 (add_prompt()) |
| 2 | 프롬프트 목록 | 전체 프롬프트 번호, 카테고리, 제목, 즐겨찾기(⭐) 표출 (show_list()) |
| 3 | 카테고리별 조회 | 지정한 카테고리의 프롬프트만 필터링 출력 (show_by_category()) |
| 4 | 프롬프트 검색 | 키워드 입력으로 제목 및 내용 통합 검색 (search_prompt()) |
| 5 | 상세 보기 | 프롬프트 번호 선택 시 제목, 카테고리, 즐겨찾기, 전체 본문 출력 (show_detail()) |
| 6 | 즐겨찾기 관리 | 특정 프롬프트의 즐겨찾기 상태 토글(ON/OFF) (toggle_favorite()) |
| 7 | 즐겨찾기 목록 | 즐겨찾기 등록된 프롬프트만 모아보기 (show_favorites()) |

기본 탑재 데이터: 프로그램 시작 시 최소 3개 이상의 프롬프트 기본 제공
등록된 프롬프트 카테고리:

프로그램 내에서 다루는 주요 프롬프트 카테고리는 다음과 같습니다:

1. 텍스트 생성: 블로그 글 작성, 이메일 작성, 요약 등 문장 생성용 프롬프트
2. 이미지 생성: Midjourney, DALL-E 등 AI 이미지 생성을 위한 키워드/스타일 프롬프트
3. 영상 생성: 비디오 스크립트 작성 및 숏폼 영상 기획용 프롬프트
4. 페르소나: 특정 분야 전문가 및 페르소나 부여용 지시문 프롬프트
5. 자동화: 업무 자동화 및 노코드 파이프라인 연동용 프롬프트
6. 기타: 기타 자유 주제의 프롬프트

---

## 4.1 자료구조 선택 및 설계 근거 (List vs Dictionary)

본 프로젝트에서는 프롬프트 데이터의 효율적인 관리 및 조회를 위해 **`List` 안에 `Dictionary`가 포함된 중첩 구조(`List[Dict]`)**를 사용했습니다.

### 1. 리스트(List)와 딕셔너리(Dictionary) 장단점 비교

| 구분 | 리스트 (`List`) | 딕셔너리 (`Dictionary`) |
| --- | --- | --- |
| **특징** | 순서가 있는 데이터의 연속된 집합 (인덱스 기반) | 키-값(Key-Value) 쌍으로 구성된 데이터 집합 |
| **장점** | • 순서가 보장되어 목록 출력 및 정렬이 유용함<br>• 인덱스(번호)를 통한 순차 접근이 용이함<br>• 데이터의 추가(`append`) 및 삭제가 간편함 | • 키(Key)를 통한 데이터 탐색 속도가 매우 빠름($O(1)$)<br>• 각 데이터의 의미(속성)를 직관적으로 파악 가능<br>• 데이터 구조 확장이 자유로움 |
| **단점** | • 특정 값을 찾기 위해 전체 탐색이 필요함 ($O(N)$)<br>• 요소의 의미(속성)를 위치(인덱스)로만 구분해야 함 | • 데이터의 순서가 보장되지 않음 (Python 3.7+부터 삽입 순서 유지되나 정렬 기능은 없음)<br>• Key 중복을 허용하지 않음 |

### 2. 본 프로젝트의 자료구조 설계 근거

본 프로그램은 `prompts = [ {"title": "...", "content": "...", "category": "..."}, ... ]` 형태의 구조를 채택했습니다.

1. **전체 구조로 `List`를 선택한 이유**
    - 사용자에게 프롬프트 목록을 **1번, 2번, 3번과 같이 순번(인덱스)으로 나열하여 보여주고 선택**하게 하는 UI 흐름에 가장 적합합니다.
    - 새로운 프롬프트가 추가될 때 순차적으로 저장하며, 전체 목록을 순회(`for`문)하며 출력하기에 용이합니다.
2. **개별 데이터로 `Dictionary`를 선택한 이유**
    - 하나의 프롬프트가 가질 여러 속성(`title`, `content`, `category`, `favorite`)을 **Key-Value 형태**로 관리하여 코드의 가독성과 명확성을 높였습니다.
    - 단순 튜플이나 리스트 사용 시 `prompt[0]`(제목), `prompt[1]`(내용)처럼 위치로 파악해야 하는 불편함을 `prompt["title"]`과 같이 직관적으로 해결했습니다.

## 4.2 프로그램 실행 및 반복(while Loop) 제어 구조 설계

본 프로그램은 콘솔 대화형(CLI) 애플리케이션으로, 사용자가 직접 종료를 원할 때까지 연속적으로 명령을 수행할 수 있도록 **`while True:` 무한 루프 기반의 메인 이벤트 루프**를 설계했습니다.

### 1. `while True:` 반복 구조 채택 이유

- **연속적인 사용자 경험 제공**: 하나의 기능(예: 프롬프트 추가 또는 조회)이 끝났을 때 프로그램이 바로 종료되지 않고, 다시 메인 메뉴로 돌아와 다른 작업을 이어 할 수 있도록 제어하기 위함입니다.
- **입력 유효성 검사 및 재입력 유도**: 메뉴 번호나 입력값이 잘못되었을 때 프로그램이 에러로 종료(`Crash`)되지 않고, 경고 메시지 출력 후 사용자에게 재입력을 유도하는 대기 상태를 유지하기 위함입니다.

### 2. 종료 조건 및 안전한 종료 흐름 (`0` 입력)

- **종료 트리거**: 메인 메뉴 입력창에서 **`0`번을 입력**하거나, 각 세부 입력 단계에서 **`0`을 입력**할 때 루프 제어가 동작합니다.
- **종료 제어 로직**:
    1. **메인 메뉴 종료 (`main()` 함수)**: 사용자가 `0`을 입력하면 `break` 문이 실행되어 `while True:` 무한 루프를 탈출하고, "프로그램을 종료합니다." 안내 문구와 함께 프로세스가 안전하게 종료됩니다.
    2. **하위 메뉴/입력 탈출 (`add_prompt()`, `show_detail()` 등)**: 입력값으로 `0`이 들어오면 `return` 문을 통해 해당 함수를 즉시 종료하고 이전 상위 메뉴(`main()` 루프)로 복귀합니다.

> 💡 **설계 이점**: 사용자가 의도치 않게 프로그램을 종료하는 상황을 방지하고, 종료 지점(`0` 입력)을 명확히 정의함으로써 프로그램 메모리 및 상태를 안전하게 정리하며 종료할 수 있습니다.

## 4.3 데이터 영속화(Data Persistence) 설계 문서

프로그램 종료 후에도 데이터가 사라지지 않고 유지되도록 **JSON 포맷 기반 파일 영속화** 방식을 채택하여 설계했습니다.

### 1. 파일 포맷 선택 및 비교 (JSON vs CSV vs TXT)

| 포맷 | 장점 | 단점 | 본 프로젝트 적합성 |
| --- | --- | --- | --- |
| **JSON** | • **계층형/복합 구조(Dict, List)를 1:1 직렬화** 가능<br>• `bool` 타입(즐겨찾기 여부 등)을 정확히 보존<br>• 파이썬 표준 라이브러리(`json`)로 간편히 제어 | • 데이터 용량이 텍스트에 비해 약간 클 수 있음 | **최적 (선택됨)** |
| **CSV** | • 엑셀 등 표 형태 소프트웨어와 호환성 우수 | • 프롬프트 내용(`content`) 내 **줄바꿈/쉼표(,) 포함 시 파싱 오류** 위험<br>• 불리언(`True/False`) 타입을 문자열로 별도 변환 필요 | 미흡 |
| **TXT** | • 가볍고 단순 텍스트 처리에 용이함 | • 구조화된 데이터(Key-Value)를 구획(Parsing)하기 까다로움 | 미흡 |

### 💡 JSON 포맷 선택 이유

- **데이터 구조의 일치성**: 본 프로그램의 데이터 구조인 `List[Dict]`(리스트 내 딕셔너리) 형태를 데이터 손실이나 형태 변형 없이 그대로 읽고(`json.load`) 쓸 수(`json.dump`) 있습니다.
- **텍스트 개행(줄바꿈) 안전성**: 프롬프트의 '내용(`content`)' 부분은 여러 줄의 긴 문장과 특수문자가 포함되는 경우가 많은데, JSON 규격을 사용하면 인코딩/디코딩 시 줄바꿈이나 쉼표로 인한 데이터 훼손이 발생하지 않습니다.


### 2. 데이터 영속화 및 파일 내보내기 설계 구조

- **저장 파일명**: `prompts.json` (기본 데이터 영속화용 파일)
- **내보내기 파일명**: `{title}.md` (개별 프롬프트 마크다운 내보내기용)

#### A. 데이터 저장 및 불러오기 흐름 (`prompts.json`)

1. **프로그램 시작 시 (`load_prompts`)**:
    - `prompts.json` 파일 존재 여부 확인 ➔ 파일이 존재하면 데이터를 읽어와 `prompts` 리스트에 로드합니다.
    - 파일이 없을 경우 기본 초기 데이터(Sample Data)로 세팅합니다.
2. **데이터 변경 발생 시 (`save_prompts`)**:
    - 프롬프트 추가, 수정, 즐겨찾기 변경 등이 일어날 때마다 최신 `prompts` 리스트 데이터를 `prompts.json`에 덮어씌워 자동 저장합니다.

#### B. Markdown 내보내기 흐름 (`export_to_markdown`)

- 사용자가 특정 프롬프트를 마크다운 파일로 내보내길 원할 경우, 제목과 내용/카테고리를 `# Heading` 및 `> Blockquote` 형태의 `.md` 표준 규격으로 변환하여 개별 파일로 생성합니다.

---

## 5. 🛡️ 사용자 입력 검증 및 예외 처리 정책 (Validation Policy)

프로그램 실행 중 발생할 수 있는 올바르지 않은 사용자 입력을 제어하고, 프로그램이 비정상 종료(Crash)되지 않도록 다음과 같은 입력 예외 처리 규칙을 일괄 적용했습니다.

### 1. 입력 예외 처리 정책 요약

| 구분 | 예외 상황 | 프로그램 행동 규칙 (Policy) |
| --- | --- | --- |
| **중복 제목** | 이미 존재하느 제목 입력 | ⚠️ 경고 메시지 출력 후 **재입력 유도** (대소문자/공백 무시 비교) |
| **빈값 처리** | Enter만 입력하거나 공백(`" "`) 입력 | ⚠️ "내용을 입력해주세요!" 안내 문구 출력 후 **재입력 유도** (`.strip()` 처리) |
| **범위 초과** | 카테고리/목록 번호 선택 시 범위 벗어남 | ⚠️ "올바른 번호를 입력해주세요!" 경고 출력 후 **재입력 유도** |
| **문자 입력** | 숫자 선택 항목에 문자/특수문자 입력 | ⚠️ `try-except (ValueError)` 또는 `.isdigit()` 검사로 차단 후 **재입력 유도** |

### 2. 세부 검증 로직 가이드

1. **빈값(Empty Input) 처리 규칙**
    - 모든 텍스트 입력 시 `.strip()` 메서드를 적용하여 양쪽 공백을 제거합니다.
    - 공백을 제거한 결과가 빈 문자열(`""`)일 경우 필수 입력값 미충족으로 판단하여 거부하고, 경고 문구 출력 후 올바른 값이 들어올 때까지 `while` 루프로 재입력을 요구합니다.
2. **숫자 및 메뉴 선택 범위(Range Validation) 처리 규칙**
    - **카테고리 선택**: `1 <= 선택번호 <= len(CATEGORIES)` 조건을 검사하여 범위를 벗어난 숫자 입력 시 재입력을 유도합니다.
    - **상세보기/수정/즐겨찾기 번호 선택**: 현재 등록된 전체 프롬프트 개수(`len(prompts)`) 범위를 초과하는 숫자가 입력되면 경고 메시지를 출력합니다.
    - **형변환 예외 처리**: 숫자가 아닌 문자가 입력될 경우 `ValueError` 예외를 캡처하거나 `.isdigit()`으로 검증하여 에러 없이 안내 메시지를 보여줍니다.

---

## 6. 🚀 실행 방법 (How to Run)

터미널에서 아래 명령어를 순서대로 입력하여 프로그램을 실행할 수 있습니다.

```bash
# 1. 원격 저장소 클론 (Clone)
git clone <https://github.com/>[본인-GitHub-계정]/[저장소-이름].git

# 2. 프로젝트 폴더로 이동
cd [저장소-이름]

# 3. 프로그램 실행
python main.py
```

---

## 7.1 Git 버전 관리 정책

과제 제약 사항에 맞춰 Git 버전 관리를 충실히 적용하였습니다.

커밋 이력: 기능 단위로 나눈 최소 10개 이상의 의미 있는 커밋 작성

브랜치 활용: feature/list-view (또는 해당 기능 브랜치) 별도 생성 후 작업 수행 ➔ main 브랜치로 merge 수행

Git 명령어 사용 이력: init, add, commit, push, pull, checkout, clone, merge 명령어 1회 이상 필수 실행 및 이력 보유

## 7.2 병합 충돌(Merge Conflict) 해결 가이드

본 프로젝트 개발 과정에서 발생할 수 있는 병합 충돌에 대한 원인 분석 및 해결 권장 절차는 다음과 같습니다.

### 1. 충돌 발생 원인

- 동일한 파일(`main.py`)의 동일한 코드 라인을 서로 다른 브랜치에서 동시에 수정 후 병합을 시도할 때 발생합니다.

### 2. 권장 해결 순서 (원인 확인 ➔ 수정 ➔ 테스트)

1. **원인 및 파일 확인**
    - 터미널에서 `git status`를 입력하여 충돌이 발생한 파일(`Unmerged paths`)을 확인합니다.
    - 해당 파일(`main.py`)을 열어 `<<<<<<<`, `=======`, `>>>>>>>` 표시가 위치한 충돌 구간을 파악합니다.
2. **충돌 코드 수정**
    - 프로젝트 요구사항에 맞는 올바른 코드(최신 중복 처리 로직)만 남겨두고, Git 충돌 표시 기호(`<<<`, `===`, `>>>`)를 모두 제거합니다.
    - `git add main.py`를 통해 수정된 파일의 충돌 해결 상태를 스테이징합니다.
    - `git commit`을 실행하여 충돌 해결 커밋을 완료합니다.
3. **검증 및 테스트**
    - `python main.py`를 실행하여 프로그램이 정상적으로 동작하는지 테스트합니다.
    - 중복 제목 입력 시 예외 처리 로직이 의도대로 동작하는지 확인합니다.
    - 이상이 없을 경우 `git push origin main`을 실행하여 원격 저장소에 최종 반영합니다.

---

## 8. 🎯 보너스 과제 구현 여부 (선택)

- [ ]  보너스 1: JSON 파일 데이터 저장/불러오기(영속화) 및 Markdown 파일 내보내기
- [ ]  보너스 2: 프롬프트 수정/삭제(CRUD) 및 상세 보기 조회수 집계/정렬 기능

(※ 보너스 과제를 구현하지 않은 경우 "해당 없음" 처리)

---

### 최종 제출물

**1.개발환경 설정 스크린샷**

<img width="429" height="151" alt="개발환경 설정 스크린샷" src="https://github.com/user-attachments/assets/36c4f2f8-993c-4199-a24d-3170b157448a" />

1) python --version

<img width="429" height="32" alt="python --version" src="https://github.com/user-attachments/assets/9fd4c8fa-7894-49e4-bd31-cee356367ef2" />

2) git --version

<img width="429" height="35" alt="git --version" src="https://github.com/user-attachments/assets/a77af660-485e-47d7-97e8-a6c341b498bc" />

3) git config user.name

<img width="429" height="35" alt="User name" src="https://github.com/user-attachments/assets/24803e19-f2ba-4b75-a2ea-1f702d3ab7a9" />

4) git config user.email

<img width="429" height="51" alt="user email" src="https://github.com/user-attachments/assets/a0aa8885-2553-4adb-9121-da445ddfe75d" />

---

## ⚠️ 중복 제목 발생 시 행동 규칙 (Policy)

프롬프트 관리 프로그램의 데이터 일관성과 고유성을 위해 **중복 제목 등록을 엄격히 거부(차단)**합니다.

**동작 규칙**:

1. 새 프롬프트 추가(`add_prompt`) 시, 입력받은 제목이 기존 프롬프트 목록에 이미 존재하는지 사전 검사합니다.
2. **중복 제목 발견 시**:
    - `"이미 존재하는 프롬프트 제목입니다. 다른 제목을 입력해 주세요."` 안내 메시지를 출력합니다.
    - 기존 데이터를 덮어쓰지 않고, 등록 절차를 중단하거나 올바른 제목을 재입력받도록 차단합니다.
    **이유**: 동일한 제목이 존재할 경우 프롬프트 단건 조회, 수정, 삭제 시 식별 충돌이 발생할 수 있으므로 제목의 고유성(Unique Key)을 보장합니다.

**중복 제목 발생 시 스크린샷**

<img width="675" height="311" alt="중복방지" src="https://github.com/user-attachments/assets/5db11b77-093c-41dc-b237-41ba8e53f4ea" />

---

## ✏️ 카테고리 및 프롬프트 수정(편집) 가이드

프로그램 내에서 이미 등록된 프롬프트의 카테고리, 제목, 내용을 수정하는 방법과 관련 코드 위치 안내입니다.

### 1. 수정 관련 담당 함수

- **`edit_prompt()`** (위치: `main.py` 내)
    - 프롬프트의 **카테고리 변경**, **제목 수정**, **내용 수정**을 담당하는 핵심 편집 함수입니다.
- **`CATEGORIES`** (위치: `main.py` 상단 전역 변수)
    - 새로 추가하거나 변경할 수 있는 카테고리 목록(리스트)이 정의된 위치입니다. 카테고리 종류 자체를 수정하고 싶다면 이 리스트를 수정합니다.

### 2. 카테고리 변경 기능 동작 방식

1. 메인 메뉴에서 **`8. 프롬프트 수정`** 선택 (내부적으로 `edit_prompt()` 호출)
2. 수정할 프롬프트 번호 선택
3. 제목 입력 단계 통과 후, **[카테고리 변경]** 안내에 따라 원하는 새 카테고리 번호 선택
4. 변경을 원치 않고 기존 카테고리를 유지할 경우 단순히 `Enter` 키를 입력하여 스킵 가능

---

**2.프로그램 실행 결과 스크린샷**

1)프롬프트 추가

<img width="374" height="288" alt="1  프롬프트 추가" src="https://github.com/user-attachments/assets/db345dc3-1527-406b-a783-00ddefab691c" />

2) 프롬프트 목록

<img width="279" height="327" alt="2  프롬프트 목록" src="https://github.com/user-attachments/assets/570a1d50-0420-487d-a237-3991c044d054" />


3) 카테고리별 조회

<img width="240" height="463" alt="3  카테고리별 조회" src="https://github.com/user-attachments/assets/d92fd051-2b75-4de8-bd53-e6f36ce509b1" />


4) 프롬프트 검색

<img width="278" height="330" alt="4  프롬프트 검색" src="https://github.com/user-attachments/assets/05b281f5-3a5e-4366-8051-c6dd26452bf7" />


5) 프롬프트 상세보기

<img width="271" height="429" alt="5  프롬프트 상세보기" src="https://github.com/user-attachments/assets/a0eb88dd-f015-4294-9565-4adb4fd977af" />


6) 즐겨찾기 관리

<img width="277" height="432" alt="6  즐겨찾기 관리" src="https://github.com/user-attachments/assets/075988a9-7d37-4dd1-a053-fd3dbdb51954" />


7) 즐겨찾기 목록

<img width="269" height="282" alt="7  즐겨찾기 목록" src="https://github.com/user-attachments/assets/17503872-1ab3-41f9-9b77-a551c5273567" />

8) 프롬프트 수정

<img width="278" height="435" alt="8  프롬프트 수정" src="https://github.com/user-attachments/assets/515e4705-6a9b-48e1-a769-b045b0706047" />

9) 종료

<img width="288" height="227" alt="0  종료" src="https://github.com/user-attachments/assets/d8418893-a3a2-46ce-8b9d-647797d5dd33" />


**3.git log 그래프 스크린샷**

<img width="622" height="603" alt="git log --oneline --graph" src="https://github.com/user-attachments/assets/70ac3a69-0c8c-4009-a675-bf9b734fd274" />

<img width="516" height="595" alt="스크린샷" src="https://github.com/user-attachments/assets/9489a383-f38f-422b-8e82-74f47ccb7404" />

**4.github 저장소 url**

[https://github.com/bomigrace-byte/bomi-prompt-manager]

**4.레포지토리 클론 실행
스크린샷

<img width="727" height="518" alt="클론" src="https://github.com/user-attachments/assets/f23c9255-8e75-48e9-84ae-e9df1bf3c1e1" />


**5.브랜치 생성/checkout 및 merge 실행
1) 스크린샷

<img width="902" height="649" alt="브랜치 생성,checkout 및 merge 실행" src="https://github.com/user-attachments/assets/14273e59-ba38-4dd4-bde7-e8d3f982dc5f" />

2) 터미널 로그

- 브랜치 생성

PS C:\Users\user\Desktop\bomi-prompt-manager> git checkout -b feature/test-branch
Switched to a new branch 'feature/test-branch'
   
- Merge

PS C:\Users\user\Desktop\bomi-prompt-manager> git commit --allow-empty -m "feat: 브랜치 병합 증거 작성을 위한 커밋"
[feature/test-branch d03890e] feat: 브랜치 병합 증거 작성을 위한 커밋
PS C:\Users\user\Desktop\bomi-prompt-manager> git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS C:\Users\user\Desktop\bomi-prompt-manager> git merge --no-ff feature/test-branch -m "merge: feature/test-branch 브랜치 병합"
Merge made by the 'ort' strategy.
PS C:\Users\user\Desktop\bomi-prompt-manager> git branch -a
  feature/test-branch
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
PS C:\Users\user\Desktop\bomi-prompt-manager> git log --oneline --graph -n 10
*   29b94c0 (HEAD -> main) merge: feature/test-branch 브랜치 병합
|\  
| * d03890e (feature/test-branch) feat: 브랜치 병합 증거 작성을 위한 커밋
|/  
* a9ab57b (origin/main, origin/HEAD) Update README with final submission details
* e855b6a main.py 수정
* cc3cd05 docs: README 마크다운 포맷 수정
* 546d655 docs: README 마크다운 포맷 수정
* 92a53c1 docs: README 표 마크다운 포맷 수정
* 4bcfb2e docs: README.md 작성 및 프로젝트 설명 추가
*   05c2c7f Merge branch 'main' of https://github.com/bomigrace-byte/bomi-prompt-manager
|\  
| * e780fa0 Update README.md
PS C:\Users\user\Desktop\bomi-prompt-manager> git push origin main
Enumerating objects: 2, done.
Counting objects: 100% (2/2), done.
Delta compression using up to 24 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 350 bytes | 350.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/bomigrace-byte/bomi-prompt-manager.git
   a9ab57b..29b94c0  main -> main



