

class Single(object):
	instance = None
	
	def __new__(cls):
		if cls.instance is None:
			obj = super().__new__(cls)
			obj.data = []
			cls.instance = obj
		return cls.instance
	
	def append(self, x):
		self.data.append(x)
	
	def __str__(self):
		return "Single: {}".format(self.data)

s = Single()

s.append(5)

print(s is Single())
print(Single())

