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
		self.firstMove = True
		self.directions = []
		self.validMoves = []

	def draw(self, surface):
		cell = self.board.getCellFromPos(self.pos) 
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
		
		for move in self.getValidMoves():
			if move.pos == cell.pos:
				return True
			
		return False
		
	def getValidMoves(self):
		return self.getMoves(self.board, self.player, self.pos, self.pos, self.directions.values())
	
	@staticmethod
	def getMoves(board, player, origin, pos, directions=[], moves=None):
		if moves is None:
			moves = []
		
		if len(directions) == 0:
			return moves
	
		cell = board.getCellFromPos(pos) 
		piece = board.getPieceFromPos(pos)
		if cell is None: # Off the board
			return Piece.getMoves(board, player, origin, origin, directions[1:], moves)

		if piece is not None and piece.pos is not origin:
			if not piece.belongsTo(player):
				moves.append(cell)
			return Piece.getMoves(board, player, origin, origin, directions[1:], moves)
		
		moves.append(cell)
		pos += directions[0]
		return Piece.getMoves(board, player, origin, pos, directions, moves)
		
	def __str__(self):
		return str(self.pos)