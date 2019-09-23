import tkinter as tk
from tkinter import font
import random as rand
from PIL import Image
from PIL import ImageTk
from PIL import ImageOps
#    python Crawler1.py

master = tk.Tk()

master.title(string="The Dungeon")  # window name

dun_w = 11   # number of rooms wide         # variable intialization
dun_h = 11
w=300  # width of map screen
h=300
cost_mul = 1

smw = w / dun_w  # width of a room in pixels
smh = h / dun_h
screen = "navigation"

end_font = font.Font(size=40)  # more advanced variable initialization
empty_menu = tk.Menu(master)
output = tk.StringVar()
output.set("Welcome to The Dungeon!")

goblin_image = Image.open("TypicalGoblin_png.png")  # enemy icon stuff
goblin_image = ImageOps.mirror(goblin_image.resize((180, 180)))
gob_tkimage = ImageTk.PhotoImage(goblin_image)

slime_image = Image.open("SlimeMonster_png.png")
slime_image = slime_image.resize((180, 180))
slime_tkimage = ImageTk.PhotoImage(slime_image)

monsters_killed = 0

class room(object):
	"""Class for individuals cells with encounters in them."""
	
	def __init__(self):
		"room creation"
		
		self.visited = False
		self.type = rand.randint(0, 1000)
		self.en = Enemy(self.type)  # enemy generation
		if self.type > 900:
			self.info = "This is a room with a slime monster"
		elif self.type > 100:
			self.info = "This is a room with a goblin"
		elif self.type <= 100:
			self.info = "This is an empty room"

	def enter(self):
		"Set up to enter a room."
		output.set(self.info)
		if self.en.alive == True:
			if self.type > 100:
				clear_screen()
				cbt_scr.grid(row=0, column=0, columnspan=3)
				att_b.grid(row=1, column=0)
				b[4].grid(row=1, column=1)
				run_b.grid(row=1, column=2)
				out.grid(row=2, column=0, columnspan=3)
				entry.grid(row=3, column=0, columnspan=3)
				
				self.en.fight()


class Collectable_Item(object):
	def __init__(self, amount=1):
		self.amount = amount
		self.name = "undefined collectable item"
	
	def __str__(self):
		return self.name
	
	def __add__(self, other):
		if isinstance(other, type(self)):
			return type(self)(self.amount + other.amount)
		else:
			return type(self)(self.amount + other) 

	def __iadd__(self, other):
		if isinstance(other, type(self)):
			self.amount += other.amount
		else:
			self.amount += other
		return self
	
	def __sub__(self, other):
		if isinstance(other, type(self)):
			return type(self)(self.amount - other.amount)
		else:
			return type(self)(self.amount - other) 

	def __isub__(self, other):
		if isinstance(other, type(self)):
			self.amount -= other.amount
		else:
			self.amount -= other
		return self


class Gold(Collectable_Item):
	def __init__(self, amount=0):
		super().__init__(amount)


class Player(object):
	"""Class for the player. Includes stats and actions."""
	
	def __init__(self):
		"setting stats and variables"
		
		self.loc = [int((dun_w - 1) / 2), int((dun_h - 1) / 2)]
		self.max_health = 100
		self.health = self.max_health
		self.damage = 10
		self.defence = 0
		self.inven = {"gold": Gold()}
		self.equipment = {}
		
	def move(self,dir):
		"player movement on map function"
		
		dun[self.loc[0]][self.loc[1]].visited = True
		disp.itemconfig(str(self.loc[0]) + "," + str(self.loc[1]), fill="yellow")
		if dir == "north" and self.loc[1] > 0:   # up
			self.loc[1] -= 1
			disp.move("player", 0, -1 * smh)
		elif dir == "south" and self.loc[1] < dun_h-1:  # down
			self.loc[1] += 1
			disp.move("player", 0, smh)
		elif dir == "west" and self.loc[0] > 0:  # left
			self.loc[0] -= 1
			disp.move("player", -1 * smw, 0)
		elif dir == "east" and self.loc[0] < dun_w-1:  # right
			self.loc[0] += 1
			disp.move("player", smw, 0)
		dun[self.loc[0]][self.loc[1]].enter()
			
	def disp_in(self):  # inventory display
		hold = ""
		for key, val in self.inven.items():
			hold += str(key).title() + ": " + str(val.amount) + "\n"
		output.set(hold)

p = Player()  # player creation


class Enemy(object):
	def __init__(self): #   create enemy
		self.alive = True
		self.en_max_health = 1
		self.en_health = self.en_max_health  # won't work for inheritance, must be done agian
		self.en_damage = 1
		self.loot = loot_gen(self)
		self.image = None
			
	def fight(self):
		global screen
		
		screen = "fight"
		cbt_scr.create_rectangle(w + 90, 10, w - 10, 30) # enemy health bar
		
		cbt_scr.create_rectangle(
			w + 90, 10, w + 90 - (100 * self.en_health / self.en_max_health), 30, # enemy health
			fill="red", tags="en_bar")
		
		cbt_scr.create_rectangle(10, h - 30, 10 + p.max_health, h - 10) # player healthbar
		cbt_scr.create_rectangle(
			10, h - 30, 10 + (100 * p.health / p.max_health), h - 10,
			fill="green", tags="fight_health_bar")
		
		cbt_scr.create_image(210, 40, image=gob_tkimage, anchor="nw")   # enemy icon
	
	def en_attack(self):  # attack the player
		damage_delt = 0
		if p.health <= 0:
			lose()
		if self.en_damage - p.defence > 0:
			damage_delt = self.en_damage - p.defence
		p.health -= damage_delt
		update_health_bar()
		output.set("The enemy did " + str(damage_delt) + " damage!")
		
	def be_attacked(self):  # the player attacks
		self.en_health -= p.damage
		if self.en_health <= 0:
			self.die()
		cbt_scr.coords("en_bar", w + 90, 10, w + 90 - (100 * self.en_health / self.en_max_health), 30)
		if self.alive == True:
			self.en_attack()
		
	def die(self):
		global monsters_killed
		
		self.alive = False
		monsters_killed += 1
		hold = "You got: \n"
		for key, val in self.loot.items():  # display loot
			hold += str(key).title() + ": " + str(val.amount) + "\n"
		output.set(hold)
		
		disp.delete("enemy" + str(p.loc[0]) + "," + str(p.loc[1]))
		cur_room().info = "This is an empty room."
		
		for i in self.loot:  # take loot
			if i in p.inven:
				p.inven[i] += self.loot[i]
			else:
				p.inven[i] = self.loot[i]
				
		navigation_mode()


class Goblin(Enemy):
	def __init__(self, diff): #   create enemy
		if diff > -10 and diff < 200:
			self.alive = True
			self.en_max_health = rand.randint(30, 40) + monsters_killed
			self.en_health = self.en_max_health
			self.en_damage = rand.randint(3, 8) + monsters_killed // 3
			self.loot = loot_gen()
			
	def fight(self):
		global screen
		screen = "fight"
		cbt_scr.create_rectangle(w + 90, 10, w - 10, 30) # enemy health bar
		
		cbt_scr.create_rectangle(
			w + 90, 10, w + 90 - (100 * self.en_health / self.en_max_health), 30, # enemy health
			fill="red", tags="en_bar")
		
		cbt_scr.create_rectangle(10, h - 30, 10 + p.max_health, h - 10) # player healthbar
		cbt_scr.create_rectangle(
			10, h - 30, 10 + (100 * p.health / p.max_health), h - 10,
			fill="green", tags="fight_health_bar")
		
		cbt_scr.create_image(210, 40, image=gob_tkimage, anchor="nw")   # enemy icon
	
	def en_attack(self):  # attack the player
		damage_delt = 0
		if p.health <= 0:
			lose()
		if self.en_damage - p.defence > 0:
			damage_delt = self.en_damage - p.defence
		p.health -= damage_delt
		update_health_bar()
		output.set("The enemy did " + str(damage_delt) + " damage!")
		
	def be_attacked(self):  # the player attacks
		self.en_health -= p.damage
		if self.en_health <= 0:
			self.die()
		cbt_scr.coords("en_bar", w + 90, 10, w + 90 - (100 * self.en_health / self.en_max_health), 30)
		if self.alive == True:
			self.en_attack()
		
	def die(self):
		global monsters_killed
		
		self.alive = False
		monsters_killed += 1
		hold = "You got: \n"
		for key, val in self.loot.items():  # display loot
			hold += str(key).title() + ": " + str(val.amount) + "\n"
		output.set(hold)
		
		disp.delete("enemy" + str(p.loc[0]) + "," + str(p.loc[1]))
		cur_room().info = "This is an empty room."
		
		for i in self.loot:  # take loot
			if i in p.inven:
				p.inven[i] += self.loot[i]
			else:
				p.inven[i] = self.loot[i]
				
		navigation_mode()



class Usable_Item(Collectable_Item):
	def __init__(self):
		super().__init__()
		self.name = "undefined usable item"
	
	def use(self):
		output.set("Used " + self.name.title())
		p.inven[self.name] -= 1


class Equipable_Item(Collectable_Item):
	def __init__(self):
		super().__init__()
		self.name = "undefined equipable item"
		self.space = ""
	
	def equip(self):
		p.equipment[self.name] = equipment[self.name]
	
	def unequip(self):
		p.equipment.pop(self.name, None)
		

class Buyable_Item(Collectable_Item):  # items for shop
	def __init__(self):
		super().__init__()
		self.cost = 0
		self.name = "undefined_buyable_item"

	def __str__(self):
		return self.name
		
	def effect(self):
		pass


class Health_Pot(Usable_Item):
	def __init__(self):
		super().__init__()
		self.name = "health potion"
	
	def use(self):
		super().use()
		p.health += 50
		if p.health > p.max_health:
			p.health = p.max_health
		
		update_health_bar()


class Sword(Buyable_Item, Equipable_Item):  # sword in shop
	def __init__(self):
		super().__init__()
		self.name = "sword"
		self.cost = 50 * cost_mul
		
	def equip(self):
		super().__init__()
		p.damage += 10
	
	def unequip(self):
		super().__init__()
		p.damage -= 10


class Armor(Buyable_Item, Equipable_Item):
	def __init__(self):
		super().__init__()
		self.name = "armor"
		self.cost = 100 * cost_mul

	def equip(self):
		super().__init__()
		p.defence += 10
	
	def unequip(self):
		super().__init__()
		p.defence -= 10


def move_north(): p.move("north")  #  button functions
def move_south(): p.move("south")
def move_west(): p.move("west")
def move_east(): p.move("east")

def up_key(event):  # key binding functions
	if screen == "navigation":
		p.move("north")
def down_key(event):
	if screen == "navigation":
		p.move("south")
def right_key(event):
	if screen == "navigation":
		p.move("east")
def left_key(event):
	if screen == "navigation":
		p.move("west")
		
def enter_key(event):   # other key binding functions
	item = entry.get().lower()
	if item in p.inven:
		if p.inven[item].amount > 0:
			if isinstance(p.inven[item], Usable_Item):
				p.inven[item].use()
			elif item in equipment:
				p.inven[item].equip()
				output.set("You equip the " + item)
			else:
				output.set("That item is not usable")
		else:
			output.set("You do not have any of that")
	else:
		output.set("You do not have any of that")


def update_health_bar():
	cbt_scr.coords("fight_health_bar",
	10, h - 30, 10 + (100 * p.health / p.max_health), h - 10)
	healthbar.coords(
	"navigation_healthbar", 10, 10, 10 + (100 * p.health / p.max_health), 30)


def buy_item_fact(item_name, amount=1, *args):
	def buy_specific_item():
		for i in range(amount):
			item = buyable_items[item_name](*args)
			
			if p.inven["gold"].amount >= item.cost:
				if item_name in p.inven:
					p.inven[item_name].amount += 1
				else:
					p.inven[item_name] = item
				item.effect()    #   passive effect from having it
				output.set("You bought a " + item_name)
				p.inven["gold"] -= item.cost
			else:
				output.set("You do not have enough Gold for that")
	return buy_specific_item


buyable_items = {
	"sword": Sword,
	"armor": Armor
}

equipment = {
	"sword": "1 hand",
	"armor": "body",
}

def cur_room():
	room = dun[p.loc[0]][p.loc[1]]
	return(room)
	
def clear_screen():  # remove all widgets
	for i in navigation_widgets + fight_widgets + other_widgets:
		i.grid_remove()
	master.config(menu=empty_menu)

def attack():
	cur_room().en.be_attacked()
	
def flee():  # leave a fight
	chance = rand.randint(0, 100)
	if chance > 50:
		navigation_mode()
		disp.create_oval(smw * p.loc[0] + smw / 4, smh * p.loc[1] + smh / 4, # known enemy icon creation
		smw * p.loc[0] + smw * 3/4, smh * p.loc[1] + smh * 3/4,
		fill="red", tags="enemy" + str(p.loc[0]) + "," + str(p.loc[1]))
		cur_room().info = "A room with an enemy in it."
		output.set("You got away.")
	else:
		cur_room().en.en_attack()
		output.set("You couldn't get away.")

def navigation_mode():  # switch to navigation screen
	global screen
	cbt_scr.delete("all")
	for i in fight_widgets:
		i.grid_remove()
	for i in navigation_widgets:
		i.grid()
	out.grid(row=5, column=0, columnspan=4)
	b[4].grid(row=1, column=0)
	entry.grid(row=6, column=1, columnspan=2)
	master.config(menu=shop)
	screen = "navigation"
	healthbar.coords("navigation_healthbar", 10, 10, 10 + (100 * p.health / p.max_health), 30)
	
def room_info(event):  # give information on rooms by clicking on them
	x, y = event.x, event.y
	subjects = disp.find_overlapping(x - 1, y - 1, x + 1, y + 1)
	sub = []
	for i in subjects:
		if disp.type(i) == "rectangle":
			sub.append(i)
	if len(sub) == 1:
		tag = disp.gettags(sub[0])[0].split(",")
		clicked_room = dun[int(tag[0])][int(tag[1])]
		
		if int(tag[0]) == p.loc[0] and int(tag[1]) == p.loc[1]:
			output.set("This is your current location.")
		elif clicked_room.visited == True:
			output.set(clicked_room.info)
		else:
			output.set("Unknown")
			
def lose():
	screen = "game over"
	clear_screen()
	game_over = tk.Canvas(master, width=w + 100, height=h)
	game_over.create_rectangle(0, 0, w + 100, h + 50, fill="black")
	game_over.create_text(w/2 + 50, h/2, text="GAME OVER", fill="green", font=end_font)
	game_over.grid(row=0,column=0)
	
def loot_gen():
	loot = {}
	loot["gold"] = Gold(rand.randint(10, 20) + monsters_killed // 2)
	if rand.randint(0, 2) == 0:
		loot["health potion"] = Health_Pot()
		
	return loot



dun = []
for i in range(dun_w): # map generation
	column = []
	for k in range(dun_h):
		column.append(room())
	dun.append(column)
dun[int((dun_w - 1) / 2)][int((dun_h - 1) / 2)].type = 0
dun[int((dun_w - 1) / 2)][int((dun_h - 1) / 2)].info = \
	"This is the starting room. There is nothing of significance here."
	


b = [tk.Button(master) for i in range(5)] # button creation
for i, k in enumerate(b):
	k.configure(text="b" + str(i))
	
b[0].configure(text="North", command=move_north) # button configuation
b[3].configure(text="South", command=move_south)
b[1].configure(text="West", command=move_west)
b[2].configure(text="East", command=move_east)

b[4].configure(text="Inventory", command=p.disp_in) # more button configuration

b[0].grid(row=2, column=1) # button placement
b[1].grid(row=3, column=0)
b[2].grid(row=3, column=2)
b[3].grid(row=4, column=1)
b[4].grid(row=1, column=0)


disp = tk.Canvas(master, width=w, height=h)  # canvas creation
disp.grid(row=0, column=3, rowspan=5)

for i in range(dun_w):  #  display creation
	for k in range(dun_h):
		disp.create_rectangle(smw * i, smh * k, smw * i + smw, smh * k + smh,
		fill="grey", tags=str(i) + "," + str(k))
		
disp.create_oval(smw * p.loc[0] ,smh * p.loc[1], # player icon creation
smw * p.loc[0] + smw, smh * p.loc[1] +smh,
fill = "green", tags = "player")


healthbar = tk.Canvas(master, width=p.max_health + 10, height=30) # health bar creation
healthbar.grid(row=0, column=0, columnspan=3)

healthbar.create_rectangle(10, 10, 10 + p.max_health, 30)  # health bar drawing
healthbar.create_rectangle(10, 10, 10 + (100 * p.health / p.max_health), 30,
fill="green", tags="navigation_healthbar")


out = tk.Message(master, textvariable=output, width=w + 100)  # output text creation
out.grid(row=5, column=0, columnspan=4)

entry = tk.Entry(master)
entry.grid(row=6, column=1, columnspan=2)

shop = tk.Menu(master) # top level shop menu
stock = tk.Menu(shop, tearoff=0) # drop down menu
for i in buyable_items:
	stock.add_command(   # actual things you can buy
		label=i.title() + " " + str(buyable_items[i]().cost),
		command=buy_item_fact(i))

shop.add_cascade(menu=stock, label="Shop")
master.config(menu=shop) # add menu to screen


#     fight screen
cbt_scr = tk.Canvas(master, width=w + 100, height=h)

att_b = tk.Button(master, text="Attack", command=attack)
run_b = tk.Button(master, text="Flee", command=flee)

fight_widgets = [cbt_scr, att_b, run_b]
navigation_widgets = b[:-1] + [disp, healthbar, out]
other_widgets = [b[4], entry]


master.bind("<Up>", up_key)  # key bindings
master.bind("<Down>", down_key)
master.bind("<Right>", right_key)
master.bind("<Left>", left_key)
master.bind("<Return>", enter_key)
disp.bind("<Button 1>", room_info)


master.mainloop()