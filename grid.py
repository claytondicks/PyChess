import pygame
from pygame import Rect
from cell import Cell

class Grid(object):
    
    def __init__(self):
        self.grid = [None] * 64
        
        for row in range(8):
            y = row * (640/8)
            for col in range(8):
                x = col * (640/8)
                
                rect = Rect(y, x, (640/8) - 1, (640/8) - 1)
                index = row + col * 8
                
                self.grid[index] = Cell(rect)
                
    
    
    def getGrid(self):
        return self.grid
    
    
    def draw(self, surface):
        x = 0
        for cell in self.grid:
            x += 1
            if x % 9 == 0:
                x += 1
            cell.draw(surface, x)

        pygame.display.flip()