import tkinter as tk
from tkinter import filedialog
import colorsys as csys
import io
#   python paint.py
root = tk.Tk()
w = 400
h = 400
a = tk.Canvas(width=w,height=h)
a.pack()

mode = "draw"
i=0
brush_size = 1


def html_color(color):
	ans = list(map(lambda c: str(hex(int(c)))[2:],color))
	for i in range(len(ans)):
		if len(ans[i]) == 1:
			ans[i] = "0"+ans[i]
	return(ans)
	

def left(event):
	global i,x,y
	x, y = event.x, event.y
	color = csys.hls_to_rgb(color_scale.get()/1000,100,1)
	color = "#"+"".join(html_color(color))
	if color_scale.get() == 0:
		color = "black"
	if mode == "line":
		a.create_line(x,y,x,y,tags=str(i),fill=color)
		i+=1
	elif mode == "draw":
		a.create_oval(
		x-brush_size,y-brush_size,x+brush_size,y+brush_size,
		fill=color,outline=color)
		
		i+=1
		
def drag(event):
	global i
	x2, y2 = event.x, event.y
	color = csys.hls_to_rgb(color_scale.get()/1000,100,1)
	color = "#"+"".join(html_color(color))
	if color_scale.get() == 0:
		color = "black"
	if mode == "line":
		a.coords(str(i),x,y,x2,y2)
	elif mode == "draw":
		a.create_oval(
		x2-brush_size,y2-brush_size,x2+brush_size,y2+brush_size,
		fill=color,outline=color)
		
		i+=1
		
def line():
	global mode
	mode="line"
def draw():
	global mode
	mode="draw"
def plus_brush(*arg):
	global brush_size
	brush_size += 1
def minus_brush():
	global brush_size
	if brush_size > 1:
		brush_size -= 1
		
		

def save():
    global hen
    ps = a.postscript(colormode = 'color')
    hen = tk.filedialog.asksaveasfilename(defaultextension = '.jpg')
    im = PIL.Image.open(io.BytesIO(ps.encode('utf-8')))
    im.save(hen + '.jpg')		


line_b = tk.Button(root,text="line",command=line)
line_b.pack(side="left")
draw_b = tk.Button(root,text="draw",command=draw)
draw_b.pack(side="left")
brush_plus = tk.Button(root,text="+",command=plus_brush)
brush_plus.pack(side="left")
brush_minus = tk.Button(root,text="-",command=minus_brush)
brush_minus.pack(side="left")
save_b = tk.Button(root,text="save",command=save)
save_b.pack(side="left")

color_scale = tk.Scale(root,from_=0,to=1000,orient="horizontal")
color_scale.pack(side="left")


a.bind("<Button 1>",left)
a.bind("<B1 Motion>",drag)

root.mainloop()

