from pygame import Rect
from board.cell import Cell
from vec2 import Vector2

class Grid(object):
    
    def __init__(self):
        self.grid = []
        self.cellsize = 80
        
        for row in range(8):
            x = row * self.cellsize
            for col in range(8):
                y = col * self.cellsize
                
                vec = Vector2(x, y)
                rect = Rect(x, y, self.cellsize, self.cellsize)
                
                self.grid.append(Cell(rect,vec)) 
                
    
    
    def getGrid(self):
        return self.grid
    
    def getCellFromPos(self, pos):
        for cell in self.grid:
            if cell.pos == pos:
                return cell
    
    def getCellFromPoint(self, point):
        for cell in self.grid:
            if cell.rect.collidepoint(point):
                return cell
            
    
    
    def draw(self, surface):
        x = 0
        for cell in self.grid:
            x += 1
            if x % 9 == 0:
                x += 1
            cell.draw(surface, x)