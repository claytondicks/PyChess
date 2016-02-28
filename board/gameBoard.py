from grid import Grid
from pieces.piecesManager import PiecesManager

class Board(object):
	
	def __init__(self):
		self.grid = Grid()
		self.pieces = PiecesManager()
		
	def draw(self, surface):
		self.grid.draw(surface)
		self.pieces.draw(surface)
		
		for piece in self.pieces:
			if piece.isSelected():
				for cell in piece.getValidMoves():
					cell.highlight(surface, (0,0,255), 2)
					
				self.getCellFromPos(piece.pos).highlight(surface, (0,255,0), 2)


	def getCellFromPos(self, pos):
		for cell in self.grid:
			if cell.pos == pos:
				return cell
			
	def getPieceFromPos(self, pos):
		for piece in self.pieces:
			if piece.pos == pos:
				return piece
					
	def getCellFromPoint(self, point):
		for cell in self.grid:
			if cell.rect.collidepoint(point):   
				return cell
			
	def getPieceFrompoint(self, point):
		for piece in self.pieces:
			if piece.isClicked(point):
				return piece
