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

hard = """
530002000
009030200
027000010
700000000
018090005
090100002
000410070
085700029
004900500
"""

expert = """
479005000
000030008
000000060
340000001
006050009
800000006
000000427
007000000
000190000
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

	def check_line(self, direction, num: int):
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
		
		return modified

	def pair(self, direction, num: int):
		modified = False
		
		if direction == "hori":
			iterable = self.board[num]
		elif direction == "vert":
			iterable = self.board
		elif direction == "box":
			iterable = [self.board[3 * (num // 3) + i // 3][3 * (num % 3) + i % 3]
				for i in range(self.size)]
		
		pairs = {}
		for obj in iterable:
			if direction == "vert":
				square = obj[num]
			else:
				square = obj
			
			if len(square) == 2:
				pairs.setdefault(frozenset(square), 0)
				pairs[frozenset(square)] += 1
		
		for obj in iterable:
			if direction == "vert":
				square = obj[num]
			else:
				square = obj
			
			for key, value in pairs.items():
				if value != 2 or square == set(key):
					continue
				
				if not modified and not set(key).isdisjoint(square):
					modified = True
				square -= set(key)
		
		return modified
	
	# notepad++ highlighting bug? triple is not a keyword
	def triple(self, direction, num: int):
		modified = False
		
		if direction == "hori":
			iterable = self.board[num]
		elif direction == "vert":
			iterable = [row[num] for row in self.board]
		elif direction == "box":
			iterable = [self.board[3 * (num // 3) + i // 3][3 * (num % 3) + i % 3]
				for i in range(self.size)]
		
		triples = {}
		for square in iterable:
			if len(square) == 3:
				triples.setdefault(frozenset(square), 0)
				triples[frozenset(square)] += 1

		for square in iterable:
			if len(square) == 2:
				for key in triples:
					if square.issubset(key):
						triples[key] += 1
		
		for square in iterable:
			for key, value in triples.items():
				if value != 3 or square.issubset(frozenset(key)):
					continue
				
				if not modified and not set(key).isdisjoint(square):
					modified = True
				square -= set(key)
		
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
		
		modified = self.basic_pass()
		while modified:
			modified = self.basic_pass()
			if not modified:
				for i in range(self.size):
					modified = modified or self.triple("hori", i)
					modified = modified or self.triple("vert", i)
					modified = modified or self.triple("box", i)
					

	def basic_pass(self) -> bool:
		mod = False
		for i in range(self.size):
			mod = mod or self.check_line("hori", i)
			mod = mod or self.check_line("vert", i)
			mod = mod or self.check_box(i)
			mod = mod or self.required_digits_row(i)
			mod = mod or self.required_digits_column(i)
			mod = mod or self.required_digits_box(i)
			mod = mod or self.pair("hori", i)
			mod = mod or self.pair("vert", i)
			mod = mod or self.pair("box", i)
			
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

board.solve()
print(board)
print(board.to_string())

	
	
	

