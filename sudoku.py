# sudoku.py

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
		
		data = string.split("\n")
		
		self.size = len(data)
		digits = {i for i in range(1, self.size + 1)}
		#{9, 8, 7, 6, 5, 4, 3, 2, 1}
		
		self.board = [
			[{int(data[j][i])} if int(data[j][i]) else digits.copy()
			for i
			in range(self.size)] for j in range(self.size)
		]

	def check_verticle(self, column: int):
		present = set()
		modified = False
		
		for row in self.board:
			square = row[column]
			if len(square) == 1:
				present.add(next(iter(square)))
		
		for row in self.board:
			square = row[column]
			if len(square) > 1:
				if not modified and not present.isdisjoint(square):
					modified = True
				square -= present
		
		return modified

	def check_horizontal(self, row: int):
		present = set()
		modified = False
		
		for square in self.board[row]:
			if len(square) == 1:
				present.add(next(iter(square)))
		
		for square in self.board[row]:
			if len(square) > 1:
				if not modified and not present.isdisjoint(square):
					modified = True
				square -= present
		
		return modified

	def check_box(self, box: int):
		column = box % 3
		row = box // 3
		
		present = set()
		modified = False
		
		squares = [self.board[3 * (box // 3) + i // 3][3 * (box % 3) + i % 3]
					for i in range(self.size)]
		
		for square in squares:
			if len(square) == 1:
				present.add(next(iter(square)))
		
		for square in squares:
			if len(square) > 1:
				if not modified and not present.isdisjoint(square):
					modified = True
				square -= present
		
		return modified
	
	def show(self):
		s = "-" * 4 * self.size + "\n|"
		
		for row in self.board:
			for i in range(3):
				for square in row:
					for j in range(1, 4):
						d = i * 3 + j
						if d in square:
							s += str(d)
						else:
							s += " "
					s += "|"
				s += "\n|"
			s += "-" * 4 * self.size + "\n|"
		
		return s[:-1]
		
	def __str__(self):
		return self.show()

	def solve(self):
	
		while self.basic_pass():
			pass
		
	def basic_pass(self) -> bool:
		mod = False
		for i in range(self.size):
			mod = mod or self.check_verticle(i)
			mod = mod or self.check_horizontal(i)
			mod = mod or self.check_box(i)
			
		return mod
		


board = Board(string[1:-1])

print(board)
board.solve()
print(board)

	
	
	

