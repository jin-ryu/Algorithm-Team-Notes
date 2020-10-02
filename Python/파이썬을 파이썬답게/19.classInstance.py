class Coord(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y
    
    # class 내부에서 출력 format 지정 가능
    def __str__ (self):
        return '({}, {})'.format(self.x, self.y)

    
point = Coord(1, 2)
print(point.__str__())