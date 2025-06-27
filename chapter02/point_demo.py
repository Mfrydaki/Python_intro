class Point:
    __count = 0

def __init__(self, x= 0, y= 0):
    self._x = x
    self._y = y
    Point.__count +=1

def __str__(self):
    return f"({self.__x},{self.__y})"

def __repr__(self):
    return f"Point(x={self.__x},y={self.__y})"

def __eq__(self, other):
    if isinstance(other, Point):
        return self.__x ==other.__x and self.__y == other.__y
    else:
        return False
    

@classmethod
def get_count(cls):
    return cls.__count



