import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
  
  
   
    x = np.array(x)
    result = np.maximum(0, x)

    return np.asarray(result)