import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    p = np.array(p)
    q = np.array(q)

    mask = p > 0

    p_pos = p[mask]
    q_pos = np.maximum(q[mask], eps)

    return float(np.sum(p_pos * np.log(p_pos / q_pos)))