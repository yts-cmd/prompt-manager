# 나만의 프롬프트 관리 프로그램

# 기본 카테고리 목록
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 기본 프롬프트 데이터 (최소 3개 등록)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "주어진 주제에 대해 SEO에 최적화된 블로그 글을 서론, 본론, 결론 구조로 작성해줘.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "쇼핑몰 상세페이지에 어울리는 미니멀하고 고급스러운 제품 썸네일 이미지를 묘사해줘.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "너는 15년 차 IT 전략 컨설턴트야. 기업의 클라우드 전환 전략에 대해 전문적으로 조언해줘.",
        "category": "페르소나",
        "favorite": False
    }
]

def show_menu():
    """메인 메뉴 출력 함수"""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    print("===========================")

def add_prompt():
    """새로운 프롬프트 등록 함수"""
    print("\n=== 프롬프트 추가 ===")
    
    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("[경고] 제목은 비어 있을 수 없습니다. 다시 입력해 주세요.")

    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("[경고] 내용은 비어 있을 수 없습니다. 다시 입력해 주세요.")

    print("\n카테고리 선택:")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}) {cat}")

    while True:
        cat_choice = input("선택: ").strip()
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(CATEGORIES):
            category = CATEGORIES[int(cat_choice) - 1]
            break
        print("[경고] 올바른 카테고리 번호를 선택해 주세요.")

    new_item = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_item)
    print("\n프롬프트가 성공적으로 추가되었습니다!")

def show_list():
    """저장된 전체 프롬프트