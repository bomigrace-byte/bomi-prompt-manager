# =============================================
# 나만의 프롬프트 관리 프로그램
# =============================================

# 📌 기본 데이터 (이전 미션 프롬프트 3개 이상 등록)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 이미지 생성",
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

# 카테고리 목록
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


# =============================================
# 함수 정의
# =============================================

def show_menu():
    """메뉴를 출력하는 함수"""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 추가/해제")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def add_prompt():
    """프롬프트를 추가하는 함수"""
    print("\n=== 프롬프트 추가 ===")
    
    # 제목 입력 (빈 값이면 다시 요청)
    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("제목을 입력해주세요!")
    
    # 내용 입력
    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("내용을 입력해주세요!")
    
    # 카테고리 선택
    print("\n카테고리 선택:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")
    
    while True:
        choice = input("선택: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            category = CATEGORIES[int(choice) - 1]
            break
        print("올바른 번호를 입력해주세요!")
    
    # 프롬프트 저장
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False  # 기본값은 False
    }
    prompts.append(new_prompt)
    print(f"\n✅ '{title}' 프롬프트가 추가되었습니다!")


def show_list():
    """전체 프롬프트 목록을 출력하는 함수"""
    print("\n=== 프롬프트 목록 ===")
    
    if not prompts:  # 프롬프트가 없으면
        print("등록된 프롬프트가 없습니다.")
        return
    
    for i, prompt in enumerate(prompts, 1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")
    
    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    """카테고리별로 프롬프트를 조회하는 함수"""
    print("\n=== 카테고리별 조회 ===")
    
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")
    
    while True:
        choice = input("선택: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            selected = CATEGORIES[int(choice) - 1]
            break
        print("올바른 번호를 입력해주세요!")
    
    # 선택한 카테고리 필터링
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
    """키워드로 프롬프트를 검색하는 함수"""
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip()
    
    if not keyword:
        print("검색어를 입력해주세요!")
        return
    
    # 제목 또는 내용에 키워드가 포함된 것 검색
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
    """프롬프트 상세 내용을 보여주는 함수"""
    print("\n=== 프롬프트 상세 보기 ===")
    
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    
    try:
        num = int(input("번호 입력: "))
        if 1 <= num <= len(prompts):
            prompt = prompts[num - 1]
            star = "⭐" if prompt["favorite"] else "없음"
            
            print("\n" + "─" * 30)
            print(f"제목: {prompt['title']}")
            print(f"카테고리: {prompt['category']}")
            print(f"즐겨찾기: {star}")
            print("─" * 30)
            print("내용:")
            print(prompt["content"])
            print("─" * 30)
        else:
            print("올바른 번호를 입력해주세요!")
    except ValueError:
        print("숫자를 입력해주세요!")


def manage_favorite():
    """즐겨찾기를 추가/해제하는 함수"""
    print("\n=== 즐겨찾기 관리 ===")
    
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    
    show_list()  # 목록 먼저 보여주기
    
    try:
        num = int(input("\n프롬프트 번호 입력: "))
        if 1 <= num <= len(prompts):
            prompt = prompts[num - 1]
            prompt["favorite"] = not prompt["favorite"]  # True↔False 전환
            
            if prompt["favorite"]:
                print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에 추가했습니다! ⭐")
            else:
                print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에서 해제했습니다.")
        else:
            print("올바른 번호를 입력해주세요!")
    except ValueError:
        print("숫자를 입력해주세요!")


def show_favorites():
    """즐겨찾기 목록을 보여주는 함수"""
    print("\n=== 즐겨찾기 목록 ===")
    
    result = [p for p in prompts if p["favorite"]]
    
    if not result:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return
    
    for i, prompt in enumerate(result, 1):
        print(f"{i}. [{prompt['category']}] {prompt['title']} ⭐")
    
    print(f"\n총 {len(result)}개의 즐겨찾기")


# =============================================
# 메인 실행 부분
# =============================================

def main():
    """프로그램 시작점"""
    print("프롬프트 관리 프로그램을 시작합니다!")
    
    while True:
        show_menu()
        choice = input("선택: ").strip()
        
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
        elif choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요! 👋")
            break
        else:
            print("⚠️ 올바른 번호를 입력해주세요!")


# 프로그램 실행
if __name__ == "__main__":
    main()
    