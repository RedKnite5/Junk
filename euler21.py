# euler21.py


def factor(n: int) -> set:
	'''Return a list of all factors of n.'''

	factors = set()
	for i in range(1, int(n ** .5) + 1):
		if not n % i:
			factors.add(i)
			factors.add(n // i)
	return factors


def amiable(n, m):
	nf = factor(n)
	nf.remove(n)
	mf = factor(m)
	mf.remove(m)
	return sum(nf) == m and sum(mf) == n

def sum_factor(n):
	f = factor(n)
	f.remove(n)
	return sum(f)

amiable = set()
max = 10000
num = 2
while num < max:
	s = sum_factor(num)
	if sum_factor(s) == num and s != num:
		amiable.add(num)
		amiable.add(s)
	num += 1
print(sum(amiable))
