from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    

    x = np.array(x)

    mean = np.mean(x)
    median = np.median(x)

    values, counts = np.unique(x, return_counts=True)
    mode = values[np.argmax(counts)]

    return {
        "mean": float(mean),
        "median": float(median),
        "mode": float(mode)
    }