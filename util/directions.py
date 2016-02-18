from util.vec2 import Vector2


class Directions(object):
    straight = []
    
    straight.append(Vector2(0,-80))
    straight.append(Vector2(0,80))
    straight.append(Vector2(-80,0))
    straight.append(Vector2(80,0))
    
    
    # diagonals = {}
    # 
    # diagonals[ULeft] = (-80,-80)
    # diagonals[DLeft] = (-80,80)
    # diagonals[URight] = (80,-80)
    # diagonals[DRight] = (80,80)
