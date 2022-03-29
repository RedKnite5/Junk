
data = [1, 2, 3]


def mean(seq):
	return sum(seq) / len(seq)

f_hb = max
f_h = min
f_b = mean

print(f"{f_hb.__name__}: {f_hb(data)}")


modify_hb = True
modify_b = False

if modify_hb:
	import sys
	
	ab = 0
	a = 6

	f = open(sys.argv[0])
	program = "".join(f).replace(chr(98 + ab), "")
	f.close()
	exec(program)


