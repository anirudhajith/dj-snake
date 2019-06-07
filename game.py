#! dj-snake

from graphics import GraphWin, Rectangle, Point, color_rgb
from random import choice, randint
import time

TILE_SIZE = 20                                              # length of a tile in pixels
BOARD_LENGTH = 40                                           # number of tiles to a side of the entire board
BACKGROUND_COLOR = color_rgb(128,128,200)                   # board background color
SNAKE_COLOR = color_rgb(255,255,255)                        # snake body color
FOOD_COLOR = color_rgb(255,0,0)                             # food color
INITIAL_SNAKE_LENGTH = 3                                    # snake body length at the start of the game
STARTING_POINT = (BOARD_LENGTH // 2, BOARD_LENGTH // 2)     # initial position of snake head
UPDATE_INTERVAL = 0.125                                     # time interval between consecutive steps


directions = [
    'Up', 'Down', 'Left', 'Right'
]

class Block:
    coordinates = None
    rectangle = None

    def __init__(self, x, y, window, fill=SNAKE_COLOR):
        self.coordinates = (x,y)

        self.rectangle = Rectangle(
            Point(x * TILE_SIZE, y * TILE_SIZE), 
            Point((x+1) * TILE_SIZE, (y+1) * TILE_SIZE)
        )

        self.rectangle.setFill(fill)
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
    growStep = False
    
    def __init__(self, window):
        self.window = window
        self.direction = choice(directions)
        self.length = INITIAL_SNAKE_LENGTH

        head = STARTING_POINT

        if self.direction == 'Up':
            for offset in range(INITIAL_SNAKE_LENGTH):
                self.blocks.append(Block(head[0], head[1] + offset, self.window))
        elif self.direction == 'Down':
            for offset in range(INITIAL_SNAKE_LENGTH):
                self.blocks.append(Block(head[0], head[1] - offset, self.window))
        elif self.direction == 'Right':
            for offset in range(INITIAL_SNAKE_LENGTH):
                self.blocks.append(Block(head[0] - offset, head[1], self.window))
        elif self.direction == 'Left':
            for offset in range(INITIAL_SNAKE_LENGTH):
                self.blocks.append(Block(head[0] + offset, head[1], self.window))
    
    def changeDirection(self, direction):
        if direction in directions:
            if self.direction == 'Up' and direction != 'Down':
                self.direction = direction
            elif self.direction == 'Down' and direction != 'Up':
                self.direction = direction
            elif self.direction == 'Left' and direction != 'Right':
                self.direction = direction
            elif self.direction == 'Right' and direction != 'Left':
                self.direction = direction
    
    def grow(self):
        self.growStep = True
        
    def update(self):
        head = self.blocks[0].coordinates

        if self.direction == 'Up':
            self.blocks.insert(0, Block(head[0], head[1] - 1, self.window))
        elif self.direction == 'Down':
            self.blocks.insert(0, Block(head[0], head[1] + 1, self.window))
        elif self.direction == 'Right':
            self.blocks.insert(0, Block(head[0] + 1, head[1], self.window))
        elif self.direction == 'Left':
            self.blocks.insert(0, Block(head[0] - 1, head[1], self.window))

        self.blocks[-1].destroy()
        if not self.growStep:
            self.blocks.pop()
        else:
            self.length += 1
            self.growStep = False

class Game:
    window = None
    snake = None
    food = None

    def __init__(self):
        self.window = GraphWin(
            title = "dj-snake", 
            width = TILE_SIZE * BOARD_LENGTH, 
            height = TILE_SIZE * BOARD_LENGTH,
        )
        self.window.setBackground(BACKGROUND_COLOR)

        for x in range(1, BOARD_LENGTH):
            for y in range(1, BOARD_LENGTH):
                self.window.plotPixel(x * TILE_SIZE, y * TILE_SIZE, SNAKE_COLOR)
        
        self.snake = Snake(self.window)
        self.spawnFood()
    
    def spawnFood(self):
        x, y = randint(0, BOARD_LENGTH - 1), randint(0, BOARD_LENGTH - 1)
        while any(block.coordinates == (x,y) for block in self.snake.blocks):
            x, y = randint(0, BOARD_LENGTH), randint(0, BOARD_LENGTH)
        
        self.food = Block(x, y, self.window, FOOD_COLOR)
    
    def checkIllegal(self):
        headCoordinates = self.snake.blocks[0].coordinates
        if any(headCoordinates == block.coordinates for block in self.snake.blocks[1:]):
            return True
        elif any(x < 0 or x >= BOARD_LENGTH for x in headCoordinates):
            return True
        
        return False
        
    def play(self):
        while True:
            time.sleep(UPDATE_INTERVAL)
            self.snake.changeDirection(self.window.checkKey())

            if self.snake.blocks[0].coordinates == self.food.coordinates:
                self.snake.grow()
                self.food.destroy()
                self.spawnFood()
            
            if not self.checkIllegal():
                self.snake.update()
            else:
                break


def main():
    game = Game()
    game.play()
    game.window.getMouse()
    



if __name__ == '__main__':
    main()