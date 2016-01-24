'''
Created on Jan 17, 2016

@author: clayton
'''
import pygame


class Piece(object):
    
    
    def __init__(self, pos, grid, player):
        #self.king = pygame.image.load("images/wking.png").convert_alpha()
        self.pos = pos
        self.grid = grid
        self.player = player
        self.img = None
        self.selected = None

    def draw(self, surface):
        cell = self.grid.getCellFromPos(self.pos) 
        if self.selected:

            pygame.draw.rect(surface, (0,255,0), cell.rect, 2)
          

        surface.blit(self.img, (cell.rect.left, cell.rect.top))
            
        
    def isClicked(self, point):
        cell = self.grid.getCellFromPos(self.pos)
        return cell.rect.collidepoint(point)
    
    def isMine(self, player):
        if player == self.player:
            return True
        
        return False