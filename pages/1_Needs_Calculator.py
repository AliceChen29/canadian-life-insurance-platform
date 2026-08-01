import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from needs_calculator import calculate_coverage_need
from ui_style import apply_style, back_button

st.set_page_config(page_title="Needs Calculator", layout="centered")
apply_style()
back_button()

st.title("1. Insurance Needs Calculator")
st.caption("Estimate how much coverage you might need using the income replacement method.")

income = st.number_input("Annual income ($)", min_value=0, value=60000, step=1000)
debt = st.number_input("Total debt ($)", min_value=0, value=200000, step=1000)
savings = st.number_input("Existing savings ($)", min_value=0, value=20000, step=1000)
dependants = st.slider("Number of dependants", 0, 6, 1)
existing_coverage = st.number_input("Existing insurance coverage ($)", min_value=0, value=0, step=10000)
replacement_years = st.slider("Income replacement period (years)", 1, 20, 10)

with st.expander("Advanced assumptions"):
    st.caption(
        "These assumptions affect the estimate. Defaults follow common financial "
        "planning guidance, but you can adjust them to see how sensitive the result is."
    )
    replacement_rate = st.slider(
        "Income replacement rate (%)", 50, 100, 75,
        help="Percentage of income the family actually needs replaced. "
             "Typically 70-80%, not 100%, since household expenses drop "
             "when one income is lost."
    ) / 100
    discount_rate = st.slider(
        "Discount rate (%)", 0.0, 8.0, 3.0, step=0.5,
        help="Reflects the time value of money — a dollar needed in the future "
             "is worth less than a dollar today."
    ) / 100

if income == 0:
    st.warning("Annual income is $0 — income replacement will not contribute to the estimate.")

if savings + existing_coverage > (income * replacement_years + debt):
    st.info("Your existing savings and coverage may already meet a large share of your estimated need.")

if st.button("Calculate Coverage Need", type="primary"):
    education_need = 50000 * dependants if dependants > 0 else 0
    final_expenses = 15000

    result = calculate_coverage_need(
        annual_income=income,
        replacement_years=replacement_years,
        debt=debt,
        education_need=education_need,
        final_expenses=final_expenses,
        savings=savings,
        existing_coverage=existing_coverage,
        replacement_rate=replacement_rate,
        discount_rate=discount_rate
    )

    st.metric("Recommended Coverage", f"${result['coverage_need']:,.0f}")

    st.subheader("Breakdown")
    breakdown = {
        "Income Replacement (PV)": result["income_replacement_pv"],
        "Debt": debt,
        "Education Need": education_need,
        "Final Expenses": final_expenses,
        "Less: Savings": -savings,
        "Less: Existing Coverage": -existing_coverage
    }
    st.bar_chart(breakdown)

    st.caption(
        f"Income replacement is calculated as {replacement_rate*100:.0f}% of income "
        f"(${result['annual_replacement_amount']:,.0f}/year), discounted at "
        f"{discount_rate*100:.1f}% over {replacement_years} years to reflect present value."
    )
    st.caption("This is an educational estimate, not professional insurance advice.")