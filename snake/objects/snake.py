class Snake:
	def __init__(self, color, size):	
		self.size = size
		self.body = []
		self.color = [23, 123, 43]
		self.head = pygame.Rect(50, 50, self.size, self.size)

	def render(self, screen):
		for bod in self.body:
			pygame.draw.rect(screen, bod)
	
	
