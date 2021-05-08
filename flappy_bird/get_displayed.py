import pygame
import sys
pygame.init()

breadth = 574
length = int(0.8*breadth)
screen = pygame.display.set_mode((length, breadth))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


