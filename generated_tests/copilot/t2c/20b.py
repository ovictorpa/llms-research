import unittest
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two), select and return the two numbers that are closest to each other.
    The two numbers are returned in order (smaller number, larger number).
    
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    return closest_pair

class TestFindClosestElements(unittest.TestCase):
    def test_distinct_numbers(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
    
    def test_duplicate_numbers(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))
    
    def test_negative_numbers(self):
        self.assertEqual(find_closest_elements([-1.0, -2.0, -3.0, -4.0, -5.0, -2.2]), (-2.2, -2.0))
    
    def test_floating_point_numbers(self):
        self.assertEqual(find_closest_elements([1.1, 2.2, 3.3, 4.4, 5.5, 2.25]), (2.2, 2.25))
    
    def test_two_numbers(self):
        self.assertEqual(find_closest_elements([1.0, 2.0]), (1.0, 2.0))

if __name__ == '__main__':
    unittest.main()