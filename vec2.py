import math

class Vector2(object):

    def __init__(self, x, y):
        self.coords = (x, y)

    def dist(self, other):
        x = self.coords[0]
        y = self.coords[1]
        x = abs(x - other[0]);
        y = abs(y - other[1]);
        return x if x > y else y;
    
    def __getitem__(self, key):
        return self.coords[key]
    
    def __add__(self, other):
        x = self.coords[0]
        y = self.coords[1]
        x += other[0]
        y += other[1]
    
    def __eq__(self, other):
        if self[0] != other[0]:
            return False
    
        if self[1] != other[1]:
            return False
    
        return True
    
    def __str__(self):
        return str(self.coords[0]) + ' ' + str(self.coords[1])

