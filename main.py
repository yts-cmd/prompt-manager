# 나만의 프롬프트 관리 프로그램

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

def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            print("[알림] 프롬프트 추가 기능은 준비 중입니다.")
        elif choice == "2":
            print("[알림] 프롬프트 목록 기능은 준비 중입니다.")
        elif choice == "3":
            print("[알림] 카테고리별 조회 기능은 준비 중입니다.")
        elif choice == "4":
            print("[알림] 프롬프트 검색 기능은 준비 중입니다.")
        elif choice == "5":
            print("[알림] 프롬프트 상세 보기 기능은 준비 중입니다.")
        elif choice == "6":
            print("[알림] 즐겨찾기 관리 기능은 준비 중입니다.")
        elif choice == "7":
            print("[알림] 즐겨찾기 목록 기능은 준비 중입니다.")
        elif choice == "0":
            print("프로그램을 종료합니다. 이용해 주셔서 감사합니다.")
            break
        else:
            print("[오류] 잘못된 번호입니다. 다시 입력해 주세요.")

if __name__ == "__main__":
    main()