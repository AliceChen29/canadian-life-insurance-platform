def project_investment_deterministic(
    initial_investment,
    monthly_contribution,
    annual_return_rate,
    years
):
    """
    Deterministic future value projection using compound interest.
    This is an illustrative projection, not a guarantee of future performance.
    """
    if annual_return_rate < 0 or years < 0:
        raise ValueError("Return rate and years must be non-negative.")

    months = years * 12
    monthly_rate = annual_return_rate / 12

    if monthly_rate == 0:
        future_value = initial_investment + monthly_contribution * months
    else:
        future_value = (
            initial_investment * (1 + monthly_rate) ** months
            + monthly_contribution * (((1 + monthly_rate) ** months - 1) / monthly_rate)
        )

    total_contributions = initial_investment + monthly_contribution * months
    total_growth = future_value - total_contributions

    return {
        "future_value": round(future_value, 2),
        "total_contributions": round(total_contributions, 2),
        "total_growth": round(total_growth, 2)
    }


def project_investment_monte_carlo(
    initial_investment,
    monthly_contribution,
    expected_annual_return,
    volatility,
    years,
    simulations=1000,
    seed=42
):
    """
    Monte Carlo simulation of investment outcomes under uncertainty.
    Returns percentile outcomes across simulated paths.
    """
    import numpy as np

    rng = np.random.default_rng(seed)
    months = years * 12
    monthly_return_mean = expected_annual_return / 12
    monthly_return_std = volatility / 12

    ending_values = []

    for _ in range(simulations):
        value = initial_investment
        monthly_returns = rng.normal(monthly_return_mean, monthly_return_std, months)
        for r in monthly_returns:
            value = value * (1 + r) + monthly_contribution
        ending_values.append(value)

    ending_values = np.array(ending_values)

    return {
        "median": round(float(np.percentile(ending_values, 50)), 2),
        "percentile_10": round(float(np.percentile(ending_values, 10)), 2),
        "percentile_90": round(float(np.percentile(ending_values, 90)), 2),
        "mean": round(float(np.mean(ending_values)), 2)
    }


if __name__ == "__main__":
    deterministic = project_investment_deterministic(
        initial_investment=5000,
        monthly_contribution=200,
        annual_return_rate=0.06,
        years=20
    )
    print("Deterministic projection:")
    print(deterministic)

    monte_carlo = project_investment_monte_carlo(
        initial_investment=5000,
        monthly_contribution=200,
        expected_annual_return=0.06,
        volatility=0.15,
        years=20
    )
    print("\nMonte Carlo projection:")
    print(monte_carlo)