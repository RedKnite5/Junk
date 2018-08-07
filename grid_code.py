#  python grid_code.py
import tkinter as tk

class square(object):
	def __init__(self,loc,vars):
		self.loc = loc
		i,k = self.loc
		self.tw, self.th, self.blank = vars
		self.blank.create_rectangle(self.tw * i + 1, self.th * k + 1,
		self.tw * i + self.tw + 1, self.th * k + self.th + 1,
		tags=str(i) + "," + str(k))

		
class grid(object):
	def __init__(self):
		self.root = tk.Tk()
		
		self.squares = []
		self.wide = 400
		self.high = 400
		self.tiles_w = 11
		self.tiles_h = 11
		self.tw = self.wide/self.tiles_w
		self.th = self.high/self.tiles_h
		
		
		self.blank = tk.Canvas(width=self.wide,height=self.high)
		self.blank.pack()
		
		self.vars = (self.tw, self.th, self.blank)
		
		
		for i in range(self.tiles_w):
			for k in range(self.tiles_h):
				self.squares.append(square((i,k),self.vars))
		
		self.root.mainloop()