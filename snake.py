'''
snake.py


problems:
	if you are going right then hit up and then left before you move you can head
	backwards and hit yourself

'''


import pygame as pg
from random import randint, choice



boxsize = boxwidth, boxheight = 30, 30
boxeswide, boxeshigh = 10, 10
time = 550

size = width, height = boxwidth * boxeswide, boxheight * boxeshigh

def banana_loc():
	'''Find a free space to put the banana.'''
	
	global to_update

	place = (
		randint(0, boxeswide - 1) * boxwidth + 1,   # put banana in a box not between boxes
		randint(0, boxeshigh - 1) * boxheight + 1)
	
	banana = choice(fruits)
	ban_rect = banana.get_rect()

	while pg.Rect(place, (boxwidth - 2, boxheight - 2)).collidelist(snake) != -1:
		place = (
			randint(0, boxeswide - 1) * boxwidth + 1 - ban_rect.x,
			randint(0, boxeshigh - 1) * boxheight + 1 - ban_rect.y)

	ban_rect = banana.get_rect().move(place)

	screen.blit(banana, ban_rect)

	to_update.append(ban_rect)

	return ban_rect, banana


def eat():
	'''Increase snake's length and make new banana.'''

	snake.append(snake[-1].copy())

	return banana_loc()


def die():
	'''Go to start menu'''

	global running

	running = False

	screen.fill(white)

	button = pg.Rect(width /2 - 40, height / 2 - 20, 80, 40)

	pg.draw.rect(screen, green, button)
	pg.draw.rect(screen, black, button, 1)

	font = pg.font.Font(pg.font.match_font("arial"), 20)
	text = font.render("Start", True, black)
	textbox = text.get_rect()
	textbox = textbox.move(width /2 - 17, height / 2 - 12)

	screen.blit(text, textbox)

	pg.display.update()

	run = True
	while run:
		for i in pg.event.get():
			if i.type == pg.QUIT:
				run = False
				pg.quit()
				quit()
		
			if i.type == pg.MOUSEBUTTONDOWN:  # check if clicking start button
				if button.collidepoint(pg.mouse.get_pos()):
					run = False
					start()


def start():
	global direction, to_update, snake, running, screen, ban_rect

	direction = None
	running = True
	snake = [pg.Rect(boxwidth * 2, boxheight * 2, boxwidth, boxheight)]
	to_update = []

	screen.fill(white)

	ban_rect, banana = banana_loc()

	for h in range(boxeshigh):
		for w in range(boxeswide):
			pg.draw.rect(
				screen,
				black,
				(w * boxwidth, h * boxheight, boxwidth, boxheight),
				1)

	pg.draw.rect(screen, blue, snake[0])

	pg.display.update()



white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

fruits = ("banana_icon.png", "cherry_icon.png", "apple_icon.png", "grape_icon.png")

direction = None

to_update = []

pg.init()

fruits = list(map(
	lambda a: pg.transform.scale(pg.image.load(a), (boxwidth - 2, boxheight - 2)),
	fruits))

snake = [pg.Rect(boxwidth * 2, boxheight * 2, boxwidth, boxheight)]

screen = pg.display.set_mode(size)

die()
start()

pg.time.set_timer(25, time)

running = True
while running:

	for i in pg.event.get():

		if i.type == pg.QUIT:
			running = False
			pg.quit()
			quit()

		if i.type == pg.KEYDOWN:
			if i.key == pg.K_RIGHT and\
			not (direction == "l" and len(snake) > 1):
				direction = "r"
			elif i.key == pg.K_LEFT and\
			not (direction == "r" and len(snake) > 1):
				direction = "l"
			elif i.key == pg.K_DOWN and\
			not (direction == "u" and len(snake) > 1):
				direction = "d"
			elif i.key == pg.K_UP and\
			not (direction == "d" and len(snake) > 1):
				direction = "u"

		if i.type == 25:  # timer
			try:
				if not snake[-1].colliderect(snake[-2]):   # only erase the last square
					raise IndexError                       # if the snake is not
			except IndexError:                             # colliding with the second to
				pg.draw.rect(screen, white, snake[-1])     # last square. And don't throw
				pg.draw.rect(screen, black, snake[-1], 1)  # a fit if there is no second
				to_update.append(snake[-1].copy())         # to last square

			move = [snake[0].x - snake[-1].x,
					snake[0].y - snake[-1].y]

			if direction == "r":
				move[0] += boxwidth
				snake[-1].move_ip(move)
				snake.insert(0, snake.pop())
			if direction == "l":
				move[0] -= boxwidth
				snake[-1].move_ip(move)
				snake.insert(0, snake.pop())
			if direction == "u":
				move[1] -= boxheight
				snake[-1].move_ip(move)
				snake.insert(0, snake.pop())
			if direction == "d":
				move[1] += boxheight
				snake[-1].move_ip(move)
				snake.insert(0, snake.pop())

			if snake[0].colliderect(ban_rect):
				ban_rect, banana = eat()
			elif snake[0].collidelist(snake[1:]) != -1:  # collide return -1 on no
				die()                                    # collision

			if not 0 <= snake[0].x / boxwidth < boxeswide or\
				not 0 <= snake[0].y / boxheight < boxeshigh:
				die()

			pg.draw.rect(screen, blue, snake[0])
			to_update.append(snake[0].copy())

			pg.display.update(to_update)






