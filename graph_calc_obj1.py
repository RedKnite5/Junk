import math
import tkinter as tk


class graph(object):
	def __init__(self,
	xmin=-5,xmax=5,ymin=-5,ymax=5,
	wide=400,high=400):
		self.root = tk.Tk()
		
		self.xmin = xmin
		self.xmax = xmax
		self.ymin = ymin
		self.ymax = ymax
		
		self.screen = tk.Canvas(self.root,
		width=wide,height=high,)
		self.screen.pack()
		
		self.xdraw("0")
		self.ydraw("0")
	
	def xdraw(self,func):
		density = 1000
		x = self.xmin
		xrang = self.xmax-self.xmin
		yrang = self.ymax-self.ymin
		k = 0
		while x < self.xmax:
			x += xrang/density
			if True:#try:
				y = float(simplify("eval "+func+" at "+str(x)))
				
				slope = float(simplify(
				"derivative of "+func+" at "+str(x)))
				density = int((400*math.fabs(slope))+500)
				
				if y > self.ymax or y < self.ymin:
					denstiy = 2000
					
				a = (x-self.xmin)*wide/xrang
				b = high - ((y-self.ymin)*high/yrang)
				
				self.screen.create_line(a,b,a+1,b)
				k += 1
			#except: pass
		self.root.update()
	
	def ydraw(self,func):
		density = 1000
		y = self.ymin
		xrang = self.xmax-self.xmin
		yrang = self.ymax-self.ymin
		k = 0
		
		while y < self.ymax:
			y += yrang/density
			try:
				x = float(simplify("eval "+func+" at "+str(y)))
				slope = float(simplify(
				"derivative of "+func+" at "+str(y)))
				density = int((400*math.fabs(slope))+500)
				
				if x > self.xmax or x < self.xmin:
					denstiy = 2000
					
				a = (x-self.xmin)*wide/xrang
				b = high - ((y-self.ymin)*high/yrang)
				
				self.screen.create_line(a,b,a+1,b)
				k += 1
			except: pass
		self.root.update()


