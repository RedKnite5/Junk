# euler14.py

import multiprocessing as mp

tree = {1 :1}

def key_by_val(d, v):
	return tuple(key for key, val in d.items() if v == val)

def follow(n: int):
	while n not in tree:
		if not n % 2:
			tree[n] = n // 2
			n = n // 2
		else:
			tree[n] = 3 * n + 1
			n = 3 * n + 1


def longest_path(n, q, tree):
	
	t = 0
	leave = False
	paths = [i for i in key_by_val(tree, n) if i != 1]
	print("paths: ", paths, "n: ", n)
	while len(paths) > 0:
		
		if len(paths) > 1:
			jobs = []
			for i in paths:
				p = mp.Process(target=longest_path, args=(i, q, tree))
				jobs.append(p)
				p.start()
				leave = True
			for p in jobs:
				p.join()
		else:
			t += 1
			n = paths[0]
			paths = [i for i in key_by_val(tree, n) if i != 1]
		if leave:
			break
	q.put(t)



if __name__ == "__main__":
	q = mp.Queue()
	for i in range(2, 10):
		if i not in tree:
			follow(i)

	longest_path(1, q, tree)
	print(q.get())

