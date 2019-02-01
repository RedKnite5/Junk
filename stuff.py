#   stuff.py

class a(object):
	def __init__(self):
		self.var = 1

class b(a):
	def __init__(self):
		self.var2 = 2

class c(a):
	def __init__(self):
		self.var2 = 3

class d(b, c):
	def __init__(self):
		self.var2 = 9
		super().__init__()





f = d()
print(f.var2)