import mod,math
import tkinter as tk
# python stuff.py 

root = tk.Tk()

w = 400
h = 400

eyeloc = (200,200)


def motion(event):
	global i
	x, y = event.x, event.y
	print(x,y)
	
a = tk.Canvas(width=w,height=h)
a.pack()

def draw_eye(eyeloc):
	coord = (eyeloc[0]-125,eyeloc[1]-37,eyeloc[0]+125,eyeloc[1]+213)
	rev_coord = (eyeloc[0]-125,eyeloc[1]-205,eyeloc[0]+125,eyeloc[1]+35)
	a.create_arc(coord,style="arc",start=45,tags="upper_lid")
	a.create_arc(rev_coord,style="arc",start=225,tags="lower_lid")
	a.create_oval(eyeloc[0]-30,eyeloc[1]-30,eyeloc[0]+30,eyeloc[1]+30,tags="iris",fill="#00FFFF")
	a.create_oval(eyeloc[0]-10,eyeloc[1]-10,eyeloc[0]+10,eyeloc[1]+10,tags="pupil",fill="black")

	a.create_line(eyeloc[0]-57,eyeloc[1]-22,eyeloc[0]-78,eyeloc[1]-62)
	a.create_line(eyeloc[0]-37,eyeloc[1]-31,eyeloc[0]-48,eyeloc[1]-71)
	a.create_line(eyeloc[0]-15,eyeloc[1]-36,eyeloc[0]-21,eyeloc[1]-72)
	a.create_line(eyeloc[0]+4,eyeloc[1]-37,eyeloc[0]+5,eyeloc[1]-72)
	a.create_line(eyeloc[0]+26,eyeloc[1]-33,eyeloc[0]+30,eyeloc[1]-72)
	a.create_line(eyeloc[0]+47,eyeloc[1]-30,eyeloc[0]+60,eyeloc[1]-66)
	
draw_eye(eyeloc)


root.bind('<Button 1>', motion)














root.mainloop()