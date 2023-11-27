import unittest

from points import Point

import rectangles

class TestRectangle(unittest.TestCase):

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

    if __name__ == '__main__':
        unittest.main()




