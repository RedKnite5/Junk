import tkinter as tk

x1 = float(input("Input the first x coordinate"))
y1 = float(input("Input the first y coordinate"))
x2 = float(input("Input the second x coordinate"))
y2 = float(input("Input the second y coordinate"))

vertical = False
try:
	slope = (x2 - x1) / (y2 - y1)
except ZeroDivisionError:
	if not x2 - x1:
		raise ValueError("Requires two different points")
	else:
		vertical = True
		slope = float("inf")

root = tk.Tk()

can = tk.Canvas(root, width=300, height=300)
can.pack()

can.create_line(-10, -10, 400, 400)

root.mainloop()
