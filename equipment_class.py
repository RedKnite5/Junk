import mod,sys


class equipment(object):
	def __init__(self):
		self.equip_dict = {
		"copper dagger":["damage",5],
		"leather armor":["damage",10]
		}
		self.equiped = ["copper dagger"]
		
	def equip(self,ment):
		if ment in inventory:
			
		else:
			print("You do not have that equipment.")
			return()
		
	def unequip(self,ment):
		if ment in self.equiped:
			for stat,num in self.equip_dict.items():
				stats[stat] -= num
				for i in self.equiped:
					if i == self.equiped:
						self.equiped.pop(i)
				
				print(stats[stat])
		else:
			print("Item not equiped")
			inven()
			
			
			
			
stats = {"max_health":100,"health":100,"damage":10,"armor":0}




