import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    A = np.array(A, dtype=float)
    n = len(A)

    aug = np.hstack([A, np.eye(n)])

    for i in range(n):
        pivot = i + np.argmax(np.abs(aug[i:, i]))

        if abs(aug[pivot, i]) < 1e-12:
            return None

        aug[[i, pivot]] = aug[[pivot, i]]

        aug[i] /= aug[i, i]

        for j in range(n):
            if j != i:
                aug[j] -= aug[j, i] * aug[i]

    return aug[:, n:]