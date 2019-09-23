# class_dec.py


def implement_common_functionality(cls_outer=None, *, attr=None, override=False):
	'''
	Decorator factory. This should be given an attribute to rederect all the
	dunder methods to. Override should be true if existing methods should be
	overwritten with new dunder methods.
	'''

	def dec(cls):
		'''
		A decorator for a class that creates dunder methods to classes.
		'''
	
		import copy
		import operator as op
		
		if attr:

			def _add_method(func, name, inplace=False, direct_return=False, meth_override=False):
				'''
				Bind a method to the class.
				'''
				
				n = name or func.__name__
				if override or meth_override or not hasattr(cls, n):
					def method(self, *args, **kwargs):
						'''
						Dunder method
						'''
						
						if not direct_return:
							cself = copy.deepcopy(self) if not inplace else self
							setattr(cself, attr, func(getattr(cself, attr), *args, **kwargs))
							if not inplace:
								return cself
						else:
							return func(getattr(self, attr), *args, **kwargs)
							
					setattr(cls, n, method)
					
			def _norm_r_i(op_name):
				'''
				Create and bind three methods. A normal one, a reflected one,
				and an inplace one.
				'''
				
				_add_method(getattr(op, op_name), f"__{op_name.strip('_')}__")
				_add_method(
					lambda *args, **kwargs:
						getattr(op, op_name)(*args, **kwargs),
						f"__r{op_name.strip('_')}__")
				_add_method(getattr(op, op_name), f"__i{op_name.strip('_')}__", True)
			
			_norm_r_i("add")
			_norm_r_i("sub")
			_norm_r_i("mul")
			_norm_r_i("truediv")
			_norm_r_i("floordiv")
			_norm_r_i("mod")
			_norm_r_i("pow")
			_norm_r_i("lshift")
			_norm_r_i("rshift")
			_norm_r_i("and_")
			_norm_r_i("xor")
			_norm_r_i("or_")
			_norm_r_i("neg")
			_norm_r_i("pos")
			_norm_r_i("abs")
			_norm_r_i("invert")
			
			_add_method(lambda a, b: a < b, "__lt__", False, True, True)
			_add_method(lambda a, b: a <= b, "__le__", False, True, True)
			_add_method(lambda a, b: a > b, "__gt__", False, True, True)
			_add_method(lambda a, b: a >= b, "__ge__", False, True, True)

			# I'm not sure what exactly should be returned by these methods.
			# should the values in the tuple be instances of the class? IDK
			#_add_method(lambda a, b: divmod(a, b), "__divmod__")
			#_add_method(lambda a, b: divmod(b, a), "__rdivmod__")
			


		
		return cls
	
	if cls_outer:
		return dec(cls_outer)
	return dec

@implement_common_functionality(attr="x") 
class A(object):
	def __init__(self, x=0):
		self.x = x

a = A(4)

print(a.__dict__)
print(a > 4)
