# Future Pieces

import mymod

def worm_sort(word):
	list = mymod.parse(word)
	
	li = []
	s = 0
	num_0 = list[1]
	num_1 = num_0 + "."
	num = "." + num_1
	print num
	for i in range(len(num)):
		if num[i] == ".":
			new = ""
			for h in xrange(s+1, i):
				new += num[h]
			li.append(new)
			s = i
	li.pop(0)
	print li




word = "Gestation 1.2"	
worm_sort(word)