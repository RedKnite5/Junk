import tkinter as tk
#   python stuff.py

lowercase = "abcdefghijklmnopqrstuvwxyz"

def take_sentence(string):
	delete = []
	string = string.lower()
	sen = string.split()
	for i,word in reversed(list(enumerate(sen))):
		if word[-3:] == "...":
			word = word[:-3]
		if not all(s in lowercase for s in word[1:-1]) or len(word) == 0:
			sen.pop(i)
			continue
		bool_1 = not word[0] in lowercase
		bool_2 = not word[len(word)-1] in lowercase
		if bool_1:
			word = word[1:]
		if bool_2:
			word = word[:-1]
		final = all(r in lowercase for r in word)
		if len(word) > 0 and final:
			sen[i] = word
		
	return(sen)
	
	
def gen_words(string):
	sen = string.lower().split()
	for i in sen:
		if i[0] not in lowercase:
			pass
	
print(take_sentence("hello! hoW aRE You .hello"))