'''
Created on Jan 17, 2016

@author: clayton
'''


import pygame

class Piece(object):
    
    
    def __init__(self, pos, grid):
        self.king = pygame.image.load("images/wking.png").convert_alpha()
        self.pos = pos
        self.grid = grid

    def draw(self, surface):
        cell = self.grid.getCellFromPos(self.pos)
        surface.blit(self.king, (cell.rect.left, cell.rect.top))