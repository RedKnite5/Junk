import tkinter as tk
#  python game_of_life.py

wide = 400
high = 400
tiles_w = 11
tiles_h = 11
tw = wide/tiles_w
th = high/tiles_h
live_color = "yellow"
dead_color = "grey"

root = tk.Tk()

blank = tk.Canvas(root,width=wide,height=high)
blank.pack()

class cell(object):
	def __init__(self,x,y):
		self.alive = False
		self.loc = [x,y]
	def live(self):
		self.alive = True
		blank.itemconfig(str(self.loc),fill=live_color)

board = {}
for k in range(tiles_w):
	for i in range(tiles_h):
		blank.create_rectangle(tw*k+2,th*i+2,tw*k+tw+2,th*i+th+2,
		fill=dead_color,tags=str([k,i]))
		print(str([k,i]))
		print(tags)
		board[str([k,i])] = cell(k,i)

board[str([1, 1])].live()
blank.itemconfig(str([k,i]),fill="red")
print(blank.itemcget(str([k,i]),"fill"))

'''
for i in board:
	print(i+str(board[i].loc))'''
root.mainloop()