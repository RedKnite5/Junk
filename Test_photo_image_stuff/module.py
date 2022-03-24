
import tkinter as tk


class B(object):
	def __init__(self):
		self.root = tk.Tk()
		self.can = tk.Canvas(self.root)
		self.can.pack()
		
		
	def func(self, obj):
		self.can.create_image(
			0, 0,
			image=obj.image,
			anchor="nw"
		)
		self.root.mainloop()

