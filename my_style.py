# -*- coding: utf-8 -*-

'''
my_style.py
Author: Max Friedman
'''

import sys
import os
import tokenize
import io
from token import tok_name

def find(name):
	for root, dirs, files in os.walk(os.getcwd()):
		if name in files:
			return os.path.join(root, name)
		raise FileNotFoundError


def isonly(n, only):
	'''Check if n is comprized solely of elements found in only.'''

	for i in n:
		if i not in only:
			return False
	return True

class DummyFile(io.IOBase):
	def __init__(self, content):
		super(DummyFile, self).__init__()
		self.content = content
		self.count = 0
	def read(self, index=0):
		if self.count:
			return "".encode("utf-8")
		else:
			self.count += 1
			return self.content.encode("utf-8")
		

def split_into_tokens(s):
	'''Split a string into tokens.'''
	
	if s[-1] != "\n":
		s += "\n"
	
	file = DummyFile(s)
	token = tokenize.tokenize(file.readline)
	
	token_info = token.send(None)
	tokens = []
	#print(token_info)
	start = token_info.start
	notend = True
	while notend:
		token_info = token.send(None)
		print(tok_name[token_info.type])
		if token_info.start[1] == start[1]:
			notend = False
			break
		tokens.append(token_info)
	file.close()
	return tokens

if len(sys.argv) > 1:
	file_name = sys.argv[1]

file_path = find(file_name)

with open(file_path, "r", encoding = "utf-8") as file:
	for line_number, line in enumerate(file):
		line_number = line_number + 1
		if len(line.expandtabs(tabsize = 4)) > 72:
			print(
				"line %s if %s characters long."
				% (
				line_number,
				len(line.expandtabs(tabsize = 4))))
		if isonly(line, " 	"):
			print(
				"line {} is blank except ".format(line_number)
				+ "for whitespace.")
		if  len(line) > 1:
			if line[-2] in " 	":
				print("line {} has ".format(line_number)
					+ "trailing whitespace")
		
		tokens = split_into_tokens(line)
		token_strings = list(map(lambda a: a.string, tokens))
		
		if "return" in token_strings:
			try:
				if tokens[token_strings.index("return")].end[1] ==\
					tokens[token_strings.index("return")+1].start:
				
					print("'return(' on line {}".format(line_number))
			except IndexError:
				pass
			
		


