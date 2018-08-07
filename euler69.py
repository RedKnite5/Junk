# euler69.py

from math import gcd

def check_prime(n):
	'''Return True if a number is prime.'''
	
	if n == 1:
		return(False)
	elif n == 2:
		return(True)
	elif n%2 == 0:
		return(False)
	
	i = 3
	while i < int(n**.5):
		if n%i == 0:
			return(False)
		i += 2
	return(True)



def totient(n):
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result

max = (0, 0)
for i in range(1, 1_000_000):
	val = i / totient(i)
	if i%1000 == 0:
		print(i)
	if val > max[0]:
		max = (val, i)

print(max)