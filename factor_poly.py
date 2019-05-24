# python factor_poly.py


def find_factor(n: int, i: int=2) -> int:
	'''Find the smallest prime factor of n above i.'''

	if i == 2:
		if not n % 2:
			return 2
		i = 3

	sqrt_n = int(n ** .5) + 1
	while i < sqrt_n:
		if not n % i:
			return i
		i += 2
	return n


def factorize(n: int, start: int=2):
	'''Return a tuple of prime factors of n'''

	factors = []
	while n > 1:
		f = find_factor(n, start)
		n = n // f
		factors.append(f)

	return tuple(factors)


def rational_root_thm(*coef):
	coef = tuple(map(lambda a: abs(a), coef))
	p_factors = set.union(set(factorize(coef[-1])), {1, coef[-1]})
	q_factors = set.union(set(factorize(coef[0])), {1, coef[0]})

	roots = set.union(*[{p/q for q in q_factors} for p in p_factors])
	roots = set.union(roots, set(map(lambda a: -a, roots)))
	
	return roots

def synthetic(divisor, *coefs):
	total = 0
	new = []
	for i in coefs:
		total += i
		new.append(total)
		total *= divisor
	if not total:
		new.pop()
		return tuple(new)
	else:
		return False

		
def express(*coef):
	ans = ""
	for i in range(len(coef)):
		if len(coef) - i > 2:
			"{coef}*x^{index-1}".format(coef=coef[i], index=i)
	
	
coef = "1 0 -4"
#coef = input("Give coefficients seperated by spaces./n")

coef = tuple(map(int, coef.split()))

factors = []
done = False
while not done:
	roots = rational_root_thm(*coef)
	for i in roots:
		factor = synthetic(i, *coef)
		if factor:
			print("factor: ", "x{:+g}".format(i))
			factors.append("x{:+g}".format(i))
			coef = factor
			break
	else:
		done = True
		factors.append(coef)


print(factors)
print(coef)

