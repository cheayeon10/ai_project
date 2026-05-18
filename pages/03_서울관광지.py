import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지 TOP10", layout="wide")

st.title("서울 관광지 TOP10")

places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "station": "경복궁역",
        "fun": "한복 체험"
    },
    {
        "name": "N서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "station": "명동역",
        "fun": "야경 감상"
    },
    {
        "name": "홍대거리",
        "lat": 37.556268,
        "lon": 126.922641,
        "station": "홍대입구역",
        "fun": "버스킹"
    }
]

m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

for place in places:
    folium.Marker(
        [place["lat"], place["lon"]],
        popup=place["name"]
    ).add_to(m)

map_data = st_folium(m, width=900, height=500)

st.write("---")

clicked = None

if map_data:
    clicked = map_data.get("last_object_clicked_popup")

if clicked:
    for place in places:
        if place["name"] == clicked:
            st.success(
                f"가까운 지하철역: {place['station']} | 놀거리: {place['fun']}"
            )
```

requirements.txt 파일에는 아래만 넣어.

```txt
streamlit
folium
streamlit-folium
```

# 실행 방법

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
