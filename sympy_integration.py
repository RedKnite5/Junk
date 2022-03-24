
from math import pi

import sympy
from sympy.functions.elementary.exponential import exp


h = 6.626E-34
c = 3.0E8
k = 1.3806E-23


T = sympy.Symbol("T")
x = sympy.Symbol("x")

def f(x):
    return 4*pi*h*c**2/(x**5*exp(h*c/(x*k*T))-1)

def g(x):
	return sympy.functions.elementary.exponential.exp(h/(x*T))

res = sympy.integrate(f(x), (x, 0.0, 3))
print(res)
