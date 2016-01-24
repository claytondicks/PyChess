'''
Created on Jan 20, 2016

@author: clayton
'''
import pygame, sys


class Player(object):

    def __init__(self, colour, piecesManager):
        self.colour = colour   
        self.piecesManager = piecesManager
    
    def turn(self):
        
        LEFT = 1
        
        event = pygame.event.get()
        
        for e in event:
            pos = pygame.mouse.get_pos()
            
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == LEFT:
                for piece in self.piecesManager.thePieces:
                    if piece.isClicked(pos) and piece.isMine(self):
                        piece.selected = True
                        return True
                        
        
        return False