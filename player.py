'''
Created on Jan 20, 2016

@author: clayton
'''
import pygame, sys


class Player(object):

    def __init__(self, colour, board):
        self.colour = colour   
        self.board = board
    
    def turn(self):
        
        LEFT = 1
        RIGHT = 3
        
        event = pygame.event.get()
        
        for e in event:
            point = pygame.mouse.get_pos()
            
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == LEFT:
                self.board.clearSelection()
                piece = self.board.getPieceFrompoint(point)
                if piece is None:
                    return             
                
                if piece.belongsTo(self):
                    piece.selected = True                                             

                        
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == RIGHT:
                for piece in self.board.pieces:
                    if piece.selected == True and piece.isValidMove(point):
                        piece.move(point)
                        piece.selected = None
                        piece.validMoves = []
                        return True
                            
                
        return False