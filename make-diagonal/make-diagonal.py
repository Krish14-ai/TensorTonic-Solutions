import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    if(len(v) == 0):
        raise ValueError("List must be of length 1")
    arr = np.zeros((len(v), len(v)))
    for i in range(len(v)):
        arr[i][i] = v[i]
            
    return arr
