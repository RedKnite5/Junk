import math
from math import e
import tkinter as tk
import list_functions as li
#   python graph_calc.py

class graph(object):
	def __init__(self,func,
	scr_width=400,scr_height=400,
	xmin=-5,xmax=5,ymin=-5,ymax=5):
		def axis(x,y): return(0)

		def y1(x,y): return(eval(func))
			
		xfunc = [axis,y1]

		yfunc = [axis]

		fields = []



		root = tk.Tk()
		
		def close():
			root.quit()

		screen = tk.Canvas(root,width=scr_width,height=scr_height)
		screen.pack()
		
		close = tk.Button(root,text="Close",command=close)
		close.pack()

		for i in xfunc:
			density = 1000
			x = xmin
			k = 0
			while x < xmax:
				xrang = xmax-xmin
				yrang = ymax-ymin		
				x += xrang/density
				try:
					y = i(x,0)
					
					slope = (i(x,0)-i(x-.0001,0))/.0001
					
					density = int((400*math.fabs(slope))+500)
					
					if y > ymax or y < ymin:
						density = 2000
					
					a = (x-xmin)*scr_width/xrang
					b = scr_height -( (y-ymin)*scr_height/yrang)

					screen.create_line(a,b,a+1,b)
					k += 1
				except: pass
		
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
		
		'''		
		for i in fields:
			field_density = 30
			for k in range(int(field_density)):
				for h in range(int(field_density)):
					xrang = xmax-xmin
					yrang = ymax-ymin
					x = (h+((xmin+xmax)/2 - field_density/2))*xrang/field_density
					y = (k+((ymin+ymax)/2 - field_density/2))*yrang/field_density
					
					slope = i(x,y)
					
					a = (x-xmin)*scr_width/xrang
					b = scr_height - (y-ymin)*scr_height/yrang
					
					slope_line_len = slope*(30/(1+slope**4))**.5
					try:
						c = math.fabs(slope_line_len/slope)
					except:
						c = slope_line_len
					d = slope_line_len*slope
					print("")
					print(b,d,b-d,b+d)
					print(round(((4*c*c)+(4*d*d))**.5))
					print("C: ",c," D: ",d)
					screen.create_line(a+c,b-d,a-c,b+d)
		'''



		root.update()

