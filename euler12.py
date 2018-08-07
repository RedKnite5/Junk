# euler12.py


def factor(n):
	'''Return a list of all factors of n.'''
	
	factors = set()
	for i in range(1, int(n ** .5) + 1):
		if not n % i:
			factors.add(i)
			factors.add(n // i)
	return factors

def triangle():
	'''Return the triangle numbers.'''
	
	t = 1
	c = 2
	while 1:
		yield t
		t += c
		c += 1

for i in triangle():
	if len(factor(i)) > 500:
		print(i)
		break