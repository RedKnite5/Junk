# row_ops.py

import numpy as np


def echelon(a, reduced=False):
	a = np.array(a, dtype=np.float64)
	
	if not a.any():
		return a
	
	row_num = 1
	while a[0, 0] == 0:
		a[[0, row_num]] = a[[row_num, 0]]
		row_num += 1
	
	a[0, :] /= a[0, 0]
	
	for i in range(1, a.shape[0]):
		if a[i, 0] != 0:
			a[i, :] += -a[i, 0] * a[0, :]
	
	a[1:, 1:] = echelon(a[1:, 1:])
	
	if not reduced:
		return a
	else:
		
		coords = np.column_stack(np.where(a == 1))
		pivot = sorted(coords.tolist(), key=lambda var: (var[0], -var[1]), reverse=True)[0]
		for i in range(0, pivot[0]):
			a[i, :] += -a[i, pivot[1]] * a[pivot[0], :]
			
		
		
		print(a)


a = np.arange(12).reshape(3, 4) + np.arange(6, 18).reshape(3, 4)
ap = echelon(a, reduced=True)


