# python shunting_yard.py

import re, math

def is_number(str):
	try:
		int(str)
		return True
	except ValueError:
		return False

def is_name(str):
	return re.match("\w+", str)

def peek(stack):
	return stack[-1] if stack else None

def apply_operator(operators, values):
	binary_operators = ["+", "-", "*", "/", "**"]
	operator = operators.pop()
	right = values.pop()
	if operator in binary_operators:
		print("before error", operators)
		print("before error", values)
		left = values.pop()
		values.append(eval("{0}{1}{2}".format(left, operator, right)))
	elif operator == "!":
		values.append(math.gamma(float(right) + 1))

def greater_precedence(op1, op2):
	precedences = {'+' : 0, '-' : 0, '*' : 1, '/' : 1, "**": 2, "!": 3, "cos": float("inf")}
	return precedences[op1] > precedences[op2]

def evaluate(expression):
	tokens = re.findall("\*\*|[!+/*()-]|\d+|[a-zA-Z]+", expression)
	values = []
	operators = []
	print(operators)
	print(values)
	for token in tokens:
		if is_number(token):
			values.append(int(token))
		elif token == '(':
			operators.append(token)
			print(operators)
			print(values)
		elif token == ')':
			top = peek(operators)
			while top is not None and top != '(':
				apply_operator(operators, values)
				top = peek(operators)
			operators.pop() # Discard the '('
		else:
			# Operator
			top = peek(operators)
			while top is not None and top not in "()" and greater_precedence(top, token):
				apply_operator(operators, values)
				top = peek(operators)
			operators.append(token)
			print(operators)
			print(values)
	while peek(operators) is not None:
		apply_operator(operators, values)

	return values[0]









expression = "1+cos(2-2)+ 1"
print("Shunting Yard Algorithm: {0}".format(evaluate(expression)))
#print("Python: {0}".format(eval(expression)))
