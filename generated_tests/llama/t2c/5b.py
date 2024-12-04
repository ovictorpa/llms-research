import unittest
from your_module import intersperse  # Replace 'your_module' with the actual module name
from typing import List

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_no_delimiter(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 2, 3])

    def test_single_element(self):
        self.assertEqual(intersperse([5], 4), [5])

    def test_simple_interspersing(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()