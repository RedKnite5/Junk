import math
from math import e
import tkinter as tk
#   python tk_calc.py

scr_width = 400
scr_height = 400

def axis(x,y): return(0)

def y1(x,y): return(1/(1+e**(-1*x)))
def y2(x,y): return(x)
	
xfunc = [axis,y2]

yfunc = [axis]

fields = [y2]

xmin = -5
xmax = 5

ymin = -5
ymax = 5



root = tk.Tk()

screen = tk.Canvas(root,width=scr_width,height=scr_height)
screen.pack()

for i in xfunc:
	density = 1000
	x = xmin
	k = 0
	while x < xmax:
		xrang = xmax-xmin
		yrang = ymax-ymin		
		x += xrang/density
		y = i(x,0)
		
		slope = (i(x,0)-i(x-.0001,0))/.0001
		
		density = int((400*math.fabs(slope))+500)
		
		if y > ymax or y < ymin:
			density = 2000
		
		a = (x-xmin)*scr_width/xrang
		b = scr_height -( (y-ymin)*scr_height/yrang)

		screen.create_line(a,b,a+1,b)
		k += 1
	
for i in yfunc:
	density = 1000
	y = ymin
	k = 0
	while y < ymax:
		xrang = xmax-xmin
		yrang = ymax-ymin		
		y += yrang/density
		x = i(y,0)
		slope = (i(y,0)-i(y-.0001,0))/.0001
		
		density = int((400*math.fabs(slope))+1000)
		
		if x > xmax or x < xmin:
			density = 2000
		
		a = (x-xmin)*scr_width/xrang
		b = scr_height -( (y-ymin)*scr_height/yrang)

		screen.create_line(a,b,a+1,b)
		k += 1
		
for i in fields:
	field_density = 10
	slope_line_len = 5
	for k in range(int(field_density)):
		for h in range(int(field_density)):
			xrang = xmax-xmin
			yrang = ymax-ymin
			x = xrang*h/scr_width
			y = yrang*k/scr_height
			
			slope = i(x,y)
			
			a = (x-xmin)*scr_width/xrang
			b = scr_height - (y-ymin)*scr_height/yrang
			try:
				c = slope_line_len/slope
			except:
				c = 0
			d = slope_line_len*slope
			print(slope)
			print(a-c,b-d,a+c,b+d)
			screen.create_line(a-c,b-d,a+c,b+d)



root.mainloop()