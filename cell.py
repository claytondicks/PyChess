import pygame


class Cell(object):

    def __init__(self, rect):

        self.rect = rect
        
        self.width = self.rect.width
        self.height = self.rect.height

        self.cellSurface = pygame.Surface((self.width , self.height))
    
    def draw(self, surface, state):
        
        if state % 2 == 0:
            self.cellSurface.fill((255,255,255))
        else:
            self.cellSurface.fill((128,128,128))
        surface.blit(self.cellSurface, (self.rect.left, self.rect.top))