import tkinter as tk
import cmath as c
import colorsys as csys
from numba import autojit
#   mandelbrot_zoom.py
	

def html_color(color):
	ans = list(map(lambda c: str(hex(int(c)))[2:],color))
	for i in range(len(ans)):
		if len(ans[i]) == 1:
			ans[i] = "0"+ans[i]
	return(ans)
	
size = 1
iter = 200
loc = (0,0)
magnify = 0
i = 0


zoom = 10**magnify

def give_point(event):
	global loc, magnify, zoom, iter
	x, y = event.x, event.y
	x = (((x/(100*size))-2)/zoom)+loc[0]
	y = (((y/(100*size))-2)/zoom)+loc[1]
	print(x," ",y)
	loc = (x,y)
	magnify += 1 
	zoom = 10**magnify
	iter += 0
	load()


def point(A,B):
	z = 0
	a = (((A/(100*size))-2)/zoom)+loc[0]
	b = (((B/(100*size))-2)/zoom)+loc[1]
	for k in range(iter):
		if c.polar(z)[0] > 2:
			return(k)
		z = z*z + (a+b*1j)
	return(iter)
	
def load():
	for a in range(int(size*400)):
		for b in range(int(size*400)):
			value = point(a,b)
			
			color = csys.hls_to_rgb(value/iter,100,1)
			color = "#"+"".join(html_color(color))
			if value == iter:
				color = "black"
			can.create_line(a,b,a+1,b,fill=color)
		
root = tk.Tk()
		
can = tk.Canvas(root,width=size*400,height=size*400)
can.pack()

load()

can.bind("<Button 1>",give_point)

root.mainloop()