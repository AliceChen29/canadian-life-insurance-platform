import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from recommendation import recommend_product
from ui_style import apply_style, back_button

st.set_page_config(page_title="Product Recommendation", layout="centered")
apply_style()
back_button()

st.title("2. Product Recommendation")
st.caption("See which illustrative product type best fits your situation.")

age = st.slider("Age", 18, 70, 30)
budget = st.selectbox("Monthly budget level", ["Low", "Medium", "High"])
dependants = st.slider("Number of dependants", 0, 6, 1)
term_needed = st.selectbox("Desired coverage period (years)", [10, 20, 30, 99],
                             format_func=lambda x: "Whole life" if x == 99 else f"{x} years")
estate_need = st.checkbox("Do you have estate planning needs?")

if st.button("Get Recommendation", type="primary"):
    product, scores = recommend_product(
        age=age, budget_level=budget, dependants=dependants,
        term_needed=term_needed, estate_need=estate_need
    )

    st.metric("Recommended Product", product)

    if max(scores.values()) == 0:
        st.info("Your inputs didn't strongly favor any single product — consider adjusting term length or budget.")

    st.subheader("How each product scored")
    st.bar_chart(scores)

    st.caption("These are illustrative product categories, not real insurance company products.")