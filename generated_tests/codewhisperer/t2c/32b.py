import unittest
import math
from typing import List

def poly(xs: List[float], x: float) -> float:
    # Function implementation goes here
    # For testing purposes, we'll leave this empty
    pass

def find_zero(xs: List[float]) -> float:
    # Function implementation goes here
    # For testing purposes, we'll leave this empty
    pass

class TestPolynomialFunctions(unittest.TestCase):
    def test_poly_example_1(self):
        self.assertAlmostEqual(poly([1, 2], 1), 3.0)

    def test_poly_example_2(self):
        self.assertAlmostEqual(poly([1, 0, -1], 2), 1.0)

    def test_poly_constant(self):
        self.assertAlmostEqual(poly([5], 10), 5.0)

    def test_poly_linear(self):
        self.assertAlmostEqual(poly([1, 1], 2), 3.0)

    def test_poly_quadratic(self):
        self.assertAlmostEqual(poly([1, 2, 1], 2), 9.0)

    def test_poly_cubic(self):

    def test_poly_negative_x(self):
        self.assertAlmostEqual(poly([1, 1, 1], -2), -1.0)

    def test_poly_zero_x(self):

    def test_find_zero_example_1(self):
        self.assertAlmostEqual(round(find_zero([1, 2]), 2), -0.5)

    def test_find_zero_example_2(self):
        self.assertAlmostEqual(round(find_zero([-6, 11, -6, 1]), 2), 1.0)

    def test_find_zero_quadratic(self):
        self.assertAlmostEqual(round(find_zero([1, 0, -1]), 2), -1.0)

    def test_find_zero_cubic(self):
        self.assertAlmostEqual(round(find_zero([-1, 0, 0, 1]), 2), 1.0)

    def test_find_zero_even_coefficients(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])

    def test_find_zero_all_zeros(self):
        with self.assertRaises(ValueError):
            find_zero([0, 0, 0, 0])

    def test_find_zero_verify(self):
        coeffs = [1, -5, 6]  # (x-2)(x-3)
        zero = find_zero(coeffs)

    def test_poly_input_unchanged(self):
        coeffs = [1, 2, 3]
        original_coeffs = coeffs.copy()
        poly(coeffs, 2)
        self.assertEqual(coeffs, original_coeffs, "Input list should not be modified")

    def test_find_zero_input_unchanged(self):
        coeffs = [1, -5, 6]
        original_coeffs = coeffs.copy()
        find_zero(coeffs)
        self.assertEqual(coeffs, original_coeffs, "Input list should not be modified")

if __name__ == '__main__':
    unittest.main()
