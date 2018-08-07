import mod, sys, string
# python sandbox.py


class rect(object):
	def __init__(self,width=1,depth=1,height=1):
		self.title = ""
		self.width=width
		self.depth=depth
		self.height=height
	def print_title(self):
		print(self.title)
	def write_title(self,new_title):
		self.title = new_title
	def print_dem(self):
		print(self.width,self.depth,self.height)
	def vol(self):
		return(self.width*self.depth*self.height)

x = rect(2)
x.write_title("title")
x.print_title()
x.print_dem()

class cube(rect):
	def __init__(self,width=1):
		self.side=width
	def print_dem(self):
		print(self.side)
	def vol(self):
		return(self.side**3)
		
y = cube(width=2)
y.write_title("cubey")
y.print_title()
y.print_dem()

print(x.vol(),y.vol())



