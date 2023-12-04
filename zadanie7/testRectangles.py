import unittest

from points import Point

import rectangles

class TestRectangle(unittest.TestCase):

    def init(self):
        rectangle = rectangles.Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.pt1.x, 1)
        self.assertEqual(rectangle.pt1.y, 2)
        self.assertEqual(rectangle.pt2.x, 3)
        self.assertEqual(rectangle.pt2.y, 4)

        with self.assertRaises(ValueError):
            rectangles.Rectangle(4, 3, 2, 1)

    def test_str(self):
        rectangle = rectangles.Rectangle(1, 2, 3, 4)
        rectangle2 = rectangles.Rectangle(0, 1, 8, 12)
        self.assertEqual(str(rectangle), "[(1, 2), (3, 4)]")
        self.assertEqual(str(rectangle2), "[(0, 1), (8, 12)")

    def test_repr(self):
        rectangle = rectangles.Rectangle(1, 2, 3, 4)
        rectangle2 = rectangles.Rectangle(18, 9, 23, 45)
        self.assertEqual(repr(rectangle), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(repr(rectangle2), "Rectangle(18, 9, 23, 45")

    def test_eq(self):
        rectangle1 = rectangles.Rectangle(1, 2, 3, 4)
        rectangle2 = rectangles.Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle1, rectangle2)

    def test_ne(self):
        rectangle1 = rectangles.Rectangle(1, 2, 3, 4)
        rectangle2 = rectangles.Rectangle(0, 0, 0, 0)
        self.assertNotEqual(rectangle1, rectangle2)

    def test_center(self):
        rectangle = rectangles.Rectangle(1, 2, 5, 6)
        self.assertEqual(rectangle.center(), Point(3.0, 4.0))

    def test_area(self):
        rectangle = rectangles.Rectangle(1, 2, 5, 6)
        self.assertEqual(rectangle.area(), 16)

    def test_move(self):
        rectangle = rectangles.Rectangle(1, 2, 3, 4)
        rectangle.move(1, 1)
        self.assertEqual(rectangle, rectangles.Rectangle(2, 3, 4, 5))

    def test_intersection(self):
        a = rectangles.Rectangle(1, 0, 4, 6)
        b = rectangles.Rectangle(1, 2, 3, 3)
        c = rectangles.Rectangle(1, 2, 3, 3)
        self.assertEqual(a.intersection(b), c)

    def test_cover(self):
        a = rectangles.Rectangle(2, 2, 4, 4)
        b = rectangles.Rectangle(4, 4, 6, 6)
        c = rectangles.Rectangle(2, 2, 6, 6)
        self.assertEqual(a.cover(b), c)

    def test_make4(self):
        a = rectangles.Rectangle(0, 0, 2, 2)
        b = rectangles.Rectangle(0, 1, 1, 2)
        c = rectangles.Rectangle(1, 1, 2, 2)
        d = rectangles.Rectangle(1, 0, 2, 1)
        e = rectangles.Rectangle(0, 0, 1, 1)
        self.assertEqual(a.make4(), (b, c, d, e))

    if __name__ == '__main__':
        unittest.main()




