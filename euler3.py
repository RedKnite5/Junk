# euler3.py

# find the larges prime factor of 600851475143.


def factorize(n):
	'''Return a tuple of prime factors of n'''
	
	factors = []
	for i in range(2, int(n**.5) + 1):
		if n % i == 0:
			factors.append(i)
			factors.extend(factorize(n // i))
			break
	else:
		factors.append(n)
	return(tuple(factors))

x = factorize(15*34*44*89*13+1)
print(x)
