import sympy as s
#   python take_deriv.py

x = s.symbols("x")
f = s.symbols("f", cls=s.Function)


f = x*2
a = s.diff(f,x)
print(a)