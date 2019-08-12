# list_tools.py

import numpy as np

a = np.arange(0,27).reshape(3,3,3)

def to_tuple(a):
	if isinstance(a, (np.ndarray, list, tuple, set, frozenset)):
		return tuple(map(to_tuple, a))
	else:
		return a


b = set((1,3, 2,2))
print(tuple(b))