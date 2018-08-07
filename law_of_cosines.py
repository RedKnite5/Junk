#   law_of_cosines.py
import math

# c^2 = a^2 + b^2 - 2ab*cos(C)


a = 3**.5
b = 2*3**.5
c = 3
C = None

def law_cos(a, b, c, C):
	'''Return the value of the variable that has the value None.'''
	
	if c is None:
		ans = (a*a + b*b - 2*a*b*math.cos(C))**.5
	if a is None:
		ans = ((4 * b*b * math.cos(C)*math.cos(C) - 4*(b*b-c*c))**.5 +
		2*b*math.cos(C)) / 2
	if b is None:
		ans = ((4 * a*a * math.cos(C)*math.cos(C) - 4*(a*a-c*c))**.5
		+ 2*a*math.cos(C)) / 2
	if C is None:
		ans = math.acos((a*a + b*b - c*c) / (2*a*b))
	
	return(ans)


print(ans)
print(math.pi/3)


