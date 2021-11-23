#!C:\Users\RedKnite\AppData\Local\Programs\Python\Python38\python

# file_ops.py


class File(object):
	def __init__(self, filename=None):
		self.filename = filename
		if self.filename is not None:
			try:
				with open(self.filename, "r") as f:
					self.text = f.read()
			except FileNotFoundError:
				self.text = ""
				with open(self.filename, "x"):
					pass
					
			
		else:
			self.text = ""
	
	def set_filename(self, filename):
		self.filename = filename
	
	def __str__(self):
		return f"file({self.filename})"

	def __add__(self, other):
		return self.text + str(other)
	
	def __iadd__(self, other):
		with open(self.filename, "w") as f:
			f.write(self.text + str(other))
		self.text += str(other)
	
	def clear(self):
		with open(self.filename, "w"):
			pass
	
	def read(self):
		return self.text

	def readlines(self):
		return text.split("\n")
	
	def append(self, string):
		with open(self.filename, "a") as f:
			f.write(string)
		self.text += string
	
	def insert(self, string, index=0):
		pass
	
	


if __name__ == "__main__":
	a = File("text.txt")
	a += "Hello!"
