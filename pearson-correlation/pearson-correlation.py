import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    
    X = np.array(X, dtype=float)
    return np.corrcoef(X, rowvar=False)