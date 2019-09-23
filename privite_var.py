#   privite_var.py


from pprint import pprint
import inspect


'''
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
	
'''


class PriviteDict(dict):
	import inspect
	
	def __setitem__(self, key, value):
		frame = inspect.currentframe()
		info = inspect.getouterframes(frame)
		for i in info:
			print("")
			#pprint(inspect.getframeinfo(i))
			pprint(inspect.getmembers(i))
		
		super().__setitem__(key, value)
	
	def __getitem__(self, key):
		super().__getitem__(key)
		

class PriviteNamespace(type):
	
	def __prepare__(self, name, *bases):
		return PriviteDict()


class Secret(object, metaclass=PriviteNamespace):
	def __init__(self):
		self.__num = 231
		self.pub_num = 10

s = Secret()
