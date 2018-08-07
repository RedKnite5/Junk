import math
from list_functions import factorize
# python factor_func.py

g = "5x**3"

def count(co):
	x=0
	for i in co:
		if i > x:
			x=i
	return(x)
	
	
def convert_back(col): #in dev
	degree = len(col)
	col = list(reversed(col))
	ans = ""
	for i in range(len(col)):
		if i == 0:
			ans = str(col[i])+ans
		if i == 1 and col[i] != 0:
			ans = str(col[i])+"x+"+ans
		if i>1 and col[i] != 0:
			ans = str(col[i])+"x**"+str(i)+"+"+ans
	return(ans)


def find_co(f):
	co = {}
	f=f.replace("-","+-")
	terms = f.split("+")
	for i in terms:
		if "**" in i:
			co[int(i[i.find("x")+3:])]=i[:i.find("x")]
		elif "x" in i:
			co[1]=i[:i.find("x")]
		else:
			co[0]=i
	for i in co:
		if co[i] == "":
			co[i]=1
		else:
			co[i] = int(co[i])
	return(co)
	
def find_pq(co):		
	x=count(co)
	if 0 in co:
		p = factorize(co[0])
	else:
		p=[1]
	q = factorize(co[x])
	factors = []
	for P in p:
		for Q in q:
			factors.append(P/Q)
	factors=list(set(factors))
	fac = []
	for i in factors:
		fac.append(-1*i)
	return(factors+fac)
	
def conv_li(dict):
	ans = []
	x=count(dict)
	for i in range(x,-1,-1):
		if i in dict:
			ans.append(dict[i])
		else:
			ans.append(0)
	return(ans)
			
def synthetic(co):
	factors = find_pq(co)
	coef = conv_li(co)
	for i in factors:
		ans = []
		ans.append(coef[0])
		for j in range(1,len(coef)):
			ans.append(ans[j-1]*i+coef[j])
		if ans[len(ans)-1]==0:
			ans.pop()
			return(i,ans)
			break
			

	

def factor_func(f): #in dev
	global final
	final = []
	co = find_co(f)
	
	if len(co)==1:
		final.append(f)
		
	x,y=synthetic(co)
	if x > 0:
		x="x+"+str(x)
	elif x < 0:
		x="x"+str(x)
	else:
		x=""
	final.append(x)
	f = y
	print(convert_back(f))
	
	return(final)

def det(g): #in dev
	co=find_co(g)
	x=count(co)
	
	
	

			
	
	
print(len(find_co(g)))
	
#factor_func(g)	














