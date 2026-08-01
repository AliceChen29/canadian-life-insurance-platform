import streamlit as st
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

st.set_page_config(
    page_title="Life Insurance Planning Tool",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
[data-testid="stSidebarNav"] { display: none; }
[data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)

if "started" not in st.session_state:
    st.session_state.started = False

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #F6F7F9; }
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

.block-container { padding-top: 4rem; max-width: 560px; }

.hero-badge {
    width: 56px; height: 56px; border-radius: 16px;
    background: #E6F4F3; display: flex; align-items: center;
    justify-content: center; font-size: 28px; margin-bottom: 20px;
}
.hero-title {
    font-family: 'Manrope', sans-serif; font-weight: 800;
    font-size: 2.1rem; color: #142440; line-height: 1.25; margin-bottom: 8px;
}
.hero-sub { font-size: 1rem; color: #5B6B82; line-height: 1.5; margin-bottom: 24px; }

.disclaimer-pill {
    margin-top: 20px; padding: 12px 16px; background: #FFF9EC;
    border: 1px solid #F5E3B3; border-radius: 12px;
    font-size: 0.8rem; color: #8A6D1D; line-height: 1.5;
}

button[kind="primary"] {
    background: #0E7C7B !important; color: white !important; border: none !important;
    border-radius: 12px !important; padding: 0.9rem 1rem !important; font-weight: 600 !important;
    font-size: 1rem !important; margin-top: 8px !important;
}
button[kind="primary"]:hover { background: #0B615F !important; }

button[kind="secondary"] {
    background: #FFFFFF !important;
    color: #142440 !important;
    border: 1px solid #E7E9EF !important;
    border-radius: 16px !important;
    padding: 20px 22px !important;
    min-height: 68px !important;
    font-weight: 600 !important;
    font-size: 1.02rem !important;
    text-align: left !important;
    justify-content: flex-start !important;
    margin-bottom: 14px !important;
    box-shadow: 0 1px 3px rgba(20,36,64,0.05);
    transition: all 0.18s ease;
}
button[kind="secondary"]:hover {
    border-color: #0E7C7B !important;
    color: #0B615F !important;
    box-shadow: 0 6px 16px rgba(14,124,123,0.14);
    transform: translateY(-1px);
}
</style>
""", unsafe_allow_html=True)

features = [
    ("📊", "Coverage needs calculator", "pages/1_Needs_Calculator.py"),
    ("🧭", "Product recommendation", "pages/2_Recommendation.py"),
    ("💰", "Premium estimator", "pages/3_Premium_Calculator.py"),
    ("📈", "Investment projection", "pages/4_Investment_Projection.py"),
    ("🔍", "Model insights", "pages/5_Model_Insights.py"),
]

if not st.session_state.started:
    st.markdown('<div class="hero-badge">🛡️</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Plan your life insurance,<br>with confidence.</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Five quick tools to help you understand your coverage needs before you talk to an advisor.</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="disclaimer-pill">
    ⚠️ Educational student project. Figures are illustrative estimates only —
    not real quotes or professional advice. Always consult a licensed insurance advisor.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Get Started →", type="primary", width="stretch"):
        st.session_state.started = True
        st.rerun()

else:
    st.markdown('<div class="hero-badge">🛡️</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Choose a tool</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Tap any tool below to get started.</div>', unsafe_allow_html=True)

    for icon, label, page in features:
        if st.button(f"{icon}    {label}", key=page, type="secondary", width="stretch"):
            st.switch_page(page)