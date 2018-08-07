#   sin_approx.py
import math
pi = 3.1415926535897932

def sin(x):
	
	while x >= 2*pi:
		x = x - 2*pi
	
	while x < 0:
		x = x + 2*pi
	
	a = x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 - x**11/39916800
	a = a + x**13/6227020800 + x**15/1307674368000
	return(a)

s = 1
print(math.sin(s))
print(sin(s))






