# self_docing_ints

import operator
from copy import deepcopy

class SD_Int(int):
	def __init__(self, x, base=10, doc=""):
		self.doc = str(self)
	
	@classmethod
	def ops(cls, op, symbol):
		def func(self, other):
			if isinstance(other, cls):
				self.doc = f"{self.doc} {symbol} {other.doc}"
				return super().__add__(int(other))
			else:
				self.doc = f"{self.doc} {symbol} {other}"
				return super().__add__(other)

		def rfunc(self, other):
			if isinstance(other, cls):
				self.doc = f"{other.doc} {symbol} {self.doc}"
				return super().__add__(int(other))
			else:
				self.doc = f"{other} {symbol} {self.doc}"
				return super().__add__(other)
		
		func.__name__ = f"__{op.__name__}__"
		func.__doc__ = op.__doc__
		
		ifunc = func
		
		rfunc.__name__ = f"__r{op.__name__}__"
		rfunc.__doc__ = op.__doc__
		
	
		
	def __add__(self, other):
		self.doc = f"{self.doc} + {other}"
		return super().__add__(other)
	
	def __radd__(self, other):
		self.doc = f"{other} + {self.doc}"
		return super().__radd__(other)
	
	def __iadd__(self, other):
		self.doc = f"{self.doc} + {other}"
		return super().__add__(other)
	
	def __sub__(self, other):
		self.doc = f"{self.doc} - {other}"
		return super().__sub__(other)
	
	def __rsub__(self, other):
		self.doc = f"{other} - {self.doc}"
		return super().__rsub__(other)
	
	def __isub__(self, other):
		self.doc = f"{self.doc} - {other}"
		return super().__isub__(other)
		


x = SD_Int(5)
print(x)
x += 4
print(x.doc)


def f():
	print(1)
	
g = deepcopy(f)

print(f is g)
