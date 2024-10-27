import pygame
import sys
from game import Game
from utils import DIRECTIONS

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLOCKSIZE = 20
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SNAKE GAME USING LINKED LIST")

SNAKE_COLOR = (0, 255, 0)  # Green
FOOD_COLOR = (255, 0, 0)    # Red
BACKGROUND_COLOR = (0, 0, 0) 
TEXT_COLOR = (255, 255, 255)

game = Game(SCREEN_WIDTH // BLOCKSIZE, SCREEN_HEIGHT // BLOCKSIZE)

def show_home_screen():
    highscore = read_high_score()
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, 32)
    
    title_text = font.render("THE SNAKE GAME", True, TEXT_COLOR)
    name_text = font.render("by Sankeerth M P", True, TEXT_COLOR)
    start_text = font.render("Press 'ENTER' to start", True, TEXT_COLOR)
    highscore_text = font.render(f"Highscore: {highscore}", True, TEXT_COLOR)

    screen.blit(title_text, (100, 100))
    screen.blit(name_text, (100, 150))
    screen.blit(highscore_text, (100, 300))
    screen.blit(start_text, (100, 400))

    pygame.display.flip()

def read_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0
def save_high_score(score):
    highscore=read_high_score()
    if score>highscore:
        with open("highscore.txt","w")as f:
            f.write(str(score))

def game_over_session(score):
    save_high_score(score)
    highscore=read_high_score()
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, 32)
    
    game_over_text = font.render("game Over", True, TEXT_COLOR)
    screen.blit(game_over_text, (100, 100))
    score_text = font.render(f"score {score}", True, TEXT_COLOR)
    screen.blit(score_text, (100, 200))
    highscore_text = font.render(f"Highscore {highscore}", True, TEXT_COLOR)
    screen.blit(highscore_text, (100, 250))
    retry_text = font.render("Press 'R' to retry ", True, TEXT_COLOR)
    screen.blit(retry_text, (100, 300))
    quit_text = font.render("Press 'q' to quit", True, TEXT_COLOR)
    screen.blit(quit_text, (100, 350))
    pygame.display.flip()

def draw_game():
    screen.fill(BACKGROUND_COLOR)
    
    for (x, y) in game.snake.getCoordinates():
        pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(x * BLOCKSIZE, y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
    
    food_x, food_y = game.food
    pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(food_x * BLOCKSIZE, food_y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
    
    pygame.display.flip()

def gameloop():
    running = True
    clock = pygame.time.Clock()
    FPS = 10
    score=0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
            running = False 
            score=game.score # Stop the game loop if there's a collision

        draw_game()
        clock.tick(FPS)
    game_over_session(score)

on_home_screen = True
running = True

while running:
    if on_home_screen:
        show_home_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Start the game with 'S'
                    on_home_screen = False  # Exit home screen
                    game = Game(SCREEN_WIDTH // BLOCKSIZE, SCREEN_HEIGHT // BLOCKSIZE)
                    gameloop()  # Call the game loop function
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Start the game with 'S'
                    running=False  # Exit home screen
                elif event.key==pygame.K_r:
                    game = Game(SCREEN_WIDTH // BLOCKSIZE, SCREEN_HEIGHT // BLOCKSIZE)
                    gameloop()
pygame.quit()

