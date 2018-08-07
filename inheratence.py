#   python stuff.py



class person:
	def __init__(self, name):
		self.name = name
		
	def __repr__(self):
		return(self.name)
	
	
class employee(person):
	__employees = 0
	
	def __init__(self,name):
		type(self).__employees += 1
		super().__init__(name)
		self.employee_number = type(self).__employees
		
	def __repr__(self):
		return(super().__repr__() + ", " + str(self.employee_number))
	
	
	
joe = employee("Joe")
pam = employee("Pam")
jay = employee("Jay")

print(str(jay))
	

	
	
	













