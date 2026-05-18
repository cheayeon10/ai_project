import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지", layout="wide")

st.title("🌏 서울 관광지 TOP10")

places = [
    ["경복궁", 37.579617, 126.977041, "경복궁역", "한복 체험"],
    ["N서울타워", 37.551169, 126.988227, "명동역", "야경 감상"],
    ["명동", 37.563757, 126.985302, "명동역", "쇼핑"],
    ["홍대거리", 37.556268, 126.922641, "홍대입구역", "버스킹"],
    ["롯데월드타워", 37.512462, 127.102544, "잠실역", "전망대"],
]

m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

for p in places:
    folium.Marker(
        location=[p[1], p[2]],
        popup=p[0],
        tooltip=p[0]
    ).add_to(m)

map_data = st_folium(m, width=900, height=500)

st.write("---")
st.subheader("관광지 정보")

clicked = None

if map_data:
    clicked = map_data.get("last_object_clicked_popup")

if clicked:
    for p in places:
        if p[0] == clicked:
            st.success(f"가까운 지하철역: {p[3]} | 놀거리: {p[4]}")
