import pygame
import objects.game as game

class Snake:

	# constructor for the snake that player controls
	def __init__(self, color):	
		self.size = game.SNAKE_BODY_SIZE
		self.color = color
		self.head = pygame.Rect(game.GAME_HEIGHT / 3, game.GAME_WIDTH / 3, self.size, self.size)
		self.body = [self.head]
		self.movement = [0, -1]

	# renders the snake onto the game screen 
	def render(self, screen):
		for body in self.body:
			pygame.draw.rect(screen, self.color, body)

	# moves the snake and also checks if it has eaten any food
	def move(self, x, y, food):
		self.head.move_ip(x, y)
		if len(self.body) > 1 and not self.head.colliderect(self.body[1]):
			self.body.insert(1, pygame.Rect(self.head.left, self.head.top, self.size, self.size))
			self.body.pop()

		if self.head.colliderect(food.rect):
			self.eat_food(food)
			food.teleport()

	# checks if the snake has collided with a wall or itself
	def check_lose(self):
		if self.head.x < 0 or self.head.x > game.GAME_WIDTH - game.SNAKE_BODY_SIZE:
			return True
		if self.head.y < 0 or self.head.y > game.GAME_HEIGHT - game.SNAKE_BODY_SIZE:
			return True
		
		return not len(self.head.collidelistall(self.body[2:])) == 0

	# grows snake if it has eaten food
	def eat_food(self, food):
		# if false (snake going vertically, append vertically)
		last = self.body[-1]
		if self.movement[1]:
			self.body.append(pygame.Rect(last.left, last.top - self.movement[1] * game.SNAKE_BODY_SIZE, self.size, self.size))
		else:
			self.body.append(pygame.Rect(last.left - self.movement[0] * game.SNAKE_BODY_SIZE, last.top, self.size, self.size))		

	# player key handler for controlling where the snake goes
	def snake_controls(self, food):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.movement = [-1, 0]
		if keys[pygame.K_RIGHT]:
			self.movement = [1, 0]
		if keys[pygame.K_UP]:
			self.movement = [0, -1]
		if keys[pygame.K_DOWN]:
			self.movement = [0, 1]
		self.move(self.movement[0], self.movement[1], food)
