import pygame
from objects.food import Food
import os
os.environ['SDL_VIDEODRIVER']='dummy'

pygame.init()

size = width, height = 100, 100
screen = pygame.display.set_mode(size)

food = Food(5, "red")
while 1:
	screen.fill(pygame.Color(0,0,0))
	food.render(screen)
	pygame.display.flip()
