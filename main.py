import pygame, sys
from gameManager import GameManager


pygame.init()
screenSize = (640, 640)
surface = pygame.display.set_mode(screenSize)

theGame = GameManager()



while True:
    surface.fill((0,0,0))
    
    theGame.draw(surface)    
    theGame.doTurn()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()   #quit pygame
                sys.exit()      #exit the game