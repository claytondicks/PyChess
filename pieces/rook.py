'''
Created on Jan 23, 2016

@author: clayton
'''
import pygame


from piece import Piece

class Rook(Piece):
    
    def __init__(self, pos, grid, player):
        Piece.__init__(self, pos, grid, player)
        
        if self.player.colour == 0:
            self.img = pygame.image.load("images/wrook.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/brook.png").convert_alpha()
        
    def getValidMoves(self):
        for cell in self.grid.grid:
            if cell.pos.x - self.pos.x == 0:
                self.validMoves.append(cell.pos)
                
            if cell.pos.y - self.pos.y == 0:
                self.validMoves.append(cell.pos)
            
        return self.validMoves