import tkinter as tk
import operator
import pickle
#   python worm_data.py


#root = tk.Tk()

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pop_words = pickle.load(open("pickled_pop_words.txt","rb"))

def gen_words(string):
	delete = []
	sen = string.split()
	for i,word in reversed(list(enumerate(sen))):
		if word[-3:] == "...":
			word = word[:-3]
		if not all(s in letters for s in word[1:-1]) or len(word) == 0:
			sen.pop(i)
			continue
		bool_1 = not word[0] in letters
		bool_2 = not word[len(word)-1] in letters
		if bool_1:
			word = word[1:]
		if bool_2:
			word = word[:-1]
		final = all(r in letters for r in word)
		if len(word) > 0 and final:
			sen[i] = word
		
	return(sen)

file = open("C:\\Users\\Max\Dropbox\\Python\\Worm\\Gestation 1.1 .txt", encoding="utf8")

data = {}
for line in file:
	for word in gen_words(line):
		if word in data:
			data[word] +=1
		else:
			data[word] = 1
			
caps = {}
for i in data:
	if i[0] in upper:
		caps[i] = data[i]

interest = {}		
for i in caps:
	if i.lower() not in pop_words:
		interest[i] = caps[i]
			
disp_data = dict(sorted(interest.items(), key=operator.itemgetter(1), reverse=True)[:])




for word,num in disp_data.items():
	print(word,": ",num)
	
	
	
#root.mainloop()