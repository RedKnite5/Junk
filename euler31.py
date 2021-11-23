# euler31.py


def check(comp):
	return sum(num * val for num, val in zip(comp, check.coins))
check.coins = (1, 2, 5, 10, 20, 50, 100, 200)


def add(comp, t):
	p = list(comp)
	
	if check(p) != t:
		p[0] += t - check(p)
		return tuple(p)
	
	p = list(comp)
	for c in range(0, 8):
		p[c] += 1
		if check(p) > t:
			for i in range(c + 1):
				p[i] = 0
		else:
			return tuple(p)
	raise ValueError("Out of places")


def count(t):

	count = 0
	comp = (0, 0, 0, 0, 0, 0, 0, 0)
	while True:
		try:
			comp = add(comp, t)
		except ValueError:
			return count
		
		if check(comp) == t:
			count += 1
			print(comp)

ans = count(200)
print(f"Ans: {ans}")


