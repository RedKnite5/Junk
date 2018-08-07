import math as m
import random as r
#   python stuff.py

for i in range(20):
	doors = [False,False,False]
	car = r.randint(0,2)
	doors[car] = True
	pick = r.randint(0,2)
	if doors[pick] == True:
		indices = [k for k, x in enumerate(doors) if x == False]
		open = r.randint(0,1)
		print(open," ",doors[indices[open]])
		
	else:
		for k,a in enumerate(doors):
			if k != pick and a == False:
				print(k," ",a)





