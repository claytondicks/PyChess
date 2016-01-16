import pygame, sys
from grid import Grid

pygame.init()
screenSize = (640, 640)
surface = pygame.display.set_mode(screenSize)


theGrid = Grid()

while True:
    surface.fill((0,0,0))
    
    theGrid.draw(surface)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()   #quit pygame
                sys.exit()      #exit the game