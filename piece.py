import pygame

class Piece(object):
    
    king = pygame.image.load("images/wking.png").convert_alpha()
    
    def __init__(self, pos):
        self.pos = pos
        

    def draw(self, surface):
        surface.blit(Piece.king,(0,0))