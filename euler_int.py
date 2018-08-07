import sympy as s
#   python euler_int.py

x = 3
y = 0
dx = .05
end = 4

g = s.symbols("g")
f,dydx = s.symbols("f dydx", cls=s.Function)
f = g**2

dydx = s.sin(g)/g

for i in range(round(end/dx)):
	slope = dydx.subs(g,x)
	dy = dx * slope
	y += dy
	x += dx
print(y)

