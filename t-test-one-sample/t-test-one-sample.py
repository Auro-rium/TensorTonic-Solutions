import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    x = np.array(x)

    mean = np.mean(x)
    s = np.std(x, ddof=1)

    

    se = s / np.sqrt(len(x))

    return float((mean - mu0) / se)