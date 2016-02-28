'''
Created on Jan 23, 2016

@author: clayton
'''
import pygame
from util.directions import Directions

from piece import Piece

class Pawn(Piece):
    
    def __init__(self, pos, board, player):
        Piece.__init__(self, pos, board, player)        
        
        if self.player.colour == 0:
            self.img = pygame.image.load("images/wpawn.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/bpawn.png").convert_alpha()
            
            
    def getValidMoves(self):
        if self.player.colour == 0:
            direction = Directions.straight['North']
        else:
            direction = Directions.straight['South']
        
        oneMove = self.pos + direction
        cell = self.board.getCellFromPos(oneMove) 
        
        if not cell:
            return
               
        self.validMoves.append(cell)
        
        if self.firstMove:
            twoMove = oneMove + direction
            cell2 = self.board.getCellFromPos(twoMove) 
            if not cell2:
                return
            
            self.validMoves.append(cell2)
        
            
        for move in self.validMoves:
            piece = self.board.getPieceFromPos(move.pos)
            if piece:
                if self.belongsTo(self.player) and piece != self:
                        self.validMoves.remove(move)    
                        
                          
        
        return self.validMoves