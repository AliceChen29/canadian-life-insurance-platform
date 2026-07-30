def estimate_annual_premium(
    coverage,
    age,
    smoker,
    health_risk,
    term_years
):
    """
    Estimate an illustrative annual premium.
    This is NOT a real insurance quote — for educational purposes only.
    """
    if coverage < 0:
        raise ValueError("Coverage amount cannot be negative.")

    base_rate = 0.001

    if age < 30:
        age_factor = 0.8
    elif age < 40:
        age_factor = 1.0
    elif age < 50:
        age_factor = 1.4
    else:
        age_factor = 2.2

    smoker_factor = 2.0 if smoker else 1.0

    health_factors = {"Low": 1.0, "Moderate": 1.3, "High": 1.8}
    health_factor = health_factors.get(health_risk, 1.0)

    term_factor = 1.0 + (term_years / 100)

    annual_premium = (
        coverage
        * base_rate
        * age_factor
        * smoker_factor
        * health_factor
        * term_factor
    )

    return round(annual_premium, 2)


def estimate_monthly_premium(annual_premium):
    return round(annual_premium / 12, 2)


if __name__ == "__main__":
    annual = estimate_annual_premium(
        coverage=985000,
        age=45,
        smoker=True,
        health_risk="Moderate",
        term_years=20
    )
    monthly = estimate_monthly_premium(annual)

    print(f"Estimated annual premium: ${annual:,.2f}")
    print(f"Estimated monthly premium: ${monthly:,.2f}")