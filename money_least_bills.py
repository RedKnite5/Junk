import math

def start():
	money(36.41)
	
def money(cents,*arg):
	money = cents*100
	ans = {}
	if len(arg) > 0:
		denoms = arg[0]
	else:
		denoms = {
		"twenty":2000,
		"ten":1000,
		"five":500,
		"one":100,
		"quarter":25,
		"dime":10,
		"nickle":5,
		"penny":1}
	keys = denoms.keys()
	ans = ans.fromkeys(keys,0)
	for key, value in sorted(denoms.iteritems(), key=lambda (k,v): (-1*v,k)):
		while money >= denoms[key]:
			money -= denoms[key]
			ans[key] += 1
	
	return ans
	

start()