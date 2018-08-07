import tkinter as tk
import random as rand
import mod
#   python tk_grid.py 

master = tk.Tk()

dun_w = 11
dun_h = 11
w=300
h=200
smh = h/dun_h
smw = w/dun_w


class room():
	def __init__(self):
		self.visited = False
	def get_color(self):
		if self.visited == False:
			return("grey")
		elif self.visited == True:
			return("yellow")

class player():
	def __init__(self):
		self.loc = [5,5]
		self.max_health = 100
		self.health = 100
		self.damage = 10
	def move(self,dir):
		dun[self.loc[0]][self.loc[1]].visited = True
		if dir == "north":
			self.loc[1] -= 1
			disp.move("player",0,-1*smh)
		elif dir == "south":
			self.loc[1] += 1
			disp.move("player",0,smh)
		elif dir == "west":
			self.loc[0] -= 1
			disp.move("player",-1*smw,0)
		elif dir == "east":
			self.loc[1] += 1
			disp.move("player",smw,0)
		else:
			raise RuntimeError
			

p = player()

def move_north(): p.move("north")
def move_south(): p.move("south")
def move_west(): p.move("west")
def move_east(): p.move("east")

dun = []
for i in range(dun_w):
	column = []
	for k in range(dun_h):
		column.append(room())
	dun.append(column)
	

b = [tk.Button(master) for i in range(12)]
for i,k in enumerate(b):
	k.configure(text="b"+str(i))
	
b[1].configure(text="North",command=move_north)
b[7].configure(text="South",command=move_south)
b[3].configure(text="West",command=move_west)
b[5].configure(text="East",command=move_east)


b[0].grid(row=0, column=0)
b[1].grid(row=0, column=1)
b[2].grid(row=0, column=2)

b[3].grid(row=1, column=0)
b[4].grid(row=1, column=1)
b[5].grid(row=1, column=2)

b[6].grid(row=2, column=0)
b[7].grid(row=2, column=1)
b[8].grid(row=2, column=2)

b[9].grid(row=3, column=0)
b[10].grid(row=3, column=1)
b[11].grid(row=3, column=2)


disp = tk.Canvas(master,width=w,height=h)
disp.grid(row=0, column=3, rowspan=4)

for i in range(dun_w):  #  generate display 
	for k in range(dun_h):
		disp.create_rectangle(smw*i,smh*k,smw*i+smw,smh*k+smh,
		fill="grey")

disp.create_oval(smw * p.loc[0] ,smh * p.loc[1], # player
smw * p.loc[0] + smw, smh * p.loc[1] +smh,
fill = "green",
tags = "player")

out = tk.Message(master,text="output",width=w+100)

out.grid(row=4, column=0, columnspan=4)

master.mainloop()