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
        
        self.players = {}
        
        self.players[WHT] = Player(WHT, self.piecesManager)
        self.players[BLK] = Player(BLK, self.piecesManager)
        self.turn = WHT
        
        self.buildBoard()
    
    def draw(self, surface):
        self.grid.draw(surface)
        self.piecesManager.draw(surface)
        
        pygame.display.flip()
        
    def doTurn(self):
        if self.players[self.turn].turn():
            self.turn = not self.turn
            return self.getWinner()
        
        return None
        
        
    def getWinner(self):
        return None    
          
    def buildBoard(self):
        
        ##White side
        self.whiteKing = King(Vector2(320,560), self.grid, self.players[WHT])
        self.whiteQueen = Queen(Vector2(240,560), self.grid, self.players[WHT])
        self.whiteRook = Rook(Vector2(0, 560), self.grid, self.players[WHT])
        self.whiteRook2 = Rook(Vector2(560,560), self.grid, self.players[WHT])
        self.whiteBishop = Bishop(Vector2(160, 560), self.grid, self.players[WHT])
        self.whiteBishop2 = Bishop(Vector2(400, 560), self.grid, self.players[WHT])
        self.whiteKnight = Knight(Vector2(80, 560), self.grid, self.players[WHT])
        self.whiteKnight2 = Knight(Vector2(480, 560), self.grid, self.players[WHT])
        self.whitePawn = Pawn(Vector2(0, 480), self.grid, self.players[WHT])
        self.whitePawn2 = Pawn(Vector2(80, 480), self.grid, self.players[WHT])
        self.whitePawn3 = Pawn(Vector2(160, 480), self.grid, self.players[WHT])
        self.whitePawn4 = Pawn(Vector2(240, 480), self.grid, self.players[WHT])
        self.whitePawn5= Pawn(Vector2(320, 480), self.grid, self.players[WHT])
        self.whitePawn6 = Pawn(Vector2(400, 480), self.grid, self.players[WHT])
        self.whitePawn7 = Pawn(Vector2(480,480), self.grid, self.players[WHT])
        self.whitePawn8 = Pawn(Vector2(560, 480), self.grid, self.players[WHT])
         
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
        self.blackKing = King(Vector2(320, 0), self.grid, self.players[BLK])
        self.blackQueen = Queen(Vector2(240, 0), self.grid, self.players[BLK])
        self.blackRook = Rook(Vector2(0,0), self.grid, self.players[BLK])
        self.blackRook2 = Rook(Vector2(560, 0), self.grid, self.players[BLK])
        self.blackBishop = Bishop(Vector2(160, 0), self.grid, self.players[BLK])
        self.blackBishop2 = Bishop(Vector2(400, 0), self.grid, self.players[BLK])
        self.blackKnight = Knight(Vector2(80, 0), self.grid, self.players[BLK])
        self.blackKnight2 = Knight(Vector2(480, 0), self.grid, self.players[BLK])
        self.blackPawn = Pawn(Vector2(0, 80), self.grid, self.players[BLK])
        self.blackPawn2 = Pawn(Vector2(80, 80), self.grid, self.players[BLK])
        self.blackPawn3 = Pawn(Vector2(160, 80), self.grid, self.players[BLK])
        self.blackPawn4 = Pawn(Vector2(240, 80), self.grid, self.players[BLK])
        self.blackPawn5= Pawn(Vector2(320, 80), self.grid, self.players[BLK])
        self.blackPawn6 = Pawn(Vector2(400, 80), self.grid, self.players[BLK])
        self.blackPawn7 = Pawn(Vector2(480, 80), self.grid, self.players[BLK])
        self.blackPawn8 = Pawn(Vector2(560, 80), self.grid, self.players[BLK])
         
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
    