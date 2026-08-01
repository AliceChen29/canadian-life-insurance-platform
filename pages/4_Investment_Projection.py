import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from investment_projection import project_investment_deterministic, project_investment_monte_carlo

st.set_page_config(page_title="Investment Projection", layout="centered")

st.markdown("""
<style>
[data-testid="stSidebarNav"] { display: none; }
[data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)

if st.button("← Back to Home"):
    st.session_state.started = True
    st.switch_page("app.py")

st.title("4. Investment Projection")
st.caption("Compare potential investment growth over time.")

col_a, col_b = st.columns(2)
with col_a:
    initial_investment = st.number_input("Initial investment ($)", min_value=0, value=5000, step=500)
    monthly_contribution = st.number_input("Monthly contribution ($)", min_value=0, value=200, step=50)
with col_b:
    expected_return = st.slider("Expected annual return (%)", 0.0, 12.0, 6.0, step=0.5) / 100
    investment_years = st.slider("Investment period (years)", 1, 40, 20)

if st.button("Project My Investment"):
    deterministic = project_investment_deterministic(
        initial_investment=initial_investment,
        monthly_contribution=monthly_contribution,
        annual_return_rate=expected_return,
        years=investment_years
    )

    monte_carlo = project_investment_monte_carlo(
        initial_investment=initial_investment,
        monthly_contribution=monthly_contribution,
        expected_annual_return=expected_return,
        volatility=0.15,
        years=investment_years
    )

    st.subheader("Deterministic Projection")
    col1, col2, col3 = st.columns(3)
    col1.metric("Future Value", f"${deterministic['future_value']:,.0f}")
    col2.metric("Total Contributions", f"${deterministic['total_contributions']:,.0f}")
    col3.metric("Total Growth", f"${deterministic['total_growth']:,.0f}")

    st.subheader("Monte Carlo Simulation (1,000 paths)")
    col4, col5, col6 = st.columns(3)
    col4.metric("10th Percentile", f"${monte_carlo['percentile_10']:,.0f}")
    col5.metric("Median", f"${monte_carlo['median']:,.0f}")
    col6.metric("90th Percentile", f"${monte_carlo['percentile_90']:,.0f}")

    st.caption("Investment projections are illustrative only and do not guarantee future performance.")