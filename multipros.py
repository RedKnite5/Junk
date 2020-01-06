
import multiprocessing as mp
import time

def square(x):
	time.sleep(1)
	return x*x

if __name__ == "__main__":
	x = tuple(range(50))

	with mp.Pool(10) as p:
		l = p.map(square, x)

	print(l)
