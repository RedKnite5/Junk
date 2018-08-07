import sympy, math
# python int_approx.py

x = sympy.Symbol("x")
#y = sympy.Function("y")


mode = "midpoint rect"
def y(x):
	return(-1*sympy.sin(x))
inter = [0,2]
pieces = 100

def div(inter,pieces):
	ans = []
	for i in range(pieces):
		first = inter[0]+i*(inter[1]-inter[0])/pieces
		second = inter[0]+(i+1)*(inter[1]-inter[0])/pieces
		ans.append([first,second])
	return(ans)

def rect(par = [[0,1]], point = "m", y = lambda a:a):
	area = 0
	for i in par:
		if point in ("m","mid","midpoint"):
			x_val = (i[0]+i[1])/2
		elif point in ("l","left","left end point"):
			x_val = i[0]
		elif point in ("r","right","right end point"):
			x_val = i[1]
	
		area += (i[1]-i[0])*y(x_val)
	return(area)
	
def trap(par = [[0,1]], y = lambda a:a):
	area = 0
	for i in par:
		area += (i[1]-i[0])*(y(i[0])+y(i[1]))/2
	return(area)
	
	
def simp(par=[[0,1]], y = lambda a:a):
	area = 0
	for i in par:
		area += ((i[1]-i[0])/6) * (y(i[0]) + 4*y((i[0]+i[1])/2) + y(i[1]))
	return(area)
	
print(rect(par=part))
	
	
	
	
	
	
	
	
	
	
	