# sudoku.py

easy = """
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

evil = """
000600010
007000000
820009300
004000500
003007000
570900006
000080003
950002800
400000000
"""

#ToDo:
#  Pairs
#  Hidden Pairs
#  X-Wing
#  XY-Wing


class Board(object):
	def __init__(self, string: str):
		
		data = string.split("\n")
		
		self.size = len(data)
		digits = {i for i in range(1, self.size + 1)}
		
		self.board = [
			[{int(data[j][i])} if int(data[j][i]) else digits.copy()
			for i
			in range(self.size)] for j in range(self.size)
		]

	def pair(self):
		pass

	def check_line(self, direction, num: int):
		assert direction in ("hori", "vert")
		
		present = set()
		modified = False
		
		iterable = self.board[num] if direction == "hori" else self.board
		
		for obj in iterable:
			if direction == "vert":
				square = obj[num]
			else:
				square = obj
			
			if len(square) == 1:
				present.add(next(iter(square)))
		
		for obj in iterable:
			if direction == "vert":
				square = obj[num]
			else:
				square = obj

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
	
	def required_digits_row(self, row):
		modified = False
		
		for d in range(1, self.size + 1):
			count = 0
			location = None
			for square in self.board[row]:
				if d in square:
					count += 1
					location = square
			if count == 1 and len(location) > 1:
				location.clear()
				location.add(d)
				modified = True
		
		if modified:
			print("row")
		return modified

	def required_digits_column(self, column):
		modified = False
		
		for d in range(1, self.size + 1):
			count = 0
			location = None
			for row in self.board:
				square = row[column]
				if d in square:
					count += 1
					location = square
			if count == 1 and len(location) > 1:
				location.clear()
				location.add(d)
				modified = True
		
		if modified:
			print("column")
		return modified

	def required_digits_box(self, box):
		modified = False
		
		squares = [self.board[3 * (box // 3) + i // 3][3 * (box % 3) + i % 3]
			for i in range(self.size)]
		for d in range(1, self.size + 1):
			count = 0
			location = None
			for square in squares:
				if d in square:
					count += 1
					location = square
			if count == 1 and len(location) > 1:
				location.clear()
				location.add(d)
				modified = True
		
		if modified:
			print("box")
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
		
		condition = self.basic_pass()
		while condition:
			condition = self.basic_pass()

	def basic_pass(self) -> bool:
		mod = False
		for i in range(self.size):
			mod = mod or self.check_line("hori", i)
			mod = mod or self.check_line("vert", i)
			mod = mod or self.check_box(i)
			mod = mod or self.required_digits_row(i)
			mod = mod or self.required_digits_column(i)
			mod = mod or self.required_digits_box(i)
			
		return mod
	
	def to_string(self):
		s = ""
		for row in self.board:
			for square in row:
				if len(square) == 1:
					s += str(next(iter(square)))
				else:
					s += "0"
			s += "\n"
		return s


board = Board(evil[1:-1])

print(board)
board.solve()
print(board)
print(board.to_string())

	
	
	

