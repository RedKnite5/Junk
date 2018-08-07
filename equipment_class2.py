import mod,sys
# python equipment_class2.py

class equipment(object):
	def __init__(self):
		# [damage, max health, defence]
		self.log = {
		"nothing":[0,0,0],
		"bronze dagger":[5,0,0]
		}
		#weapon, breastplate, helmet, leggings, boots
		self.equiped = ["nothing","nothing","nothing","nothing","nothing"]
		
		
	
	def equip(self,ment):
		ment_stats = self.log[ment]
		print(ment_stats)
		for i in range(len(stats)):
			stats[i] += ment_stats[i]
		print(stats)
		
		
my_equipment = equipment()
stats = [5,100,0]

my_equipment.equip("bronze dagger")