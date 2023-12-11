from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie"""

    def __init__(self, x1, y1, x2, y2):
        #chcemy, aby x1 < x2, y1 < y2.
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Wrong rectangle values!")
        else:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, points):
        x1 = points[0].x
        y1 = points[0].y
        x2 = points[1].x
        y2 = points[1].y

        if len(points) != 2:
            raise ValueError("There should be 2 points to make a rectangle")

        result = cls(x1, y1, x2, y2)
        return result

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        width = self.pt2.x - self.pt1.x
        return abs(width)

    @property
    def height(self):
        height = self.pt2.y - self.pt1.y
        return abs(height)

    @property
    def topleft(self):
        x1 = self.pt1.x
        y2 = self.pt2.y
        return Point(x1, y2)

    @property
    def bottomleft(self):
        x1 = self.pt1.x
        y1 = self.pt1.y
        return Point(x1, y1)

    @property
    def topright(self):
        x2 = self.pt2.x
        y2 = self.pt2.y
        return Point(x2, y2)

    @property
    def bottomright(self):
        x2 = self.pt2.x
        y1 = self.pt1.y
        return Point(x2, y1)

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

    def intersection(self, other): #część wspólna prostokątów
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)

        case1 = self.pt1.y > other.pt2.y
        case2 = self.pt2.y < other.pt1.y
        case3 = self.pt1.x > other.pt2.x
        case4 = self.pt2.x < other.pt1.x

        if case1 or case2 or case3 or case4:
            raise ValueError("There is no intersection!")
        else:
            return Rectangle(x1, y1, x2, y2)

    def cover(self, other): #prostokąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        result = Rectangle(x1, y1, x2, y2)
        return result

    def make4(self): #zwraca krotkę czterech mniejszych
        a = Rectangle(self.pt1.x, self.center().y, self.center().x, self.pt2.y)
        b = Rectangle(self.center().x, self.center().y, self.pt2.x, self.pt2.y)
        c = Rectangle(self.center().x, self.pt1.y, self.pt2.x, self.center().y)
        d = Rectangle(self.pt1.x, self.pt1.y, self.center().x, self.center().y)

        result = (a, b, c, d)

        return result
