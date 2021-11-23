import tkinter as tk
import cmath as c
#   python mandelbrot.py

def iterate(z,c):
	return(z*z+c)
	
root = tk.Tk()

bg = tk.Canvas(root,width=400,height=400)
bg.pack()

def point(A,B):
	z = 0
	a = (A/100)-2
	b = (B/100)-2
	for i in range(100):
		if c.polar(z)[0] > 2:
			return(False)
		z = iterate(z,a+b*1j)
	return(True)
			

for a in range(400):
	for b in range(400):
		if point(a,b):
			bg.create_line(a,b,a+1,b)
		





root.mainloop()