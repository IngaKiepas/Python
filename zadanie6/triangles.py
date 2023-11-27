from points import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):      # "[(x1, y1), (x2, y2), (x3, y3)]"
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]"

    def __repr__(self):     # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"

    def __eq__(self, other):    # obsługa tr1 == tr2
        selfPoints = {self.pt1, self.pt2, self.pt3}
        otherPoints = {other.pt1, other.pt2, other.pt3}
        return selfPoints == otherPoints

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):           # zwraca środek (masy) trójkąta
        x = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        y = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(x, y)

    def area(self):             # pole powierzchni
        # wzór Herona
        a = self.pt1.distance(self.pt2)
        b = self.pt2.distance(self.pt3)
        c = self.pt3.distance(self.pt1)
        h = (a + b + c) / 2
        return (h * (h - a) * (h - b) * (h - c)) ** 0.5

    def move(self, x, y):       # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        self.pt3.x += x
        self.pt3.y += y