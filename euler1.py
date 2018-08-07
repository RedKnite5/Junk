# euler1.py

# Find the sum of all the multiples of 3 or 5 below 1000.
# 233168

max = 1000

def sum_multiples(max, factors):
	'''Sum the multiples of the factors that are less than max then
	return the value.'''
	
	multiples = set()
	
	for f in factors:
		i = 0
		while i < max:
			multiples.add(i)
			i += f

	return(sum(multiples))

x = sum_multiples(max, (3,5))
print(x)
