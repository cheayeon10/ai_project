# Streamlit + Folium 서울 관광지 TOP10 지도 앱

## app.py

```python
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지 TOP10", layout="wide")

st.title("🌏 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("지도의 마커를 클릭하면 아래에 가까운 지하철역과 놀거리를 볼 수 있어요!")

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "station": "경복궁역",
        "fun": "한복 체험, 북촌한옥마을 산책"
    },
    {
        "name": "N서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "station": "명동역",
        "fun": "야경 감상, 케이블카"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "station": "명동역",
        "fun": "길거리 음식, 쇼핑"
    },
    {
        "name": "홍대거리",
        "lat": 37.556268,
        "lon": 126.922641,
        "station": "홍대입구역",
        "fun": "버스킹, 카페 투어"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.512462,
        "lon": 127.102544,
        "station": "잠실역",
        "fun": "전망대, 쇼핑몰"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "station": "안국역",
        "fun": "전통 한옥 구경, 사진 촬영"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009223,
        "station": "동대문역사문화공원역",
        "fun": "야경, 전시회"
    },
    {
        "name": "코엑스",
        "lat": 37.511685,
        "lon": 127.059151,
        "station": "삼성역",
        "fun": "별마당도서관, 아쿠아리움"
    },
    {
        "name": "광장시장",
        "lat": 37.570377,
        "lon": 126.999997,
        "station": "종로5가역",
        "fun": "빈대떡, 마약김밥 먹방"
    },
    {
        "name": "한강공원",
        "lat": 37.528316,
        "lon": 126.932651,
        "station": "여의나루역",
        "fun": "자전거, 치맥"
    }
]

# 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

for place in places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=place["name"],
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="star")
    ).add_to(m)

# 지도 출력
map_data = st_folium(m, width=1000, height=600)

# 클릭한 장소 정보 출력
st.markdown("---")
st.subheader("📍 관광지 정보")

if map_data["last_object_clicked_popup"]:
    clicked_place = map_data["last_object_clicked_popup"]

    for place in places:
        if place["name"] == clicked_place:
            st.success(
                f"🚉 가까운 지하철역: {place['station']} | 🎡 놀거리: {place['fun']}"
            )
            break
else:
    st.info("지도의 관광지를 클릭해보세요!")
```

---

## requirements.txt

```txt
streamlit
folium
streamlit-folium
```

---

# 실행 방법

## 1. 파일 생성

* app.py
* requirements.txt

## 2. 터미널 실행

```bash
streamlit run app.py
```

---

# Streamlit Cloud 배포 방법

1. GitHub에 app.py와 requirements.txt 업로드
2. urlStreamlit Community Cloud[https://share.streamlit.io/](https://share.streamlit.io/) 접속
3. GitHub 저장소 연결
4. Main file path에 app.py 입력
5. Deploy 클릭
