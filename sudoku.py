# sudoku.py

import numpy as np

string = """
000005409
451002300
982000561
607000980
003460000
500287010
040070096
300000700
005946802
"""

class Board(object):
	def __init__(self, string: str):
		digits = {9, 8, 7, 6, 5, 4, 3, 2, 1}
		data = string.split("\n")
		self.possiblities = [
			[{int(data[j][i])} if data[j][i] else digits.copy()
			for i
			in range(9)] for j in range(9)
		]

	def check_verticle_missing(self, column: int):
		present = set()
		
		for row in self.board:
			square = row[column]
			if square != {0}:
				present.add(square)
		
		for row in self.board:
			square = row[column]
			if len(square) > 1:
				square -= present
	
	
		
		
		


board = Board(string[1:-1])

m = board.check_verticle_missing(0)
print(m)


	
	
	

