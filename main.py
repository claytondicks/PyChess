import pygame
from gameManager import GameManager


pygame.init()
screenSize = (640, 640)
surface = pygame.display.set_mode(screenSize)

theGame = GameManager()

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    
    theGame.draw(surface)    
    theGame.doTurn()