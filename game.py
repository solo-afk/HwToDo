import pygame, sys
import random
from pygame.math import Vector2

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
pos = Vector2(400,400)
wallrightpos = Vector2(430,0)
wallleftpos = Vector2(-370,0)
wallleft = pygame.Rect(wallleftpos.x, wallleftpos.y,800,70)
wallright = pygame.Rect(wallrightpos.x, wallrightpos.y,800,70)
startpos = random.randint(0,400)
gapwidth = random.randint(60,170)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if pos.y != 0:
            pos.y -= 5
    if keys[pygame.K_DOWN]:
        if pos.y != 800:
            pos.y += 5
    if keys[pygame.K_RIGHT]:
        if pos.x != 800:   
            pos.x += 5
    if keys[pygame.K_LEFT]:
        if pos.x != 0:
            pos.x -= 5
    
    if wallleftpos.y == 800:
        startpos = random.randint(70,730)
        gapwidth = random.randint(60,170)
        wallleftpos.y = 0
        wallrightpos.y = 0
    
    if wallleftpos.y == pos.y:
        wallleftpos.y += 5
    
    if wallrightpos.y == pos.y:
        wallleftpos.y += 5
    wallrightpos.y += 5
    wallleftlen = startpos - gapwidth
    wallrightpos.x = startpos
    wallleft = pygame.Rect(0, wallleftpos.y, wallleftlen , 70)
    wallright = pygame.Rect(wallrightpos.x ,wallrightpos.y, 800, 70)
    
    
    screen.fill((100,50,150))
    pygame.draw.circle(screen, (0,0,0), (pos.x, pos.y), 10)
    pygame.draw.rect(screen, (50,50,50), wallleft)
    pygame.draw.rect(screen, (50,50,50), wallright)
    pygame.display.update()
    clock.tick(60)

    