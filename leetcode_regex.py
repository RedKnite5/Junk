

'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''
def regex(s, p):
	si = 0
	pi = 0
	while True:
		if pi + 1 < len(p) and p[pi + 1] == "*":
			pass






