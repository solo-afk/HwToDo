import pygame, sys, time

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
player = pygame.Rect(50, 450, 50, 50)
floor = pygame.Rect(0,500, 800, 150)
gravity = 5
velocity = 0

#OBSTACLES
obstacle1 = pygame.Rect(800,460, 40,40)

#BACKGROUNDS
clouds = pygame.image.load("/Users/solo/Desktop/VS code projects/clouds-clipart-lg.png")
clouds = pygame.transform.scale(clouds, (200,120))
rect1 = pygame.Rect(500,20 ,200,120)
rect2 = pygame.Rect(5, 100, 200, 120)
#rect3 = pygame.Rect(600, 200, 200, 120)

#trees = pygame.image.load("/Users/solo/Desktop/VS code projects/sakura tree.jpeg")

jumping = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.bottom == floor.top and not jumping:
                    velocity = -40
                    jumping = True
            
                

    
    screen.fill((90,150,200)) 
    pygame.draw.rect(screen, "blue", player)
    pygame.draw.rect(screen, (50,50,50), floor)

    
    
    pygame.draw.rect(screen, (90,150,200), rect1 )
    screen.blit(clouds, (rect1.x,rect1.y))

    pygame.draw.rect(screen, (90,150,200), rect2 )
    screen.blit(clouds, (rect2.x,rect2.y))
    """
    pygame.draw.rect(screen, "blue", rect3 )
    screen.blit(clouds, (rect3.x,rect3.y))
    """ 
    
    
#JUMPING
    if velocity < 0:
        player.y += velocity
        velocity += gravity
    if player.bottom != floor.top:
        player.y += gravity
        jumping = False

#NON PLAYER MOVEMENT
    obstacle1.x -= 5
    pygame.draw.rect(screen, "red", obstacle1)
    if obstacle1.right < 0:
        obstacle1.x = 800

    rect1.x -= 3
    if rect1.right < 0:
        rect1.left = 800
    
    rect2.x -= 3
    if rect2.right < 0:
        rect2.left = 800
    
    """
    rect3.x -= 5
    if rect3.right < 0:
        rect3.right = 800
    """

    #screen.blit(trees, (0,0))

    #COLLISION


    
    
    pygame.display.update()
    clock.tick(60)
