import streamlit as st

st.set_page_config(
    page_title="MBTI 책 & 영화 추천",
    page_icon="📚"
)

st.title("📚 MBTI 책 & 영화 추천 프로그램")
st.write("MBTI를 선택하면 어울리는 책과 영화를 추천해줘요!")

mbti_data = {
    "INTJ": {
        "movies": [
            {
                "title": "인터스텔라",
                "reason": "깊게 생각하고 미래를 분석하는 성향에게 잘 어울리는 영화"
            },
            {
                "title": "이미테이션 게임",
                "reason": "논리적이고 전략적인 사고를 좋아하는 사람에게 추천"
            }
        ],
        "books": [
            {
                "title": "데미안",
                "reason": "자기 성찰을 좋아하는 사람에게 적합한 책"
            },
            {
                "title": "사피엔스",
                "reason": "지적 호기심이 강한 사람에게 추천"
            }
        ]
    },

    "INTP": {
        "movies": [
            {
                "title": "매트릭스",
                "reason": "철학적이고 분석적인 사람에게 어울리는 영화"
            },
            {
                "title": "인셉션",
                "reason": "복잡한 전개와 사고를 좋아하는 사람에게 추천"
            }
        ],
        "books": [
            {
                "title": "코스모스",
                "reason": "과학과 탐구를 좋아하는 사람에게 적합"
            },
            {
                "title": "1984",
                "reason": "사회 구조를 깊게 생각하는 사람에게 추천"
            }
        ]
    },

    "ENTJ": {
        "movies": [
            {
                "title": "아이언맨",
                "reason": "리더십과 추진력을 가진 사람에게 잘 맞는 영화"
            },
            {
                "title": "울프 오브 월스트리트",
                "reason": "도전적이고 목표 지향적인 성향에게 추천"
            }
        ],
        "books": [
            {
                "title": "자기관리론",
                "reason": "성공과 목표 달성을 중요하게 생각하는 사람에게 추천"
            },
            {
                "title": "넛지",
                "reason": "전략적 사고를 좋아하는 사람에게 적합"
            }
        ]
    },

    "ENTP": {
        "movies": [
            {
                "title": "셜록 홈즈",
                "reason": "아이디어가 많고 추리를 좋아하는 사람에게 추천"
            },
            {
                "title": "나우 유 씨 미",
                "reason": "창의적이고 새로운 것을 좋아하는 성향과 잘 맞음"
            }
        ],
        "books": [
            {
                "title": "트렌드 코리아",
                "reason": "새로운 흐름에 관심이 많은 사람에게 추천"
            },
            {
                "title": "해리포터",
                "reason": "상상력이 풍부한 사람에게 적합"
            }
        ]
    },

    "INFJ": {
        "movies": [
            {
                "title": "소울",
                "reason": "감성적이고 의미를 중요하게 생각하는 사람에게 추천"
            },
            {
                "title": "죽은 시인의 사회",
                "reason": "이상과 가치관을 중요하게 여기는 성향과 잘 맞음"
            }
        ],
        "books": [
            {
                "title": "어린 왕자",
                "reason": "따뜻한 감성과 깊은 생각을 가진 사람에게 적합"
            },
            {
                "title": "미움받을 용기",
                "reason": "인간관계와 삶의 의미를 고민하는 사람에게 추천"
            }
        ]
    },

    "INFP": {
        "movies": [
            {
                "title": "라라랜드",
                "reason": "감성적이고 꿈을 중요하게 생각하는 사람에게 추천"
            },
            {
                "title": "월플라워",
                "reason": "섬세한 감정을 가진 사람에게 잘 어울림"
            }
        ],
        "books": [
            {
                "title": "나미야 잡화점의 기적",
                "reason": "따뜻한 이야기를 좋아하는 사람에게 적합"
            },
            {
                "title": "연금술사",
                "reason": "꿈과 인생의 의미를 고민하는 사람에게 추천"
            }
        ]
    },

    "ENFJ": {
        "movies": [
            {
                "title": "코코",
                "reason": "사람과 관계를 중요하게 생각하는 사람에게 추천"
            },
            {
                "title": "위대한 쇼맨",
                "reason": "열정적이고 사람들을 이끄는 성향과 잘 맞음"
            }
        ],
        "books": [
            {
                "title": "아몬드",
                "reason": "감정과 공감을 중요하게 여기는 사람에게 적합"
            },
            {
                "title": "페인트",
                "reason": "사람 사이의 관계를 좋아하는 사람에게 추천"
            }
        ]
    },

    "ENFP": {
        "movies": [
            {
                "title": "업",
                "reason": "모험과 자유를 좋아하는 사람에게 추천"
            },
            {
                "title": "스파이더맨: 뉴 유니버스",
                "reason": "에너지 넘치고 창의적인 사람과 잘 맞음"
            }
        ],
        "books": [
            {
                "title": "모모",
                "reason": "상상력이 풍부한 사람에게 적합"
            },
            {
                "title": "해변의 카프카",
                "reason": "감성과 자유로운 사고를 가진 사람에게 추천"
            }
        ]
    },

    "ISTJ": {
        "movies": [
            {
                "title": "포레스트 검프",
                "reason": "성실하고 책임감 있는 사람에게 추천"
            },
            {
                "title": "설리: 허드슨강의 기적",
                "reason": "침착하고 현실적인 성향과 잘 맞음"
            }
        ],
        "books": [
            {
                "title": "총균쇠",
                "reason": "체계적인 지식을 좋아하는 사람에게 적합"
            },
            {
                "title": "국부론",
                "reason": "논리와 현실을 중요하게 생각하는 사람에게 추천"
            }
        ]
    },

    "ISFJ": {
        "movies": [
            {
                "title": "리틀 포레스트",
                "reason": "따뜻하고 안정적인 분위기를 좋아하는 사람에게 추천"
            },
            {
                "title": "인사이드 아웃",
                "reason": "감정 공감 능력이 높은 사람과 잘 맞음"
            }
        ],
        "books": [
            {
                "title": "완득이",
                "reason": "따뜻한 인간관계를 좋아하는 사람에게 적합"
            },
            {
                "title": "불편한 편의점",
                "reason": "편안하고 감동적인 이야기를 좋아하는 사람에게 추천"
            }
        ]
    },

    "ESTJ": {
        "movies": [
            {
                "title": "탑건: 매버릭",
                "reason": "목표 지향적이고 책임감 있는 사람에게 추천"
            },
            {
                "title": "머니볼",
                "reason": "현실적이고 전략적인 사고를 좋아하는 사람과 잘 맞음"
            }
        ],
        "books": [
            {
                "title": "원씽",
                "reason": "효율과 목표 달성을 중요하게 생각하는 사람에게 적합"
            },
            {
                "title": "그릿",
                "reason": "끈기와 노력의 가치를 중요하게 여기는 사람에게 추천"
            }
        ]
    },

    "ESFJ": {
        "movies": [
            {
                "title": "맘마미아",
                "reason": "사람들과 어울리는 걸 좋아하는 사람에게 추천"
            },
            {
                "title": "겨울왕국",
                "reason": "따뜻한 관계와 감정을 중요하게 여기는 성향과 잘 맞음"
            }
        ],
        "books": [
            {
                "title": "아주 작은 습관의 힘",
                "reason": "꾸준함과 일상을 중요하게 생각하는 사람에게 적합"
            },
            {
                "title": "오베라는 남자",
                "reason": "정이 많고 공감 능력이 높은 사람에게 추천"
            }
        ]
    },

    "ISTP": {
        "movies": [
            {
                "title": "분노의 질주",
                "reason": "스릴과 행동 중심의 영화를 좋아하는 사람에게 추천"
            },
            {
                "title": "존 윅",
                "reason": "조용하지만 강한 매력을 가진 성향과 잘 맞음"
            }
        ],
        "books": [
            {
                "title": "삼국지",
                "reason": "전략과 상황 판단을 좋아하는 사람에게 적합"
            },
            {
                "title": "드래곤 라자",
                "reason": "모험과 자유로운 분위기를 좋아하는 사람에게 추천"
            }
        ]
    },

    "ISFP": {
        "movies": [
            {
                "title": "미드나잇 인 파리",
                "reason": "예술적 감성과 감성을 중요하게 생각하는 사람에게 추천"
            },
            {
                "title": "너의 이름은",
                "reason": "감성적이고 섬세한 사람과 잘 맞음"
            }
        ],
        "books": [
            {
                "title": "채식주의자",
                "reason": "감정선이 깊은 이야기를 좋아하는 사람에게 적합"
            },
            {
                "title": "달러구트 꿈 백화점",
                "reason": "따뜻한 상상력을 가진 사람에게 추천"
            }
        ]
    },

    "ESTP": {
        "movies": [
            {
                "title": "베이비 드라이버",
                "reason": "속도감 있고 활동적인 영화를 좋아하는 사람에게 추천"
            },
            {
                "title": "미션 임파서블",
                "reason": "도전과 액션을 즐기는 성향과 잘 맞음"
            }
        ],
        "books": [
            {
                "title": "부의 추월차선",
                "reason": "현실적이고 도전적인 사람에게 적합"
            },
            {
                "title": "아웃라이어",
                "reason": "성공과 경험을 중요하게 생각하는 사람에게 추천"
            }
        ]
    },

    "ESFP": {
        "movies": [
            {
                "title": "알라딘",
                "reason": "밝고 자유로운 분위기를 좋아하는 사람에게 추천"
            },
            {
                "title": "싱 스트리트",
                "reason": "음악과 열정을 좋아하는 사람과 잘 맞음"
            }
        ],
        "books": [
            {
                "title": "미드나잇 라이브러리",
                "reason": "감성과 재미를 중요하게 생각하는 사람에게 적합"
            },
            {
                "title": "구의 증명",
                "reason": "감정 표현이 풍부한 사람에게 추천"
            }
        ]
    }
}

selected_mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(mbti_data.keys())
)

if st.button("추천 보기"):
    data = mbti_data[selected_mbti]

    st.header(f"✨ {selected_mbti} 추천 영화")

    for movie in data["movies"]:
        st.subheader(f"🎬 {movie['title']}")
        st.write(f"✔ 추천 이유: {movie['reason']}")
        st.markdown("---")

    st.header(f"📚 {selected_mbti} 추천 책")

    for book in data["books"]:
        st.subheader(f"📖 {book['title']}")
        st.write(f"✔ 추천 이유: {book['reason']}")
        st.markdown("---")
