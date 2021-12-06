def newton_raphson(f,f_der,x0,tol):
    """Newton-Raphson algorithm for root finding of a single-variable function.

    Args:
        f (function): single-variable function returning a number. f must be continuous.
        f_der (function): function returning the derivative of f.
        x0 (float): initial solution guess of the problem.
        tol (float): nonnegative tolerance.

    Returns:
        r (float): root

    """

    r=x0
    while abs(f(r))>tol:
        r=r-float(f(r)/f_der(r))
    return(r)


def f(x):
    return(x**2-x-1)
def f_der(x):
    return(2*x-1)
print(newton_raphson(f,f_der,10,1e-6))