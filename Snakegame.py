import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]

    def drawSnake(self):
        for block in self.body:
            #create a rect
            snakeRect = pygame.Rect(int(block.x * cellSize), int(block.y * cellSize), cellSize, cellSize)
            pygame.draw.rect(screen, (50,180,200), snakeRect)
            #draw the rectangle

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cellNumber - 1)
        self.y = random.randint(0, cellNumber - 1)
        self.pos = Vector2(self.x, self.y)
        #create an x and y position
        #draw a square
    
    def drawFruit(self):
        #create recatngle in correct pos
        fruit_rect = pygame.Rect(int(self.pos.x * cellSize), int(self.pos.y * cellSize), cellSize, cellSize)
        #draw the rectangle
        pygame.draw.rect(screen, (240,100,70), fruit_rect)

#starts the pygame module
pygame.init()
cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellNumber * cellSize, cellNumber * cellSize)) #sets the screen size to the exact number of cells
clock = pygame.time.Clock() #clock object caps how fast the game runs; keep it consitent

fruit = FRUIT()
snake = SNAKE()

#create game loop, so the screen will stay up
while True:
    for event in pygame.event.get(): #event loop, to check for actions
        if event.type == pygame.QUIT:
            pygame.quit() #quits but some other things may still be running
            sys.exit() #amkes sure everyhting is closed
    
   
    screen.fill((150,210,100))
    fruit.drawFruit()
    snake.drawSnake()
    pygame.display.update() #display the screen and changes made
    clock.tick(60)
    
    


