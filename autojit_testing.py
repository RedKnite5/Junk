#   python autojit_testing.py
from numba import autojit
from timeit import default_timer as timer

@autojit
def add(max):
	r = 0
	for i in range(max+1):
		r+=i
	return(r)

start = timer()
print(add(100000000))
print(timer()-start)




