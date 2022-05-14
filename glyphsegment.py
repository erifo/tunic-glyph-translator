class Glyphsegment:
    def __init__(self, bin, x1, y1, x2, y2, padding) -> None:
        self.bin = bin
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.padding = padding
    
    def isPointWithinBoundary(self, x, y):
        if (x < min(self.x1, self.x2)-self.padding
            or x > max(self.x1, self.x2)+self.padding
            or y < min(self.y1, self.y2)-self.padding
            or y > max(self.y1, self.y2)+self.padding):
            return False
        return True