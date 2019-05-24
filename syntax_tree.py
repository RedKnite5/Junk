# syntax_tree.py

import regex

op = ("+", "-", "*", "/", "^")
func = ("sin", "cos", "tan", "log")


tokens = {
	"+": {"precedence": 1, "associativity": "left"},
	"-": {"precedence": 1, "associativity": "left"},
	"*": {"precedence": 2, "associativity": "left"},
	"/": {"precedence": 2, "associativity": "left"},
	"^": {"precedence": 3, "associativity": "right"},
	#"!": {"precedence": 4, "associativity": "left"},
}

def tokenize(s):
	return list(reversed(s.split(" ")))

def num(s):
	try:
		float(s)
		return True
	except:
		return False

def post(l):
	op = []
	out = []
	for i in l:
		if num(s):
			out.append(i)
		elif i in func:
			op.append(i)
		
		
		
		

s = "3 * ( 1 + 1 )"

print(tokenize(s))
