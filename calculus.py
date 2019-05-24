# calculus.py


def make_int(i):
	if i.is_integer():
		return int(i)
	else:
		return i


class vector(object):
	def __init__(self, i=0, j=0, k=0):
		self.i = i
		self.j = j
		self.k = k
	
	def __repr__(self):
		return f"vector{self.i, self.j, self.k}"
	
	def __str__(self):
		return f"{self.i}i + {self.j}j + {self.k}k"
		
	def __mul__(self, s):
		if not isinstance(s, vector):
			self.i *= s
			self.j *= s
			self.k *= s
			return self
		else:
			raise ValueError("Can not scale vectors by other vectors")
	
	def __rmul__(self, s):
		if not isinstance(s, vector):
			self.i *= s
			self.j *= s
			self.k *= s
			return self
		else:
			raise TypeError("Can not scale vectors by other vectors")
	
	def __truediv__(self, s):
		if not isinstance(s, vector):
			self.i = make_int(self.i / s)
			self.j = make_int(self.j / s)
			self.k = make_int(self.k / s)
		else:
			raise TypeError("Can not divide vectors")
	
	def __add__(self, v):
		if isinstance(v, vector):
			return vector(self.i + v.i, self.j + v.j, self.k + v.k)
		else:
			raise TypeError(f"Can not add type: {type(v)} to vectors")
	
	def __sub__(self, v):
		if isinstance(v, vector):
			return vector(self.i - v.i, self.j - v.j, self.k - v.k)
		else:
			raise TypeError(f"Can not subtract type: {type(v)} to vectors")
	
	def magnitude(self):
		return (self.i * self.i + self.j * self.j + self.k * self.k) ** .5
	
	def unitize(self):
		self /= self.magnitude()
	
	def dot(self, v):
		if isinstance(v, vector):
			return self.i * v.i + self.j * v.j + self.k * v.k
		else:
			raise TypeError(f"Can no dot {type(v)}")
	
	def cross(self, v):
		if isinstance(v, vector):
			return vector(
				self.j * v.k - self.k * v.j,
				self.k * v.i - self.i * v.k,
				self.i * v.j - self.j * v.i)
		else:
			raise TypeError(f"Can no cross {type(v)}")




v = vector(1, 0, 0)
u = vector(0, 1, 0)
print(u.cross(v))










