#   python simon.py
import tkinter as tk
import random as rand
import time
import pydub

master = tk.Tk()

can = tk.Canvas(master,width=400,height=410)
can.pack()

choices = ("green","red","yellow","blue")

pat = []
ans = None

can.create_arc(0,10,400,410, fill="#A00000", start=0, tags="red")
can.create_arc(0,10,400,410, fill="#00A000", start=90, tags="green")
can.create_arc(0,10,400,410, fill="#A0A000", start=180, tags="yellow")
can.create_arc(0,10,400,410, fill="#0000A0", start=270, tags="blue")

def green():
	can.itemconfig("green",fill="#00FF00")
	master.update()
	time.sleep(.6)
	can.itemconfig("green",fill="#00A000")
	master.update()
	time.sleep(.3)
	
	
def red():
	can.itemconfig("red",fill="#FF0000")
	master.update()
	time.sleep(.6)
	can.itemconfig("red",fill="#A00000")
	master.update()
	time.sleep(.3)
	
def yellow():
	can.itemconfig("yellow",fill="#FFFF00")
	master.update()
	time.sleep(.6)
	can.itemconfig("yellow",fill="#A0A000")
	master.update()
	time.sleep(.3)
	
def blue():
	can.itemconfig("blue",fill="#0000FF")
	master.update()
	time.sleep(.6)
	can.itemconfig("blue",fill="#0000A0")
	master.update()
	time.sleep(.3)
	
def empty(event):
	pass
	
def click(event):
	x,y = event.x, event.y
	new_ans = can.find_overlapping(x-1,y-1,x+1,y+1)
	if len(new_ans) == 1:
		ans = new_ans
	
def get_answer():
	can.bind("<Button>",click)
	
	
	
	
def start():
	global pat
	new = choices[rand.randint(0,3)]
	pat.append(new)
	for i in pat:
		if i == "green":
			green()
		elif i == "red":
			red()
		elif i == "yellow":
			yellow()
		elif i == "blue":
			blue()
			
	get_answer()
	
	start()
	
	

	
	
	
start_b = tk.Button(master, text="Start", command=start)
start_b.pack()

master.mainloop()