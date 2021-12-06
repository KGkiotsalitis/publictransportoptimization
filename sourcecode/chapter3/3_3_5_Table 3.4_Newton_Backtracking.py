# Newton's Line Search with Backtracking
import numpy as np #import numpy library
import math
import matplotlib.pyplot as plt
import numdifftools as nd
from numpy.linalg import inv
from scipy.optimize import line_search
from scipy.optimize.linesearch import line_search_armijo
import scipy

rho = 0.99; c = 1e-4; c2=0.4
x=[2,2]

k=0; epsilon=0.0001
def f(x_k):
    return(100*(x_k[1]-x_k[0]**2)**2+(1-x_k[0])**2)

while(np.linalg.norm(nd.Gradient(f)(x))>epsilon):
    f_grad = np.array(nd.Gradient(f)(x))
    Inverse_Hessian = inv(nd.Hessian(f)(x))
    p_k = - Inverse_Hessian.dot(f_grad)
    #backtracking line search
    a = 1
    y=[x[0]+a*p_k[0],x[1]+a*p_k[1]]
    while (f(x+a*p_k) > f(x)+c*a*f_grad.T.dot(p_k) ):
        a = rho * a
    a_k = a
    print(k,x[0],x[1],f(x),np.dot(p_k.T,f_grad),a_k,np.linalg.norm(nd.Gradient(f)(x))  )
    x=x+a_k*p_k
    k=k+1


print(k,x[0],x[1],f(x),np.linalg.norm(nd.Gradient(f)(x)))