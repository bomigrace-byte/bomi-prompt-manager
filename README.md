
# 📌 나만의 프롬프트 관리자 (Prompt Manager)

> 파편화된 프롬프트를 한곳에서 저장, 조회, 검색, 즐겨찾기하고 관리할 수 있는 파이썬 콘솔 기반 프로그램입니다.

---

## 1. 📖 프로젝트 개요

개발 목적: 다양한 GenAI 도구를 사용하며 흩어진 프롬프트를 체계적으로 정리하고 다룰 수 있는 나만의 프롬프트 집(House)을 구축합니다.

* 학습 목표: 
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
| :---: | :--- | :--- |
| 0 | 프로그램 종료 | 루프를 종료하고 프로그램을 안전하게 마칩니다. |
| 1 | 프롬프트 추가 | 제목, 내용, 카테고리를 입력받아 신규 등록 (add_prompt()) |
| 2 | 프롬프트 목록 | 전체 프롬프트 번호, 카테고리, 제목, 즐겨찾기(⭐) 표출 (show_list()) |
| 3 | 카테고리별 조회 | 지정한 카테고리의 프롬프트만 필터링 출력 (show_by_category()) |
| 4 | 프롬프트 검색 | 키워드 입력으로 제목 및 내용 통합 검색 (search_prompt()) |
| 5 | 상세 보기 | 프롬프트 번호 선택 시 제목, 카테고리, 즐겨찾기, 전체 본문 출력 (show_detail()) |
| 6 | 즐겨찾기 관리 | 특정 프롬프트의 즐겨찾기 상태 토글(ON/OFF) (toggle_favorite()) |
| 7 | 즐겨찾기 목록 | 즐겨찾기 등록된 프롬프트만 모아보기 (show_favorites()) |


기본 탑재 데이터: 프로그램 시작 시 최소 3개 이상의 프롬프트 기본 제공

---

## 4. 🏷️ 등록된 프롬프트 카테고리

프로그램 내에서 다루는 주요 프롬프트 카테고리는 다음과 같습니다:

1. 텍스트 생성: 블로그 글 작성, 이메일 작성, 요약 등 문장 생성용 프롬프트
2. 이미지 생성: Midjourney, DALL-E 등 AI 이미지 생성을 위한 키워드/스타일 프롬프트
3. 영상 생성: 비디오 스크립트 작성 및 숏폼 영상 기획용 프롬프트
4. 페르소나: 특정 분야 전문가 및 페르소나 부여용 지시문 프롬프트
5. 자동화: 업무 자동화 및 노코드 파이프라인 연동용 프롬프트
6. 기타: 기타 자유 주제의 프롬프트

---

## 5. 🚀 실행 방법 (How to Run)

터미널에서 아래 명령어를 순서대로 입력하여 프로그램을 실행할 수 있습니다.

```bash
# 1. 원격 저장소 클론 (Clone)
git clone [https://github.com/](https://github.com/)[본인-GitHub-계정]/[저장소-이름].git

# 2. 프로젝트 폴더로 이동
cd [저장소-이름]

# 3. 프로그램 실행
python main.py

```

---

## 6. Git / GitHub 버전 관리 이력
과제 제약 사항에 맞춰 Git 버전 관리를 충실히 적용하였습니다.

커밋 이력: 기능 단위로 나눈 최소 10개 이상의 의미 있는 커밋 작성

브랜치 활용: feature/list-view (또는 해당 기능 브랜치) 별도 생성 후 작업 수행 ➔ main 브랜치로 merge 수행

Git 명령어 사용 이력: init, add, commit, push, pull, checkout, clone, merge 명령어 1회 이상 필수 실행 및 이력 보유

---

## 7. 🎯 보너스 과제 구현 여부 (선택)
[ ] 보너스 1: JSON 파일 데이터 저장/불러오기(영속화) 및 Markdown 파일 내보내기

[ ] 보너스 2: 프롬프트 수정/삭제(CRUD) 및 상세 보기 조회수 집계/정렬 기능

(※ 보너스 과제를 구현하지 않은 경우 "해당 없음" 처리)

---
### 최종 제출물

**1.개발환경 설정 스크린샷**

<img width="429" height="151" alt="개발환경 설정 스크린샷" src="https://github.com/user-attachments/assets/36c4f2f8-993c-4199-a24d-3170b157448a" />


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


8) 종료

<img width="288" height="227" alt="0  종료" src="https://github.com/user-attachments/assets/d8418893-a3a2-46ce-8b9d-647797d5dd33" />


**3.git log 그래프 스크린샷**

<img width="622" height="603" alt="git log --oneline --graph" src="https://github.com/user-attachments/assets/70ac3a69-0c8c-4009-a675-bf9b734fd274" />

**4.github 저장소 url**

[https://github.com/bomigrace-byte/bomi-prompt-manager]
