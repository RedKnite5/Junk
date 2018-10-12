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

def way1():
	return sum(i**i for i in range(1,1000))%int(1e10)

def way2():
	return sum(mod_exp(i, i, int(1e10)) for i in range(1, int(1000)))%int(1e10)

x = timeit.timeit("way1()", globals={"way1": way1})
y = timeit.timeit("way2()", globals={"way2": way2})
print(x)
print(y)
