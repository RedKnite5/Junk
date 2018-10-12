# euler22.py

import sys
from os.path import join, dirname

alpha = {l: i + 1 for i, l in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

def word_sum(word):
	return sum(map(lambda a: alpha[a], list(word)))

with open(join(dirname(sys.argv[0]), "names.txt"), "r") as file:
	names = "".join(file.readlines()).split(",")

names = sorted(list(map(lambda a: a[1:-1], names)))	

total = 0
for num, name in enumerate(names):
	total += (num + 1) * word_sum(name)
print(total)
