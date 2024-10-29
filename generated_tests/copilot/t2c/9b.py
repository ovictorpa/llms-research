import unittest
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found up to each point in the sequence.
    
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    max_so_far = numbers[0]
    result = []
    for num in numbers:
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)
    return result

class TestRollingMax(unittest.TestCase):
    def test_example(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])
    
    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])
    
    def test_single_element(self):
        self.assertEqual(rolling_max([5]), [5])
    
    def test_decreasing_numbers(self):
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])
    
    def test_all_same_numbers(self):
        self.assertEqual(rolling_max([3, 3, 3, 3]), [3, 3, 3, 3])

if __name__ == '__main__':
    unittest.main()