import mod 
# python power_rule.py

def pwr_rl(expression):
	x_index = expression.find("x")
	coef = expression[:x_index]
	var = len(coef) == 0
	if len(coef) == 0:
		coef = "1"
	else:
		coef = coef[:-1]
	int(coef)
	exp_index = expression.find("**")
	exp = int(expression[exp_index+2:])
	coef = int(coef)*exp
	exp-=1
	ans = str(coef) + "x**" + str(exp)
	return(ans)
	
print(pwr_rl("4*x**9"))