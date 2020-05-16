from objects.game import GAME_WIDTH, GAME_HEIGHT
from objects.food import Food
from objects.snake import Snake

import pygame
import os
os.environ['SDL_AUDIODRIVER']='dsp'

# initialize pygame components 
pygame.init()
screen = pygame.display.set_mode((GAME_HEIGHT, GAME_WIDTH))
clock = pygame.time.Clock()

# create food and snake
food = Food((34, 231, 2))
snake = Snake((255, 64, 89))

# condition to run the game
done = False

# main game loop
while not done:
	
	# render the animation of the game
	clock.tick(100 * (1 + len(snake.body) / 50))
	screen.fill(pygame.Color(0,0,0))
	food.render(screen)
	snake.render(screen)

	# update the snake location and check lose conditions
	snake.snake_controls(food)
	done = snake.check_lose()

	# handler for exit button on gui
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# refresh the animation
	pygame.display.flip()


