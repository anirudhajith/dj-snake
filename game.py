#! dj-snake

from graphics import *
from random import choice
import threading

TILE_SIZE = 20                                              # length of a tile in pixels
BOARD_LENGTH = 40                                           # number of tiles to a side of the entire board
BACKGROUND_COLOR = color_rgb(128,128,200)                   # board background color
SNAKE_COLOR = color_rgb(255,255,255)                        # snake body color
INITIAL_SNAKE_LENGTH = 3                                    # snake body length at the start of the game
STARTING_POINT = (BOARD_LENGTH // 2, BOARD_LENGTH // 2)     # initial position of snake head

directions = [
    'up', 'down', 'left', 'right'
]

class Block:
    coordinates = None
    rectangle = None

    def __init__(self, x, y, window):
        self.coordinates = (x,y)

        self.rectangle = Rectangle(
            Point(x * TILE_SIZE, y * TILE_SIZE), 
            Point((x+1) * TILE_SIZE, (y+1) * TILE_SIZE)
        )

        self.rectangle.setFill(SNAKE_COLOR)
        self.rectangle.setOutline(BACKGROUND_COLOR)
        self.rectangle.draw(window)
    
    def destroy(self):
        self.rectangle.undraw()
        return self.rectangle

class Snake:
    window = None
    direction = None
    length = None
    blocks = []
    
    def __init__(self, window):
        self.window = window
        self.direction = choice(directions)
        self.length = INITIAL_SNAKE_LENGTH

        head = STARTING_POINT

        if self.direction == 'up':
            for offset in range(INITIAL_SNAKE_LENGTH):
                self.blocks.append(Block(head[0], head[1] - offset, self.window))
        elif self.direction == 'down':
            for offset in range(INITIAL_SNAKE_LENGTH):
                self.blocks.append(Block(head[0], head[1] + offset, self.window))
        elif self.direction == 'right':
            for offset in range(INITIAL_SNAKE_LENGTH):
                self.blocks.append(Block(head[0] - offset, head[1], self.window))
        elif self.direction == 'left':
            for offset in range(INITIAL_SNAKE_LENGTH):
                self.blocks.append(Block(head[0] + offset, head[1], self.window))
    
    def update(self):
        head = self.blocks[0].coordinates

        if self.direction == 'up':
            self.blocks.insert(0, Block(head[0], head[1] - 1, self.window))
        elif self.direction == 'down':
            self.blocks.insert(0, Block(head[0], head[1] + 1, self.window))
        elif self.direction == 'right':
            self.blocks.insert(0, Block(head[0] - 1, head[1], self.window))
        elif self.direction == 'left':
            self.blocks.insert(0, Block(head[0] + 1, head[1], self.window))

        self.blocks[-1].destroy()
        self.blocks.pop()


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


def play():
    window = initializeWindow()
    snake = Snake(window)
    

    
    window.getMouse()







if __name__ == '__main__':
    play()