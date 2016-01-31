'''
Created on Jan 23, 2016

@author: clayton
'''
import pygame
from vec2 import Vector2

from piece import Piece

class Pawn(Piece):
    
    def __init__(self, pos, grid, player):
        Piece.__init__(self, pos, grid, player)
        
        if self.player.colour == 0:
            self.img = pygame.image.load("images/wpawn.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/bpawn.png").convert_alpha()
            
            
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
    
    
    def getValidMoves(self):
        diff = Vector2(0, self.grid.cellsize)
        diff2 = Vector2(0, self.grid.cellsize + self.grid.cellsize)
        
        if self.player.colour == 0:
            theMove = self.pos - diff
        else:
            theMove = self.pos + diff

        self.validMoves.append(theMove)
        
        if self.firstMove:
            if self.player.colour == 0:
                theMove2 = self.pos - diff2
            else:
                theMove2 = self.pos + diff2
        
        self.validMoves.append(theMove2)
        
        for piece in self.player.piecesManager.thePieces:
            for move in self.validMoves:
                if piece.pos == move:
                    self.validMoves.remove(move)
        
        return self.validMoves