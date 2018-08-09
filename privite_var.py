#   stuff.py
# cd C:\Users\Max\Documents\Python\ReCalc
# cd C:\Users\Max\Documents\Python\Junk

import sys
import inspect



class A(object):
	__slots__ = ["__a"]

	def __init__(self):
		self.__a = 7
		
		
	def inc(self):
		self.__a += 1
		return self.__a
		
	def __getattribute__(self, attr):
		if attr in ("__dict__", "_A__a"):
			methods = (self.__init__, self.inc, self.__setattr__)
			method_codes = map(lambda a: a.__code__, methods)
			if sys._getframe(1).f_code in method_codes:
				return object.__getattribute__(self, attr)
			else:
				raise AttributeError(
					"'{}' has no attribute '{}'".format(
						self.__class__.__name__,
						attr))
		else:
			return object.__getattribute__(self, attr)
	
	def __setattr__(self, attr, value):
		if attr in ("__dict__", "_A__a"):
			methods = (self.__init__, self.inc, self.__setattr__)
			method_codes = tuple(map(lambda a: a.__code__, methods))

			if sys._getframe(1).f_code in method_codes:
				object.__setattr__(self, attr, value)
			else:
				raise AttributeError(
					"'{}' has no attribute '{}'".format(
						self.__class__.__name__,
						attr))
		else:
			object.__setattr__(self, attr, value)
	
t = A()

print(t.inc())

print(inspect.getattr_static(t, "_A__a"))

print(object.__getattribute__(t, "_A__a"))





