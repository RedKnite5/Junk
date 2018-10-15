# euler48.py
import timeit

def mod_exp(a, b, c):
	binary = "".join(reversed(bin(b)[2:]))
	
	powers = [a % c]
	for i in range(len(binary) - 1):
		powers.append((powers[-1] ** 2) % c)
	
	product = 1
	for i, n in enumerate(binary):
		if int(n):
			product *= powers[i]
	
	return product % c


def way2(total):
	return sum(mod_exp(i, i, int(1e10)) for i in range(1, total)) % int(1e10)

print(way2(1000))
