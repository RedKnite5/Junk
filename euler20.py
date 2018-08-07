# euler20.py

def fact(n):
	'''Return the factorial of n with all the trailing zeros removed.'''

	result = 1
	for i in range(1, n):
		result *= i
		while not result % 10:
			result //= 10
	return result

def sum_digits(n):
	'''Sum the digits of a number.'''

	digits = list(str(n))
	return sum(map(lambda x: int(x), digits))

x = sum_digits(fact(100))
print(x)