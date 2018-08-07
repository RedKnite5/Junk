import mod
import sympy as s
# python lawcos.py

def lawcos(solve_for,_a,_b,_c,_C):
	a,b,c,C = s.symbols("a b c C")
	
	for i in (a,b,c,C):
		if solve_for != i:
			i = eval("_"+str(i))
	
	law = s.Eq(c**2,a**2+b**2-(2*a*b*s.cos(C)))
	print(
	print(s.solveset(law,s.sympify(solve_for)))
	
lawcos("c",2,2,0,30)