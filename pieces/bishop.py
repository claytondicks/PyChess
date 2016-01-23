'''
Created on Jan 23, 2016

@author: clayton
'''
import pygame


from piece import Piece

class Bishop(Piece):
    
    def __init__(self, pos, grid, player):
        Piece.__init__(self, pos, grid, player)
        if self.player.colour == 1:
            self.img = pygame.image.load("images/wbishop.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/bbishop.png").convert_alpha()
        
    
