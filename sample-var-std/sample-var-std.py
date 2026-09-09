def sample_var_std(x: list) -> dict:
    n = len(x)

    if n < 2:
        return {
            "variance": 0.0,
            "standard_deviation": 0.0
        }

    mean = sum(x) / n

    squared_diff = 0
    for value in x:
        squared_diff += (value - mean) ** 2

    variance = squared_diff / (n - 1)
    standard_deviation = variance ** 0.5

    return {
        "variance": variance,
        "standard_deviation": standard_deviation
    }