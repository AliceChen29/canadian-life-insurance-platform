import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from needs_calculator import calculate_coverage_need

st.set_page_config(page_title="Needs Calculator", layout="centered")

st.markdown("""
<style>
[data-testid="stSidebarNav"] { display: none; }
[data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)

if st.button("← Back to Home"):
    st.session_state.started = True
    st.switch_page("app.py")

st.title("1. Insurance Needs Calculator")
st.caption("Estimate how much coverage you might need using the income replacement method.")

income = st.number_input("Annual income ($)", min_value=0, value=60000, step=1000)
debt = st.number_input("Total debt ($)", min_value=0, value=200000, step=1000)
savings = st.number_input("Existing savings ($)", min_value=0, value=20000, step=1000)
dependants = st.slider("Number of dependants", 0, 6, 1)
existing_coverage = st.number_input("Existing insurance coverage ($)", min_value=0, value=0, step=10000)
replacement_years = st.slider("Income replacement period (years)", 1, 20, 10)

if st.button("Calculate Coverage Need"):
    education_need = 50000 * dependants if dependants > 0 else 0
    final_expenses = 15000

    coverage_need = calculate_coverage_need(
        annual_income=income,
        replacement_years=replacement_years,
        debt=debt,
        education_need=education_need,
        final_expenses=final_expenses,
        savings=savings,
        existing_coverage=existing_coverage
    )

    st.metric("Recommended Coverage", f"${coverage_need:,.0f}")

    st.subheader("Breakdown")
    breakdown = {
        "Income Replacement": income * replacement_years,
        "Debt": debt,
        "Education Need": education_need,
        "Final Expenses": final_expenses,
        "Less: Savings": -savings,
        "Less: Existing Coverage": -existing_coverage
    }
    st.bar_chart(breakdown)

    st.caption("This is an educational estimate, not professional insurance advice.")