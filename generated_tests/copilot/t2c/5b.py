import unittest
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if not numbers:
        return []
    result = []
    for i in range(len(numbers) - 1):
        result.append(numbers[i])
        result.append(delimiter)
    result.append(numbers[-1])
    return result

class TestIntersperse(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])
        self.assertEqual(intersperse([10, 20, 30], 5), [10, 5, 20, 5, 30])

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])
        self.assertEqual(intersperse([10], 5), [10])

    def test_multiple_elements(self):
        self.assertEqual(intersperse([1, 2, 3, 4], 0), [1, 0, 2, 0, 3, 0, 4])
        self.assertEqual(intersperse([5, 6, 7, 8, 9], -1), [5, -1, 6, -1, 7, -1, 8, -1, 9])

if __name__ == '__main__':
    unittest.main()