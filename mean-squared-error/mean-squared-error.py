import numpy as np

def mean_squared_error(y_true: list, y_pred: list) -> float:
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    return float(np.mean((y_true - y_pred) ** 2))