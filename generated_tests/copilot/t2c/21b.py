import unittest
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (with at least two elements), apply a linear transformation to rescale the list 
    such that the smallest number becomes 0 and the largest number becomes 1.
    
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_num = min(numbers)
    max_num = max(numbers)
    return [(num - min_num) / (max_num - min_num) for num in numbers]

class TestRescaleToUnit(unittest.TestCase):
    def test_sequential_numbers(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
    
    def test_negative_numbers(self):
        self.assertEqual(rescale_to_unit([-5.0, -4.0, -3.0, -2.0, -1.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
    
    def test_duplicate_numbers(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 2.0, 4.0, 5.0]), [0.0, 0.25, 0.25, 0.75, 1.0])
    
    def test_floating_point_numbers(self):
        self.assertEqual(rescale_to_unit([1.1, 2.2, 3.3, 4.4, 5.5]), [0.0, 0.25, 0.5, 0.75, 1.0])
    
    def test_two_numbers(self):
        self.assertEqual(rescale_to_unit([1.0, 5.0]), [0.0, 1.0])

if __name__ == '__main__':
    unittest.main()