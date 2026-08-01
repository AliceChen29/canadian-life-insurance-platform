import streamlit as st

def apply_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@700;800&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: #F6F7F9; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebarNav"] { display: none; }
    [data-testid="stSidebar"] { display: none; }

    .block-container { padding-top: 2.5rem; max-width: 640px; }

    h1 { font-family: 'Manrope', sans-serif !important; font-weight: 800 !important; color: #142440 !important; }
    h2, h3 { font-family: 'Manrope', sans-serif !important; font-weight: 700 !important; color: #142440 !important; }

    button[kind="primary"] {
        background: #0E7C7B !important; color: white !important; border: none !important;
        border-radius: 12px !important; font-weight: 600 !important;
    }
    button[kind="primary"]:hover { background: #0B615F !important; }

    button[kind="secondary"] {
        background: #FFFFFF !important; color: #142440 !important;
        border: 1px solid #E7E9EF !important; border-radius: 10px !important;
        font-weight: 600 !important;
    }
    button[kind="secondary"]:hover { border-color: #0E7C7B !important; color: #0B615F !important; }

    div[data-testid="stMetric"] {
        background: #FFFFFF; border: 1px solid #E7E9EF; border-radius: 14px;
        padding: 16px 18px;
    }
    div[data-testid="stMetricLabel"] { color: #5B6B82 !important; }
    div[data-testid="stMetricValue"] { color: #142440 !important; }

    div[data-testid="stExpander"] {
        background: #FFFFFF; border: 1px solid #E7E9EF; border-radius: 14px;
    }
    </style>
    """, unsafe_allow_html=True)


def back_button():
    if st.button("← Back to Home"):
        st.session_state.started = True
        st.switch_page("app.py")