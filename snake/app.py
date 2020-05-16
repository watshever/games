from objects.game import GAME_WIDTH, GAME_HEIGHT
from objects.food import Food
from objects.snake import Snake

import pygame
import os
os.environ['SDL_AUDIODRIVER']='dsp'

pygame.init()
screen = pygame.display.set_mode((GAME_HEIGHT, GAME_WIDTH))
clock = pygame.time.Clock()

food = Food((34, 231, 2))
snake = Snake((255, 64, 89))

done = False

while not done:
	#screen.fill(pygame.Color(0,0,0))
	done = snake.check_lose()

	food.render(screen)
	snake.render(screen)
	clock.tick(100)

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		snake.movement = [-1, 0]
	if keys[pygame.K_RIGHT]:
		snake.movement = [1, 0]
	if keys[pygame.K_UP]:
		snake.movement = [0, -1]
	if keys[pygame.K_DOWN]:
		snake.movement = [0, 1]
	snake.move(snake.movement[0], snake.movement[1], food)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
	
	pygame.display.flip()


