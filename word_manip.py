import mod, sys, random, pickle
#python word_manip.py

def start():
	words = pickle.load(open("list_of_Eng_words.txt","rb"))
	blacklisted = []
	dict = [words,blacklisted]
	pickle.dump(dict, open("list_of_Eng_words.txt","wb"))
	


def rand_words(num):
	ans = []
	for i in range(num):
		ans.append(mod.words[random.randint(0,len(mod.words)-1)])
	return ans

def length_words():
	print(len(mod.words))
	
def num_letters():
	lengths = {}
	for i in mod.words:
		try:
			lengths[len(i)] += 1
		except:
			lengths[len(i)] = 1
	for key, val in lengths.items():
		print(key, val)
		
def total_letters():
	total = 0
	for i in mod.words:
		total += len(i)
	print(total)
	
def start_with(start):
	ans = []
	for i in mod.words:
		if mod.str_start(start,i):
			ans.append(i)
	return ans

def del_dupe():
	words = pickle.load(open("list_of_Eng_words.txt","rb"))
	
	for j,i in enumerate(mod.words):
		if mod.count(i) > 1:
			mod.words.pop(j)
	
	pickle.dump(words, open("list_of_Eng_words.txt","wb"))

start()
