#  stuff.py

def tokenize(string, categories=None):
	if categories is None:
		categories = [
			"abcdefghijklmnopqrstuvwxyz_", "0123456789",
			"`~!@#$%^&*()-=+{[}]\\|;:'\"<,>./?"]
	
	token = ''
	tokens = []
	category = None
	for char in string:
		if token:
			if category and char in category:
				token += char
			else:
				tokens.append( token )
				token = char
				category = None
				for cat in categories:
					if char in cat:
						category = cat
						break
		else:
			category = None
			if not category:
				for cat in categories:
					if char in cat:
						category = cat
						break
			token += char
	if token:
		tokens.append( token )
	return tokens


def make_tree(tokens):
	branch = []
	
	i = 0
	while i < len(tokens):
		t = tokens[i]
		i += 1
		if t == "(":
			branch.append(make_tree(tokens[i:]))
		elif t == ")":
			return branch
		else:
			branch.append(t)
			
			


t = make_tree("1+3+(4-1)+5")
print(t)


















