

# multipart_init.py

import types

class Split_Func(object):

	def __init__(self1):
		self1.parts_dyn = {}
		self1.parts = ()
		
		def func_manager(*args,
			start=None, stop=None, step=None, index=None,
			**kwargs):
			
			to_run = (self1.parts[slice(start, stop, step)] if
				index is None else (self1.parts[index],))

			for func in to_run:
				func(*args, **kwargs)
		
		self1.func_manager_l = (func_manager,)

	def part(self, num):
		if num in self.parts_dyn:
			raise ValueError(f"part {num} is already accounted for")
		
		def descriptor(func):
			self.parts_dyn[num] = func
			rev_dict = {v: k for k, v in self.parts_dyn.items()}
			self.parts = sorted(
				self.parts_dyn.values(),
				key=lambda v: rev_dict[v])
			return func
		
		return descriptor
	
	
	def __call__(self, func):
		'''The decorator that defines the how the function will be called'''
		
		return self.func_manager_l[0]



if __name__ == "__main__":

	class To_Split(object):
		
		splitter = Split_Func()
		
		@splitter
		def __init__():
			pass
		
		@splitter.part(0)
		def init1(self):
			print("part 1")
		
		@splitter.part(1)
		def init2(self):
			print("part 2")
		
		@splitter.part(2)
		def init_part3(self):
			print("end")




	class Weird(To_Split):
		def __init__(self):
			super().__init__(index=0)
			print("middle")
			super().__init__(index=2)



	func_splitter = Split_Func()
	
	@func_splitter
	def func1():
		pass
	
	@func_splitter.part(0)
	def funcp1(var, string):
		print(1, " ", var, string)
	
	@func_splitter.part(1)
	def funcp2(var, string):
		print(2, " ", var)
	
	func1(9, "yo")
	
	w = Weird()












