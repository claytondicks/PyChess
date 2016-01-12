from pygame import Rect
from cell import Cell

class Board(object):
    
    def __init__(self):
        self.board = [None] * 64
        
        for row in range(8):
            y = row * (640/8)
            for col in range(8):
                x = col * (640/8)
                
                rect = Rect(y, x, (640/8) - 1, (640/8) - 1)
                index = row + col * 8
                
                self.board[index] = Cell(rect)
                
    
    
    def getBoard(self):
        return self.board
    