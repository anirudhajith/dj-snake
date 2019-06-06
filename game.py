#! dj-snake

from graphics import *
from random import choice, random

TILE_SIZE = 30                                              # length of a tile in pixels
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
    return window

def initializeSnake():
    initialDirection = choice(directions)
    head = STARTING_POINT
    snakeBlocks = []

    if initialDirection == 'up':
        for offset in range(INITIAL_SNAKE_LENGTH):
            snakeBlocks.append(head[0], head[1] - offset)
    elif initialDirection == 'down':
        for offset in range(INITIAL_SNAKE_LENGTH):
            snakeBlocks.append(head[0], head[1] + offset)
    elif initialDirection == 'right':
        for offset in range(INITIAL_SNAKE_LENGTH):
            snakeBlocks.append(head[0] - offset, head[1])
    elif initialDirection == 'left':
        for offset in range(INITIAL_SNAKE_LENGTH):
            snakeBlocks.append(head[0] + offset, head[1])

    return snakeBlocks


def play():
    window = initializeWindow()
    window.getMouse()







if __name__ == '__main__':
    play()