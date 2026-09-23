import math
import numpy as np

def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    x = np.array(x)

    erf_values = np.vectorize(math.erf)(x / np.sqrt(2))

    return 0.5 * x * (1 + erf_values)