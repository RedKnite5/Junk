#!C:\Users\RedKnite\AppData\Local\Programs\Python\Python38\python

# stuff.py



class A(object):	
	def __new__(cls, x=0):
		obj = super().__new__(cls)
		obj._x = x
		return obj
	
	@property
	def x(self):
		return self._x

a = A()
#a.x = 3

print(a.x)

