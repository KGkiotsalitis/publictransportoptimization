# Newton Line Search with Backtracking
import numpy as np #import numpy library
import math
import matplotlib.pyplot as plt
import numdifftools as nd
from numpy.linalg import inv
from scipy.optimize import line_search
from scipy.optimize.linesearch import line_search_armijo
import scipy

rho = 0.99; c = 0.001; c2=0.1
#x=[15,20]
x=[1,2]

k=0; epsilon=0.0001
def f(x):
    return(math.pow(x[0],4)-2*math.pow(x[0],2)*x[1]+x[0]**2+x[1]**2-2*x[0]+5)

p_k=np.array([500,500]) #initialize step direction to a large value
H_k=np.identity(2)
I=np.identity(2)



def callbackF(x):
    print (x[0],x[1],f(x), np.linalg.norm(nd.Gradient(f)(x)),np.linalg.norm([x[0]-(1),x[1]-(1)]))

from scipy.optimize import fmin_bfgs
res = fmin_bfgs(f, np.asarray([1,2]), callback=callbackF,gtol=1e-6,
    disp=True,retall=True,full_output=True)


while(np.linalg.norm(nd.Gradient(f)(x))>epsilon):
    #p_k = - H_k.dot(nd.Gradient(f)(x))
    p_k = - np.dot(H_k,nd.Gradient(f)(x))

    f_grad=nd.Gradient(f)(x)
    a = 1000
    while (f(x+a*p_k) > f(x)+c*a*np.dot(f_grad.T,p_k) or
    abs(np.dot(p_k.T,nd.Gradient(f)(x+a*p_k)))>c2*abs(np.dot(p_k.T,nd.Gradient(f)(x)))):
        a=rho*a
    a_k=a
    print('k', k, f(x), p_k.T.dot(nd.Gradient(f)(x)), a_k, np.linalg.norm(f_grad),np.linalg.norm([x[0]-(1),x[1]-(1)]))

    x_new = x+a*p_k
    d = x_new-x; y=nd.Gradient(f)(x_new)-nd.Gradient(f)(x)
    x=x_new

    y_dot_d_inv = np.dot(y.T,d)
    #print(y_dot_d_inv)
    if y_dot_d_inv==0.:
        y_dot_d=1000.0
    else:
        y_dot_d = 1. / y_dot_d_inv
    #print('y_dot_d',y_dot_d)
    d_dot_y = d.dot(y.transpose())

    A1 = I - y_dot_d * d[:, np.newaxis] * y[np.newaxis, :] #np.dot(d,y.T)
    A2 = I - y_dot_d * y[:, np.newaxis] * d[np.newaxis, :] #np.dot(y,d.T)
    H_k = np.dot(A1, np.dot(H_k, A2)) + y_dot_d * d[:, np.newaxis] * d[np.newaxis, :] #np.dot(d,d.T)

    k=k+1

print('k', k, f(x), p_k.T.dot(nd.Gradient(f)(x)), np.linalg.norm(nd.Gradient(f)(x)),np.linalg.norm([x[0]-(1),x[1]-(1)]))