'''
Created on Jan 23, 2016

@author: clayton
'''
import pygame


from piece import Piece

class Queen(Piece):
    
    def __init__(self, pos, grid, player):
        Piece.__init__(self, pos, grid, player)
        if self.player.colour == 0:
            self.img = pygame.image.load("images/wqueen.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/bqueen.png").convert_alpha()
        
    