# euler65.py

from fractions import Fraction

def collaspe_frac(it):
	
	x = Fraction(0)
	for count, val in enumerate(reversed(it)):
		
		if count == len(it) - 1:
			return(val + x)

		if not count:
			x = Fraction(1, val)
		else:
			x = 1 / (val + x)


def cont_frac_e(values=-1):
	'''Generate a sequence of denomenators for the contiued fraction
	for e.'''
	
	count = 0
	while True:
		if count != values:
			if not count:
				yield 2
			elif not (count + 1) % 3:
				yield int((count + 1) * 2 / 3)
			else:
				yield 1
			count += 1
		else:
			return

def sum_digits(n):
	digits = list(str(n))
	return(sum(map(lambda x: int(x), digits)))

x = collaspe_frac(list(cont_frac_e(100)))
print(sum_digits(x.numerator))
