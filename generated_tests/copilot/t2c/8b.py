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
    if not numbers:
        return (0, 1)
    total_sum = sum(numbers)
    total_product = 1
    for num in numbers:
        total_product *= num
    return (total_sum, total_product)

class TestSumProduct(unittest.TestCase):
    def test_example_empty(self):
        self.assertEqual(sum_product([]), (0, 1))
    
    def test_example_non_empty(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
    
    def test_single_element(self):
        self.assertEqual(sum_product([5]), (5, 5))
    
    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, 24))
    
    def test_mixed_numbers(self):
        self.assertEqual(sum_product([1, -2, 3, -4]), (-2, 24))

if __name__ == '__main__':
    unittest.main()