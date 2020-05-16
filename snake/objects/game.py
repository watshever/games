from objects.food import Food
from objects.snake import Snake
import pygame

# global game variables for access by all modules

# gameboard controls
GAME_WIDTH = 400
GAME_HEIGHT = 400
CLOCK_SPEED = 100

# snake controls
SNAKE_BODY_SIZE = 10
SNAKE_COLOR = (255, 64, 89)

# food controls
FOOD_SIZE = 10
FOOD_COLOR = (34, 231, 2)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((GAME_HEIGHT, GAME_WIDTH))
        self.clock = pygame.time.Clock()
        self.food = Food(FOOD_COLOR)
        self.snake = Snake(SNAKE_COLOR)
        self.game_over = False

    def run(self):
        # update core game components
        self.clock.tick(100 * (1 + len(self.snake.body) / 50))
        self.screen.fill(pygame.Color(0,0,0))
	    
        # render the snake and food for the game
        self.food.render(self.screen)
        self.snake.render(self.screen)

        # update the snake and check for lose conditions
        self.snake.snake_controls(self.food)
        self.game_over = self.snake.check_lose()

        return self.game_over
