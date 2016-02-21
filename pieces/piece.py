'''
Created on Jan 17, 2016

@author: clayton
'''
import pygame


class Piece(object):
    
    
    def __init__(self, pos, board, player):
        self.pos = pos
        self.board = board
        self.player = player
        self.img = None
        self.selected = None
        self.validMoves = []
        self.firstMove = True
        self.directions = []

    def draw(self, surface):
        cell = self.board.getCellFromPos(self.pos) 
        
#         if self.selected:
#             pygame.draw.rect(surface, (0,255,0), cell.rect, 5)
        

        surface.blit(self.img, (cell.rect.left, cell.rect.top))
            
        
    def isClicked(self, point):
        cell = self.board.getCellFromPos(self.pos)
        return cell.rect.collidepoint(point)
    
    def isMine(self, player):
        if player == self.player:
            return True
        
        return False
    
    def move(self, point):        
        cell = self.board.getCellFromPoint(point)        
        self.pos = cell.pos
               
       
    def isValidMove(self, point):
        cell = self.board.getCellFromPoint(point)
        
        for moves in self.validMoves:
            if moves.pos == cell.pos:
                return True
            
        return False
        
    def getValidMoves(self):
        for name, direction in self.directions.iteritems():
            self.getMoves(self.pos + direction, direction)
            
        return self.validMoves           

    
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