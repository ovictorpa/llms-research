import unittest
import math
from c2c.32a import find_zero, poly  # Adjust the import statement as needed

class TestFindZero(unittest.TestCase):

    def test_linear_function(self):
        coeffs = [0, 1]  # f(x) = x
        self.assertAlmostEqual(find_zero(coeffs), 0, places=6)

    def test_quadratic_function(self):
        coeffs = [1, 0, -1]  # f(x) = x^2 - 1
        self.assertAlmostEqual(find_zero(coeffs), 1, places=6)

    def test_cubic_function(self):
        coeffs = [-1, 0, 0, 1]  # f(x) = x^3 - 1
        self.assertAlmostEqual(find_zero(coeffs), 1, places=6)

    def test_complex_polynomial(self):
        coeffs = [1, -5, 6]  # f(x) = x^2 - 5x + 6
        self.assertAlmostEqual(find_zero(coeffs), 2, places=6)

    def test_no_real_roots(self):
        coeffs = [1, 0, 1]  # f(x) = x^2 + 1
        with self.assertRaises(ValueError):
            find_zero(coeffs)

    def test_multiple_roots(self):
        coeffs = [0, 0, 1]  # f(x) = x^2
        self.assertAlmostEqual(find_zero(coeffs), 0, places=6)

    def test_root_outside_initial_range(self):
        coeffs = [10, 0, 1]  # f(x) = x^2 + 10
        root = find_zero(coeffs)


    def test_poly_function(self):
        coeffs = [1, -5, 6]  # f(x) = x^2 - 5x + 6
        self.assertAlmostEqual(poly(coeffs, 2), 0, places=6)
        self.assertAlmostEqual(poly(coeffs, 3), 0, places=6)

if __name__ == '__main__':
    unittest.main()
