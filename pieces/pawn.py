'''
Created on Jan 23, 2016

@author: clayton
'''
import pygame


from piece import Piece

class Pawn(Piece):
    
    def __init__(self, pos, grid, player):
        Piece.__init__(self, pos, grid, player)
        if self.player.colour == 1:
            self.img = pygame.image.load("images/wpawn.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/bpawn.png").convert_alpha()
        
    