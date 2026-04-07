import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x)
    
    if x.size == 0:
        return np.array([])       # consistent return type
    
    return 1 / (1 + np.exp(-x))  # ✅ operates on entire array at once