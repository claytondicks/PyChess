'''
Created on Jan 20, 2016

@author: clayton
'''
import pygame


class Player(object):

    def __init__(self, colour, board):
        self.colour = colour
        self.board = board
    
    
    
    def turn(self):
        
        event = pygame.event.get()
        
        for e in event:
            if e.type == pygame.MOUSEBUTTONUP:
                pass