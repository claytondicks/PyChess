'''
Created on Jan 17, 2016

@author: clayton
'''

import pygame

from board.gameBoard import Board

from player import Player
from util.vec2 import Vector2
from pieces import *


WHT = 0
BLK = 1

class GameManager(object):
    
    def __init__(self, surface):
        pygame.display.set_caption('Pygame Chess')

        self.surface = surface
        self.board = Board()
        self.players = {}
        
        self.players[WHT] = Player(WHT, self.board)
        self.players[BLK] = Player(BLK, self.board)
        self.turn = WHT
        
        self.buildBoard()
    
    def draw(self):
        self.board.draw(self.surface)
        
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
        self.whiteKing = King(Vector2(320,560), self.board, self.players[WHT])
        self.whiteQueen = Queen(Vector2(240,560), self.board, self.players[WHT])
        self.whiteRook = Rook(Vector2(0, 560), self.board, self.players[WHT])
        self.whiteRook2 = Rook(Vector2(560,560), self.board, self.players[WHT])
        self.whiteBishop = Bishop(Vector2(160, 560), self.board, self.players[WHT])
        self.whiteBishop2 = Bishop(Vector2(400, 560), self.board, self.players[WHT])
        self.whiteKnight = Knight(Vector2(80, 560), self.board, self.players[WHT])
        self.whiteKnight2 = Knight(Vector2(480, 560), self.board, self.players[WHT])
        self.whitePawn = Pawn(Vector2(0, 480), self.board, self.players[WHT])
        self.whitePawn2 = Pawn(Vector2(80, 480), self.board, self.players[WHT])
        self.whitePawn3 = Pawn(Vector2(160, 480), self.board, self.players[WHT])
        self.whitePawn4 = Pawn(Vector2(240, 480), self.board, self.players[WHT])
        self.whitePawn5= Pawn(Vector2(320, 480), self.board, self.players[WHT])
        self.whitePawn6 = Pawn(Vector2(400, 480), self.board, self.players[WHT])
        self.whitePawn7 = Pawn(Vector2(480,480), self.board, self.players[WHT])
        self.whitePawn8 = Pawn(Vector2(560, 480), self.board, self.players[WHT])
#           
        self.board.pieces.add(self.whiteKing)
        self.board.pieces.add(self.whiteQueen)
        self.board.pieces.add(self.whiteRook)
        self.board.pieces.add(self.whiteRook2)
        self.board.pieces.add(self.whiteBishop)
        self.board.pieces.add(self.whiteBishop2)
        self.board.pieces.add(self.whiteKnight)
        self.board.pieces.add(self.whiteKnight2)
        self.board.pieces.add(self.whitePawn)
        self.board.pieces.add(self.whitePawn2)
        self.board.pieces.add(self.whitePawn3)
        self.board.pieces.add(self.whitePawn4)
        self.board.pieces.add(self.whitePawn5)
        self.board.pieces.add(self.whitePawn6)
        self.board.pieces.add(self.whitePawn7)
        self.board.pieces.add(self.whitePawn8)
           
           
        ##Black side
        self.blackKing = King(Vector2(320, 0), self.board, self.players[BLK])
        self.blackQueen = Queen(Vector2(240, 0), self.board, self.players[BLK])
        self.blackRook = Rook(Vector2(0,0), self.board, self.players[BLK])
        self.blackRook2 = Rook(Vector2(560, 0), self.board, self.players[BLK])
        self.blackBishop = Bishop(Vector2(160, 0), self.board, self.players[BLK])
        self.blackBishop2 = Bishop(Vector2(400, 0), self.board, self.players[BLK])
        self.blackKnight = Knight(Vector2(80, 0), self.board, self.players[BLK])
        self.blackKnight2 = Knight(Vector2(480, 0), self.board, self.players[BLK])
        self.blackPawn = Pawn(Vector2(0, 80), self.board, self.players[BLK])
        self.blackPawn2 = Pawn(Vector2(80, 80), self.board, self.players[BLK])
        self.blackPawn3 = Pawn(Vector2(160, 80), self.board, self.players[BLK])
        self.blackPawn4 = Pawn(Vector2(240, 80), self.board, self.players[BLK])
        self.blackPawn5= Pawn(Vector2(320, 80), self.board, self.players[BLK])
        self.blackPawn6 = Pawn(Vector2(400, 80), self.board, self.players[BLK])
        self.blackPawn7 = Pawn(Vector2(480, 80), self.board, self.players[BLK])
        self.blackPawn8 = Pawn(Vector2(560, 80), self.board, self.players[BLK])
           
        self.board.pieces.add(self.blackKing)
        self.board.pieces.add(self.blackQueen)
        self.board.pieces.add(self.blackRook)
        self.board.pieces.add(self.blackRook2)
        self.board.pieces.add(self.blackBishop)
        self.board.pieces.add(self.blackBishop2)
        self.board.pieces.add(self.blackKnight)
        self.board.pieces.add(self.blackKnight2)
        self.board.pieces.add(self.blackPawn)
        self.board.pieces.add(self.blackPawn2)
        self.board.pieces.add(self.blackPawn3)
        self.board.pieces.add(self.blackPawn4)
        self.board.pieces.add(self.blackPawn5)
        self.board.pieces.add(self.blackPawn6)
        self.board.pieces.add(self.blackPawn7)
        self.board.pieces.add(self.blackPawn8)   