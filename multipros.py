
import multiprocessing as mp
import time
from timeit import timeit

def square(x):
	time.sleep(1)
	return x*x

def square_list_multi(x, size):
	with mp.Pool(size) as p:
		return p.map(square, x)


if __name__ == "__main__":
	x = tuple(range(30))
	
	times = tuple(map(lambda s: timeit(
	f"multi(x, {s})", number=10, globals={"x": x, "multi": square_list_multi}),
	range(4, 12)))

	print(times)
	