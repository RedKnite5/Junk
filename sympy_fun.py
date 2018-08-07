# sympy_fun.py

from sympy import *
import numpy as np


x = symbols("x")


exp = cos(x - 2) + 1

val = exp.subs([(1, 2*x), (x, x**4), (2, sin(x))])

pie = pi.evalf(23)

one = cos(2)**2 + sin(2)**2
z = (one-1).evalf(chop = True)

f = lambdify(x, val, "numpy")

print(f(np.arange(10)))

g = (cos(x)-1)*(cos(x)+2)*(cos(x)+5)**2

print(expand(g - cos(x)))

