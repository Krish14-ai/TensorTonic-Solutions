import numpy as np
import math as m

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    if len(x) != len(y):
        raise ValueError("Vectors must have the same length")
    
    d = 0
    for i in range(len(x)):
        d += (x[i] - y[i]) ** 2
    
    return m.sqrt(d)