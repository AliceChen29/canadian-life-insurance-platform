import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from premium_model import estimate_annual_premium, estimate_monthly_premium
from risk_score import calculate_risk_score, classify_risk
from ui_style import apply_style, back_button

st.set_page_config(page_title="Premium Calculator", layout="centered")
apply_style()
back_button()

st.title("3. Premium Calculator")
st.caption("Get an illustrative premium estimate. This is NOT a real insurance quote.")

age = st.slider("Age", 18, 70, 30)
smoker = st.selectbox("Smoking status", ["Non-smoker", "Smoker"]) == "Smoker"
coverage = st.number_input("Coverage amount ($)", min_value=0, value=500000, step=50000)
term_years = st.selectbox("Term (years)", [10, 20, 30])
health_risk = st.selectbox("Health risk category", ["Low", "Moderate", "High"])
bmi_category = st.selectbox("BMI category", ["Standard", "Elevated", "High"])
medical_condition = st.checkbox("Any pre-existing medical condition?")
occupation_risk = st.selectbox("Occupation risk level", ["Low", "Medium", "High"])

if coverage == 0:
    st.warning("Coverage amount is $0 — enter a coverage amount to get a meaningful premium estimate.")

if st.button("Estimate Premium", type="primary"):
    annual = estimate_annual_premium(
        coverage=coverage, age=age, smoker=smoker,
        health_risk=health_risk, term_years=term_years
    )
    monthly = estimate_monthly_premium(annual)

    risk = calculate_risk_score(
        age=age, smoker=smoker, bmi_category=bmi_category,
        medical_condition=medical_condition, occupation_risk=occupation_risk
    )
    risk_cat = classify_risk(risk)

    col1, col2 = st.columns(2)
    col1.metric("Est. Monthly Premium", f"${monthly:,.2f}")
    col2.metric("Est. Annual Premium", f"${annual:,.2f}")

    st.metric("Risk Score", f"{risk} ({risk_cat})")

    if risk_cat in ("High", "Very High"):
        st.info("A higher risk score reflects factors like age, smoking, and health status — this drives the higher premium above.")

    st.caption("This is an illustrative estimate for educational purposes only.")