import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    A = np.array(matrix, dtype=float)

    if norm_type == "l1":
        norms = np.sum(np.abs(A), axis=axis, keepdims=True)

    elif norm_type == "l2":
        norms = np.sqrt(np.sum(A ** 2, axis=axis, keepdims=True))

    elif norm_type == "max":
        norms = np.max(np.abs(A), axis=axis, keepdims=True)

    safe_norms = np.where(norms == 0, 1, norms)

    return A / safe_norms