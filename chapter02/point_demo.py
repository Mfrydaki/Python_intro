class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
        Point.__count += 1

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return f"Point(x={self._x}, y={self._y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self._x == other._x and self._y == other._y
        else:
            return False

    @classmethod
    def get_count(cls):
        return cls.__count


    @property
    def x(self):  #getter
     return self._x

    @x.setter
    def x(self, x):   #setter
     self._x = x

    @property
    def y(self):
     return self._y

    @y.setter
    def y(self, y):
     self._y = y

def main():
    p1 = Point(10, 20)
    p2= Point (11, 20)

    print(p1)
    print(p2)

    p1.x = 10
    print(p1.x, p1.y)
    print(f"p1 == p2: {p1 == p2}")
    
    print(Point.get_count())

if __name__ == "__main__":
    main()
