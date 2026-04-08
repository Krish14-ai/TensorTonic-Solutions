import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    X = np.array(x)
    P = np.array(p)
    if len(x) != len(p):
        raise ValueError("x and p must have the same length")
        
    if not np.isclose(np.sum(p),1): 
        raise ValueError("Value Error,Sum of probabilities should be 1")
        
## np.isclose is used to check whether two numbers are approximately equal, not exactly equal.as in python 0.1 + 0.2 != 0.3
    
    y=0
    for i in range(len(x)):
        y = y+x[i]*p[i]

    return y
