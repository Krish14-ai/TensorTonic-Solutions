def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    
    for i in range(0,steps):
        x0=x0 - (2*a*x0 +b)*lr
        
    return x0
        