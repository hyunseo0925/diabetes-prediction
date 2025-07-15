import streamlit as st
import plotly.graph_objects as go

# ✅ 페이지 설정
st.set_page_config(page_title="당뇨병 예측 프로젝트", layout="wide")

# ✅ 제목 및 설명
st.title("🩺 건강 데이터를 활용한 당뇨병 예측 모델")
st.markdown("""
이 웹앱은 건강 설문 데이터와 머신러닝을 활용하여 당뇨병 위험 여부를 예측하는 프로젝트입니다.

- **사용자 건강 정보**를 입력하면
- **랜덤 포레스트 모델**이 당뇨병 발병 가능성을 예측합니다.
- 직관적인 **시각화(Plotly)**를 통해 모델의 중요 feature도 확인할 수 있습니다.
""")

# ✅ 프로젝트 개요
st.subheader("📌 프로젝트 개요")
st.markdown("""
- **주제**: 건강 데이터를 기반으로 당뇨병 발병 여부 예측
- **목표**: 사용자 입력을 통해 실시간으로 당뇨병 위험 수준을 판단
- **데이터**: Kaggle의 `diabetes_prediction_dataset.csv`
- **모델**: RandomForestClassifier (scikit-learn)
- **UI**: Streamlit + Plotly 시각화
""")

# ✅ 데이터 예시 Plotly (더미 그래프)
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=73,
    title={'text': "예측 정확도 (%)"},
    gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "green"}},
))
st.plotly_chart(fig, use_container_width=False)

# ✅ 메뉴 설명
st.subheader("📁 메뉴 소개")
st.markdown("""
- 🧪 **당뇨병 예측기**: 사용자 입력 기반으로 당뇨병 예측  
- 📊 **Feature 중요도 시각화**: 어떤 요소들이 당뇨병과 가장 관련이 있는지 시각적으로 확인  
- 📄 **데이터 탐색 (EDA)**: 원본 데이터에 대한 분석 및 분포 시각화 (추가 가능)
""")

# ✅ 개발자 정보
st.subheader("👨‍💻 만든 사람")
st.markdown("""
- 이름: [Your Name]
- GitHub: [https://github.com/yourname](https://github.com/yourname)
- 프로젝트 출처: Kaggle [Diabetes Prediction Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)
""")

