import pygame
import sys
from game import Game
from utils import DIRECTIONS
pygame.init()

SCREEN_WIDTH,SCREEN_HEIGHT=600,400
BLOCKSIZE=20
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("SNAKE GAME USING LINKED LIST")

SNAKE_COLOR = (0, 255, 0)  # Green
FOOD_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (0, 0, 0) 

game=Game(SCREEN_WIDTH//BLOCKSIZE,SCREEN_HEIGHT//BLOCKSIZE)

clock=pygame.time.Clock()
FPS=10
def draw_game():
    screen.fill(BACKGROUND_COLOR)
    for (x,y) in game.snake.getCoordinates():
        pygame.draw.rect(screen,SNAKE_COLOR,pygame.Rect(x*BLOCKSIZE,y*BLOCKSIZE,BLOCKSIZE,BLOCKSIZE))
    food_x,food_y=game.food
    pygame.draw.rect(screen,FOOD_COLOR,pygame.Rect(food_x*BLOCKSIZE,food_y*BLOCKSIZE,BLOCKSIZE,BLOCKSIZE))
    pygame.display.flip()


running =True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.update_direction(DIRECTIONS["UP"])
            elif event.key == pygame.K_DOWN:
                game.update_direction(DIRECTIONS["DOWN"])
            elif event.key == pygame.K_LEFT:
                game.update_direction(DIRECTIONS["LEFT"])
            elif event.key == pygame.K_RIGHT:
                game.update_direction(DIRECTIONS["RIGHT"])
    try:
        game.moveSnake()
        game.check_self_collision()
    except ValueError as e:
        print(str(e))
        running=False

    draw_game()
    clock.tick(FPS)
pygame.quit()
    