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

print(f"등록된 기본 프롬프트 개수: {len(prompts)}개")