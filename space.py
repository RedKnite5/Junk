import math, mymod, sys, random, tkinter


class new_world(object):
	def __init__(self):
		self.map = []
		self.new = [250,250,250,0]
		self.map.append(self.new)
		self.num_systems = 20
		self.place = 0
		
		
	def gen_map(self, num_systems):
		coor = []
		for i in range(num_systems):
			coor = [0,0,0,0]
			for z in range(4):
				coor[z-1] = random.randint(0,500)
			coor[3] = random.randint(2,10)
			self.map.append(coor)

class new_player(object):
	def __init__(self):
		hull = {"max health":100, "health":100}
		engine = {"max health":20, "health":20, "ly per ton":1}
		fuel = {"fuel capacity":100, "fuel":100}
		hold = {"capacity":1000}
		ship = [hull, engine, fuel, hold]
		
def actions():
	print("What would you like to do?")
	print("move")
	print("renivate")
	print("display map")
	
	choice = mymod.lower_input()
	if choice == ("exit" or "quit"):
		sys.exit()
	elif choice == ("renivate" or "repair"):
		renivate()
	elif choice == ("map" or "display map"):
		disp_map()
	elif choice == ("move" or "travel"):
		move()
	else:
		print("ERROR")
		sys.exit()
	actions()
		
def move():
	disp_map()
	go = mymod.lower_input("Where do you want to go?")
	if go == ("exit" or "quit"):
		sys.exit()
	place = int(go)
	for x in range(3):
		print(world.map[place][x], end=' ')
	print("")
	actions()
	
	
def renivate():
	pass
	
def disp_map():
	loc = ""
	for x in range(3):
		loc += str(world.map[world.place][x])
		loc += " "
		
	print("You are at %s" %loc)
	print("")
	del loc
	for i in range(len(world.map)):
		text = ""
		text += str(i)
		text += ": "
		for h in range(3):
			text += str(world.map[i][h])
			text += " "
		text += "is: "
		for g in range(20-len(text)):
			text += " "
		text += str(world.map[i][3])
		print(text)
	print("")
	return
			
	
	
	
world = new_world()
player = new_player()



world.gen_map(world.num_systems)
disp_map()
actions()











