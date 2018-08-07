'''
sympy_stuff.py

Author: Max Friedman
'''

import sympy


x = sympy.symbols("x")

expr = x ** 2 + 2 * x + 1

expr2 = (x + 1) ** 2

a = sympy.simplify(expr + expr2)
print(a)

