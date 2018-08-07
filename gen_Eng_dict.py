import mod,pickle,enchant,sys
#python gen_Eng_dict.py

store = pickle.load(open("list_of_Eng_words.txt","rb"))
words = store[0]
blacklisted = store[1]

def commands(command):
	if "delete dupe" == command:
		for j,i in enumerate(words):
			if words.count(i) > 1:
				words.pop(j)
				
	elif command.startswith("del "):
		com = command[4:]
		del_word(com)
		
	elif "num words" == command:
		print(len(words))

	elif command.startswith("last "):
		for i in range(int(command[5:]),0,-1):
			print(words[len(words)-i])
			
	elif command.startswith("rep "):
		rep = command[4:]
		arguments = mod.parse(rep," ")
		old = arguments[0]
		new = arguments[1]
		del_word(old)
		blacklisted.append(old)
		print("blacklisted: ", old)
		add_word(new)
		
	elif "check words" == command:
		result = []
		e = enchant.Dict("en_US")
		for i in words:
			if not(e.check(i)):
				result.append(i)
		print(result)
		
	elif "sort list" == command:
		words.sort()
		
	elif "print list" == command:
		print(words)
	
	elif command.startswith("sentence "):
		sen = command[9:]
		begin_len = len(words)
		for i in take_sentence(sen):
			add_word(i)
		print("added words: ",len(words)-begin_len)
		
	elif command.startswith("file "):
		begin_len = len(words)
		file(command[5:])
		print("added words: ", len(words)-begin_len)
	
	elif command.startswith("blacklist "):
		blacklisted.append(command[10:])
		print("blacklisted: ", command[10:])
		
	elif command.startswith("unblacklist "):
		unblacklist(command[12:])
		
	elif command.startswith("ban "):
		del_word(command[4:])
		blacklisted.append(command[4:])
		print("blacklisted: ", command[4:])
	
	
	else:
		print("Error")
		end()
		
def take_sentence(string):
	delete = []
	string = string.lower()
	sen = mod.parse(string)
	for i,word in reversed(list(enumerate(sen))):
		if word[-3:] == "...":
			word = word[:-3]
		if not all(s in mod.lowercase for s in word[1:-1]) or len(word) == 0:
			sen.pop(i)
			continue
		bool_1 = not word[0] in mod.lowercase
		bool_2 = not word[len(word)-1] in mod.lowercase
		if bool_1:
			word = word[1:]
		if bool_2:
			word = word[:-1]
		final = all(r in mod.lowercase for r in word)
		if len(word) > 0 and final:
			sen[i] = word
		
	return(sen)
	
def file(filename):
	file = open(filename,"r")
	for line in file:
		for i in take_sentence(line):
			add_word(i)
	
def del_word(word):
	for i in range(len(words)-1):
		if word == words[i]:
			print("deleted: ", words[i])
			words.pop(i)
			
def unblacklist(word):
	for i in range(len(blacklisted)-1):
		if word == blacklisted[i]:
			print("unblacklisted: ", blacklisted[i])
			blacklisted.pop(i)
				
def add_word(new_word):
	if new_word in words:
		print("duplicate: ", new_word)
	elif new_word in blacklisted:
		print("blacklisted")
	else:
		print("added: ",new_word)
		words.append(new_word)

def end():
	store = [words,blacklisted]
	pickle.dump(store, open("list_of_Eng_words.txt","wb"))
	sys.exit()
	
	
	
for i in range(200):
	store = [words,blacklisted]
	pickle.dump(store, open("list_of_Eng_words.txt","wb"))
	
	new_word = mod.lower_input("word?")

	if True:
		if new_word in ("quit","exit"):
			end()
		elif new_word == "del":
			print("deleted: ", words[len(words)-1])
			words.pop()
		elif new_word == "blacklist":
			print(blacklisted)
		elif " " in new_word:
			commands(new_word)
		else:
			add_word(new_word)


end()