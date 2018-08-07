#   python magic_methods.py
import datetime



class person(object):
	__total_people = 0
	
	
	def __init__(self, name = None, birthday = datetime.date.today()):
		type(self).__total_people += 1
		self.birthday = birthday
		if name is not None:
			self.name = name
		
	def __getattr__(self, attr, default = None):
		try:
			return(eval("self."+attr))
		except:
			return(default)
			
	def __repr__(self):
		string = getattr(self, "name")
		if string is not None:
			return(string)
		else:
			return("person")
			
	def get_birthday(self):
		return(getattr(self, "birthday"))
		
	def set_name(self, name):
		self.name = name
		
	def get_name(self):
		return(getattr(self, "name"))
		
	def get_first_name(self):
		self.name_list = self.name.split(" ")
		return(self.name_list[0])
	
	@staticmethod
	def get_total_people():
		return(person.__total_people)



me = person("Max Friedman")

print(me)

















