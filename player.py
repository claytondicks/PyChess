'''
Created on Jan 20, 2016

@author: clayton
'''
import pygame, sys


class Player(object):

	def __init__(self, colour, board):
		self.colour = colour   
		self.board = board
		self.selected = None
		
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
				piece = self.board.getPieceFrompoint(point)
				if piece is None:
					return
				
				if piece.belongsTo(self):
					self.selected = piece
						
			if e.type == pygame.MOUSEBUTTONDOWN and e.button == RIGHT:
				if self.selected is not None and self.selected.isValidMove(point):
					self.selected.move(point)
					self.selected.validMoves = []
					self.selected = None
					return True

		return False