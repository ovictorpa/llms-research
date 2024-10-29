import unittest
from c2c._32a import poly, find_zero

class TestPolyAndFindZero(unittest.TestCase):

    def test_poly_positive_coefficients(self):
        self.assertAlmostEqual(poly([1, 2, 3], 2), 17)
        self.assertAlmostEqual(poly([0, 1, 2], 3), 21)
        self.assertAlmostEqual(poly([1, 0, 2], 1), 3)

    def test_poly_negative_coefficients(self):
        self.assertAlmostEqual(poly([-1, -2, -3], 2), -17)
        self.assertAlmostEqual(poly([0, -1, -2], 3), -21)
        self.assertAlmostEqual(poly([-1, 0, -2], 1), -3)

    def test_poly_mixed_coefficients(self):
        self.assertAlmostEqual(poly([1, -2, 3], 2), 9)
        self.assertAlmostEqual(poly([0, 1, -2], 3), -15)
        self.assertAlmostEqual(poly([-1, 0, 2], 1), 1)

    def test_poly_single_coefficient(self):
        self.assertAlmostEqual(poly([5], 2), 5)
        self.assertAlmostEqual(poly([0], 3), 0)
        self.assertAlmostEqual(poly([-3], 1), -3)

    def test_poly_empty_list(self):
        self.assertAlmostEqual(poly([], 2), 0)

    def test_find_zero_simple_polynomial(self):
        self.assertAlmostEqual(find_zero([1, -2, 1]), 1, places=9)  # (x-1)^2 = 0

    def test_find_zero_no_real_root(self):
        self.assertAlmostEqual(find_zero([1, 0, 1]), 0, places=9)  # x^2 + 1 = 0 (no real root)

    def test_find_zero_multiple_roots(self):
        self.assertAlmostEqual(find_zero([1, -3, 2]), 1, places=9)  # (x-1)(x-2) = 0

    def test_find_zero_large_coefficients(self):
        self.assertAlmostEqual(find_zero([1000, -2000, 1000]), 1, places=9)  # 1000(x-1)^2 = 0

if __name__ == '__main__':
    unittest.main()