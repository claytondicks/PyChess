from util.vec2 import Vector2


class Directions(object):
    straight = {}
    
    straight['North'] = Vector2(0,-1)
    straight['South'] = Vector2(0,1)
    straight['West'] = Vector2(-1,0)
    straight['East'] = Vector2(1,0)
    
    
    diagonals = {}
     
    diagonals['Topleft'] = Vector2(-1,-1)
    diagonals['Topright'] = Vector2(-1,1)
    diagonals['Bottomleft'] = Vector2(1,-1)
    diagonals['Bottomright'] = Vector2(1,1)
    
    knight = {}
    
    knight['TL'] = Vector2(-1,-2)
    knight['TL2'] = Vector2(-2,-1)
    knight['BL'] = Vector2(-2,1)
    knight['BL2'] = Vector2(-1,2)
    knight['TR'] = Vector2(1,-2)
    knight['TR2'] = Vector2(2,-1)
    knight['BR'] = Vector2(2,1)
    knight['BR2'] = Vector2(1,2)