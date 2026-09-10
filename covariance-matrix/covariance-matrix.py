import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X = np.array(X, dtype=float)

    cov = np.cov(X, rowvar=False)

    return np.atleast_2d(cov)