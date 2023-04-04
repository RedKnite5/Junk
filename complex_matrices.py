
from sympy import *
init_printing(use_unicode=True)

def polar(x):
	r, i = x.as_real_imag()
	mag = (r*r + i*i)**.5
	ang = atan(i / r)
	return f"{mag}∠{ang}"

'''
m = [
	[10-10*I, 10*I],
	[50+10*I, -10*I],
]

m = Matrix(m)
v = [
	40-40*I,
	0
]

v = Matrix(v)
out = simplify(m**-1*v)
pprint(N(out))
'''

w, R, L1, L2, C = symbols("w R L1 L2 C")
a = I*L1*w/(I*w*(L1+L2)+R)
z = a*(I*L2*w+R)-I/(w*C)
H = R*a/z

eq1 = H.subs([(C, 1), (L1, 1), (L2, 1), (R, 1)])
eq2 = (I*w)**2 / ((I*w)**3 + (I*w)**2 + 2*I*w + 1)
print(simplify(eq1-eq2))

