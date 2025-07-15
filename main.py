import pandas as pd
import plotly.express as px

# CSV 파일 불러오기
df = pd.read_csv("diabetes_prediction_dataset.csv")

# 필요한 컬럼 존재 확인
if 'age' not in df.columns or 'diabetes' not in df.columns:
    raise ValueError("데이터셋에 'age' 또는 'diabetes' 컬럼이 존재하지 않습니다.")

# 연령 구간 설정
df['age_group'] = pd.cut(
    df['age'],
    bins=[0, 20, 30, 40, 50, 60, 70, 120],
    labels=['10대 이하', '20대', '30대', '40대', '50대', '60대', '70대 이상'],
    right=False
)

# NaN 제거 (연령 구간 범위 외 데이터)
df = df.dropna(subset=['age_group'])

# 당뇨병 발병률 계산 (%)
age_diabetes_rate = df.groupby('age_group', observed=True)['diabetes'].mean().reset_index()
age_diabetes_rate['diabetes'] *= 100  # 퍼센트로 변환

# Plotly 막대그래프 생성
fig = px.bar(
    age_diabetes_rate,
    x='age_group',
    y='diabetes',
    labels={'age_group': '연령대', 'diabetes': '당뇨병 유병률 (%)'},
    title='📊 연령대별 당뇨병 유병률',
    color='diabetes',
    color_continuous_scale='reds',
    text=age_diabetes_rate['diabetes'].round(1).astype(str) + '%'
)

fig.update_traces(textposition='outside')
fig.update_layout(yaxis_range=[0, age_diabetes_rate['diabetes'].max() * 1.2])

# Streamlit에서도 사용 가능하게 하기
try:
    import streamlit as st
    st.plotly_chart(fig, use_container_width=True)
except ImportError:
    fig.show()

