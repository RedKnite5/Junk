import tkinter as tk
from tkinter import font
from list_functions import overlap
from timeline_events import events
#  python timeline.py

root = tk.Tk()

font = font.Font(family="Helvetica", size=12)
height = (font.metrics("linespace"))

rang = [1857,1940]
can_width = 1200

rang_len = rang[1]-rang[0]
mult = can_width/rang_len
line_h = 370


places = [[0,1,0]]




box = tk.Canvas(root,width=can_width,height=400)
box.pack()
box.create_line(0,line_h,can_width,line_h)

def check_space(i,h):
	global places
	for j in places:
		if i in (False,None):
			break
		if overlap([mult*(events[i]-rang[0])-(w/2),mult*(events[i]-rang[0])+(w/2)],j[:-1]) != 0 and j[2]==h:
			h -= height
			if h<5:
				raise ValueError
			i=check_space(i,h)
	if i:
		box.create_text(mult*(events[i]-rang[0]),h,text=i+" ("+str(events[i])+")")
		places.append([mult*(events[i]-rang[0])-(w/2),mult*(events[i]-rang[0])+(w/2),h])
		return(False)
			


for i in events:
	box.create_line(mult*(events[i]-rang[0]),line_h-10,mult*(events[i]-rang[0]),line_h+10)
	w = font.measure(i+" ("+str(events[i])+")")-20
	check_space(i,line_h-20)

	
box.update()
box.postscript(file="timeline.ps",colormod="color")

root.mainloop()


