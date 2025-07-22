class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def __eq__(self, other):
        return isinstance(other, Point) and self._x == other._x and self._y  == other._y
    
    def __hash__(self):
        return hash((self._x, self._y))
    
    def __repr__(self):
        return f"Point({self._x}, {self._y})"
    
def main():
    p1 = Point(1,3)
    p2 = Point(2,5)
    p3=  Point(1,2)
    p4 = Point(100,200)

    print(f"p1 == p2: {p1  == p2}")
    print(f"p1 == p3: {p1 == p3}")

    print("Hash Values")
    print(f"Hash(p1): {hash(p1)}")
    print(f"Hash(p2): {hash(p2)}")
    print(f"Hash(p3): {hash(p3)}")
    print(f"Hash(p4): {hash(p4)}")


    point_dict = {
        p1 : "Point_1",
        p2 : "Point_2",
        p3 : "Point_3"    }
    
    for key, value in point_dict.items():
        print(f"{key}:{value}")




if __name__ == "__main__":
    main()
        