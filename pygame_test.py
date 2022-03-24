
import pygame 
from pygame import font


pygame.init()
font.init()

boxsize = boxwidth, boxheight = 30, 30
boxeswide, boxeshigh = 10, 10
time = 550

size = width, height = boxwidth * boxeswide, boxheight * boxeshigh

screen = pygame.display.set_mode(size)

font = pygame.font.Font('freesansbold.ttf', 20)

TextX = 20
TextY = 10

def showText(x,y):
    text = font.render("random text", True, (255,0,0))
    screen.blit(text, (x,y))

# Game Loop
running = True
while running:
	showText(TextX,TextY)
	pygame.display.update()