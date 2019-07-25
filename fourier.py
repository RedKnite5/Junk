#  fourier.py

from sympy import fourier_series
from sympy.abc import x
from sympy.plotting import plot
import sympy
from sympy import *

#s = fourier_series(sin(x**x)/(2**((x**x-pi/2)/pi)), (x, -1.5, 1.5))

g = 1.6**((x**x)*sin(x**x))
f = x**x

print(f)
for i in range(100):
	print(f.subs(x, i//10).evalf())

plot(f, (x, 1, 10), yscale="log")

