def bisection(f,a,b,tol):
    """Bisection algorithm for root finding of a single-variable function.

    Args:
        f (function): function returning a number. f must be continuous, and f(a) and f(b) must have opposite signs.
        a (float): one end of the bracketing interval [a, b].
        b (float): other end of the bracketing interval [a, b].
        tol (float): nonnegative tolerance.

    Returns:
        c (float): root

    """

    c=0.5*(a+b)
    while abs(f(c))>tol:
        if f(a)*f(c)>0:
            a=c
        else:
            b=c
        c=0.5*(a+b)
    return(c)

def f(x):
    return(x**2-1)

print(bisection(f,0,3,1e-12))

def f(x):
    return(x**2-x-1)
print(bisection(f,0,10,1e-6))