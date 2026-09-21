import numpy as np

def pca_projection(X: list, k: int) -> list:
    X = np.array(X, dtype=float)

    
    Xc = X - np.mean(X, axis=0)

    
    C = (Xc.T @ Xc) / (X.shape[0] - 1)

    
    eigenvalues, eigenvectors = np.linalg.eigh(C)

    
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]

    for j in range(k):
        col = eigenvectors[:, j]
        first_nonzero = np.flatnonzero(np.abs(col) > 1e-12)
        if len(first_nonzero) > 0 and col[first_nonzero[0]] < 0:
            eigenvectors[:, j] *= -1

    W = eigenvectors[:, :k]

    Xproj = Xc @ W

    return Xproj.tolist()