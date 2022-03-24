from math import gcd


top = [3, 7]
bound = [2, 5]
tmp = [2, 5]
d = 1
while tmp[1] < 1_000_000:
	bound = [tmp[0] // d, tmp[1] // d]
	tmp = [top[0] + bound[0], top[1] + bound[1]]
	d = gcd(tmp[0], tmp[1])
print(bound)
print(tmp)

