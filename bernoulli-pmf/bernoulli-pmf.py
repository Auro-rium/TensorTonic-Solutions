import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    x = np.array(x)

    pmf = np.where(
        x == 1,
        p,
        np.where(x == 0, 1 - p, 0.0)
    )

    mean = p
    variance = p * (1 - p)

    return {
        "pmf": pmf,
        "mean": float(mean),
        "variance": float(variance)
    }

