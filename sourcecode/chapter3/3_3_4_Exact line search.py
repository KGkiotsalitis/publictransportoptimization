# Gradient Descent Line Search with Backtracking
import numpy as np #import numpy library
import math
import matplotlib.pyplot as plt
import numdifftools as nd

x=5; k=0; epsilon=0.0001
def f(x):
    return(x**2-5*x)
def f_derivative(x):
    return(2*x-5)
def z_derivative(x,p_k,a):
    return(2*x-5)

while(abs(f_derivative(x))>epsilon):
    f_grad = f_derivative(x)
    p_k = -f_derivative(x)
    a=(1/(2*p_k))*(5-2*x)
    a_k=(1/(2*p_k))*(5-2*x)
    print(k,x,f(x),f_grad,p_k,a_k)
    x=x+a_k*p_k
    k=k+1
    #print(k, x, f(x), f_derivative(x), p_k, a_k)
    #print('x_k+1',x,k,f(x),f_derivative(x))


