import unittest
from typing import List

# Import the function we're testing
from c2c.9a import rolling_max

class TestRollingMax(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element(self):
        self.assertEqual(rolling_max([5]), [5])

    def test_increasing_sequence(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_decreasing_sequence(self):
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])

    def test_mixed_sequence(self):
        self.assertEqual(rolling_max([1, 3, 2, 4, 5, 2, 1]), [1, 3, 3, 4, 5, 5, 5])

    def test_repeated_elements(self):
        self.assertEqual(rolling_max([2, 2, 2, 2]), [2, 2, 2, 2])

    def test_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -3, -2, -4, -5]), [-1, -1, -1, -1, -1])

    def test_mixed_positive_negative(self):
        self.assertEqual(rolling_max([-2, 1, -3, 4, 0, -1, 5]), [-2, 1, 1, 4, 4, 4, 5])

    def test_large_numbers(self):
        self.assertEqual(rolling_max([1000000, 2000000, 1500000]), [1000000, 2000000, 2000000])

if __name__ == '__main__':
    unittest.main()
