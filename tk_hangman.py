#  python tk_hangman.py
import tkinter as tk
import pickle
import random


root = tk.Tk()

info = tk.StringVar()
info.set("")

word_mess = tk.Message(root,textvariable=info,width=350)
word_mess.grid(row=0,column=0)

enter = tk.Entry(root)
enter.grid(row=3,column=0)

drawing = tk.Canvas(root,width=100,height=150)
drawing.grid(row=2,column=0)

trys = 0

drawing.create_line(30,120,70,120)
drawing.create_line(50,120,50,30)
drawing.create_line(50,30,75,30)
drawing.create_line(75,30,75,40)


letters = []
miss = tk.StringVar()
miss.set("Missed letters: " + " ".join(letters))

missed = tk.Message(root,textvariable=miss,width=80)
missed.grid(row=1,column=0)


words = pickle.load(open("list_of_eng_words.txt","rb"))
word = words[0][random.randint(0,len(words[0]))]

info_mess = "_"*len(word)
info.set(info_mess)

def find_indecies(string,sub):
	last = -1
	while True:
		last = string.find(sub,last+1)
		if last == -1:
			break
		yield(last)

def nothing(event):
	pass
		
def win():
	global miss
	miss.set("You Win!!!")
	enter.bind("<Return>",nothing)
	
def lose():
	global miss
	miss.set("You Lose")
	enter.bind("<Return>",nothing)

def collect(event):
	global trys, info_mess, info
	
	entered = enter.get()
	if entered in word:
		for i in find_indecies(word,entered):
			info_mess = info_mess[:i] + entered + info_mess[i+len(entered):]
		info.set(info_mess)
		if "_" not in info_mess:
			win()
	elif entered not in letters:
		letters.append(entered)
		miss.set("Missed letters: " + " ".join(letters))
		trys += 1
		if trys == 1:
			drawing.create_oval(70,40,80,50)
		elif trys == 2:
			drawing.create_line(75,50,75,80)
		elif trys == 3:
			drawing.create_line(75,80,85,100)
		elif trys == 4:
			drawing.create_line(75,80,65,100)
		elif trys == 5:
			drawing.create_line(75,60,70,75)
		elif trys == 6:
			drawing.create_line(75,60,80,75)
			lose()
	
	else:
		pass
	
			



enter.bind("<Return>",collect)

root.mainloop()