from sys import exit
	
def win():
	print "Congrats you win!"

def friend(made_friend):
	
	print "You go into the secret passage and see some one there."
	print "Do you say hi or ignore him?"
	
	intro = raw_input()
	
	if intro == "Hi":
		making_friends(made_friend)
	elif intro == "ignore":
		print "You walk past the person."
	else:
		print "I don't understand."
		
	if made_friend == True:
		print "You continue along the corradoor and you trip a tripwire and James sees the"
		print "arrow and saves you just in time."
	else:
		print "You walk along and unknowingly trip a tripwire and a arrow hits you in the"
		print "temple and you die."
		exit(0)
		
	print "You walk out into the sunlight and do stuff."
	win()
	exit(0)
	
def making_friends(made_friends):
	print "Hello there stranger could you perhaps lead me to the outside?"
	
	reply = raw_input()
	
	if reply == "yes":
		made_friends = True
		print "Thanks, my name's James.  We should get going."
		friend(made_friends)
		print "You continue along the corradoor and you trip a tripwire and James sees the"
		print "arrow and saves you just in time."
	else:
		print "okay"
		print "You walk along and unknowingly trip a tripwire and a arrow hits you in the"
		print "temple and you die."
		exit(0)
		
def minotar_room(item_1, item_2):
	print "You see a massive monster that was half man half bull."
	
	horn = False
	if item_1 == True and item_2 == True:
		print "The monster sees the yarn and sits excitedly you throw the yarn and as the monster"
		print "runs away you lop off its head."
		horn = True
		print "You take one of its horns as a trophy."
		print "You go back to the trident in the road."
		second_trident()
	else:
		print "The monster charges so fast you don't have a chance to do anything before"
		print "kills you."
		exit(0)

def weapons_room():
	item1 = False
	item2 = False

	print "You see a room full of swords trinkets and string."
	print "What do you take?"
	weapon = raw_input()
	if weapon == "sword":
		item1 = True
		print "What else?"
		second_weapon(item1, item2)
	else:
		print "What else?"
		second_weapon(item1, item2)

def second_weapon(item_one, item_two):
	weapon_two = raw_input()
	if weapon_two == "string":
		item_two = True
		minotar_room(item_one, item_two)
	else:
		minotar_room(item_one, item_two)
	
def witch():
	print "you see a ginger bread house and you smell something so amazing you littealy have no"
	print "choice but to go inside and get eaten."
	exit(0)
	
def trident_in_the_road():
		print "You see two paths the left one looks pretty safe the right one looks incredably dargerous."
		print "What do you choose?"
		path = raw_input()
		if path == "left":
			safe_path()
		else:
			dargerous_path()
			
def dargerous_path():
	print "You notice a hidden button."
	print "Do you press it or continue?"
	button = raw_input()
	if button == "continue":
		weapons_room()
	else:
		print "You press the button and go back to find a secret passage."
		James_friend = False
		friend(James_friend)
		
def safe_path():
	print "You go along until you see a door.  You could also turn left."
	restart = raw_input()
	if restart == "door":
		print "You go through the door and"
		witch()
	else:
		print "You turn left and go through a door which slams shut behind you, no turning back now,"
		print "you continue, turn right, and go through a door and"
		start()
		
def snake():
	print "You see a massive snake which slowly blocks the door then quickly eats you."
	exit(0)
	
def key_room():
	rusty_key = False
	print "You see a room full of keys shiny and ornate with one dull rusty one in the corrner."
	print "Which do you choose rusty or shiny?"
	key = raw_input()
	if key == "shiny":
		print "As soon as you touch it you are crushed into a key shape and land on one of the shelves."
		exit(0)
	else:
		print "You got a rusty key.  You go back to the locked door and use the key."
		trident_in_the_road()

def first_hall():
	print "You find a fork in the road there is a trip wire to the left."
	fork = raw_input()
	if fork == "right":
		snake()
	else:
		print "Do you step over the trip wire or break it?"
		trip_wire()
		
def trip_wire():
	break_wire = raw_input()
	if break_wire == "break":
		print "You accidentaly trigger it and an axe lops of your head."
		exit(0)
	else:
		print "You carfully step over it."
		key_room()
	
def start():
	locked_door = False
	print "You are in a room with two doors.  One on the left and one on the right."
	door = raw_input()
	if door == "left":
		print "It is locked."
		start()
	elif door == "right":
		first_hall()
	else:
		print "I do not understand."
		start()

def second_trident():
	print "You see two paths the left one looks pretty safe the right one looks incredably dargerous."
	print "What do you choose?"
	path = raw_input()
	if path == "left":
		safe_path()
	else:
		second_dargerous_path()
			
def second_dargerous_path():
	friends = False
	print "You notice a hidden button you press it and return to the road to discover a secrt passage."
	friend(friends)

start()