# mario.py

import pygame as pg
from pygame import draw, Rect


size = width, height = (500, 300)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brown = (205, 133, 63)

to_update = []

pg.init()

screen = pg.display.set_mode(size)

screen.fill(white)
draw.rect(screen, brown, (0, 250, width, 50))

mario = Rect(50, 230, 20, 20)
draw.rect(screen, green, mario)

pg.display.update()

running = True
while running:
	for i in pg.event.get():
		if i.type == pg.QUIT:
			running = False
			pg.quit()
			quit()

		if i.type == pg.K_RIGHT:
			pass


