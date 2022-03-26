#!/mnt/c/Users/RedKnite/AppData/Local/Programs/Python/Python38/python.exe
# stuff.py






class DocInt(object):
	def __init__(self, x=0, doc=None):
		if doc is None:
			if isinstance(x, DocInt):
				self.doc = x.doc
			else:
				self.doc = str(x)
		
		self.x = x
	
	def __getattr__(self, attr):
		return getattr(x, attr)
	

	@classmethod
	def ops(cls, op, symbol):
		def func(self, other):
			if isinstance(other, cls):
				op(
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
		




