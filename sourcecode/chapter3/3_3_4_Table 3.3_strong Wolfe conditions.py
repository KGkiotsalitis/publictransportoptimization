# Gradient Descent Line Search with Backtracking
import numpy as np #import numpy library
import math
import matplotlib.pyplot as plt
import numdifftools as nd

rho = 0.7; c = 0.1; c2=0.4
#x=[15,20]
x=5

k=0; epsilon=0.0001
def f(x):
    return(x**2-5*x)

def f_derivative(x):
    return(2*x-5)


while(abs(f_derivative(x))>epsilon):
    #print('gradient norm',np.linalg.norm(nd.Gradient(f)(x)),math.sqrt(nd.Gradient(f)(x)[0]**2+nd.Gradient(f)(x)[1]**2))
    f_grad = f_derivative(x)
    p_k = -f_derivative(x)
    a = 1
    while ( f(x+a*p_k) > f(x)+c*a*p_k*f_grad or
    abs(p_k*f_derivative(x+a*p_k)>c2*abs(p_k*f_derivative(x)))):
        a=rho*a
    a_k=a
    print(k,x,f(x),f_grad,p_k,a_k)
    x=x+a_k*p_k
    k=k+1
    #print(k, x, f(x), f_derivative(x), p_k, a_k)
    #print('x_k+1',x,k,f(x),f_derivative(x))


