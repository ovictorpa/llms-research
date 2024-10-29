import unittest
from typing import List
import collections

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep the order of the elements left the same as in the input.
    
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    counter = collections.Counter(numbers)
    return [num for num in numbers if counter[num] == 1]

class TestRemoveDuplicates(unittest.TestCase):
    def test_example(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])
    
    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3]), [])
    
    def test_mixed_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 3, 5])
    
    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])
    
    def test_single_element(self):
        self.assertEqual(remove_duplicates([1]), [1])

if __name__ == '__main__':
    unittest.main()