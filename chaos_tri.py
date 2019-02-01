# chaos_tri.py

import random as rand
import pygame as pg
import time

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

screen_size = (700, 500)

to_update = []

points = ((10, 10), (10, 490), (690, 490), (690, 10))
time = 2
size = 1

p = (200, 200)

pg.init()

screen = pg.display.set_mode(screen_size)

screen.fill(white)

for i in points:
	pg.draw.circle(screen, red, i, 7, 0)

pg.display.update()

def find_new(old, corner, fraction):
	a = int(old[0] * (1 - fraction) + fraction * corner[0])
	b = int(old[1] * (1 - fraction) + fraction * corner[1])
	return a, b

count = 0
while count < 200:
	print(count)
	if pg.event.get() == pg.QUIT:
		pg.quit()
		quit()
	
	for i in range(100):
		chosen = rand.choice(points)
		p = find_new(p, chosen, 17/32)
		pg.draw.circle(screen, black, p, size, 0)
		to_update.append((p[0] - size, p[1] - size, 2*size, 2*size))
		
	pg.display.update(to_update)
	del to_update[:]
	pg.time.wait(20)
	
	count += 1
pg.time.wait(2000)
