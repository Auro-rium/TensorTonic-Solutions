import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    X = np.asarray(X)
    y = np.asarray(y)

    N, D = X.shape

    # Initialize parameters
    w = np.zeros(D)
    b = 0.0

    for _ in range(steps):
        # Forward pass
        z = X @ w + b
        p = _sigmoid(z)

        # Gradients
        error = p - y
        grad_w = (X.T @ error) / N
        grad_b = np.mean(error)

        # Gradient descent update
        w -= lr * grad_w
        b -= lr * grad_b

    return w, float(b)