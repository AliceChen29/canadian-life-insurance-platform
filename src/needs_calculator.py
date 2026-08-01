def calculate_coverage_need(
    annual_income,
    replacement_years,
    debt,
    education_need,
    final_expenses,
    savings,
    existing_coverage,
    replacement_rate=0.75,
    discount_rate=0.03
):
    """
    Calculate the recommended life insurance coverage amount
    using an income replacement method with present value discounting.

    replacement_rate: Percentage of income the family actually needs
        replaced (typically 70-80%, not 100%, since household expenses
        drop when one income is lost).

    discount_rate: Annual discount rate used to calculate the present
        value of future income replacement, since a dollar needed in
        15 years is worth less than a dollar today.

    This is an educational estimate, not professional insurance advice.
    """
    if annual_income < 0 or debt < 0 or savings < 0:
        raise ValueError("Income, debt, and savings must be non-negative.")

    if not (0 < replacement_rate <= 1):
        raise ValueError("Replacement rate must be between 0 and 1.")

    if discount_rate < 0:
        raise ValueError("Discount rate cannot be negative.")

    annual_replacement_amount = annual_income * replacement_rate

    if discount_rate > 0:
        # Present value of an annuity formula:
        # PV = PMT * [1 - (1 + r)^-n] / r
        pv_factor = (1 - (1 + discount_rate) ** -replacement_years) / discount_rate
    else:
        pv_factor = replacement_years

    income_replacement_pv = annual_replacement_amount * pv_factor

    gross_need = (
        income_replacement_pv
        + debt
        + education_need
        + final_expenses
    )

    net_need = gross_need - savings - existing_coverage

    return {
        "coverage_need": round(max(net_need, 0), 2),
        "income_replacement_pv": round(income_replacement_pv, 2),
        "annual_replacement_amount": round(annual_replacement_amount, 2)
    }


if __name__ == "__main__":
    result = calculate_coverage_need(
        annual_income=70000,
        replacement_years=15,
        debt=201000,
        education_need=100000,
        final_expenses=15000,
        savings=21000,
        existing_coverage=10000,
        replacement_rate=0.75,
        discount_rate=0.03
    )
    print(result)