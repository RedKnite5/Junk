# euler5.py

import functools

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


def sort_by_length(a, b):
	'''Return the input as a tuple sorted with shortest items first.'''
	
	if len(a) > len(b):
		return(b, a)
	return(a, b)


def list_union(n, m):
	'''Return the smallest list that both lists are subsets of.'''
	
	n, m = sort_by_length(n, m)
	
	m = list(m)
	
	for i in n:
		if m.count(i) < n.count(i):
			m.append(i)
	return(m)
	
def lcm(a, b):
	'''Find the lowest common multiple of two numbers.'''
	
	alist = factorize(a)
	blist = factorize(b)
	
	return(functools.reduce(lambda a, b: a*b, list_union(alist, blist)))

x = functools.reduce(lcm, range(1, 100))
print(x)
