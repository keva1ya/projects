import pygame
import random
import sys

# Constants
GRID_SIZE = 4
TILE_SIZE = 100
TILE_MARGIN = 10
WINDOW_SIZE = GRID_SIZE * TILE_SIZE + (GRID_SIZE + 1) * TILE_MARGIN
FONT_SIZE = 40
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("2048")
font = pygame.font.Font(None, FONT_SIZE)

def initialize_game():
    board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if board[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = 2 if random.random() < 0.9 else 4

def slide_row_left(row):
    new_row = [cell for cell in row if cell != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [cell for cell in new_row if cell != 0]
    return new_row + [0] * (GRID_SIZE - len(new_row))

def slide_left(board):
    return [slide_row_left(row) for row in board]

def slide_right(board):
    return [slide_row_left(row[::-1])[::-1] for row in board]

def slide_up(board):
    transposed = list(zip(*board))
    transposed = slide_left([list(row) for row in transposed])
    return [list(row) for row in zip(*transposed)]

def slide_down(board):
    transposed = list(zip(*board))
    transposed = slide_right([list(row) for row in transposed])
    return [list(row) for row in zip(*transposed)]

def is_game_over(board):
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if board[r][c] == 0:
                return False
            if c < GRID_SIZE - 1 and board[r][c] == board[r][c + 1]:
                return False
            if r < GRID_SIZE - 1 and board[r][c] == board[r + 1][c]:
                return False
    return True

def draw_board(board):
    screen.fill(BACKGROUND_COLOR)
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            value = board[r][c]
            color = TILE_COLORS.get(value, (60, 58, 50))
            rect = pygame.Rect(
                c * TILE_SIZE + (c + 1) * TILE_MARGIN,
                r * TILE_SIZE + (r + 1) * TILE_MARGIN,
                TILE_SIZE,
                TILE_SIZE,
            )
            pygame.draw.rect(screen, color, rect, border_radius=5)
            if value != 0:
                text = font.render(str(value), True, (119, 110, 101))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    pygame.display.flip()

def main():
    board = initialize_game()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            new_board = slide_up(board)
        elif keys[pygame.K_a]:
            new_board = slide_left(board)
        elif keys[pygame.K_s]:
            new_board = slide_down(board)
        elif keys[pygame.K_d]:
            new_board = slide_right(board)
        else:
            new_board = board

        if new_board != board:
            board = new_board
            add_new_tile(board)

        draw_board(board)

        if is_game_over(board):
            print("Game Over!")
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

        clock.tick(10)

if __name__ == "__main__":
    main()