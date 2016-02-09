from grid import Grid
from pieces.piecesManager import PiecesManager

class Board(object):
    
    def __init__(self):
        self.grid = Grid()
        self.pieces = PiecesManager()
        
        
    def draw(self, surface):
        self.grid.draw(surface)
        self.pieces.draw(surface)


    def getCellFromPos(self, pos):
        for cell in self.grid:
            if cell.pos == pos:
                return cell
            
            
    def getCellFromPoint(self, point):
        for cell in self.grid:
            if cell.rect.collidepoint(point):   
                return cell
            
            
    def getPieceFrompoint(self, point):
        for piece in self.pieces:
            if piece.isClicked(point):
                return piece
    
    def clearSelection(self):
        for piece in self.pieces:
            piece.selected = None