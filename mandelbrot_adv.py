import tkinter as tk
import cmath as c
import colorsys as csys
#   python mandelbrot_adv.py

#          look at this dave!

def iterate(z,c):
	return(z*z+c)
	

def html_color(color):
	ans = list(map(lambda c: str(hex(int(c)))[2:],color))
	for i in range(len(ans)):
		if len(ans[i]) == 1:
			ans[i] = "0"+ans[i]
	return(ans)
	
size = 6
	
root = tk.Tk()

bg = tk.Canvas(root,width=size*300,height=size*250)
bg.pack()

def point(A,B):
	z = 0
	a = (A/(100*size))-2
	b = (B/(100*size))-2
	for i in range(500):
		if c.polar(z)[0] > 2:
			return(i)
		z = iterate(z,a+b*1j)
	return(500)
			

for a in range(size*300):
	for b in range(size*250):
		value = point(a,b+(75*size))
		
		color = csys.hls_to_rgb(value/500,100,1)
		color = "#"+"".join(html_color(color))
		if value == 500:
			color = "black"
		bg.create_line(a,b,a+1,b,fill=color)





root.mainloop()