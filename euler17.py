# euler17.py
from num_word_conversions import num_2_word


total = 0
for i in range(1, 1001):
	x = num_2_word(i)
	total += len(x) - x.count(" ")
print(total)
