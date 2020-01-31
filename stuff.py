#!C:\Users\RedKnite\AppData\Local\Programs\Python\Python38\python

# stuff.py

import multipart_init as mpi



class To_Split(object):
	
	splitter = mpi.Split_Init()
	
	@splitter.init
	def __init__(self):
		print("fail")
	
	@splitter.part(0)
	def init1(self):
		print("part 1")
	
	@splitter.part(1)
	def init2(self):
		print("part 2")
	
	@splitter.part(2)
	def init_part3(self):
		print("end")


class To_Split(object):
	def __init__(self):
		
		self.init1()
		self.init2()
		self.init_part3()
	
	def init1(self):
		print("part 1")
	
	def init2(self):
		print("part 2")
	
	def init_part3(self):
		print("end")



class Weird(To_Split):
	def __init__(self):
		super().__init__(0)
		print("middle")
		super().__init__(1)
		super().__init__(2)



w = Weird()


di = {"x": 5, "var": "hi"}
def fun(d):
	#for key, val in d.items():
	#	exec(f"{key}={repr(val)}")
	exec("x=6", {}, locals())
	print("x: ", x)



fun(di)


#for key, val in di.items():
#	exec(f"{key}={repr(val)}")

#print("glo x: ", x)


























def func():
	ns.x = 6

def foo():
	print(ns.x)








