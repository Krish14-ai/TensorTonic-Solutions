import numpy as np
import math

def entropy_node(y):
    """
    Compute entropy for a single node.
    
    Args:
        y: array-like of probabilities (summing to 1) 
           OR raw class labels (integers/strings)
    Returns:
        Entropy value (float), in bits (log base 2)
    """
    y = np.array(y)
    
    # If raw labels are passed, convert to probability distribution
    if not np.issubdtype(y.dtype, np.floating):
        _, counts = np.unique(y, return_counts=True)
        y = counts / counts.sum()
    
    # Mask zero probabilities to avoid log2(0) → convention: 0 * log(0) = 0
    nonzero = y[y > 0]
    
    entropy = -np.sum(nonzero * np.log2(nonzero))
    return entropy