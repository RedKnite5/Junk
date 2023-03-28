from sympy import *

var("x")

def convolve(f, g, x):
    T = Symbol("T")
    fp = f.subs(x, T)
    gp = g.subs(x, x-T)
    return integrate(fp * gp, (T, -oo, oo))


u = Heaviside

c = convolve(u(x), u(x), x)
pprint(c)


