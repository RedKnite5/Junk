import mymod, sys, math, itertools, re, random

def start():
	hangman()




	
def hangman():
	global word,know,not_let,trys
	print know
	for i in xrange(len(not_let)):
		print not_let[i],
	print "\n %d trys left" %trys
	guess = mymod.lower_input()
	if len(guess) > 1:
		if guess in ("exit","quit"):
			quit = mymod.lower_input("Was that a guess or do you want to quit?")
			if quit == "guess":
				if guess == word:
					win()
				else:
					print "Wrong"
					trys -= 1
					hangman()
			else:
				sys.exit()
		if guess == word:
			win()
		else:
			print "Wrong"
			trys -= 1
			hangman()
	else:
		if guess in word:
			 for let,index in zip(word,xrange(len(word)-1)):
				if guess == let:
					know[index] = guess
	hangman()


def win():
	print "Correct!!!"
	sys.exit()







words = ["friend","jungle"]
word = words[random.randint(0,len(words))-1]
know = "_"*len(word)
list(know)
not_let = []
trys = 10

start()

