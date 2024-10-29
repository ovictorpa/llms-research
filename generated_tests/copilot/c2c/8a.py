import unittest
from c2c.8a import sum_product

class TestSumProduct(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, 24))

    def test_mixed_numbers(self):
        self.assertEqual(sum_product([1, -2, 3, -4]), (-2, 24))

    def test_single_number(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

if __name__ == '__main__':
    unittest.main()