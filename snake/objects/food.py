import pygame
import objects.game as game
from random import randint 

class Food:
	def __init__(self, color):
		self.color = (25, 34, 89)
		self.size = game.FOOD_SIZE
		self.rect = pygame.Rect(game.GAME_HEIGHT / 2, game.GAME_WIDTH / 2, self.size, self.size)
	
	def move(self, x, y):
		self.rect = self.rect.move(x, y)

	def teleport(self):
		self.rect = pygame.Rect(randint(0, game.GAME_WIDTH - self.size), randint(0, game.GAME_HEIGHT - self.size), self.size, self.size)

	def render(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)
