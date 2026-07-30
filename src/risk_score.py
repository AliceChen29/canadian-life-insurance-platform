def calculate_risk_score(age, smoker, bmi_category, medical_condition, occupation_risk):
    """
    Calculate an illustrative risk score (0-100).
    This is an educational model, not a real underwriting system.
    """
    score = 0
    score += min(max(age - 18, 0) * 0.8, 35)

    if smoker:
        score += 25

    if bmi_category == "Elevated":
        score += 8
    elif bmi_category == "High":
        score += 15

    if medical_condition:
        score += 15

    if occupation_risk == "Medium":
        score += 5
    elif occupation_risk == "High":
        score += 10

    return min(round(score, 1), 100)


def classify_risk(score):
    if score <= 25:
        return "Low"
    elif score <= 50:
        return "Moderate"
    elif score <= 75:
        return "High"
    else:
        return "Very High"


if __name__ == "__main__":
    score = calculate_risk_score(
        age=45,
        smoker=True,
        bmi_category="Elevated",
        medical_condition=False,
        occupation_risk="Low"
    )
    print(f"Risk score: {score} ({classify_risk(score)})")