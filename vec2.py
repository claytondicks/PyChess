import math


class Vector2(object):

    def __init__(self, x, y=None):
            if(y is None):
                self.x = x[0]
                self.y = x[1]
            else:
                self.x = x
                self.y = y

    def dist(self, other):
        relx = abs(self.x - other[0])
        rely = abs(self.y - other[1])
        return math.sqrt(relx**2 + rely**2)


    def __add__(self, other):
        newx = self.x + other[0]
        newy = self.y + other[1]
        return Vector2(newx, newy)

        
    def __sub__(self, other):
        newx = self.x - other[0]
        newy = self.y - other[1]
        return Vector2(newx, newy)

    
    def __eq__(self, other):
        if self.x != other[0]:
            return False

        if self.y != other[1]:
            return False

        return True

    def center(self):
        self.x = math.floor(self.x) + 0.5
        self.y = math.floor(self.y) + 0.5
        
    def save(self):
        return Vector2.save(self)

    def __getitem__(self, key):
        return (self.x, self.y)[key]

    def __str__(self):
            return str(self.x) + ' ' + str(self.y)