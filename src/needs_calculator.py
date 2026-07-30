def calculate_coverage_need(
    annual_income,
    replacement_years,
    debt,
    education_need,
    final_expenses,
    savings,
    existing_coverage
):
    """
    Calculate the recommended life insurance coverage amount
    using a simplified income replacement method.

    This is an educational estimate, not professional insurance advice.
    """
    if annual_income < 0 or debt < 0 or savings < 0:
        raise ValueError("Income, debt, and savings must be non-negative.")

    gross_need = (
        annual_income * replacement_years
        + debt
        + education_need
        + final_expenses
    )

    net_need = gross_need - savings - existing_coverage

    return max(net_need, 0)


# Quick test when running this file directly
if __name__ == "__main__":
    result = calculate_coverage_need(
        annual_income=70000,
        replacement_years=10,
        debt=300000,
        education_need=100000,
        final_expenses=15000,
        savings=80000,
        existing_coverage=50000
    )
    print(f"Recommended coverage: ${result:,.0f}")