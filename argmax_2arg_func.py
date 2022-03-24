# argmax_2arg_func.py
# specifically for savetowayback


import random as r

def func(x, y):
	return 10 - x**2 - (y - 2)**2
	
def argmax(func, args, limits):
	
	value = []
	for i in range(args):
		value.append(r.randint(*limits[i]))
	
	test = func(*value)
	for i in range(args):
		
	
	
	
	
max = argmax(func, 2, [(0, 500), (0, 1000)])
print(max)