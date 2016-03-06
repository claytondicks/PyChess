import pygame


class Cell(object):

    def __init__(self, rect, pos):

        self.rect = rect
        self.pos = pos
        
#         self.width = self.rect.width
#         self.height = self.rect.height

    
    def draw(self, surface, state):
        
        if state % 2 == 0:
            pygame.draw.rect(surface, (128, 128, 128), self.rect, 0)
        else:
            pygame.draw.rect(surface, (255,255,255), self.rect, 0)
        
        
    def highlight(self, surface, colour, pad):
        pygame.draw.rect(surface, colour, self.rect, pad)