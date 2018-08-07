#   series.py
import math
from numba import autojit

@autojit
def term(n, x):
	a = 1/x**n
	return(a)

def series_factory(term):
	@autojit
	def series(x):
		par = 0
		for n in range(1, 1000000):
			next = term(n, x)
			if next > float(1e-10):
				par += next
			else:
				break
		return(par)
	return(series)

p_series = series_factory(term)
print(p_series(3))