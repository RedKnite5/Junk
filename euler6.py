# euler6.py


def sum_square_difference(x):
	'''Find the difference between the sum of the squares of the natural
	numbers up to x and the square of the sum of the natural numbers
	up to x.'''

	a = sum(range(x))**2
	b = sum(map(lambda a: a*a, range(x)))
	return(a-b)
	
print(sum_square_difference(101))