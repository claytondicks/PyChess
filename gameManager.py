'''
Created on Jan 17, 2016

@author: clayton
'''

import pygame


from pieces import *
from board.grid import Grid
from player import Player
from vec2 import Vector2


WHT = 1
BLK = 0

class GameManager(object):
    
    def __init__(self):
        pygame.display.set_caption('Pygame Chess')
        self.grid = Grid()
        self.piecesManager = PiecesManager()
        self.whitePlayer = Player(WHT)
        self.blackPlayer = Player(BLK)
        
        self.buildBoard()
    
    def draw(self, surface):
        self.grid.draw(surface)
        self.piecesManager.draw(surface)
        
        pygame.display.flip()
        
        
    def buildBoard(self):
        
        ##White side
        self.whiteKing = King(Vector2(560,240), self.grid, self.whitePlayer)
        self.whiteQueen = Queen(Vector2(560,320), self.grid, self.whitePlayer)
        self.whiteRook = Rook(Vector2(560,0), self.grid, self.whitePlayer)
        self.whiteRook2 = Rook(Vector2(560,560), self.grid, self.whitePlayer)
        self.whiteBishop = Bishop(Vector2(560,160), self.grid, self.whitePlayer)
        self.whiteBishop2 = Bishop(Vector2(560,400), self.grid, self.whitePlayer)
        self.whiteKnight = Knight(Vector2(560,80), self.grid, self.whitePlayer)
        self.whiteKnight2 = Knight(Vector2(560,480), self.grid, self.whitePlayer)
        self.whitePawn = Pawn(Vector2(480,0), self.grid, self.whitePlayer)
        self.whitePawn2 = Pawn(Vector2(480,80), self.grid, self.whitePlayer)
        self.whitePawn3 = Pawn(Vector2(480,160), self.grid, self.whitePlayer)
        self.whitePawn4 = Pawn(Vector2(480,240), self.grid, self.whitePlayer)
        self.whitePawn5= Pawn(Vector2(480,320), self.grid, self.whitePlayer)
        self.whitePawn6 = Pawn(Vector2(480,400), self.grid, self.whitePlayer)
        self.whitePawn7 = Pawn(Vector2(480,480), self.grid, self.whitePlayer)
        self.whitePawn8 = Pawn(Vector2(480,560), self.grid, self.whitePlayer)
        
        self.piecesManager.thePieces.append(self.whiteKing)
        self.piecesManager.thePieces.append(self.whiteQueen)
        self.piecesManager.thePieces.append(self.whiteRook)
        self.piecesManager.thePieces.append(self.whiteRook2)
        self.piecesManager.thePieces.append(self.whiteBishop)
        self.piecesManager.thePieces.append(self.whiteBishop2)
        self.piecesManager.thePieces.append(self.whiteKnight)
        self.piecesManager.thePieces.append(self.whiteKnight2)
        self.piecesManager.thePieces.append(self.whitePawn)
        self.piecesManager.thePieces.append(self.whitePawn2)
        self.piecesManager.thePieces.append(self.whitePawn3)
        self.piecesManager.thePieces.append(self.whitePawn4)
        self.piecesManager.thePieces.append(self.whitePawn5)
        self.piecesManager.thePieces.append(self.whitePawn6)
        self.piecesManager.thePieces.append(self.whitePawn7)
        self.piecesManager.thePieces.append(self.whitePawn8)
        
        
        ##Black side
        self.blackKing = King(Vector2(0,240), self.grid, self.blackPlayer)
        self.blackQueen = Queen(Vector2(0,320), self.grid, self.blackPlayer)
        self.blackRook = Rook(Vector2(0,0), self.grid, self.blackPlayer)
        self.blackRook2 = Rook(Vector2(0,560), self.grid, self.blackPlayer)
        self.blackBishop = Bishop(Vector2(0,160), self.grid, self.blackPlayer)
        self.blackBishop2 = Bishop(Vector2(0,400), self.grid, self.blackPlayer)
        self.blackKnight = Knight(Vector2(0,80), self.grid, self.blackPlayer)
        self.blackKnight2 = Knight(Vector2(0,480), self.grid, self.blackPlayer)
        self.blackPawn = Pawn(Vector2(80,0), self.grid, self.blackPlayer)
        self.blackPawn2 = Pawn(Vector2(80,80), self.grid, self.blackPlayer)
        self.blackPawn3 = Pawn(Vector2(80,160), self.grid, self.blackPlayer)
        self.blackPawn4 = Pawn(Vector2(80,240), self.grid, self.blackPlayer)
        self.blackPawn5= Pawn(Vector2(80,320), self.grid, self.blackPlayer)
        self.blackPawn6 = Pawn(Vector2(80,400), self.grid, self.blackPlayer)
        self.blackPawn7 = Pawn(Vector2(80,480), self.grid, self.blackPlayer)
        self.blackPawn8 = Pawn(Vector2(80,560), self.grid, self.blackPlayer)
        
        self.piecesManager.thePieces.append(self.blackKing)
        self.piecesManager.thePieces.append(self.blackQueen)
        self.piecesManager.thePieces.append(self.blackRook)
        self.piecesManager.thePieces.append(self.blackRook2)
        self.piecesManager.thePieces.append(self.blackBishop)
        self.piecesManager.thePieces.append(self.blackBishop2)
        self.piecesManager.thePieces.append(self.blackKnight)
        self.piecesManager.thePieces.append(self.blackKnight2)
        self.piecesManager.thePieces.append(self.blackPawn)
        self.piecesManager.thePieces.append(self.blackPawn2)
        self.piecesManager.thePieces.append(self.blackPawn3)
        self.piecesManager.thePieces.append(self.blackPawn4)
        self.piecesManager.thePieces.append(self.blackPawn5)
        self.piecesManager.thePieces.append(self.blackPawn6)
        self.piecesManager.thePieces.append(self.blackPawn7)
        self.piecesManager.thePieces.append(self.blackPawn8)
    