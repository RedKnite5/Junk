import tkinter as tk
#   python box.py


root = tk.Tk()

w = 400
h = 400

a = tk.Canvas(root,width=w,height=h)
a.pack()

def find_center(item):
	c = a.coords(item)
	if len(c) == 4:
		x = (c[0]+c[2])/2
		y = (c[1]+c[3])/2
		return(x,y)
	else:
		return(0,0)

def move_shape(event):
	x,y = event.x,event.y
	o = a.find_overlapping(x-1,y-1,x+1,y+1)
	center = find_center(o)
	dx = x-center[0]
	dy = y-center[1]
	a.move(o,dx,dy)

shapes = []
shapes.append(a.create_oval(190,190,210,210,tags=10,fill="white"))
shapes.append(a.create_oval(10,10,40,40,tags=30,fill="white"))
shapes.append(a.create_oval(350,350,370,370,fill="white"))








a.bind("<Button 1>",move_shape)
a.bind("<B1 Motion>",move_shape)

root.mainloop()