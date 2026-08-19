import json  # 참조: JSON 파일 처리를 위한 라이브러리 추가
import os    # 참조: 파일 존재 여부 확인을 위한 라이브러리 추가

# =============================================
# 나만의 프롬프트 관리 프로그램 (데이터 영속화 및 조회수 기능 추가)
# =============================================

FILE_PATH = "prompts.json"  # 참조: 데이터 저장 파일 경로 설정
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 기본 데이터 (파일이 없을 때 초기화용)
default_prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False,
        "views": 0  # 참조: 조회수 항목 추가
    },
    {
        "title": "회의록 요약 비서",
        "content": "당신은 회의록 전문 작성 AI입니다. 회의 내용을 간결하게 요약하고, 주요 결정 사항과 액션 아이템을 정리해주세요.",
        "category": "텍스트 생성",
        "favorite": True,
        "views": 0  # 참조: 조회수 항목 추가
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 배경은 흰색, 제품이 중앙에 위치하도록 해주세요.",
        "category": "이미지 생성",
        "favorite": False,
        "views": 0  # 참조: 조회수 항목 추가
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 15년 경력의 IT 컨설턴트입니다. 기업의 디지털 전환 전략을 전문적으로 조언해주세요.",
        "category": "페르소나",
        "favorite": False,
        "views": 0  # 참조: 조회수 항목 추가
    }
]


# =============================================
# 참조: 파일 입출력 및 데이터 영속화 함수
# =============================================

def load_prompts():
    """참조: JSON 파일에서 프롬프트 데이터 불러오기"""
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                # 이전 데이터 구조 호환성 유지 (views 필드 보장)
                for p in data:
                    if "views" not in p:
                        p["views"] = 0
                return data
        except Exception as e:
            print(f"⚠️ 파일 불러오기 실패 ({e}). 기본 데이터를 사용합니다.")
    return default_prompts


def save_prompts():
    """참조: 변경된 데이터를 JSON 파일로 자동 저장"""
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(prompts, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"⚠️ 파일 저장 실패: {e}")


# 프로그램 실행 시 데이터 로드
prompts = load_prompts()


# =============================================
# 참조: Markdown 내보내기 함수 (보너스 1)
# =============================================

def export_to_markdown():
    """참조: 전체 프롬프트를 카테고리별 Markdown(.md) 파일로 저장"""
    print("\n=== Markdown 내보내기 ===")
    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return

    exported_count = 0
    for cat in CATEGORIES:
        cat_prompts = [p for p in prompts if p["category"] == cat]
        if not cat_prompts:
            continue

        filename = f"prompts_{cat.replace(' ', '_')}.md"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"# 📂 {cat} 프롬프트 모음\n\n")
                for p in cat_prompts:
                    star = "⭐ " if p["favorite"] else ""
                    f.write(f"## {star}{p['title']}\n")
                    f.write(f"- **조회수**: {p.get('views', 0)}회\n\n")
                    f.write("```\n")
                    f.write(f"{p['content']}\n")
                    f.write("```\n\n")
                    f.write("---\n\n")
            print(f"📄 '{filename}' 파일 생성 완료")
            exported_count += 1
        except Exception as e:
            print(f"⚠️ {filename} 저장 중 오류: {e}")

    if exported_count > 0:
        print(f"\n✅ 총 {exported_count}개의 카테고리별 Markdown 파일이 내보내졌습니다.")


# =============================================
# 프롬프트 관리 기능
# =============================================

def show_menu():
    """메뉴 출력 함수 (참조: 신규 번호 체계 반영)"""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기 (조회수 +1)")  # 참조: 기능 설명 수정
    print("6. 인기 프롬프트 Top 목록")          # 참조: 신규 메뉴 추가
    print("7. 즐겨찾기 관리")
    print("8. 즐겨찾기 목록")
    print("9. 프롬프트 수정")
    print("10. 프롬프트 삭제")
    print("11. Markdown으로 내보내기")          # 참조: 신규 메뉴 추가
    print("0. 종료")


def add_prompt():
    """프롬프트 추가 함수"""
    print("\n=== 프롬프트 추가 ===")
    while True:
        title = input("제목 (0: 이전으로): ").strip()
        if title == "0":
            return
        if not title:
            print("제목을 입력해주세요!")
            continue

        user_title_clean = title.replace(" ", "").lower()
        if any(p["title"].replace(" ", "").lower() == user_title_clean for p in prompts):
            print("⚠️ 이미 존재하는 프롬프트 제목입니다.")
            continue
        break

    while True:
        content = input("내용 (0: 이전으로): ").strip()
        if content == "0":
            return
        if content:
            break
        print("내용을 입력해주세요!")

    print("\n카테고리 선택 (0: 이전으로):")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")

    while True:
        choice = input("선택: ").strip()
        if choice == "0":
            return
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            category = CATEGORIES[int(choice) - 1]
            break
        print("올바른 번호를 입력해주세요!")

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "views": 0  # 참조: 초기 조회수 설정
    })
    save_prompts()  # 참조: 파일 자동 저장 연동
    print(f"\n✅ '{title}' 프롬프트가 추가되었습니다!")


def show_list():
    """전체 목록 출력 함수"""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, prompt in enumerate(prompts, 1):
        star = "⭐" if prompt["favorite"] else ""
        views = prompt.get("views", 0)  # 참조: 조회수 표시
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star} (조회수: {views})")
    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    """카테고리별 조회 함수"""
    print("\n=== 카테고리별 조회 ===")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")
    print("0) 이전으로")

    while True:
        choice = input("선택: ").strip()
        if choice == "0":
            return
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            selected = CATEGORIES[int(choice) - 1]
            break
        print("올바른 번호를 입력해주세요!")

    result = [p for p in prompts if p["category"] == selected]
    print(f"\n[{selected}] 카테고리 프롬프트:")
    if not result:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return
    for i, prompt in enumerate(result, 1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. {prompt['title']} {star} (조회수: {prompt.get('views', 0)})")


def search_prompt():
    """검색 함수"""
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어 (0: 이전으로): ").strip()
    if keyword == "0" or not keyword:
        return
    result = [p for p in prompts if keyword in p["title"] or keyword in p["content"]]
    print(f"\n검색 결과:")
    if not result:
        print("검색 결과가 없습니다.")
        return
    for i, prompt in enumerate(result, 1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")


def show_detail():
    """상세 보기 및 조회수 카운트 함수 (보너스 2)"""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    show_list()
    print("0) 이전으로")

    try:
        num = int(input("\n번호 입력: "))
        if num == 0:
            return
        if 1 <= num <= len(prompts):
            prompt = prompts[num - 1]
            
            # 참조: 상세 조회의 핵심 - 조회수 1 증가 및 저장
            prompt["views"] = prompt.get("views", 0) + 1
            save_prompts()

            star = "⭐" if prompt["favorite"] else "없음"
            print("\n" + "─" * 30)
            print(f"제목: {prompt['title']}")
            print(f"카테고리: {prompt['category']}")
            print(f"즐겨찾기: {star}")
            print(f"조회수: {prompt['views']}회")  # 참조: 조회수 출력
            print("─" * 30)
            print("내용:\n" + prompt["content"])
            print("─" * 30)
        else:
            print("올바른 번호를 입력해주세요!")
    except ValueError:
        print("숫자를 입력해주세요!")


def show_top_prompts():
    """참조: 조회수 기준 정렬 및 Top 5 출력 함수 (보너스 2)"""
    print("\n=== 인기 프롬프트 (조회수 Top) ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 참조: sorted() 함수와 lambda 키를 활용한 내림차순 정렬
    sorted_prompts = sorted(prompts, key=lambda x: x.get("views", 0), reverse=True)
    
    for i, prompt in enumerate(sorted_prompts[:5], 1):  # 상위 5개까지 제한
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}위. [{prompt['category']}] {prompt['title']} {star} - {prompt.get('views', 0)}회")


def manage_favorite():
    """즐겨찾기 추가/해제 함수"""
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        return
    show_list()
    try:
        num = int(input("\n프롬프트 번호 입력 (0: 이전으로): "))
        if num == 0:
            return
        if 1 <= num <= len(prompts):
            prompt = prompts[num - 1]
            prompt["favorite"] = not prompt["favorite"]
            save_prompts()  # 참조: 변경사항 저장
            status = "추가" if prompt["favorite"] else "해제"
            print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에 {status}했습니다!")
    except ValueError:
        print("숫자를 입력해주세요!")


def show_favorites():
    """즐겨찾기 목록 함수"""
    print("\n=== 즐겨찾기 목록 ===")
    result = [p for p in prompts if p["favorite"]]
    if not result:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return
    for i, prompt in enumerate(result, 1):
        print(f"{i}. [{prompt['category']}] {prompt['title']} ⭐")


def edit_prompt():
    """수정 함수 (CRUD)"""
    print("\n=== 프롬프트 수정 ===")
    if not prompts:
        return
    show_list()
    try:
        num = int(input("\n수정할 번호 선택 (0: 이전으로): "))
        if num == 0 or not (1 <= num <= len(prompts)):
            return

        target = prompts[num - 1]
        new_title = input(f"새 제목 (기존 유지 시 Enter): ").strip()
        if new_title:
            user_title_clean = new_title.replace(" ", "").lower()
            if not any(p["title"].replace(" ", "").lower() == user_title_clean and p != target for p in prompts):
                target["title"] = new_title

        print("\n[카테고리 변경]")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"{i}) {cat}")
        cat_choice = input(f"새 번호 선택 (기존 [{target['category']}] 유지 시 Enter): ").strip()
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(CATEGORIES):
            target["category"] = CATEGORIES[int(cat_choice) - 1]

        new_content = input(f"새 내용 (기존 유지 시 Enter): ").strip()
        if new_content:
            target["content"] = new_content

        save_prompts()  # 참조: 수정내용 영구 저장
        print(f"\n✅ 수정이 완료되었습니다!")
    except ValueError:
        print("숫자를 입력해주세요!")


def delete_prompt():
    """삭제 함수 (CRUD)"""
    print("\n=== 프롬프트 삭제 ===")
    if not prompts:
        return
    show_list()
    try:
        num = int(input("\n삭제할 번호 선택 (0: 이전으로): "))
        if num == 0:
            return
        if 1 <= num <= len(prompts):
            removed = prompts.pop(num - 1)
            save_prompts()  # 참조: 삭제내용 영구 저장
            print(f"\n✅ '{removed['title']}' 프롬프트가 삭제되었습니다.")
    except ValueError:
        print("숫자를 입력해주세요!")


# =============================================
# 메인 제어 루프
# =============================================

def main():
    while True:
        show_menu()
        choice = input("\n선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            show_top_prompts()   # 참조: 인기 목록 분기 연결
        elif choice == "7":
            manage_favorite()
        elif choice == "8":
            show_favorites()
        elif choice == "9":
            edit_prompt()
        elif choice == "10":
            delete_prompt()
        elif choice == "11":
            export_to_markdown()  # 참조: MD 내보내기 분기 연결
        elif choice == "0":
            print("\n프로그램을 종료합니다. 안녕히가세요! 👋")
            break
        else:
            print("올바른 번호를 입력해주세요!")


if __name__ == "__main__":
    main()