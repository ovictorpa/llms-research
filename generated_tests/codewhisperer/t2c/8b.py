import unittest
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of the sum and the product of all the integers in the list.
    An empty sum should be equal to 0, and an empty product should be equal to 1.
    
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Function implementation goes here
    # For testing purposes, we'll assume the function is correctly implemented

class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_example_case(self):

    def test_single_element(self):

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))

    def test_mixed_positive_negative(self):
        self.assertEqual(sum_product([-1, 0, 1]), (0, 0))

    def test_large_numbers(self):
        self.assertEqual(sum_product([1000000, 2000000]), (3000000, 2000000000000))

    def test_zeros(self):
        self.assertEqual(sum_product([0, 0, 0]), (0, 0))

    def test_ones(self):
        self.assertEqual(sum_product([1, 1, 1, 1]), (4, 1))

    def test_integer_overflow(self):
        # This test checks if the function handles large products correctly
        # Note: This might fail if the implementation doesn't handle large integers
        large_list = [2] * 100  # 2^100 is a very large number
        result = sum_product(large_list)
        self.assertEqual(result[0], 200)
        self.assertEqual(result[1], 2**100)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            sum_product([1, 2, 3.5])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            sum_product(123)

if __name__ == '__main__':
    unittest.main()
