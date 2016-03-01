'''
Created on Jan 23, 2016

@author: clayton
'''
import pygame


from piece import Piece
from util.directions import Directions

class King(Piece):
	
	def __init__(self, pos, board, player):
		Piece.__init__(self, pos, board, player)		
		self.validMoves = []
		self.directions = dict(Directions.diagonals.items() + Directions.straight.items())
		
		if self.player.colour == 0:
			self.img = pygame.image.load("images/wking.png").convert_alpha()
			self.img = pygame.transform.scale(self.img, (self.board.grid.cellsize, self.board.grid.cellsize))
		else:
			self.img = pygame.image.load("images/bking.png").convert_alpha()
			self.img = pygame.transform.scale(self.img, (self.board.grid.cellsize, self.board.grid.cellsize))
		

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