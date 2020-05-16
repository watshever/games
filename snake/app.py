from objects.game import Game
from objects.food import Food
from objects.snake import Snake

import pygame
import os
os.environ['SDL_AUDIODRIVER']='dsp'

# initialize pygame components and game
pygame.init()
game = Game()

# condition to run the game
done = False

# main game loop
while not done:

	# run the snake game
	done = game.run()

	# handler for exit button on gui
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# refresh the animation
	pygame.display.flip()


