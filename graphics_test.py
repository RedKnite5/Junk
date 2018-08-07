import mod,sys,time,math
#python graphics_test.py


win = GraphWin("Pictures",400,400)

box = Rectangle(Point(5,80),Point(25,100))
ball = Circle(Point(170,90),12)

spinning_shapes = True
graph = False



if spinning_shapes:
	ball.draw(win)
	box.draw(win)
	time.sleep(1)
	for i in range(200):
		time.sleep(.04)
		ball.move(-14*math.sin(i/5),-14*math.cos(i/5))
		box.move(16*math.sin(i/5),16*math.cos(i/5))
		
if graph:
	for x in range(-200,200):
		pt = Point(x+200,-1*(x**2-200))
		pt.draw(win)













close = input("press any key")
print(close)