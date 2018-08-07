import random
#   python stuff.py


class Fib:                                        
    def __init__(self, max):                      
        self.max = max

    def __iter__(self):                          
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        #if fib > self.max:
	#   raise StopIteration                  
        self.a, self.b = self.b, self.a + self.b
        return fib

class count:
	def __init__(self, start=0, max=10, step=1, stop=True):
		self.max = max
		self.start = start
		self.step = step
	
	def __iter__(self):
		self.num = self.start
		return(self)
		
	def __next__(self):
		if self.num > self.max and stop:
			raise StopIteration
		self.num += self.step
		return(self.num-self.step)
		
class rational:
	def __init__(self, max=10):
		self.max = max
		self.dir = "up"
	
	def __iter__(self):
		self.a = 0
		self.b = 1
		return(self)
		
	def __next__(self):
		ans = self.a / self.b
		
		if self.a == self.max:
			raise StopIteration
		
		if self.a == 1 and self.dir == "down":
			self.b += 1
			self.dir = "up"
		elif self.b == 1 and self.dir == "up":
			self.a += 1
			self.dir = "down"
		else:
			if self.dir == "down":
				self.a -= 1
				self.b += 1
			if self.dir == "up":
				self.a += 1
				self.b -= 1
				
		return(self.a/self.b)

for i in Fib(10):
	print(i)







			
		
		