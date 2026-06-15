import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    n_samples,n_features =  X.shape
    b = 0.0
    w = np.zeros(n_features)
    for i in range(steps):
        z = np.dot(X,w) + b

        ## Prediction
        y_pred = _sigmoid(z)

        ## gradients 
        
        dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
        db = (1 / n_samples) * np.sum(y_pred - y)

        # Parameter update
        w -= lr * dw
        b -= lr * db
        
        
    # Write code here
    return w,b