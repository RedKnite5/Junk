#!/mnt/c/Users/RedKnite/AppData/Local/Programs/Python/Python38/python.exe
# stuff.py



class MyDict(dict):
	def __getitem__(self, attr):
		print(f"Getting {attr!r}")
		return super().__getitem__(attr)
	
	def __setitem__(self, attr, val):
		print(f"Setting {attr!r} to {val!r}")
		super().__setitem__(attr, val)
	
	def __repr__(self):
		return f"MyDict({super().__repr__()})"


class Meta(type):
	@classmethod
	def __prepare__(cls, name, bases, **kwds):
		print(f"{name = !r}\n{bases = !r}\n{kwds = !r}")
		
		return MyDict()
	
	def __new__(cls, name, bases, ns):
		print(f"{ns = }")
		
		obj = super().__new__(cls, name, bases, ns)
		
		#obj.__dict__["hi"] = "test"
		#setattr(obj, "__dict__", ns)
		return obj


class Base(metaclass=Meta):
	def __init__(self):
		self.x = 5
	

print(MyDict())

a = Base()


print(Base.__dict__)

print(getattr(a, "x"))

