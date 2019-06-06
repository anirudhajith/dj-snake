#! dj-snake

from graphics import *
from random import choice, random

TILE_SIZE = 20                                              # length of a tile in pixels
BOARD_LENGTH = 40                                           # number of tiles to a side of the entire board
BACKGROUND_COLOR = color_rgb(128,128,200)                   # board background color
SNAKE_COLOR = color_rgb(255,255,255)                        # snake body color
INITIAL_SNAKE_LENGTH = 3                                    # snake body length at the start of the game
STARTING_POINT = (BOARD_LENGTH // 2, BOARD_LENGTH // 2)     # initial position of snake head

directions = [
    'up', 'down', 'left', 'right'
]

def initializeWindow():
    window = GraphWin(
        title = "dj-snake", 
        width = TILE_SIZE * BOARD_LENGTH, 
        height = TILE_SIZE * BOARD_LENGTH,
    )
    window.setBackground(BACKGROUND_COLOR)

    for x in range(BOARD_LENGTH):
        for y in range(BOARD_LENGTH):
            window.plotPixel(x * TILE_SIZE, y * TILE_SIZE, SNAKE_COLOR)

    return window

def initializeSnake():
    initialDirection = choice(directions)
    head = STARTING_POINT
    snakeBlocks = []

    if initialDirection == 'up':
        for offset in range(INITIAL_SNAKE_LENGTH):
            snakeBlocks.append((head[0], head[1] - offset))
    elif initialDirection == 'down':
        for offset in range(INITIAL_SNAKE_LENGTH):
            snakeBlocks.append((head[0], head[1] + offset))
    elif initialDirection == 'right':
        for offset in range(INITIAL_SNAKE_LENGTH):
            snakeBlocks.append((head[0] - offset, head[1]))
    elif initialDirection == 'left':
        for offset in range(INITIAL_SNAKE_LENGTH):
            snakeBlocks.append((head[0] + offset, head[1]))

    return snakeBlocks

def drawBlock(x, y, window):
    block = Rectangle(
        Point(x * TILE_SIZE, y * TILE_SIZE), 
        Point((x+1) * TILE_SIZE, (y+1) * TILE_SIZE)
    )
    block.draw(window)
    block.setFill(SNAKE_COLOR)

def drawSnake(snakeBlocks, window):
    for block in snakeBlocks:
        drawBlock(block[0], block[1], window)


def play():
    window = initializeWindow()
    snakeBlocks = initializeSnake()
    drawSnake(snakeBlocks, window)

    
    window.getMouse()








if __name__ == '__main__':
    play()