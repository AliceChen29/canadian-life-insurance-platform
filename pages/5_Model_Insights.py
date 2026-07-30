import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Model Insights", layout="centered")
st.title("5. Model Insights")
st.caption("Statistical analysis behind the premium estimation model, built in R.")

base_path = os.path.join(os.path.dirname(__file__), "..", "results")

st.header("Model Performance Comparison")
st.write(
    "Two models were compared to predict estimated premiums: a standard "
    "linear regression baseline, and a Gamma Generalized Linear Model (GLM). "
    "Because insurance premiums are strictly positive and right-skewed, "
    "the Gamma distribution is theoretically a better fit than ordinary least squares."
)

try:
    performance = pd.read_csv(os.path.join(base_path, "model_performance.csv"))
    st.dataframe(performance, use_container_width=True)

    improvement = (
        (performance.loc[performance['Model'] == 'Linear Regression', 'MAE'].values[0]
         - performance.loc[performance['Model'] == 'Gamma GLM', 'MAE'].values[0])
        / performance.loc[performance['Model'] == 'Linear Regression', 'MAE'].values[0]
        * 100
    )
    st.success(f"The Gamma GLM reduced Mean Absolute Error (MAE) by approximately {improvement:.1f}% compared to the linear regression baseline.")

except FileNotFoundError:
    st.warning("Model performance results not found. Please run the R analysis scripts first.")

st.header("Model Coefficients")
st.write("Coefficients from the Gamma GLM (log link), showing how each factor affects estimated premiums.")

try:
    coefficients = pd.read_csv(os.path.join(base_path, "model_coefficients.csv"))
    st.dataframe(coefficients, use_container_width=True)
except FileNotFoundError:
    st.warning("Model coefficients not found. Please run the R analysis scripts first.")

st.header("Dataset")
st.write(
    "All analysis is based on a synthetically generated dataset of 3,000 applicant "
    "records, created for educational purposes. No real personal data was used."
)

st.header("Methodology Summary")
st.markdown("""
- **Exploratory Data Analysis (EDA):** Conducted in R using `ggplot2` to examine 
  distributions of age, premiums, and the relationship between smoking status and cost.
- **Baseline Model:** Ordinary least squares linear regression.
- **Primary Model:** Gamma GLM with a log link function, chosen because premium data 
  is positive and right-skewed.
- **Evaluation Metrics:** Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE), 
  compared across both models.
""")

st.caption("This analysis is for educational purposes and does not reflect real actuarial pricing models.")