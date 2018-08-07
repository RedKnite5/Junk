# euler7.py

from itertools import islice

def check_prime(n):
	'''Return True if a number is prime.'''
	
	if n == 1:
		return(False)
	elif n == 2:
		return(True)
	elif not n%2:
		return(False)
	
	i = 3
	sqrt_n = int(n**.5)
	while i <= sqrt_n:
		if not n%i:
			return(False)
		i += 2
	return(True)


def primes():
	'''Generate a list of primes.'''
	
	count = 3
	yield 2
	while 1:
		if check_prime(count):
			yield count
		count += 2

c = 10000
x = list(islice(primes(), c, c+1))[0]
print(x)


