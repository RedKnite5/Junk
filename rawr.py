'''
rawr

my own language

by Max Friedman
'''

import sys


sys.path.append("C:\\Users\\Max\\Dropbox\\Python")

with open(sys.argv[1], "r") as file:
	lines = file.readlines()

def if_only(l, only):
	'''Check if l is only composed of elements in only.'''
	
	return not set(l).issubset(only)


def remove_blank_lines(lines):
	'''Filter out all the lines that are just whitespace.'''

	return list(filter(lambda a: if_only(a, whitespace), lines))
	
class RawrInt(int):
	pass

class RawrFloat(float):
	pass


whitespace = {' ', '\t', '\n', '\r', '\x0b', '\x0c'}
types = {"integer", "string", "function", "float"}
keywords = {"a", "is",}


print(lines)