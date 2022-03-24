
# parsing.py

import re


def to_tokens(s):

	# Resource for updating
	# http://lisperator.net/pltut/parser/token-stream
	
	nums = "[0-9][0-9_]*"
	open_paren = "\\("
	close_paren = "\\)"
	operator = "[-+*^%!/]"
	name = "[a-zA-Z_][a-zA-Z0-9_]*"
	space = "[ ]+"
	
	token = '|'.join((nums, open_paren, close_paren, operator, name, space))
	
	tokens = []
	while len(s) > 0:
		if " " in (m := re.match(token, s))[0]:
			pass
		else:
			tokens.append(m[0])
		
		s = s[m.end():]
	
	return tokens
	
	
def make_tree(tokens):
	
	for t in tokens:
		pass



	
s = "(1 + 2 ) * 3"


print(to_tokens(s))