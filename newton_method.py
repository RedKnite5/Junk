import sympy
#python newton_method.py 

x = sympy.symbols("x")
f = sympy.symbols("f",cls=sympy.Function)

ans = [1]
f = x**2-3
element = 3

for i in range(element):
	ans.append(ans[-1]-f(ans[-1])/sympy.diff(f(ans[-1]),x))


print(ans[-1])


