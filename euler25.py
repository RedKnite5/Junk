from math import log10 as log
from decimal import Decimal

PHI = Decimal(1.6180339887498948482045868343656381177203091798057628621354486227052604628189024497072072041893911374)
pHI = Decimal(0.6180339887498948482045868343656381177203091798057628621354486227052604628189024497072072041893911374)


def fib(n):
	pn = PHI ** n
	npn = -pHI ** n if n & 1 else pHI ** n
	
	return (pn - npn) / Decimal(5 ** .5)





def fib_digits(n):
	return n * log(PHI) - .5 * log(5) + 1


for i in range(1000, 6000):
	d = fib_digits(i)
	print(d)
	
	if d >= 1000:
		print("Done: ", end="")
		print(i)
		break


print(fib(4782))
print(len(str(int(fib(4782)))))
#print(fib(12))
#print(fib_digits(11))



