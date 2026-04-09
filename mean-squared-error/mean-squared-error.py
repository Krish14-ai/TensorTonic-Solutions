import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    MSE =0
    List = []
    y_p = np.array(y_pred)
    y_tr = np.array(y_true)
    for i in range(len(y_pred)):
         List.append((y_pred[i] - y_true[i])**2)
    result = np.mean(List)
    return result
    
    
        