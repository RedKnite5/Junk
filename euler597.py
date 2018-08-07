# euler597.py


n = 2
L = 1800

order = tuple(range(n))

def even_parity(l1, l2):
	'''Determine whether a permutaion of a list is even or odd.'''

	assert len(l1) == len(l2), str(l1) + str(l2)
	assert set(l1) == set(l2), str(l1) + str(l2)

	inversions = 0
	for count, i in enumerate(l2):
		for k in l2[count:]:
			if i > k:
				inversions += 1
	return not inversions % 2
