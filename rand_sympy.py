# rand_sympy.py

from sympy import *

x = symbols("x")
f = sec(x)**3
print(integrate(f, x))
