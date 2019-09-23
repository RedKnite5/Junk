#  stuff.py


class Tree(object):

	op_prec = {
		"+": {"precidence": 1, "operands": (-1, 1)},
		"-": {"precidence": 1, "operands": (-1, 1)},
		"*": {"precidence": 2, "operands": (-1, 1)},
		"/": {"precidence": 2, "operands": (-1, 1)},
		"%": {"precidence": 2, "operands": (-1, 1)},
		"**": {"precidence": 4, "operands": (-1, 1)},
		"^": {"precidence": 4, "operands": (-1, 1)},
		"!": {"precidence": 5, "operands": (-1)},
		"sin": {"precidence": 6, "operands": (1)},
		"cos": {"precidence": 6, "operands": (1)},
	}

	def __init__(self, s):
		branches = self.make_branches(s)
		self.tree = self.structure(branches)
		
	def structure(self, branches):
		
		branches = branches[::-1]
		
		ops = sorted(self.__class__.op_prec.items(),
			key=lambda a: a[1]["precidence"])
		for op, data in ops:
			try:
				index = branches.index(op)
				
				# doesn't include all of either side of the operator
				return {op: tuple((self.structure(branches[index + i]) if isinstance(branches[index + i], list) else branches[index + i] for i in data["operands"]))}
			except ValueError:
				pass
		
		
	def make_branches(self, tokens):
		branch = []
		
		i = 0
		while i < len(tokens):
			t = tokens[i]
			i += 1
			if t == "(":
				branch.append(self.make_branches(tokens[i:]))
			elif t == ")":
				return branch
			else:
				branch.append(t)

	def tokenize(string, categories=None):
		if categories is None:
			categories = [
				"abcdefghijklmnopqrstuvwxyz_", "0123456789",
				*"`~!@#$%^&*()-=+{[}]\\|;:'\"<,>./?"]
		
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

	def __str__(self):
		return str(self.tree)

t = Tree("1+3+(4-1)+5")
print(t)











