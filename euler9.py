# euler9.py

from fractions import Fraction

a = Fraction(1)
while 1:
	b = (10 ** 6 - 2000 * a) / (2000 - 2 * a)
	c = (b*b + a*a)**.5
	if a.denominator == 1 and b.denominator == 1 and c.is_integer():
		print(a*b*c)
		break
	a += 1