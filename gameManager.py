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
        
        ##white side
        self.whiteKing = King(Vector2(3, 7), self.board, self.players[WHT])
        self.whiteQueen = Queen(Vector2(4, 7), self.board, self.players[WHT])
        self.whiteRook = Rook(Vector2(0,7), self.board, self.players[WHT])
        self.whiteRook2 = Rook(Vector2(7, 7), self.board, self.players[WHT])
        self.whiteBishop = Bishop(Vector2(2, 7), self.board, self.players[WHT])
        self.whiteBishop2 = Bishop(Vector2(5, 7), self.board, self.players[WHT])
        self.whiteKnight = Knight(Vector2(1, 7), self.board, self.players[WHT])
        self.whiteKnight2 = Knight(Vector2(6, 7), self.board, self.players[WHT])
        self.whitePawn = Pawn(Vector2(0, 6), self.board, self.players[WHT])
        self.whitePawn2 = Pawn(Vector2(1, 6), self.board, self.players[WHT])
        self.whitePawn3 = Pawn(Vector2(2, 6), self.board, self.players[WHT])
        self.whitePawn4 = Pawn(Vector2(3, 6), self.board, self.players[WHT])
        self.whitePawn5= Pawn(Vector2(4, 6), self.board, self.players[WHT])
        self.whitePawn6 = Pawn(Vector2(5, 6), self.board, self.players[WHT])
        self.whitePawn7 = Pawn(Vector2(6, 6), self.board, self.players[WHT])
        self.whitePawn8 = Pawn(Vector2(7, 6 ), self.board, self.players[WHT])
             
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
        
        
        ##black side
        self.blackKing = King(Vector2(3,0), self.board, self.players[BLK])
        self.blackQueen = Queen(Vector2(4,0), self.board, self.players[BLK])
        self.blackRook = Rook(Vector2(0, 0), self.board, self.players[BLK])
        self.blackRook2 = Rook(Vector2(7,0), self.board, self.players[BLK])
        self.blackBishop = Bishop(Vector2(2, 0), self.board, self.players[BLK])
        self.blackBishop2 = Bishop(Vector2(5, 0), self.board, self.players[BLK])
        self.blackKnight = Knight(Vector2(6, 0), self.board, self.players[BLK])
        self.blackKnight2 = Knight(Vector2(1, 0), self.board, self.players[BLK])
        self.blackPawn = Pawn(Vector2(0, 1), self.board, self.players[BLK])
        self.blackPawn2 = Pawn(Vector2(1, 1), self.board, self.players[BLK])
        self.blackPawn3 = Pawn(Vector2(2, 1), self.board, self.players[BLK])
        self.blackPawn4 = Pawn(Vector2(3, 1), self.board, self.players[BLK])
        self.blackPawn5= Pawn(Vector2(4, 1), self.board, self.players[BLK])
        self.blackPawn6 = Pawn(Vector2(5, 1), self.board, self.players[BLK])
        self.blackPawn7 = Pawn(Vector2(6,1), self.board, self.players[BLK])
        self.blackPawn8 = Pawn(Vector2(7, 1), self.board, self.players[BLK])
           
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