import unittest
from typing import List, Tuple

class TestSumProduct(unittest.TestCase):

    def test_sum_and_product_of_empty_list(self):
        numbers = []
        self.assertEqual(sum_product(numbers), (0, 1))

    def test_sum_and_product_of_non_empty_list(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(sum_product(numbers), (10, 24))

    def test_single_element_list(self):
        numbers = [5]
        self.assertEqual(sum_product(numbers), (5, 5))

    def test_multiple_single_elements(self):
        numbers = [1, 1, 1]
        self.assertEqual(sum_product(numbers), (3, 1))

    def test_negative_numbers(self):
        numbers = [-1, -2, -3]
        self.assertEqual(sum_product(numbers), (-6, -6))

if __name__ == '__main__':
    unittest.main()