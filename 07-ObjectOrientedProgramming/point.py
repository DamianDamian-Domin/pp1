from math import sqrt, floor

class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return 'Odległość pomiędzy punktami wynosi 0'
        else:
            d = sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
            return f'Odległość pomiędzy punktami wynosi {d:.2f}' 

