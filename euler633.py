# euler633.py

from math import sqrt

import cProfile as cp


def prime_factors(n):
	d = {}

	while not n % 2:
		d[2] = d.get(2, 0) + 1
		n /= 2
		  
	# n must be odd at this point 
	# so a skip of 2 ( i = i + 2) can be used 
	for i in range(3, int(sqrt(n)) + 1, 2): 

		while not n % i:
			d[i] = d.get(i, 0) + 1
			n /= i 

	if n > 2: 
		d[n] = d.get(n, 0) + 1

	return d

def count_sqr(n):
	count = 0
	for mul in prime_factors(n).values():
		if mul > 1:
			count += 1
	return count

def C_k(n, k):
	count = 0
	for i in range(1, n + 1):
		if count_sqr(i) == k:
			count += 1
	return count

def ratio(n, k):
	return C_k(n, k) / n


#print(ratio(int(1e6), 1))
s = cp.run("ratio(int(1e6), 1)")
print(s)


