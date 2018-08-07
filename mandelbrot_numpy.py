#   mandelbrot_numpy.py

import numpy as np
from PIL import Image, ImageTk
from numba import autojit
from cmath import polar
from colorsys import hls_to_rgb
import tkinter as tk

w, h = 512, 512

size = 1
magnify = 0
loc = (0, 0)

zoom = 10 ** magnify
w_mult = 4 / w
h_mult = 4 / h

iterations = 500


@autojit
def point(A, B, iterations, zoom, loc):
	"""Find what color a point on the graph should be."""
	
	z = 0
	a = (((A * w_mult) - 2) / zoom) + loc[0]
	b = (((B * h_mult) - 2) / zoom) + loc[1]
	for k in range(iterations):
		if polar(z)[0] > 2:
			return(k)
		# function line
		z = z ** z + (a + b * 1j)
	return(iterations)
	
def move_point(event):
	'''Move the focus of the image to where the user has clicked and
	zoom in.'''
	
	global iterations, zoom, loc, holder
	x, y = event.x, event.y
	x = (((x * w_mult) - 2) / zoom) + loc[0]
	y = (((y * h_mult) - 2) / zoom) + loc[1]
	print("x = ", x)
	print("y = ", y)
	loc = (x, y)
	zoom *= 10
	iterations = int(iterations * 2)
	holder = load(iterations, zoom, loc)
	

@autojit
def load(iterations, zoom, loc):
	
	data = np.zeros((h, w, 3), dtype = np.uint8)
	
	for p in np.ndindex(h, w):
		value = point(p[0], p[1], iterations, zoom, loc)

		if value == iterations:
			color = (0, 0, 0)
		else:
			color = hls_to_rgb(value / iterations, 100, 1)

		data[p[1], p[0]] = color
	photo = ImageTk.PhotoImage(Image.fromarray(data, "RGB"))
	canvas.create_image(w / 2, h / 2, image = photo)

	return(photo)


root = tk.Tk()
canvas = tk.Canvas(root, width = w, height = h)
canvas.pack()

holder = load(iterations, zoom, loc)

canvas.bind("<Button 1>", move_point)

root.mainloop()
