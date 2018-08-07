# python tic_tac_toe.py
import tkinter as tk
from threading import Thread
from pydub import AudioSegment
from pydub.playback import play
import pydub
import sys
import time

width = 3
sq_w = 130

background_music = "No_Strings.mp4"

player = "X"
sound = (AudioSegment.from_file(background_music))

root = tk.Tk()

mess = tk.StringVar()
mess.set(player+"'s turn")

display = tk.Message(root,textvariable=mess,width=50)
display.grid(row=0,column=0)

def quit(abcdef):
	while keep_music:
		time.sleep(1)
		print("live")
keep_music = True

def play_bgm(sound):
	while keep_music:
		play(sound)

#catch = Thread(target=quit,args=[0])
#catch.start()

music = Thread(target=play_bgm,args=[sound],daemon=True)
music.start()


def check():
	for i in range(width):
		lsum = list((x.contain for x in squares[i]))
		if None in lsum:
			pass
		elif "".join(lsum) == "X"*width:
			return(("X","c"+str(i)))
		elif "".join(lsum) == "O"*width:
			return(("O","c"+str(i)))
		else:
			pass

	for i in range(width):
		lsum = list((x[i].contain for x in squares))
		if None in lsum:
			pass
		elif "".join(lsum) == "X"*width:
			return(("X","r"+str(i)))
		elif "".join(lsum) == "O"*width:
			return(("O","r"+str(i)))
		else:
			pass
	
	d1 = list((squares[i][i].contain for i in range(width)))
	if None in d1:
		pass
	elif "".join(d1) == "X"*width:
		return(("X","d1"))
	elif "".join(d1) == "O"*width:
		return(("O","d1"))
	
	d2 = list((squares[width-1-i][i].contain for i in range(width)))
	if None in d2:
		pass
	elif "".join(d2) == "X"*width:
		return(("X","d2"))
	elif "".join(d2) == "O"*width:
		return(("O","d2"))
	
	tie = list((1 for i in range(width) if squares[i][i].contain == None))
	if len(tie) == 0:
		return("Tie")
		
	return(None)

def highlight(line):
	if line[0] == "c":
		for i in squares[int(line[1])]:
			i.light()
	if line[0] == "r":
		for i in squares:
			i[int(line[1])].light()
	if line[0] == "d":
		if line[1] == "1":
			for i in range(width):
				squares[i][i].light()
		if line[1] == "2":
			for i in range(width):
				squares[width-1-i][i].light()


class square(object):
	def __init__(self,loc):
		self.id = loc
		self.contain = None
		self.can = tk.Canvas(root,width=sq_w,height=sq_w)
		self.can.grid(row=self.id[0]+1,column=self.id[1])
		self.can.bind("<Button 1>",self.draw)
		self.can.create_rectangle(0,0,sq_w,sq_w)
	
	def draw(self,event):
		global player, keep_music
		
		if self.contain == None:
			self.can.delete("x1")
			self.can.delete("x2")
			self.can.delete("o")
			
			if player == "X":
				self.can.create_line(5,5,sq_w-5,sq_w-5,tags="x1")
				self.can.create_line(5,sq_w-5,sq_w-5,5,tags="x2")
			if player == "O":
				self.can.create_oval(5,5,sq_w-5,sq_w-5,tags="o")
			
			self.contain = player
			
			if player == "X":
				player = "O"
			elif player == "O":
				player = "X"
			
			mess.set(player+"'s turn")
			
			ans = check()
			if ans == None:
				pass
			else:
				keep_music = False
				print(keep_music)
				if ans == "Tie":
					mess.set("TIE!")
				else:
					mess.set(ans[0]+" wins!!!")
					highlight(ans[1])
	
	def light(self):
		self.can.itemconfig("x1",fill="red")
		self.can.itemconfig("x2",fill="red")
		self.can.itemconfig("o",outline="red")


squares = []
column = []
for i in range(width): # down
	for k in range(width): # across
		column.append(square([k,i]))
	squares.append(column)
	column = []

def clear():
	for i in squares:
		for k in i:
			k.can.delete("x1")
			k.can.delete("x2")
			k.can.delete("o")
			k.contain = None

restart = tk.Button(root,text="Restart",command=clear)
restart.grid(row=width+1,column=0)


root.mainloop()