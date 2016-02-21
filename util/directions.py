from util.vec2 import Vector2


class Directions(object):
    straight = {}
    
    straight['North'] = Vector2(0,-80)
    straight['South'] = Vector2(0,80)
    straight['West'] = Vector2(-80,0)
    straight['East'] = Vector2(80,0)
    
    
    diagonals = {}
     
    diagonals['Topleft'] = Vector2(-80,-80)
    diagonals['Topright'] = Vector2(-80,80)
    diagonals['Bottomleft'] = Vector2(80,-80)
    diagonals['Bottomright'] = Vector2(80,80)
    
    knight = {}
    
    knight['TL'] = Vector2(-80,-160)
    knight['TL2'] = Vector2(-160,-80)
    knight['BL'] = Vector2(-160,80)
    knight['BL2'] = Vector2(-80,160)
    knight['TR'] = Vector2(80,-160)
    knight['TR2'] = Vector2(160,-80)
    knight['BR'] = Vector2(160,80)
    knight['BR2'] = Vector2(80,160)