
#  python probability.py

times = 100
prob = 1/40000

def sum_prob(a,b):
	return(a + b - a*b)

a = prob	
for i in range(times-1):
	 a = sum_prob(a,a)
print(a)