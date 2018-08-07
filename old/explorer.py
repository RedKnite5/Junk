import mod,sys,random,pickle,math
from graphics import *
#python explorer.py
	
def room():
	pla = ""
	print("")
	print(str(place[0])+", "+str(place[1])+" Floor: "+str(place[2])) #print location
	room_data = map[place[0]][place[1]][place[2]] #currently unused
	print(room_data)
	if map[place[0]][place[1]][place[2]][0] >= 10 and map[place[0]][place[1]][place[2]][0] <= 19: #10-19 item room
		item_room()
	command()
	
def command():
	print("What would you like to do?")
	print("move")
	print("inventory")
	print("map")
	com = mod.lower_input()
	if com in ("exit","quit"):
		sys.exit()
		
	elif com in ("move"):
		move()
		
	elif com in ("north", "go north", "move north"):
		move("north")
	elif com in ("west", "go west", "move west"):
		move("west")
	elif com in ("east", "go east", "move east"):
		move("east")
	elif com in ("south", "go south", "move south"):
		move("south")
		
	elif com in ("i","inventory"):
		inven()
		command()
		
	elif com in ("map","show map"):
		show_map()
		
	else:
		print("That is not a valid action")
		command()
		
def move(*args):
	if len(args) > 0:
		dir = args[0]
	else:
		dir = mod.lower_input("What direction do you want to go?")
	map[place[0]][place[1]][place[2]][1] = True
	#the below should be improved
	if dir == "north":
		if place[0] == 10:
			print("Edge of map reached")
			command()
		place[0] += 1
	elif dir == "west":
		if place[1] == 0:
			print("Edge of map reached")
			command()
		place[1] -= 1
	elif dir == "east":
		if place[1] == 10:
			print("Edge of map reached")
			command()
		place[1] += 1
	elif dir == "south":
		if place[0] == 0:
			print("Edge of map reached")
			command()
		place[0] -= 1
	else:
		raise RuntimeError("interal wrong direction")
		
	room()
		
		
		
def inven():
	for item,number in inventory.items():
		print(item+": "+str(number))
	item = mod.lower_input("What would you like to use?")
	if item in ("close","exit","quit"):
		return()
	elif item in inventory:
		if inventory[item] > 0:
			use(item)
		else:
			print("You do not have enough")
	else:
		print("You do not have that")
	room()
	
def use(item):
	pass
	#if item 
	
def show_map():
	size = 25
	boarder = 10
	win = GraphWin("Map",2*boarder+map_width*size,2*boarder+map_depth*size) #window size
	
	#the below can probably be improved
	for y in range(map_depth):
		for x in range(map_width): #map grid
			box = Rectangle(Point(size*x+boarder,size*y+boarder),Point(size*x+size+boarder,size*y+size+boarder))
			box.draw(win)
			if map[y][x][place[2]][1]: #places been
				box.setFill("blue")
			if place[0] == y and place[1] == x: #player location
				player = Circle(Point(x*size+boarder+math.floor(size/2),y*size+boarder+math.floor(size/2)),math.floor(size/2))
				player.setFill("black")
				player.draw(win)
				
				
	wait = input("press enter to close map")
	win.close()
	command()
	
def item_room():
	#determine type of room in future
	open_chest = mod.lower_input("There is a chest. Would you like to open it?")
	if open_chest in ("yes","open"):
		rand_gold = random.randint(0,20)
		inventory["gold"] += rand_gold
		print("You got %s gold!" %rand_gold)
		num_chest_items = random.randint(0,3)
	
class equipment(object):
	def __init__(self):
		# type, max health, health, damage, armor
		self.log = {
		"nothing":[0,0,0,0,0],
		"bronze dagger":[0,0,5,0],
		"bronze breastplate":[10,0,0,5]
		}
		#weapon, breastplate, helmet, leggings, boots
		self.equiped = ["nothing","nothing","nothing","nothing","nothing"]
		
		
	def equip(self,ment):
		ment_stats = self.log[ment]
		print(ment_stats)
		for i in range(len(stats)):
			stats[i] += ment_stats[i]
		print(stats)
		self.equiped =
	
	
	
map = []
depth = []
height = []
rooms = []
place = [5,5,0]
inventory = {"gold":0}
stats = [100,100,5,0] # max health, health, damage, armor



map_width = 11
map_depth = 11
map_height = 11


#generate a new map
""" 
new_map = mod.lower_input("Generate a new map? This will take a minute")
if new_map in ("yes","new map","generate a new map","y"):
	for i in range(map_width):
		for k in range(map_depth):
			for h in range(map_height):
				coordinates = str(i) + " " + str(k) + " " + str(h)
				rooms = [random.randint(10,100),False]
				height.append(rooms)
			depth.append(height)
			height = []
		map.append(depth)
		depth = []
	map[math.floor(map_width/2)][math.floor(map_depth/2)][0][0] = 1
	#pickle.dump(map,open("explorer_default_map.txt","wb"))
else:
"""


map = pickle.load(open("explorer_default_map.txt","rb"))
		

room()



