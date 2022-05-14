from math import sqrt

class Glyphcircle:
    def __init__(self, bin, x1, y1, radius, padding) -> None:
        self.bin = bin
        self.x1 = x1
        self.y1 = y1
        self.radius = radius
        self.padding = padding
    
    def isPointWithinBoundary(self, x2, y2):
        a = (x2-self.x1)**2
        b = (y2-self.y1)**2
        dist = sqrt(a+b)
        if dist > (self.radius + self.padding):
            return False
        return True