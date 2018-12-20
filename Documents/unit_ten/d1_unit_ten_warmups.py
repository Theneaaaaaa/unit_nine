import pygame, sys
from pygame.locals import *


pygame.init()
mainSurface = pygame.display.set_mode((600, 500), 0, 32)
pygame.display.set_captain("Pygame Test Window")

while True:
    for event in pygame.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
