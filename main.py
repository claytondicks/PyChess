import pygame, sys
from board import Board

pygame.init()
screenSize = (640, 640)
surface = pygame.display.set_mode(screenSize)


theBoard = Board()

while True:
    surface.fill((0,0,0))
    
    theBoard.draw(surface)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()   #quit pygame
                sys.exit()      #exit the game