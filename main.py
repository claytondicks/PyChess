import pygame
from gameManager import GameManager


pygame.init()
screenSize = (400, 400)
surface = pygame.display.set_mode(screenSize)

theGame = GameManager(surface)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    
    theGame.draw()    
    theGame.doTurn()