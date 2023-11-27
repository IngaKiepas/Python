from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie"""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):     # "[(x1, y1), (x2, y2)]"
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):    # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}"

    def __eq__(self, other):    # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __neg__(self, other):       # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        x = (self.pt1.x + self.pt2.x) / 2
        y = (self.pt1.y + self.pt2.y) / 2
        return Point(x, y)

    def area(self):             # pole powierzchni
        length = self.pt2.x - self.pt1.x
        width = self.pt2.y - self.pt1.y
        area1 = abs(length)
        area2 = abs(width)
        area = area1 * area2
        return area

    def move(self, x, y):       # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y