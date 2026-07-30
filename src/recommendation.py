def recommend_product(age, budget_level, dependants, term_needed, estate_need):
    """
    Score four illustrative product types and recommend the best fit.
    """
    scores = {"Term 10": 0, "Term 20": 0, "Term 30": 0, "Permanent Life": 0}

    if term_needed <= 10:
        scores["Term 10"] += 3
    elif term_needed <= 20:
        scores["Term 20"] += 3
    elif term_needed <= 30:
        scores["Term 30"] += 3
    else:
        scores["Permanent Life"] += 3

    if dependants >= 2:
        scores["Term 20"] += 2
        scores["Term 30"] += 1

    if budget_level == "Low":
        scores["Term 10"] += 2
    elif budget_level == "High":
        scores["Permanent Life"] += 2

    if estate_need:
        scores["Permanent Life"] += 3

    best = max(scores, key=scores.get)
    return best, scores


if __name__ == "__main__":
    product, scores = recommend_product(
        age=35,
        budget_level="Medium",
        dependants=2,
        term_needed=20,
        estate_need=False
    )
    print(f"Recommended product: {product}")
    print(f"All scores: {scores}")