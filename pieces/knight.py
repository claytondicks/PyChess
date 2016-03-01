'''
Created on Jan 23, 2016

@author: clayton
'''
import pygame


from piece import Piece
from util.directions import Directions

class Knight(Piece):
	
	def __init__(self, pos, board, player):
		Piece.__init__(self, pos, board, player)
		
		self.directions = Directions.knight
		
		if self.player.colour == 0:
			self.img = pygame.image.load("images/wknight.png").convert_alpha()
		else:
			self.img = pygame.image.load("images/bknight.png").convert_alpha()
		
	def getValidMoves(self):
		for name, direction in self.directions.iteritems():
			newPos = self.pos + direction
			cell = self.board.getCellFromPos(newPos) 
		
			if not cell:
				continue
				   
			piece = self.board.getPieceFromPos(cell.pos)
			if not piece:
				self.validMoves.append(cell)

					
		return self.validMoves	  