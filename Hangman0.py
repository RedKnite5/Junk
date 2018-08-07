import mod, sys, random, pickle
#  python Hangman0.py

def start():
	print("Hangman")
	hangman()




	
def hangman():
	global word,know,not_let,trys
	print("".join(know))
	list(know)
	for i in range(len(not_let)):
		print(not_let[i], end=' ')
	print("\n %d trys left" %trys)
	
	draw_man()
	
	if not "_" in know:
		print("You Win!!!")
		sys.exit()
	
	if trys < 1:
		print("You Lose")
		print(word)
		sys.exit()
	
	new_letter = False
	while new_letter == False:
		guess = mod.lower_input()
		if guess in not_let:
			print("You have already used that letter.")
		else:
			new_letter = True
		
		
	if len(guess) > 1:
		if guess in ("exit","quit"):
			quit = mod.lower_input("Was that a guess or do you want to quit?")
			if quit == "guess":
				if guess == word:
					win()
				else:
					print("Wrong")
					trys -= 1
					hangman()
			else:
				sys.exit()
		if guess == word:
			win()
		else:
			print("Wrong")
			trys -= 1
			hangman()
	else:
		if guess in word:
			not_let.append(guess)
			for let,index in zip(word,range(len(word))):
				if guess == let:
					know = list(know)
					know[index] = guess
		
		else:
			not_let.append(guess)
			trys -= 1
	hangman()


def win():
	print("Correct!!!")
	sys.exit()

def draw_man():
	global head,torso,legs
	if trys < 1:
		legs += "_"
	elif trys < 2:
		legs = mod.insert_string(legs,"_",5)
	elif trys < 3:
		legs += " \\"
	elif trys < 4:
		legs += "/"
	elif trys < 5:
		torso += "-"
	elif trys < 6:
		torso = mod.insert_string(torso,"-",6)
		print(torso)
	elif trys < 7:
		torso += "|"
	elif trys < 8:
		head += "0"
	
	print("  _____")
	print("  |    |")
	print(head)
	print(torso)
	print(legs)
	print("__|__")
	
	
"""
  _____
  |    |
  |    0
  |   -|-
  |  _/ \_  
__|__
"""





words = pickle.load(open("list_of_Eng_words.txt","rb"))
word = words[random.randint(0,len(words))-1]
list(word)
know = "_"*len(word)
list(know)
not_let = []
trys = 8
head = "  |    "
torso = "  |   "
legs = "  |  "

start()


"""
  _____
  |    |
  |    0
  |   -|-
  |   / \
__|__
"""