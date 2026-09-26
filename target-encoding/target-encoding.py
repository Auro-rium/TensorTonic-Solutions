def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    sums = {}
    counts = {}

    for category, target in zip(categories, targets):
        sums[category] = sums.get(category, 0) + target
        counts[category] = counts.get(category, 0) + 1

    means = {
        category: sums[category] / counts[category]
        for category in sums
    }

    return [float(means[category]) for category in categories]