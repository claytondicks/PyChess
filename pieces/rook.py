'''
Created on Jan 23, 2016

@author: clayton
'''
import pygame


from piece import Piece
from util.directions import Directions

class Rook(Piece):
	
	def __init__(self, pos, board, player):
		Piece.__init__(self, pos, board, player)
		self.validMoves = []
		
		self.directions = Directions.straight
		
		if self.player.colour == 0:
			self.img = pygame.image.load("images/wrook.png").convert_alpha()
		else:
			self.img = pygame.image.load("images/brook.png").convert_alpha()
			
		self.img = pygame.transform.scale(self.img, (self.board.grid.cellsize, self.board.grid.cellsize))