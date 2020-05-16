import pygame
import objects.game as game
from random import randint 

class Food:

	# creates a snake food 
	def __init__(self, color):
		self.color = (25, 34, 89)
		self.size = game.FOOD_SIZE
		self.rect = pygame.Rect(game.GAME_HEIGHT / 2, game.GAME_WIDTH / 2, self.size, self.size)
	
	# teleports the food when the snake has eaten one already
	def teleport(self):
		self.rect = pygame.Rect(randint(0, game.GAME_WIDTH - self.size), randint(0, game.GAME_HEIGHT - self.size), self.size, self.size)

	# renders the food onto the screen 
	def render(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)
