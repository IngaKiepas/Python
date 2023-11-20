import unittest
from fracs import *

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 5], [1, 3]), [8, 15])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([2, 3], [1, 2]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([5, 12], [3, 2]), [5, 8])

    def test_div_frac(self):
        self.assertEqual(div_frac([2, 3], [1, 4]), [8, 3])

    def test_is_positive(self):
        self.assertTrue(is_positive([2, 3]))
        self.assertFalse(is_positive([-4, 3]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertFalse(is_zero([2, 5]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([1, 2], [3, 4]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 4]), 0.25)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     #uruchamia wszystkie testy

