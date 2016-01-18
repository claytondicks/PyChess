'''
Created on Jan 17, 2016

@author: clayton
'''
from pieces.piece import Piece
from vec2 import Vector2

class PiecesManager(object):

    def __init__(self, grid):
        self.grid = grid
        self.thePieces = []
        self.kingPiece = Piece(Vector2(160,0), self.grid)
        self.thePieces.append(self.kingPiece)
     
    def add(self, piece):
        self.thePieces.append(piece) 
    
    
    def draw(self, surface):
        for piece in self.thePieces:
            piece.draw(surface)