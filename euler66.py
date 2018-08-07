# euler66.py


def counter(start=0):
	
	x = start
	while True:
		x += 1
		yield x
		
def range_no_squares(end):
	
	
	x = 0
	while True:
		x += 1
		if (x**.5).is_integer():
			x += 1
		if x == end:
			return
		yield x


def find_solution(d):
	'''Find the minimal solution to the diophantine equation
	y^2 - d*x^2 = 1'''
	
	for i in counter(850000000):
		if i%1000 == 0:
			print(i)
		if (((i*i-1)/d)**.5) and (((i*i-1)/d)**.5).is_integer():
			return(i)

#x = [find_solution(i) for i in range_no_squares(61)]
#print(max(x))

print(find_solution(61))
