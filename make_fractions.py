import math
#   python fractions.py

dec = 1.49534878122
def fraction(dec):
	i=1
	while True:
		if (i/dec)%1 == 0:
			return(str(i)+"/"+str(int(i/dec)))
			break
		if i > 100000:
			break
		i+=1

def roots(dec):
	for i in range(2,10):
		x = (fraction(round(dec**i,15)))
		if x != None:
			return(str(int(eval(x)))+"**"+fraction(1/i))
			break
		
print(roots(dec))