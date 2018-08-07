# euler11.py

from functools import reduce
import numpy as np

filename = "C:\\Users\\Max\\Dropbox\\Python\\grid.txt"


def largest_product(l):
	'''Find the largest product of adjacent elements of a list.'''

	m = 0
	for i in range(len(l) - 3):
		b = reduce(lambda a, b: a * b, l[i:i + 4])
		if b > m:
			m = b
	return m


with open(filename, "r") as file:
	lines = file.readlines()
	lines = np.array(tuple(tuple(map(int, line.split())) for line in lines))
	
	a = []
	a.append(max(map(largest_product, lines)))
	a.append(max(map(largest_product, lines.swapaxes(0, 1))))

	for i in range(lines.shape[0] - 3):
		#print(np.diagonal(lines, i))
		a.append(largest_product(np.diagonal(lines, i)))
	for i in range(lines.shape[1] - 3):
		a.append(largest_product(np.diagonal(lines.swapaxes(0, 1), i)))

	for i in range(lines.shape[0] - 3):
		#print(np.diagonal(lines[:, ::-1], i))
		a.append(largest_product(np.diagonal(lines[:, ::-1], i)))
	for i in range(lines.shape[1] - 3):
		a.append(largest_product(np.diagonal(lines[:, ::-1].swapaxes(0, 1), i)))
	
	print(max(a))
	