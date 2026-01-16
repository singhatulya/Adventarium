# Adventarium. Made by Atulya
import pygame
from level import level1
from level import level2

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("Adventarium")
screen = pygame.display.set_mode((1280, 720))
running = True

player_right = pygame.image.load("p_right.png")
player_right = pygame.transform.scale(player_right, (80, 80))

shadow = pygame.image.load("shadow.png")
shadow = pygame.transform.scale(shadow, (90, 20))

keys = pygame.image.load("key.png")
keys = pygame.transform.scale(keys, (80, 40))

player_rect = player_right.get_rect(topleft=(20, 20))
keys_rect = keys.get_rect(topleft=(150, 347))

vx, vy = 0, 0
ease, easey = 0.2, 0.3
maximum, maximumy = 5, 5
target, targety = 0, 0

l1 = level1()
l2 = level2()

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

    if player_rect.colliderect(keys_rect):
        print("44")
        l2.update()
        l2.draw(screen)
    else:
        l1.update()
        l1.draw(screen)
        print("22")

    vx += (target - vx) * ease
    vy += (targety - vy) * easey
    player_rect.x += vx
    player_rect.y += vy

    
    
    screen.blit(shadow, (player_rect.x - 5, player_rect.y + 65))
    screen.blit(player_right, player_rect.topleft)
    screen.blit(keys, keys_rect.topleft)

    pygame.display.flip()
    clock.tick(75)

pygame.quit()
