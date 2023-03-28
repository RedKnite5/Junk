
from sympy import *

x = Symbol("x")

f = 1/(sin(x))**.5)
a = integrate(f, (x, -1, 1))
print(N(a))
