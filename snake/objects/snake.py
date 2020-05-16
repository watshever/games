import pygame
import objects.game as game

class Snake:
	def __init__(self, color):	
		self.size = game.SNAKE_BODY_SIZE
		self.color = color
		self.head = pygame.Rect(game.GAME_HEIGHT / 3, game.GAME_WIDTH / 3, self.size, self.size)
		self.body = [self.head]
		self.movement = [0, -1]

	def render(self, screen):
		self.head = pygame.draw.rect(screen, self.color, self.head)
		for bod in self.body[1:]:
			pygame.draw.rect(screen, self.color, bod)

	def move(self, x, y, food):
		self.head = self.head.move(x, y)
		if len(self.body) > 1 and not self.head.colliderect(self.body[1]):
			self.body.pop()
			self.body.insert(1, pygame.Rect(self.head.left, self.head.top, self.size, self.size))

		if self.head.colliderect(food.rect):
			self.eat_food(food)
			food.teleport()
		 	


	def check_lose(self):
		if self.head.x < 0 or self.head.x > game.GAME_WIDTH - game.SNAKE_BODY_SIZE:
			return True
		if self.head.y < 0 or self.head.y > game.GAME_HEIGHT - game.SNAKE_BODY_SIZE:
			return True
		
		for b in self.body[2:]:
			return b.colliderect(self.head)

	def eat_food(self, food):
		# if false (snake going vertically, append vertically)
		last = self.body[-1]
		if self.movement[1]:
			self.body.append(pygame.Rect(last.left, last.top - self.movement[1] * game.SNAKE_BODY_SIZE, self.size, self.size))
		else:
			self.body.append(pygame.Rect(last.left - self.movement[0] * game.SNAKE_BODY_SIZE, last.top, self.size, self.size))		
