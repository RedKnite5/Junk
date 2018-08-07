# euler10.py


def check_prime(n):
	'''Return True if a number is prime.'''
	

	if n == 2:
		return True
	elif not n%2:
		return False
	elif n == 1:
		return False
	
	i = 3
	while i <= int(n**.5):
		if not n%i:
			return False
		i += 2
	return True



def primes(x=float("nan")):
	'''Generate a list of primes.'''
	
	count = 3
	yield 2
	while 1:
		if check_prime(count):
			yield count
		count += 2
		if count > x:
			return


x = sum(primes(2_000_000))
print(x)