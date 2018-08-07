import math, mymod, sys, random, Tkinter


class world(object):
	def __init__(self):
		self.map = {250+250j: "oragin"}
		self.num_systems = 20
		self.sys_coor = []
		
	def gen_map(self, num_systems, sys_coor):
		for i in range(num_systems):
			x = random.randint(0,500)+random.randint(0,500) * 1j
			if not(x in self.map):
				self.map[eval(x)]=random.randint(2,10)
			else:
				del x

class player(object):
	def __init__(self):
		hull = {"max health":100, "health":100}
		engine = {"max health":20, "health":20, "ly per ton":1}
		fuel = {"fuel capacity":100, "fuel":100}
		hold = {"capacity":1000}
		ship = [hull, engine, fuel, hold]
		
def actions():
	choice = mymod.lower_input("What would you like to do?")
	if choice == "move" or "travel":
		move()
	elif choice == "renivate" or "repair":
		renivate()
	elif choice == "map":
		disp_map()
		
def move():
	pass
	
def renivate():
	pass
	
def disp_map():
	pass
	
	
	
iniworld = world()
start = player()



iniworld.gen_map(iniworld.num_systems, iniworld.sys_coor)
print iniworld.map
actions()











