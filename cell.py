import pygame


class Cell(object):

    size = 80

    def __init__(self, rect, pos):

        self.rect = rect
        self.pos = pos
        
        self.width = self.rect.width
        self.height = self.rect.height

        self.cellSurface = pygame.Surface((self.width , self.height))
    
    def draw(self, surface, state):
        
        if state % 2 == 0:
            self.cellSurface.fill((255,255,255))
        else:
            self.cellSurface.fill((128,128,128))
        surface.blit(self.cellSurface, (self.rect.left, self.rect.top))