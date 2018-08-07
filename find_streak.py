import mod,time,math
import random as rand
# python stuff3.py

l = []
for i in range(10):
	l.append(rand.randint(0,1))
s = [0]
ts = [0]
n=0
tn=0
for i in l:
	if i == 1:
		s[n] += 1
		tn+=1
		ts.append(0)
	else:
		s.append(0)
		n+=1
		ts[tn] += 1

s=list(filter(lambda a: a!=0,s))
ts=list(filter(lambda a: a!=0,ts))
print(max(s),s)
print(max(ts),ts)