'''
Created on Jan 17, 2016

@author: clayton
'''
import pygame


class Piece(object):
	
	
	def __init__(self, pos, board, player):
		self.pos = pos
		self.board = board
		self.player = player
		self.img = None
		self.selected = None
		self.validMoves = []
		self.firstMove = True
		self.directions = []

	def draw(self, surface):
		cell = self.board.getCellFromPos(self.pos) 
		
#		 if self.selected:
#			 pygame.draw.rect(surface, (0,255,0), cell.rect, 5)
		

		surface.blit(self.img, (cell.rect.left, cell.rect.top))
			
		
	def isClicked(self, point):
		cell = self.board.getCellFromPos(self.pos)
		return cell.rect.collidepoint(point)
	
	def belongsTo(self, player):
		if player == self.player:
			return True
		
		return False
	
	def move(self, point):		
		cell = self.board.getCellFromPoint(point)
		piece = self.board.getPieceFromPos(cell.pos)
		
		if piece != None:
			if piece.player != self.player:
				self.board.pieces.captured(piece)
				
		self.pos = cell.pos
			   
	   
	def isValidMove(self, point):
		cell = self.board.getCellFromPoint(point)
		
		for moves in self.validMoves:
			if moves.pos == cell.pos:
				return True
			
		return False
		
	def getValidMoves(self):		
		self.validMoves = self.getMoves(self.pos, self.directions.values())
		return self.validMoves
	
	def getMoves(self, pos, directions, moves=[]):
		if len(directions) == 0:
			return moves
	
		cell = self.board.getCellFromPos(pos) 
		piece = self.board.getPieceFromPos(pos)
		if not cell: # Off the board
			return self.getMoves(self.pos, directions[1:], moves)

		if piece is not None and piece is not self:
			if not piece.belongsTo(self.player):
				moves.append(cell)
			return self.getMoves(self.pos, directions[1:], moves)
		
		moves.append(cell)
		pos += directions[0]
		return self.getMoves(pos, directions, moves)