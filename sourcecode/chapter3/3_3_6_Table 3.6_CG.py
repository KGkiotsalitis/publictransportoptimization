# Newton Line Search with Backtracking
import numpy as np #import numpy library
import math
import matplotlib.pyplot as plt
import numdifftools as nd
from numpy.linalg import inv
from scipy.optimize import line_search
from scipy.optimize.linesearch import line_search_armijo
import scipy

rho = 0.99; c = 1e-4; c2=0.1
#x=[15,20]
x=[1,2]

k=0; epsilon=0.0001
def f(x):
    return(math.pow(x[0],4)-2*math.pow(x[0],2)*x[1]+x[0]**2+x[1]**2-2*x[0]+5)

p_k=-nd.Gradient(f)(x)
while(np.linalg.norm(nd.Gradient(f)(x))>epsilon):
    f_grad=nd.Gradient(f)(x)
    a = 5
    while (f(x+a*p_k) > f(x)+c*a*f_grad.T.dot(p_k) or
    abs(p_k.T.dot(nd.Gradient(f)(x+a*p_k))>c2*abs(p_k.T.dot(nd.Gradient(f)(x))))):
        a=rho*a
    a_k=a
    print('k', k, f(x), p_k.T.dot(nd.Gradient(f)(x)), np.linalg.norm(nd.Gradient(f)(x)), a_k, np.linalg.norm([x[0]-(1),x[1]-(1)]))
    x_new = x+a*p_k
    nominator = np.dot(nd.Gradient(f)(x_new).T,nd.Gradient(f)(x_new))
    denominator = np.dot(nd.Gradient(f)(x).T,nd.Gradient(f)(x))
    p_k = -nd.Gradient(f)(x_new) + p_k*(float(nominator)/float(denominator))
    x=x_new
    k=k+1

print('k', k, f(x), p_k.T.dot(nd.Gradient(f)(x)), np.linalg.norm(nd.Gradient(f)(x)), np.linalg.norm([x[0]-(1),x[1]-(1)]))
