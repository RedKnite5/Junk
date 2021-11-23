from sys import exit
	
def win():
	print "Congrats, you win!"

def friend():
	print "You go into the secret passage and see someone there."
	print "Do you say \"hi\" or ignore him?"
	print " "
	intro = raw_input()
	if intro == "hi" or intro == "say hi" or intro == "hello":
		making_friends()
	elif intro == "ignore" or intro == "ignore him":
		print "You walk along, unknowingly trip a tripwire, a arrow hits you in the"
		print "temple, and you die."
		exit(0)
	else:
		print "What did you just say!"
		friend()
	
def making_friends():
	print "Hello there, stranger.  Could you perhaps lead me to the outside?"
	print " "
	reply = raw_input()
	if reply == "yes" or reply == "sure" or reply == "I'll try":
		print "Thanks.  My name's James.  We should get going."
		print "You continue along the corridor and you trip a tripwire and James sees the"
		print "arrow and saves you just in time."
		print "You walk out into the sunlight and do stuff."
		win()
		exit(0)
	elif reply == "no":
		print "okay"
		print "You walk along and unknowingly trip a tripwire and a arrow hits you in the"
		print "temple and you die."
		exit(0)
	else:
		print "Do not speak in such riddles. Will you try?"
		making_friends()
		
def minotar_room(item_1, item_2):
	print "You see a massive monster that is half-man, half-bull."
	horn = False
	if item_1 == True and item_2 == True:
		print "The monster sees the yarn and sits excitedly. You throw the yarn and, as the monster"
		print "runs away, you lop off its head."
		horn = True
		print "You take one of its horns as a trophy."
		print "You go back to the fork in the road."
		second_trident()
	else:
		print "The monster charges so fast that you don't have a chance to do anything before it"
		print "kills you."
		exit(0)

def weapons_room():
	item1 = False
	item2 = False
	print "You see a room full of swords, trinkets, and string."
	print "What do you take?"
	print " "
	weapon = raw_input()
	if weapon == "sword" or weapon == "a sword" or weapon == "swords":
		item1 = True
		print "What else?"
		second_weapon(item1, item2)
	elif weapon == "string":
		item2 = True
		print "What else?"
		print " "
		second_weapon(item1, item2)
	else:
		print "What else?"
		second_weapon(item1, item2)

def second_weapon(item_one, item_two):
	weapon_two = raw_input()
	if weapon_two == "string" and item_one == True:
		item_two = True
		minotar_room(item_one, item_two)
	elif weapon_two == "sword" or weapon_two == "a sword" and item_two == True:
		item_one = True
		minotar_room(item_one, item_two)
	else:
		minotar_room(item_one, item_two)
	
def witch():
	print "You see a gingerbread house and you smell something so amazing you literally have no"
	print "choice but to go inside and get eaten."
	exit(0)
	
def trident_in_the_road():
	print "You see two paths: the left one looks pretty safe, the right one looks incredibly dangerous."
	print "What do you choose?"
	print " "
	path = raw_input()
	if path == "left" or path == "go left":
		safe_path()
	elif path == "right" or path == "go right":
		dangerous_path()
	else:
		print "There are two paths.  Is it that hard to choose?"
		trident_in_the_road()
			
def dangerous_path():
	print "You notice a hidden button."
	print "Do you press it or continue?"
	print " "
	button = raw_input()
	if button == "continue":
		weapons_room()
	elif button == "press" or button == "press button" or button == "press the button":
		print "You press the button and go back to find a secret passage."
		James_friend = False
		friend()
	else:
		print "That is not a answer that is in a language I recognize."
		dangerous_path()
		
def safe_path():
	print "You go along until you see a door.  You could also turn left."
	print " "
	restart = raw_input()
	if restart == "door" or restart == "open door" or restart == "open the door":
		print "You go through the door and"
		witch()
	elif restart == "go through the door" or restart == "go through door":
		print "You go through the door and"
		witch()
	elif restart == "left" or restart == "go left":
		print "You turn left and go through a door which slams shut behind you.  No turning back now."
		print "You continue, turn right, and go through a door and..."
		start(0)
	else:
		print "If thou was to cast aside thine life it would be prudent to understand life and death."
		safe_path()
		
def snake():
	print "You see a massive snake which slowly blocks the door and then eats you in the blink of half an eye."
	exit(0)
	
def key_room():
	rusty_key = False
	print "You see a room full of keys, shiny and ornate, with one dull rusty one in the corrner."
	print "Which do you choose, rusty or shiny?"
	print " "
	key = raw_input()
	if key == "shiny" or key == "shiny key" or key == "the shiny key":
		print "As soon as you touch it you are crushed into a key shape and land on one of the shelves."
		exit(0)
	elif key == "rusty" or key == "rusty key" or key == "the rusy key":
		print "You got a rusty key.  You go back to the locked door and use the key."
		trident_in_the_road()
	else:
		print "No."
		key_room()

def first_hall():
	print "You find a fork in the road.  There is a trip wire to the left."
	print " "
	fork = raw_input()
	if fork == "right" or fork == "go right":
		snake()
	elif fork == "left" or fork == "go left":
		print "Do you step over the trip wire or break it?"
		print " "
		trip_wire()
	else:
		print "Do not be careless when you are making possibly life altering or ending"
		print "decisions for you may end up staring into the mouth of a giant snake or worse."
		print "One such torment would be living in hell endlessly staring into the slimy disgusting maw full of fangs"
		print "of a massive man eating snake.  There are many such perils in this infernal"
		print "maze of horrors along with needlessly long and scary comments such as this one."
		print "But back to the original point of, wait let me just see what it was..."
		print "ahh yes instead of writing some nonsense like bananas or %s think about what you" % fork
		print "should articulate.  Instead try left or right.  They should give better results."
		first_hall()
		
def trip_wire():
	break_wire = raw_input()
	if break_wire == "break" or break_wire == "break wire" or break_wire == "break the wire":
		print "You accidentaly trigger it and an axe lops of your head."
		exit(0)
	elif break_wire == "break it":
		print "you accidentaly trigger it and an axe lops of your head."
		exit(0)
	elif break_wire == "over" or break_wire == "step over" or break_wire == "go over":
		print "You carfully step over it."
		key_room()
	elif break_wire == "step over the wire" or break_wire == "go over the wire":
		print "You carfully step over it."
		key_room()
	else:
		print "You said it wrong.  Take more care you could lose you body."
		trip_wire()
	
def start(times):
	locked_door = False
	print " "
	print "You are in a room with two doors:  one on the left and one on the right."
	print " "
	door = raw_input()
	if door == "left" or door == "go left":
		times = times + 1
		if times < 5:
			print "It is locked."
			start(times)
		elif times == 5:
			print "I said it was locked didn't I! Stop trying to open it!"
			start(times)
		else:
			print "This is all I will say until you say \"right\"."
			start(times)
	elif door == "right" or door == "go right":
		first_hall()
	elif door == "i" or door == "inventory":
		print "you have a towel"
		start(times)
	else:
		print "Insert witty thing \"here.\""
		start(times)

def second_trident():
	print "You see two paths; the left one looks pretty safe; the right one looks incredably dargerous."
	print "What do you choose?"
	print " "
	path = raw_input()
	if path == "left" or path == "go left":
		safe_path()
	elif path == "right" or path == "go right":
		second_dangerous_path()
	else:
		print "As you say %r you realize that it makes as mush sense as I do." % path
		print "Try left or right."
		second_trident()
			
def second_dangerous_path():
	print "You notice a hidden button, you press it, and return to the road to discover a secret passage."
	friend()

left = 0

start(left)