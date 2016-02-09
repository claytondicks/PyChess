'''
Created on Jan 17, 2016

@author: clayton
'''

class PiecesManager(object):

    def __init__(self):
        self.thePieces = []
        
    
    def add(self, piece):
        self.thePieces.append(piece) 
    
    
    def draw(self, surface):
        for piece in self.thePieces:
            piece.draw(surface)
            
    def __iter__(self):
        return iter(self.thePieces)
