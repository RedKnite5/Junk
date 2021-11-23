import mod,sys,time,math,numpy,_thread
from graphics import *
# python graphing_calc.py



win_width = 500
win_height = 500

win = GraphWin("Pictures",win_width,win_height)

t_min = -win_width/2
t_max = win_width/2

x_min = -10
x_max = 10

y_min = -10
y_max = 10

mode = "function"
color = "red"
qual = 100
	
def axis():
	x_axis = Line(Point(win_width/2,0),Point(win_width/2,win_height))
	y_axis = Line(Point(0,win_height/2),Point(win_width,win_height/2))
	
	for i in range(x_min+1,x_max):
		top_pt = Point((i*win_width/(2*x_max))+win_width/2,(win_height/2)+5)
		bottom_pt = Point((i*win_width/(2*x_max))+win_width/2,(win_height/2)-5)
		tic = Line(top_pt,bottom_pt)
		if i != 0:
			text_pt = bottom_pt.clone()
			text_pt.move(0,18)
			scale = Text(text_pt,i)
			scale.draw(win)
		tic.draw(win)
	
	for j in range(y_min+1,y_max):
		left_pt = Point(((win_width/2)-5),(j*win_height/(2*y_max))+(win_height/2))
		right_pt = Point(((win_width/2)+5),(j*win_height/(2*y_max))+(win_height/2))
		tic = Line(left_pt,right_pt)
		if j != 0:
			text_pt = right_pt.clone()
			text_pt.move(-18,0)
			scale = Text(text_pt,j*-1)
			scale.draw(win)
		tic.draw(win)
	
	
	x_axis.draw(win)
	y_axis.draw(win)

def function():
	for i in range(qual*int(x_min),qual*int(x_max)):
		t = i/qual
		try:
			equation = math.sin(t)
			x_of_t = ((win_width/2)+-1*t*(win_width/(2*x_min)))
			y_of_t = ((win_height/2)+equation*(win_height/(2*y_min)))
			win.plot(x_of_t,y_of_t,color)
		except:
			pass

			
			
def input_thread(list):
	input()
	list.append(None)
	
def loop_draw():
	list = []
	_thread.start_new_thread(input_thread,(list,))
	while not list:
		function()
		
		

def start():
	axis()
	loop_draw()
	
	
start()
wait = input()
sys.exit()