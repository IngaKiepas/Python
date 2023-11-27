from points import Point
import unittest

import triangles

class TestTriangle(unittest.TestCase):

    def test_str(self):
        triangle = triangles.Triangle(1, 2, 3, 4, 5, 6)
        triangle2 = triangles.Triangle(5, 6, 2, 4, 8, 10)
        self.assertEqual(str(triangle), "[(1, 2), (3, 4), (5, 6)]")
        self.assertEqual(str(triangle2), "[(5, 6), (2, 4), (8, 10)]")

    def test_repr(self):
        triangle = triangles.Triangle(1, 2, 3, 4, 5, 6)
        triangle2 = triangles.Triangle(11, 12, 13, 14, 15, 16)
        self.assertEqual(repr(triangle), "Triangle(1, 2, 3, 4, 5, 6)")
        self.assertEqual(repr(triangle2), "Triangle(11, 12, 13, 14, 15, 16)")

    def test_eq(self):
        triangle1 = triangles.Triangle(1, 2, 3, 4, 5, 6)
        triangle2 = triangles.Triangle(3, 4, 1, 2, 5, 6)
        self.assertEqual(triangle1, triangle2)

    def test_ne(self):
        triangle1 = triangles.Triangle(1, 2, 3, 4, 5, 6)
        triangle2 = triangles.Triangle(0, 0, 0, 0, 0, 0)
        self.assertNotEqual(triangle1, triangle2)

    def test_center(self):
        triangle = triangles.Triangle(1, 2, 5, 6, 9, 10)
        self.assertEqual(triangle.center(), Point(5.0, 6.0))

    def test_area(self):
        triangle = triangles.Triangle(0, 0, 3, 0, 0, 4)
        self.assertEqual(triangle.area(), 6)

    def test_move(self):
        triangle = triangles.Triangle(1, 2, 3, 4, 5, 6)
        triangle.move(1, 1)
        self.assertEqual(triangle, triangles.Triangle(2, 3, 4, 5, 6, 7))

    if __name__ == '__main__':
        unittest.main()