# langtons_ant.py


import pygame as pg


boxsize = boxwidth, boxheight = 30, 30
boxeswide, boxeshigh = 10, 10

size = width, height = boxwidth * boxeswide, boxheight * boxeshigh

white = (255, 255, 255)
black = (0, 0, 0)

to_update = []


pg.init()

screen = pg.display.set_mode(size)

screen.fill(white)

for h in range(boxeshigh):
	for w in range(boxeswide):
		pg.draw.rect(
			screen,
			black,
			(w * boxwidth, h * boxheight, boxwidth, boxheight),
			1)

pg.display.update()



running = True
while running:

	for i in pg.event.get():

		if i.type == pg.QUIT:
			running = False
			pg.quit()
			quit()
