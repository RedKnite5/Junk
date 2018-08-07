#   python integration.py
import re

i = "2x^2"


def brackets(s):
	"Inform separate whether parentheses match."
	
	x = 0
	for i in s:
		if i == "(":
			x += 1
		elif i == ")":
			x -= 1
	return(x)

def separate(s,splitter=","):
	"""Split up arguments of a function with commas
	like mod(x,y) or log(x,y) based on where commas that are only
	in one set of parentheses.
	"""
	
	# separate based on all commas
	terms = s.split(splitter)
	
	new_terms = []
	middle = False
	
	# iterate of over the groups separated by commas
	for i in range(len(terms)):
		
		# check if it is in the middle of a group of parentheses
		if middle == False:
			next_term = terms[i]
		
		# reevaluate if its in the middle of parentheses
		x = brackets(next_term)
		
		# if its not in the middle add the curren term to final list
		if x == 0:
			new_terms.append(terms[i])
			continue
		
		# if it is in the middle of a group
		if x > 0:
			
			# add the current term to the string of previous terms
			next_term = next_term + splitter + terms[i+1]
			
			# check if that was the end of the group
			if brackets(next_term) == 0:
				new_terms.append(next_term)
				middle = False
			else:
				middle = True
	
	return(new_terms)


power_rule = re.compile("([0-9]*)\*?x\^([0-9]+)")

power_m = re.search(power_rule,i)
def integrate(i):
	if power_m is not None:
		if power_m.group(1) == "":
			ans = str(float(power_m.group(2)))+"x^"+str(float(power_m.group(2))-1)
		else:
			part1 = str(float(power_m.group(1))
			* float(power_m.group(2)))
			ans = part1 + "x^" + str(float(power_m.group(2))-1)
		return(ans)

print(integrate(i))














