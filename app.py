import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from needs_calculator import calculate_coverage_need
from risk_score import calculate_risk_score, classify_risk
from recommendation import recommend_product
from premium_model import estimate_annual_premium, estimate_monthly_premium

st.set_page_config(page_title="Life Insurance Planning Tool", layout="centered")

st.title("Canadian Life Insurance Planning Tool")
st.warning(
    "⚠️ This is an educational student project. All figures are illustrative "
    "estimates and do NOT constitute real insurance quotes or professional advice. "
    "Please consult a licensed insurance advisor before making any decisions."
)

st.header("1. Your Information")

age = st.slider("Age", 18, 70, 30)
smoker = st.selectbox("Smoking status", ["Non-smoker", "Smoker"]) == "Smoker"
income = st.number_input("Annual income ($)", min_value=0, value=60000, step=1000)
debt = st.number_input("Total debt ($)", min_value=0, value=200000, step=1000)
savings = st.number_input("Existing savings ($)", min_value=0, value=20000, step=1000)
dependants = st.slider("Number of dependants", 0, 6, 1)
term_needed = st.selectbox("Desired coverage period (years)", [10, 20, 30, 99],
                             format_func=lambda x: "Whole life" if x == 99 else f"{x} years")
budget = st.selectbox("Monthly budget level", ["Low", "Medium", "High"])
health_risk = st.selectbox("Health risk category", ["Low", "Moderate", "High"])
bmi_category = st.selectbox("BMI category", ["Standard", "Elevated", "High"])
medical_condition = st.checkbox("Any pre-existing medical condition?")
occupation_risk = st.selectbox("Occupation risk level", ["Low", "Medium", "High"])

if st.button("Calculate My Results"):
    # Needs calculation
    coverage_need = calculate_coverage_need(
        annual_income=income,
        replacement_years=10,
        debt=debt,
        education_need=50000 * dependants if dependants > 0 else 0,
        final_expenses=15000,
        savings=savings,
        existing_coverage=0
    )

    # Risk score
    risk = calculate_risk_score(
        age=age, smoker=smoker, bmi_category=bmi_category,
        medical_condition=medical_condition, occupation_risk=occupation_risk
    )
    risk_category = classify_risk(risk)

    # Product recommendation
    product, scores = recommend_product(
        age=age, budget_level=budget, dependants=dependants,
        term_needed=term_needed, estate_need=(term_needed == 99)
    )

    # Premium
    annual_premium = estimate_annual_premium(
        coverage=coverage_need, age=age, smoker=smoker,
        health_risk=health_risk,
        term_years=term_needed if term_needed != 99 else 100
    )
    monthly_premium = estimate_monthly_premium(annual_premium)

    st.header("2. Your Results")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Recommended Coverage", f"${coverage_need:,.0f}")
        st.metric("Risk Score", f"{risk} ({risk_category})")
    with col2:
        st.metric("Recommended Product", product)
        st.metric("Est. Monthly Premium", f"${monthly_premium:,.2f}")

    st.subheader("Why this product?")
    st.write(f"Based on your inputs, **{product}** scored highest among the options considered.")
    st.bar_chart(scores)

    st.caption("All premium and coverage figures above are illustrative estimates for educational purposes only.")