import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천", page_icon="💼")

st.title("💼 MBTI 진로 추천 프로그램")
st.write("MBTI를 선택하면 추천 진로 2가지를 알려줘요!")

career_data = {
    "INTJ": [
        {
            "job": "데이터 분석가",
            "major": "통계학과, 컴퓨터공학과",
            "personality": "논리적이고 계획적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "연구원",
            "major": "자연과학계열, 공학계열",
            "personality": "집중력이 높고 탐구심이 강한 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],

    "INTP": [
        {
            "job": "프로그래머",
            "major": "컴퓨터공학과",
            "personality": "분석적이고 창의적인 사람",
            "salary": "평균 연봉 약 4,800만원"
        },
        {
            "job": "대학교수",
            "major": "교육학과, 전공 관련 학과",
            "personality": "지식을 탐구하고 설명하는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],

    "ENTJ": [
        {
            "job": "기업 경영인",
            "major": "경영학과",
            "personality": "리더십이 강하고 추진력이 있는 사람",
            "salary": "평균 연봉 약 7,000만원"
        },
        {
            "job": "변호사",
            "major": "법학과",
            "personality": "판단력이 좋고 논리적인 사람",
            "salary": "평균 연봉 약 8,000만원"
        }
    ],

    "ENTP": [
        {
            "job": "마케팅 기획자",
            "major": "광고홍보학과, 경영학과",
            "personality": "아이디어가 많고 말하는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "창업가",
            "major": "경영학과",
            "personality": "도전을 즐기고 창의적인 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],

    "INFJ": [
        {
            "job": "상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 3,800만원"
        },
        {
            "job": "작가",
            "major": "문예창작과",
            "personality": "감수성이 풍부한 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "INFP": [
        {
            "job": "음악 프로듀서",
            "major": "실용음악과",
            "personality": "감성이 풍부하고 창의적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "일러스트레이터",
            "major": "디자인학과",
            "personality": "예술 감각이 뛰어난 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "ENFJ": [
        {
            "job": "교사",
            "major": "교육학과",
            "personality": "사람들을 이끄는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "인사담당자",
            "major": "경영학과",
            "personality": "소통 능력이 좋은 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ENFP": [
        {
            "job": "유튜버",
            "major": "미디어학과",
            "personality": "활발하고 아이디어가 많은 사람",
            "salary": "평균 연봉 다양함"
        },
        {
            "job": "광고 기획자",
            "major": "광고홍보학과",
            "personality": "창의적이고 활동적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ISTJ": [
        {
            "job": "공무원",
            "major": "행정학과",
            "personality": "책임감이 강하고 꼼꼼한 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "회계사",
            "major": "회계학과",
            "personality": "정확하고 체계적인 사람",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],

    "ISFJ": [
        {
            "job": "간호사",
            "major": "간호학과",
            "personality": "배려심이 많고 성실한 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "사회복지사",
            "major": "사회복지학과",
            "personality": "도움을 주는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "ESTJ": [
        {
            "job": "경찰",
            "major": "경찰행정학과",
            "personality": "리더십 있고 책임감이 강한 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "관리자",
            "major": "경영학과",
            "personality": "체계적이고 추진력이 있는 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],

    "ESFJ": [
        {
            "job": "승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 사교적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "호텔리어",
            "major": "호텔관광학과",
            "personality": "서비스 정신이 뛰어난 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ISTP": [
        {
            "job": "정비사",
            "major": "자동차공학과",
            "personality": "손재주가 좋고 문제 해결을 잘하는 사람",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 판단력이 좋은 사람",
            "salary": "평균 연봉 약 8,000만원"
        }
    ],

    "ISFP": [
        {
            "job": "디자이너",
            "major": "시각디자인학과",
            "personality": "감각적이고 창의적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "플로리스트",
            "major": "원예학과",
            "personality": "섬세하고 예술적인 사람",
            "salary": "평균 연봉 약 3,000만원"
        }
    ],

    "ESTP": [
        {
            "job": "영업사원",
            "major": "경영학과",
            "personality": "활동적이고 자신감 있는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "스포츠 코치",
            "major": "체육학과",
            "personality": "에너지가 넘치고 리더십 있는 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ESFP": [
        {
            "job": "연예인",
            "major": "연극영화과",
            "personality": "사람들 앞에 서는 걸 좋아하는 사람",
            "salary": "평균 연봉 다양함"
        },
        {
            "job": "이벤트 기획자",
            "major": "이벤트학과",
            "personality": "사교적이고 활동적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ]
}

mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(career_data.keys())
)

if st.button("진로 추천 보기"):
    st.subheader(f"✨ {mbti} 추천 진로")

    for idx, career in enumerate(career_data[mbti], start=1):
        st.markdown(f"## {idx}. {career['job']}")
        st.write(f"📚 적합한 학과: {career['major']}")
        st.write(f"👤 어울리는 성격: {career['personality']}")
        st.write(f"💰 {career['salary']}")
        st.markdown("---")
