'''
Created on Jan 23, 2016

@author: clayton
'''
import pygame


from piece import Piece
from util.directions import Directions

class Bishop(Piece):
    
    def __init__(self, pos, grid, player):
        Piece.__init__(self, pos, grid, player)
        
        self.directions = Directions.diagonals
                
        if self.player.colour == 0:
            self.img = pygame.image.load("images/wbishop.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/bbishop.png").convert_alpha()