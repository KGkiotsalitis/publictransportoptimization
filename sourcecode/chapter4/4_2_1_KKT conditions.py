''''
import sympy as sp
x, y = sp.var('x,y',real=True)
f = 2 * x**2 + 3 * y**2
g = x**2 + y**2 - 4
lam = sp.symbols('lambda', real = True)
L = f - lam* g
gradL = [sp.diff(L,c) for c in [x,y]] # gradient of Lagrangian w.r.t. (x,y)
KKT_eqs = gradL + [g]
print(KKT_eqs)
stationary_points = sp.solve(KKT_eqs, [x, y, lam], dict=True) # solve the KKT equations
print(stationary_points)
[f.subs(p) for p in stationary_points]
'''

import sympy as sp
x1, x2 = sp.var('x1,x2',real=True)
f = -x1**2 - x2**2
g1 = -x1
g2=-x2
g3=x1+x2-2

l1 = sp.symbols('l1', real = True)
l2 = sp.symbols('l2', real = True)
l3 = sp.symbols('l3', real = True)
L = f + l1*g1 +l2*g2 + l3*g3
gradL = [sp.diff(L,c) for c in [x1,x2]] # gradient of Lagrangian w.r.t. (x,y)
KKT_eqs = gradL + [g1] + [g2] + [g3] + [-l1*x1] + [-l2*x2] + [l3*(x1+x2-2)] +[l1]+[l2]+[l3]
KKT_eqs2 = gradL + [-l1*x1] + [-l2*x2] + [l3*(x1+x2-2)]
print(KKT_eqs)
stationary_points = sp.solve(KKT_eqs2, [x1, x2, l1, l2, l3], dict=True) # solve the KKT equations
print('stationary_points',stationary_points)