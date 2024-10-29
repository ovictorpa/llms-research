import unittest
from c2c.9a import rolling_max

class TestRollingMax(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])

    def test_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -4, -5]), [-1, -1, -1, -1, -1])
        self.assertEqual(rolling_max([-5, -4, -3, -2, -1]), [-5, -4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(rolling_max([1, -1, 2, -2, 3]), [1, 1, 2, 2, 3])
        self.assertEqual(rolling_max([-1, 1, -2, 2, -3, 3]), [-1, 1, 1, 2, 2, 3])

    def test_single_number(self):
        self.assertEqual(rolling_max([42]), [42])

    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

if __name__ == '__main__':
    unittest.main()