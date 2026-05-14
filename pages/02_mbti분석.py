# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ---------------------------
# 페이지 설정
# ---------------------------
st.set_page_config(
    page_title="세계 MBTI 분석",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------
# 데이터 불러오기
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# ---------------------------
# 제목
# ---------------------------
st.title("🌍 국가별 MBTI 비율 분석")
st.markdown("국가를 선택하면 MBTI 비율을 인터랙티브 그래프로 확인할 수 있어.")

# ---------------------------
# 국가 선택
# ---------------------------
countries = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "국가 선택",
    countries
)

# ---------------------------
# 선택 국가 데이터
# ---------------------------
country_data = df[df["Country"] == selected_country].iloc[0]

mbti_columns = [
    "INFJ", "ISFJ", "INTP", "ISFP",
    "ENTP", "INFP", "ENTJ", "ISTP",
    "INTJ", "ESFP", "ESTJ", "ENFP",
    "ESTP", "ISTJ", "ENFJ", "ESFJ"
]

values = country_data[mbti_columns].values

chart_df = pd.DataFrame({
    "MBTI": mbti_columns,
    "Ratio": values
})

# ---------------------------
# 색상 설정
# ---------------------------
max_value = chart_df["Ratio"].max()

colors = []

for value in chart_df["Ratio"]:
    if value == max_value:
        colors.append("#ff2b2b")  # 1등 빨간색
    else:
        # 파란색 그라데이션 느낌
        intensity = value / max_value

        if intensity > 0.8:
            colors.append("#1d4ed8")
        elif intensity > 0.6:
            colors.append("#2563eb")
        elif intensity > 0.4:
            colors.append("#3b82f6")
        elif intensity > 0.2:
            colors.append("#60a5fa")
        else:
            colors.append("#93c5fd")

# ---------------------------
# 그래프 생성
# ---------------------------
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=chart_df["MBTI"],
        y=chart_df["Ratio"],
        marker_color=colors,
        text=[f"{v:.2%}" for v in chart_df["Ratio"]],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2%}<extra></extra>"
    )
)

fig.update_layout(
    title=f"{selected_country} MBTI 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    template="plotly_white",
    height=600,
    hovermode="x unified",
    title_x=0.5,
    font=dict(
        size=15
    )
)

fig.update_yaxes(tickformat=".0%")

# ---------------------------
# 그래프 출력
# ---------------------------
st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# TOP 3 출력
# ---------------------------
top3 = chart_df.sort_values(
    by="Ratio",
    ascending=False
).head(3)

st.subheader("🏆 TOP 3 MBTI")

for idx, row in top3.iterrows():
    st.markdown(
        f"**{row['MBTI']}** : {row['Ratio']:.2%}"
    )

# ---------------------------
# 데이터 테이블
# ---------------------------
with st.expander("📄 데이터 보기"):
    st.dataframe(
        chart_df.sort_values(
            by="Ratio",
            ascending=False
        ),
        use_container_width=True
    )
