import tkinter as tk

#import numpy as np
#from PIL import Image, ImageTk

import mandelbrot_lib as ml

#import timeit
#import cProfile
#import pstats

#  python mandelbrot.py

'''
def html_color(color):
	ans = list(map(lambda c: str(hex(int(c)))[2:],color))
	for i in range(len(ans)):
		if len(ans[i]) == 1:
			ans[i] = "0"+ans[i]
	return(ans)
'''
	
size = .5
iter = 200
loc = (0,0)
magnify = 0
i = 0

new_window = False


zoom = 10**magnify

windows = []
canvases = []

def give_point(event):
	global loc, magnify, zoom, iter
	x, y = event.x, event.y
	x = (((x/(100*size))-2)/zoom)+loc[0]
	y = (((y/(100*size))-2)/zoom)+loc[1]
	print(x, " ", y)
	loc = (x, y)
	magnify += 1 
	zoom = 10**magnify
	iter += 0
	load()

'''
def point(A, B):
	z = 0
	a = (((A/(100*size))-2)/zoom)+loc[0]
	b = (((B/(100*size))-2)/zoom)+loc[1]
	for k in range(iter):
		if c.polar(z)[0] > 2:
			return k
		z = z*z + (a+b*1j)
	return iter
'''

def load():
	global i
	if new_window:
		windows.append(tk.Tk())
		
		canvases.append(tk.Canvas(windows[i], width=size*400, height=size*400))
		canvases[i].pack()
	
	windows[i].bind("<Button 1>", give_point)
	
	for a in range(int(size*400)):
		for b in range(int(size*400)):
			value = ml.point(a, b, size, zoom, loc[0], loc[1], iter)
			
			color = ml.hls_to_rgb(value/iter, 100, 1)
			color = "#" + ml.html_color(*color)
			if value == iter:
				color = "black"
			canvases[i].create_line(a, b, a+1, b, fill=color)
	if new_window:
		i += 1

if __name__ == "__main__":
	'''
	t1 = timeit.timeit("ml.hls_to_rgb(.4, 100, 1)", number=100000, globals=globals())
	t2 = timeit.timeit("csys.hls_to_rgb(.4, 100, 1)", number=100000, globals=globals())
	print(f"ml hls {t1}")
	print(f"csys hls {t2}")
	
	p1 = timeit.timeit("ml.point(100, 100, size, zoom, loc[0], loc[1], iter)", number=100000, globals=globals())
	p2 = timeit.timeit("point(100, 100)", number=100000, globals=globals())
	print(f"ml point {p1}")
	print(f"py point {p2}")
	'''
	
	#with cProfile.Profile() as pr:
	windows.append(tk.Tk())

	canvases.append(tk.Canvas(windows[i],width=size*400,height=size*400))
	canvases[i].pack()

	load()
	#stats = pstats.Stats(pr)
	#stats.sort_stats(pstats.SortKey.TIME)
	#stats.dump_stats(filename="profile_stats.txt")

	windows[0].mainloop()



