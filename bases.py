# bases.py

def number(arg, func=lambda a: a):
	'''Function that creates decorator that adds methods for arithmatic
	opperations. arg is treated as the number for all purposes.'''
	
	from math import ceil, floor, trunc

	def dec(cls):
		'''Decorator for classes that have an attribute that can be treated
		as the datastructure for arithmatic opperations. This decorator implements
		all the dunder methods using arg.'''

		def add(self, other):
				return func(self.__dict__[arg]) + other
		def radd(self, other):
				return other + func(self.__dict__[arg])
		def iadd(self, other):
				return func(self.__dict__[arg]) + other
		def sub(self, other):
				return func(self.__dict__[arg]) - other
		def rsub(self, other):
				return other - func(self.__dict__[arg])
		def isub(self, other):
				return func(self.__dict__[arg]) - other
		def mul(self, other):
				return func(self.__dict__[arg]) * other
		def rmul(self, other):
				return other * func(self.__dict__[arg])
		def imul(self, other):
				return func(self.__dict__[arg]) * other
		def div(self, other):
				return func(self.__dict__[arg]) / other
		def rdiv(self, other):
				return other / func(self.__dict__[arg])
		def idiv(self, other):
				return func(self.__dict__[arg]) / other
		def floordiv(self, other):
				return func(self.__dict__[arg]) // other
		def rfloordiv(self, other):
				return other // func(self.__dict__[arg])
		def ifloordiv(self, other):
				return func(self.__dict__[arg]) // other
		def truediv(self, other):
				return func(self.__dict__[arg]) / other
		def rtruediv(self, other):
				return other / func(self.__dict__[arg])
		def itruediv(self, other):
				return func(self.__dict__[arg]) / other
		def mod(self, other):
				return func(self.__dict__[arg]) % other
		def rmod(self, other):
				return other % func(self.__dict__[arg])
		def imod(self, other):
				return func(self.__dict__[arg]) % other
		def pow(self, other):
				return func(self.__dict__[arg]) ** other
		def rpow(self, other):
				return other ** func(self.__dict__[arg])
		def ipow(self, other):
				return func(self.__dict__[arg]) ** other
		def lshift(self, other):
				return func(self.__dict__[arg]) << other
		def rlshift(self, other):
				return other << func(self.__dict__[arg])
		def ilshift(self, other):
				return func(self.__dict__[arg]) << other
		def rshift(self, other):
				return func(self.__dict__[arg]) >> other
		def rrshift(self, other):
				return other >> func(self.__dict__[arg])
		def irshift(self, other):
				return func(self.__dict__[arg]) >> other
		def andf(self, other):
				return func(self.__dict__[arg]) & other
		def rand(self, other):
				return other & func(self.__dict__[arg])
		def iand(self, other):
				return func(self.__dict__[arg]) & other
		def orf(self, other):
				return func(self.__dict__[arg]) | other
		def ror(self, other):
				return other | func(self.__dict__[arg])
		def ior(self, other):
				return func(self.__dict__[arg]) | other
		def xor(self, other):
				return func(self.__dict__[arg]) ^ other
		def rxor(self, other):
				return other ^ func(self.__dict__[arg])
		def ixor(self, other):
				return func(self.__dict__[arg]) ^ other
		def divmod(self, other):
			return divmod(func(self.__dict__[arg]), other)
		def rdivmod(self, other):
			return divmod(func(self.__dict__[arg]), other)
		def eq(self, other):
			return func(self.__dict__[arg]) == other
		def ne(self, other):
			return func(self.__dict__[arg]) != other
		def lt(self, other):
			return func(self.__dict__[arg]) < other
		def le(self, other):
			return func(self.__dict__[arg]) <= other
		def gt(self, other):
			return func(self.__dict__[arg]) > other
		def ge(self, other):
			return func(self.__dict__[arg]) >= other
		def strf(self):
			return str(func(self.__dict__[arg]))
		def reprf(self):
			return "{cls}({v})".format(
				cls=self.__class__, v=func(self.__dict__[arg]))
		def pos(self):
			return +func(self.__dict__[arg])
		def neg(self):
			return -func(self.__dict__[arg])
		def absf(self):
			return abs(func(self.__dict__[arg]))
		def invert(self):
			return ~func(self.__dict__[arg])
		def roundf(self, n=0):
			return round(func(self.__dict__[arg]), n)
		def floorf(self):
			return floor(func(self.__dict__[arg]))
		def ceilf(self):
			return ceil(func(self.__dict__[arg]))
		def truncf(self):
			return trunc(func(self.__dict__[arg]))
		
		
		fs = {add: "__add__", sub: "__sub__", mul: "__mul__",
		div: "__div__", floordiv: "__floordiv__", truediv: "__truediv__",
		mod: "__mod__", pow: "__pow__", lshift: "__lshift__",
		rshift: "__rshift__", andf: "__and__", orf: "__or__",
		xor: "__xor__", eq: "__eq__", ne: "__ne__", lt: "__lt__",
		le: "__le__", gt: "__gt__", ge: "__ge__", strf: "__str__",
		reprf: "__repr__", pos: "__pos__", neg: "__neg__", absf: "__abs__",
		invert: "__invert__", roundf: "__round__", floorf: "__floor__",
		ceilf: "__ceil__", truncf: "__trunc__",}
		
		for f, name in fs.items():
			if not hasattr(cls, name):
				setattr(cls, name, f)
		
		return cls
	return dec


#@number("val")
class Number(object):
	def __init__(self, val, base=10):
		self.val = val
		self.base = base

	

x = Number(3)
print(x)
print(str(x))









