import pygame
pygame.init()
screenSize = (640, 420)
surface = pygame.display.set_mode(screenSize)


while True:

    surface.fill((0,0,0))
    pygame.display.flip()
    pygame.event.wait()