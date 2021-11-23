# shroot.py

import random as r



def shroot():
	if r.randint(0, 1):  # 1 is lose
		return 0
	total = 2
	while True:
		if r.randint(0, 1):
			return total
		total *= 2


total = 0
for i in range(1000):
	total += shroot()
print("average: ", total / 100)


