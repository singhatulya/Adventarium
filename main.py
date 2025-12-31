import pygame
import time

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Adventarium")
screen = pygame.display.set_mode((1280, 720))
running = True

background = pygame.image.load("bg.png").convert()
player_right = pygame.image.load("p_right.png")
player_right = pygame.transform.scale(player_right, (80,80))
shadow = pygame.image.load("shadow.png")
shadow = pygame.transform.scale(shadow, (90,20))

prx = 20
pry = 20

v = 0
ease = 0.2
maximum = 5
target = 0

vy = 0
easey = 0.3
maximumy = 5
targety = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        target = -maximum
    elif key[pygame.K_RIGHT] or key[pygame.K_d]:
        target = maximum
    else:
        target = 0

    if key[pygame.K_DOWN] or key[pygame.K_s]:
        targety = maximumy
    elif key[pygame.K_UP] or key[pygame.K_w]:
        targety = -maximumy
    else:
        targety = 0


    v += (target - v) * ease 
    prx += v
    vy += (targety - vy) * easey
    pry += vy

    screen.blit(background, (0,0))
    screen.blit(shadow, (prx - 5, pry + 65))
    screen.blit(player_right, (prx,pry))
    
    pygame.display.flip()
    clock.tick(75)

pygame.quit()
