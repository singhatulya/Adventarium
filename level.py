import pygame
class level1:
    def __init__(self):
        self.bg = pygame.image.load("bg1.png").convert()

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.bg, (0,0))

class level2:
    def __init__(self):
        self.bg = pygame.image.load("bg.png").convert()

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.bg, (0,0))