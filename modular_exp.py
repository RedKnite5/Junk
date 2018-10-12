# modular_exp.py

def mod_exp(a, b, c):
	binary = "".join(reversed(bin(b)[2:]))
	
	powers = [a % c]
	for i in range(len(binary) - 1):
		powers.append((powers[-1] ** 2) % c)
	
	product = 1
	print(powers)
	for i, n in enumerate(binary):
		if int(n):
			print(powers[i])
			product *= powers[i]
	
	return product % c



m = mod_exp(7, 256, 13)

print(m)
