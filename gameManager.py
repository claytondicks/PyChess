'''
Created on Jan 17, 2016

@author: clayton
'''

import pygame
from grid import Grid
from pieces.piecesManager import PiecesManager

class GameManager(object):
    
    def __init__(self):
        pygame.display.set_caption('Pygame Chess')
        self.grid = Grid()
        self.piecesManager = PiecesManager(self.grid)
    
    
    def draw(self, surface):
        self.grid.draw(surface)
        self.piecesManager.draw(surface)
        
        pygame.display.flip()