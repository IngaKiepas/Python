import unittest

from points import Point

from rectangles import Rectangle

class TestRectangle(unittest.TestCase):

    def testProperty(self):
        rectangle = Rectangle(8, 4, 12, 9)
        assert rectangle.top == 9
        assert rectangle.left == 8
        assert rectangle.bottom == 4
        assert rectangle.right == 12
        assert rectangle.width == 4
        assert rectangle.height == 5

    def testPropertyPoint(self):
        rectangle = Rectangle(8, 4, 12, 9)
        assert rectangle.topleft == Point(8, 9)
        assert rectangle.bottomleft == Point(8, 4)
        assert rectangle.topright == Point(12, 9)
        assert rectangle.bottomright == Point(12, 4)

    def testFromPoints(self):
        part1 = Point(8, 15)
        part2 = Point(10, 16)
        assert str(Rectangle.from_points([part1, part2])) == '[(8, 15), (10, 16)]'

    def init(self):
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.pt1.x, 1)
        self.assertEqual(rectangle.pt1.y, 2)
        self.assertEqual(rectangle.pt2.x, 3)
        self.assertEqual(rectangle.pt2.y, 4)

        with self.assertRaises(ValueError):
            Rectangle(4, 3, 2, 1)

    def test_str(self):
        rectangle = Rectangle(1, 2, 3, 4)
        rectangle2 = Rectangle(0, 1, 8, 12)
        self.assertEqual(str(rectangle), "[(1, 2), (3, 4)]")
        self.assertEqual(str(rectangle2), "[(0, 1), (8, 12)")

    def test_repr(self):
        rectangle = Rectangle(1, 2, 3, 4)
        rectangle2 = Rectangle(18, 9, 23, 45)
        self.assertEqual(repr(rectangle), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(repr(rectangle2), "Rectangle(18, 9, 23, 45")

    def test_eq(self):
        rectangle1 = Rectangle(1, 2, 3, 4)
        rectangle2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle1, rectangle2)

    def test_ne(self):
        rectangle1 = Rectangle(1, 2, 3, 4)
        rectangle2 = Rectangle(0, 0, 0, 0)
        self.assertNotEqual(rectangle1, rectangle2)

    def test_center(self):
        rectangle = Rectangle(1, 2, 5, 6)
        self.assertEqual(rectangle.center(), Point(3.0, 4.0))

    def test_area(self):
        rectangle = Rectangle(1, 2, 5, 6)
        self.assertEqual(rectangle.area(), 16)

    def test_move(self):
        rectangle = Rectangle(1, 2, 3, 4)
        rectangle.move(1, 1)
        self.assertEqual(rectangle, Rectangle(2, 3, 4, 5))

    def test_intersection(self):
        a = Rectangle(1, 0, 4, 6)
        b = Rectangle(1, 2, 3, 3)
        c = Rectangle(1, 2, 3, 3)
        self.assertEqual(a.intersection(b), c)

    def test_cover(self):
        a = Rectangle(2, 2, 4, 4)
        b = Rectangle(4, 4, 6, 6)
        c = Rectangle(2, 2, 6, 6)
        self.assertEqual(a.cover(b), c)

    def test_make4(self):
        a = Rectangle(0, 0, 2, 2)
        b = Rectangle(0, 1, 1, 2)
        c = Rectangle(1, 1, 2, 2)
        d = Rectangle(1, 0, 2, 1)
        e = Rectangle(0, 0, 1, 1)
        self.assertEqual(a.make4(), (b, c, d, e))


if __name__ == '__main__':
    unittest.main()
