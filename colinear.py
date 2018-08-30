#   stuff.py

# cd C:\Users\Max\Documents\Python\ReCalc
# cd C:\Users\Max\Documents\Python\Junk


point1 = input("input a point\n")
point2 = input("input a second point\n")
point3 = input("input a third point\n")
t = eval(point1)
t2 = eval(point2)
t3 = eval(point3)

def distance(p1, p2):
	t = 0
	for n, n2 in zip(p1, p2):
		t += (n - n2) ** 2
	return t ** .5

def colinear(p1, p2, p3):
	d1 = distance(p1, p2)
	d2 = distance(p1, p3)
	d3 = distance(p2, p3)
	ds = (d1, d2, d3)
	sd = sorted(ds)
	if sd[0] + sd[1] == sd[2]:
		return True
	return False
	


print(colinear(t, t2, t3))
