import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    A = np.array(matrix, dtype=float)

    values = np.linalg.eigvals(A)

    return np.sort(values)