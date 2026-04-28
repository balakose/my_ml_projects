import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Model Hub",
    page_icon="🚀",
    layout="wide"
)

# Sidebar (Ye automatic links dikhayega agar 'pages' folder exist karta hai)
with st.sidebar:
    st.header("🛠️ Quick Navigation")
    st.info("Choose a model to begin testing.")
    st.success("Developer: Bala")

# Main Landing Page Content
st.title("🌟 AI Projects Innovation Dashboard")
st.markdown("---")

st.subheader("Select a Project to Launch:")

# Dashboard-style Buttons (3 columns layout)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🚗 SUV Predictor")
    st.write("Predicts customer purchasing behavior.")
    if st.button("Open SUV Model", key="suv"):
        st.switch_page("pages/01_SUV_Predictor.py")

with col2:
    st.markdown("### 🏥 Patient Survival")
    st.write("Clinical analysis of patient records.")
    if st.button("Open Survival Model", key="survival"):
        st.switch_page("pages/02_Patient_Survival.py")

with col3:
    st.markdown("### 🎭 Emotion AI")
    st.write("Real-time sentiment and emotion analysis.")
    if st.button("Open Emotion AI", key="emotion"):
        st.switch_page("pages/03_Emotion_Analyzer.py")

st.markdown("---")

col4, col5 = st.columns(2)

with col4:
    st.markdown("### 💻 Electronics Recommender")
    st.write("Product suggestions based on similarity.")
    if st.button("Open Recommender", key="recom"):
        st.switch_page("pages/04_Electronics_Recommender.py")

with col5:
    st.markdown("### 🎓 Career Discovery")
    st.write("Predicting the best career path for students.")
    if st.button("Open Career Model", key="career"):
        st.switch_page("pages/05_Career_Discovery.py")

st.divider()
st.caption("Developed by Bala | CSE Student |  | GitHub: @BalaAIHub")