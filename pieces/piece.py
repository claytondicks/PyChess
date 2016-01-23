'''
Created on Jan 17, 2016

@author: clayton
'''
class Piece(object):
    
    
    def __init__(self, pos, grid, player):
        #self.king = pygame.image.load("images/wking.png").convert_alpha()
        self.pos = pos
        self.grid = grid
        self.player = player
        self.img = None

    def draw(self, surface):
        cell = self.grid.getCellFromPos(self.pos)
        surface.blit(self.img, (cell.rect.left, cell.rect.top))