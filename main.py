# =============================================
# 나만의 프롬프트 관리 프로그램
# =============================================

prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "회의록 요약 비서",
        "content": "당신은 회의록 전문 작성 AI입니다. 회의 내용을 간결하게 요약하고, 주요 결정 사항과 액션 아이템을 정리해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 배경은 흰색, 제품이 중앙에 위치하도록 해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 15년 경력의 IT 컨설턴트입니다. 기업의 디지털 전환 전략을 전문적으로 조언해주세요.",
        "category": "페르소나",
        "favorite": False
    }
]

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


# =============================================
# 함수 정의
# =============================================

def show_menu():
    """메뉴 출력 함수"""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정 (카테고리/제목/내용)")
    print("9. 프롬프트 삭제")  # 👈 추가
    print("0. 종료")


def add_prompt():
    """프롬프트 추가 함수 (중복 제목 검사 포함)"""
    global prompts
    print("\n=== 프롬프트 추가 ===")
    
    # 1. 제목 입력 및 중복 검사
    while True:
        title = input("제목 (0: 이전으로): ").strip()
        
        if title == "0":
            print("이전 메뉴로 돌아갑니다.")
            return
            
        if not title:
            print("제목을 입력해주세요!")
            continue
            
        # 중복 제목 검사 (공백 제거 및 대소문자 무시)
        user_title_clean = title.replace(" ", "").lower()
        is_duplicate = any(p["title"].replace(" ", "").lower() == user_title_clean for p in prompts)
        
        if is_duplicate:
            print("⚠️ 이미 존재하는 프롬프트 제목입니다. 다른 제목을 입력해주세요!")
            continue
            
        break

    # 2. 내용 입력
    while True:
        content = input("내용 (0: 이전으로): ").strip()
        if content == "0":
            print("이전 메뉴로 돌아갑니다.")
            return
        if content:
            break
        print("내용을 입력해주세요!")

    # 3. 카테고리 선택
    print("\n카테고리 선택 (0: 이전으로):")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")

    while True:
        choice = input("선택: ").strip()
        if choice == "0":
            print("이전 메뉴로 돌아갑니다.")
            return
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            category = CATEGORIES[int(choice) - 1]
            break
        print("올바른 번호를 입력해주세요!")

    # 4. 등록 완료
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print(f"\n✅ '{title}' 프롬프트가 추가되었습니다!")


def edit_prompt():
    """프롬프트 수정 함수 (카테고리, 제목, 내용 변경)"""
    print("\n=== 프롬프트 수정 ===")
    if not prompts:
        print("수정할 프롬프트가 없습니다.")
        return

    show_list()
    print("0) 이전으로")

    try:
        num = int(input("\n수정할 프롬프트 번호 선택: "))
        if num == 0:
            print("이전 메뉴로 돌아갑니다.")
            return
        if not (1 <= num <= len(prompts)):
            print("올바른 번호를 입력해주세요!")
            return

        target = prompts[num - 1]
        print(f"\n[현재 프롬프트 정보]")
        print(f"제목: {target['title']}")
        print(f"카테고리: {target['category']}")
        print(f"내용: {target['content']}")

        # 1. 새 제목 입력 (엔터 입력 시 기존 유지)
        new_title = input(f"\n새 제목 (기존 유지 시 Enter): ").strip()
        if new_title:
            # 중복 검사 (자기 자신 제외)
            user_title_clean = new_title.replace(" ", "").lower()
            is_dup = any(
                p["title"].replace(" ", "").lower() == user_title_clean and p != target
                for p in prompts
            )
            if is_dup:
                print("⚠️ 이미 존재하는 제목이어서 기존 제목을 유지합니다.")
            else:
                target["title"] = new_title

        # 2. 새 카테고리 선택 (엔터 입력 시 기존 유지)
        print("\n[카테고리 변경]")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"{i}) {cat}")
        cat_choice = input(f"새 카테고리 번호 선택 (기존 [{target['category']}] 유지 시 Enter): ").strip()
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(CATEGORIES):
            target["category"] = CATEGORIES[int(cat_choice) - 1]

        # 3. 새 내용 입력 (엔터 입력 시 기존 유지)
        new_content = input(f"\n새 내용 (기존 유지 시 Enter): ").strip()
        if new_content:
            target["content"] = new_content

        print(f"\n✅ '{target['title']}' 프롬프트 정보가 정상적으로 수정되었습니다!")

    except ValueError:
        print("숫자를 입력해주세요!")


def delete_prompt():
    """프롬프트 삭제 함수"""
    print("\n=== 프롬프트 삭제 ===")
    if not prompts:
        print("삭제할 프롬프트가 없습니다.")
        return

    show_list()
    print("0) 이전으로")

    try:
        num = int(input("\n삭제할 프롬프트 번호 선택: "))
        if num == 0:
            print("이전 메뉴로 돌아갑니다.")
            return

        if 1 <= num <= len(prompts):
            # pop()을 사용하여 선택한 번호(인덱스 = 번호 - 1)의 항목을 삭제 및 반환
            removed = prompts.pop(num - 1)
            print(f"\n✅ '{removed['title']}' 프롬프트가 삭제되었습니다.")
        else:
            print("올바른 번호를 입력해주세요!")

    except ValueError:
        print("숫자를 입력해주세요!")        


def show_list():
    """전체 목록 출력 함수"""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, prompt in enumerate(prompts, 1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")
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
            print("이전 메뉴로 돌아갑니다.")
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
        print(f"{i}. {prompt['title']} {star}")
    print(f"\n총 {len(result)}개의 프롬프트")


def search_prompt():
    """검색 함수"""
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어 (0: 이전으로): ").strip()
    if keyword == "0":
        print("이전 메뉴로 돌아갑니다.")
        return
    if not keyword:
        print("검색어를 입력해주세요!")
        return
    result = [p for p in prompts if keyword in p["title"] or keyword in p["content"]]
    print(f"\n검색 결과:")
    if not result:
        print("검색 결과가 없습니다.")
        return
    for i, prompt in enumerate(result, 1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")
    print(f"\n{len(result)}개의 프롬프트를 찾았습니다.")


def show_detail():
    """상세 보기 함수"""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    show_list()
    print("0) 이전으로")

    try:
        num = int(input("\n번호 입력: "))
        if num == 0:
            print("이전 메뉴로 돌아갑니다.")
            return
        if 1 <= num <= len(prompts):
            prompt = prompts[num - 1]
            star = "⭐" if prompt["favorite"] else "없음"
            print("\n" + "─" * 30)
            print(f"제목: {prompt['title']}")
            print(f"카테고리: {prompt['category']}")
            print(f"즐겨찾기: {star}")
            print("─" * 30)
            print("내용:\n" + prompt["content"])
            print("─" * 30)
        else:
            print("올바른 번호를 입력해주세요!")
    except ValueError:
        print("숫자를 입력해주세요!")


def manage_favorite():
    """즐겨찾기 추가/해제 함수"""
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    show_list()
    print("0) 이전으로")

    try:
        num = int(input("\n프롬프트 번호 입력: "))
        if num == 0:
            print("이전 메뉴로 돌아갑니다.")
            return
        if 1 <= num <= len(prompts):
            prompt = prompts[num - 1]
            prompt["favorite"] = not prompt["favorite"]
            status = "추가" if prompt["favorite"] else "해제"
            print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에 {status}했습니다!")
        else:
            print("올바른 번호를 입력해주세요!")
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
    print(f"\n총 {len(result)}개의 즐겨찾기")


def main():
    """메인 함수"""
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
            manage_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "8":
            edit_prompt()
        elif choice == "9":        # 👈 추가
            delete_prompt()     # 👈 추가
        elif choice == "0":
            print("\n프로그램을 종료합니다. 안녕히가세요! 👋")
            break
        else:
            print("올바른 번호를 입력해주세요!")


if __name__ == "__main__":
    main()