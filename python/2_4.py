import pygame # type: ignore
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Initialize screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock and font
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsans", 35)

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue)
    screen.blit(value, [0, 0])

def draw_grid():
    for x in range(0, width, snake_block):
        for y in range(0, height, snake_block):
            rect = pygame.Rect(x, y, snake_block, snake_block)
            pygame.draw.rect(screen, (230, 230, 230), rect, 1)

def draw_food(x, y):
    pygame.draw.ellipse(screen, (255, 0, 0), [x, y, snake_block, snake_block])
    pygame.draw.ellipse(screen, (200, 0, 0), [x + 2, y + 2, snake_block - 4, snake_block - 4])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 150, 0), [x[0], x[1], snake_block, snake_block], border_radius=5)
        pygame.draw.rect(screen, (0, 100, 0), [x[0] + 2, x[1] + 2, snake_block - 4, snake_block - 4], border_radius=5)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def gameLoop():
    while True:  # Use a loop to restart the game
        game_over = False
        game_close = False

        x1, y1 = width / 2, height / 2
        x1_change, y1_change = 0, 0

        snake_list = []
        length_of_snake = 1

        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close:
                screen.fill(white)
                message("You Lost! Press Q-Quit or C-Play Again", red)
                your_score(length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                        if event.key == pygame.K_c:
                            game_over = True
                            game_close = False
                            break  # Exit the inner loop to restart the game

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            screen.fill(white)
            draw_grid()
            draw_food(foodx, foody)
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            our_snake(snake_block, snake_list)
            your_score(length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                length_of_snake += 1

            clock.tick(snake_speed)

gameLoop()
