import math

def binomial_pmf_cdf(n: int, k: int, p: float) -> dict:
    if k < 0 and k >n :
        return {
            "pmf": 0.0,
            "cdf": 0.0
        }

    
    pmf = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

    cdf = sum(
        math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
        for i in range(k + 1)
    )

    return {
        "pmf": float(pmf),
        "cdf": float(cdf)
    }