import streamlit as st
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(page_title="당뇨병 예측 모델", layout="wide")

# 제목
st.title("🧬 당뇨병 예측 모델 만들기")
st.markdown("**기계학습 + 생명과학의 융합 프로젝트**")

# 프로젝트 개요
st.header("📌 프로젝트 개요")
st.markdown("""
이 프로젝트는 환자의 건강 정보 (나이, BMI, 혈압, 가족력 등)를 바탕으로  
**당뇨병 발병 가능성**을 예측하는 머신러닝 모델을 구축하는 것을 목표로 합니다.

- 🔍 **목표**: 조기 예측을 통해 예방적 건강 관리 가능성 탐색
- 🧪 **데이터 기반 접근**: Kaggle 공개 데이터셋 사용
- 🧠 **예측 모델**: `RandomForestClassifier` 등 ML 기법
""")

# 사용 기술
st.header("🛠️ 사용 기술")
st.markdown("""
- **언어 및 프레임워크**: Python, Streamlit
- **분석 도구**: Pandas, Scikit-learn
- **시각화 도구**: Plotly
- **웹 인터페이스**: Streamlit으로 사용자 입력 기반 예측 제공
""")

# Plotly 예시 시각화
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=87,
    title={'text': "모델 예측 정확도 (%)"},
    gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "mediumseagreen"}},
))
st.plotly_chart(fig, use_container_width=False)

# 연계 생명과학 개념
st.header("🧬 연계 생명과학 개념")
st.markdown("""
본 프로젝트는 단순한 기술 구현을 넘어서, **인체 생리학적 메커니즘과 기계학습을 연결**합니다.

- 🧪 **인슐린 작용**: 포도당을 세포 내로 이동시켜 혈당 감소  
- 🛡️ **인슐린 저항성**: 세포가 인슐린에 둔감해져 혈당 조절 실패  
- ⚖️ **혈당 항상성 조절 메커니즘**: 인슐린/글루카곤의 상호작용

➡️ 이러한 개념은 모델이 예측한 결과를 **의학적 맥락**에서 이해하는 데 도움을 줍니다.
""")

# 향후 발전 방향
st.header("🚀 확장 아이디어")
st.markdown("""
- SHAP 시각화를 통한 **모델 해석력 강화**
- 사용자 데이터 기록 → **맞춤형 건강 피드백 제공**
- 장기적으로는 **웨어러블 센서 데이터**와 통합하여 실시간 위험 예측 가능성도 탐색 가능
""")

# 개발자 소개 (선택적)
st.markdown("---")
st.markdown("👨‍🔬 만든 사람: [Your Name] | GitHub: [github.com/yourname](https://github.com/yourname)")
