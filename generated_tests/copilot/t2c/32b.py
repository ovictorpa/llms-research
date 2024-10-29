import unittest
import math
from typing import List

def poly(xs: List[float], x: float) -> float:
    """
    Evaluates a polynomial with coefficients xs at point x.
    
    The polynomial is given by:
    f(x) = xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    
    >>> poly([1, 2], 1)
    3.0
    >>> poly([1, 0, -1], 2)
    1.0
    """
    return sum(coef * (x ** i) for i, coef in enumerate(xs))

def find_zero(xs: List[float]) -> float:
    """
    Find a zero of a polynomial with coefficients xs.
    Returns a zero point such that poly(x) = 0. Only returns one zero point,
    even if there are multiple. Assumes the list xs has an even number of coefficients
    and that the largest non-zero coefficient guarantees a solution.
    
    >>> round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2)  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    def f(x):
        return poly(xs, x)
    
    return round(math.newton(f, 0), 2)

class TestPolynomialFunctions(unittest.TestCase):
    def test_poly_example_1(self):
        self.assertEqual(poly([1, 2], 1), 3.0)
    
    def test_poly_example_2(self):
        self.assertEqual(poly([1, 0, -1], 2), 1.0)
    
    def test_poly_zero(self):
        self.assertEqual(poly([0, 0, 0], 2), 0.0)
    
    def test_poly_negative(self):
        self.assertEqual(poly([-1, -2, -3], 1), -6.0)
    
    def test_find_zero_example_1(self):
        self.assertEqual(round(find_zero([1, 2]), 2), -0.5)
    
    def test_find_zero_example_2(self):
        self.assertEqual(round(find_zero([-6, 11, -6, 1]), 2), 1.0)
    
    def test_find_zero_no_real_root(self):
        self.assertRaises(ValueError, find_zero, [1, 0, 1])  # x^2 + 1 has no real roots

if __name__ == '__main__':
    unittest.main()