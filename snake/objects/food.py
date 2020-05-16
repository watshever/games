import pygame
from random import randint 

class Food:
	def __init__(self, size, color):
		self.color = [25, 34, 89]
		self.size = size
		self.rect = pygame.Rect(50, 50, self.size, self.size)
	
	def move(self, x, y):
		self.rect = self.rect.move(x, y)

	def teleport(self):
		self.rect = pygame.Rect(randint(0, 100 - self.size), randint(0, 100 - self.size))

	def render(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)
