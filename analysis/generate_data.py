import numpy as np
import pandas as pd
import sys
import os

# Add src folder to path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from premium_model import estimate_annual_premium
from risk_score import calculate_risk_score

rng = np.random.default_rng(42)
n = 3000

# Generate synthetic applicant data
age = rng.integers(18, 66, n)
income = rng.lognormal(mean=11, sigma=0.5, size=n).round(0)
smoker = rng.binomial(1, 0.15, n)
dependants = rng.integers(0, 5, n)
bmi_category = rng.choice(["Standard", "Elevated", "High"], n, p=[0.6, 0.25, 0.15])
medical_condition = rng.binomial(1, 0.1, n)
occupation_risk = rng.choice(["Low", "Medium", "High"], n, p=[0.7, 0.2, 0.1])
coverage = rng.integers(50000, 2000000, n)
term_years = rng.choice([10, 20, 30], n)
health_risk = rng.choice(["Low", "Moderate", "High"], n, p=[0.6, 0.3, 0.1])

# Calculate premium and risk score for each row
premiums = []
risk_scores = []

for i in range(n):
    premium = estimate_annual_premium(
        coverage=coverage[i],
        age=age[i],
        smoker=bool(smoker[i]),
        health_risk=health_risk[i],
        term_years=term_years[i]
    )
    premiums.append(premium)

    risk = calculate_risk_score(
        age=age[i],
        smoker=bool(smoker[i]),
        bmi_category=bmi_category[i],
        medical_condition=bool(medical_condition[i]),
        occupation_risk=occupation_risk[i]
    )
    risk_scores.append(risk)

data = pd.DataFrame({
    "age": age,
    "income": income,
    "smoker": smoker,
    "dependants": dependants,
    "bmi_category": bmi_category,
    "medical_condition": medical_condition,
    "occupation_risk": occupation_risk,
    "coverage": coverage,
    "term_years": term_years,
    "health_risk": health_risk,
    "risk_score": risk_scores,
    "annual_premium": premiums
})

output_path = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "synthetic_applicants.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
data.to_csv(output_path, index=False)

print(f"Generated {n} synthetic applicant records.")
print(f"Saved to: {output_path}")
print(data.head())