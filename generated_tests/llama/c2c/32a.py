import unittest
from your_module import find_zero  # Replace with the actual module name

class TestFindZero(unittest.TestCase):
    def test_linear_polynomial(self):
        xs = [1, -2]  # corresponds to x^0 + (-2)x
        expected_zero = -1.0
        self.assertAlmostEqual(find_zero(xs), expected_zero)

    def test_quadratic_polynomial(self):
        xs = [1, -3, 2]  # corresponds to x^2 - 3x + 2
        expected_zero = math.sqrt(2) or -math.sqrt(2)
        self.assertAlmostEqual(find_zero(xs), expected_zero)

    def test_higher_degree_polynomial(self):
        xs = [1, -4, 6, -4]  # corresponds to x^3 - 4x^2 + 6x - 4
        expected_zero = (-1.0 + math.sqrt(5.0)) / 2.0 or (-1.0 - math.sqrt(5.0)) / 2.0
        self.assertAlmostEqual(find_zero(xs), expected_zero)

    def test_multiple_zeros(self):
        xs = [1, -2, 3, -6]  # corresponds to x^3 - 2x^2 + 3x - 6
        expected_zeros = [-1.5, 1]
        for zero in expected_zeros:
            self.assertAlmostEqual(find_zero([*xs, -zero]), zero)

if __name__ == '__main__':
    unittest.main()