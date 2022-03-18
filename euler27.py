import math



def is_prime(n):
	if n < 2:
		return False
	
	for i in range(2, int(math.sqrt(n)) + 1):
		if (n / i).is_integer():
			return False
	return True


def prime_gen():
	n = 2
	while n < 1000:
		if is_prime(n):
			yield n
		n += 1

def integer_gen():
	yield 0
	
	n = 1
	while n != 1000:
		yield n
		if n > 0:
			n *= -1
		else:
			n = 1 - n


def formula_template(a, b):
	def func(n):
		return n * n + a * n + b
	
	return func


def check_prime_len(f):
	c = 0
	while is_prime(f(c)):
		c += 1
	return c


largest = 0

for b in prime_gen():
	for a in integer_gen():
		f = formula_template(a, b)
		count = check_prime_len(f)
		if count > largest:
			largest = count
			a_large = a
			b_large = b

print(a_large, b_large, largest)
print(a_large * b_large)




		

