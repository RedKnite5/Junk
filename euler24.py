#euler24

import itertools as it





def fact(n):
	x = 1
	for i in range(2, n+1):
		x *= i
	return x




n = map(str, range(10))
s = list(it.permutations(n))

#for i, p in enumerate(s):
#	print(i, "".join(p))
print(s[1_000_000])

#print(s[3*fact(4)])



def swaps(n, x):
	n = n - 1
	swaps = []
	for i in range(n):
		swaps.append(x // fact(n-i))
		x %= fact(n-i)
	return swaps



def apply(swaps):
	l = len(swaps)
	s = list(range(l + 1))
	
	for i, n in enumerate(swaps):
		val = s.pop(i + n)
		s.insert(i, val)
		#s[i], s[i + n] = s[i + n], s[i]
		print(s)
	print("")
	return "".join(map(str, s))

print("")

print(apply(swaps(10, 1_000_000-1)))
print("")
print(apply(swaps(6, 717)))
print("")
#print(apply(swaps(5, 100)))











