# Gradient Descent Line Search with Backtracking
import numpy as np #import numpy library
import math
import matplotlib.pyplot as plt
import numdifftools as nd

rho = 0.7; c = 0.1; c2=0.4
#x=[15,20]
x=[2,2]

k=0; epsilon=0.0001
def f(x_k):
    return(100*(x_k[1]-x_k[0]**2)**2+(1-x_k[0])**2)

while(np.linalg.norm(nd.Gradient(f)(x))>epsilon):
    f_grad = nd.Gradient(f)(x)
    p_k=-nd.Gradient(f)(x)
    #backtracking line search
    a = 1
    while (f(x+a*p_k) > f(x)+c*a*f_grad.T.dot(p_k) ):
        a=rho*a
    a_k=a
    print('x_k',k,f(x),nd.Gradient(f)(x).T.dot(p_k),np.linalg.norm(nd.Gradient(f)(x)),abs(np.linalg.norm([x[0]-1,x[1]-1]))   )
    x=x+a_k*p_k
    k=k+1


print('solution',x,f(x),np.linalg.norm(nd.Gradient(f)(x)))


