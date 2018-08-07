import sympy as s
# python derivatives.py

x = s.symbols("x")
y = s.symbols("y",cls=s.Function)

string = "x"
print("Equation:")
string = input()
equation = s.sympify(string)
ans = s.diff(equation,x)
print(ans)