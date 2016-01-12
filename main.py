import pygame, sys
from board import Board

pygame.init()
screenSize = (640, 640)
surface = pygame.display.set_mode(screenSize)


theBoard = Board()

e = 0
while True:
    surface.fill((0,0,0))
    

    for cell in theBoard.getBoard():
        e += 1
        if e % 9 == 0:
            e += 1
        cell.draw(surface, e)

    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()   #quit pygame
                sys.exit()      #exit the game