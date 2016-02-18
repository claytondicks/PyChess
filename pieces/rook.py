'''
Created on Jan 23, 2016

@author: clayton
'''
import pygame


from piece import Piece
from util.directions import Directions

class Rook(Piece):
    
    def __init__(self, pos, board, player):
        Piece.__init__(self, pos, board, player)
        
        self.directions = Directions.straight
        
        if self.player.colour == 0:
            self.img = pygame.image.load("images/wrook.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/brook.png").convert_alpha()
        
    def getMoves(self, pos, direction):        
        cell = self.board.getCellFromPos(pos) 
        
        if not cell:
            return
               
        
        for piece in self.board.pieces:
            if piece.pos == cell.pos:
                if self.isMine(self.player) and piece != self:
                    return 
                if piece.player != self.player:
                    return self.validMoves.append(cell)
                
                
        
        pos += direction
        self.validMoves.append(cell)
        return self.getMoves(pos,direction)
    
    def getValidMoves(self):
        for direction in self.directions:
            self.getMoves(self.pos, direction)
            
        return self.validMoves           
