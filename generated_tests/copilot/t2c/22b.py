# t2c/test_22b.txt
import unittest
from typing import List, Any
from your_module import filter_integers  # Replace 'your_module' with the actual module name

class TestFilterIntegers(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

    def test_example_2(self):
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(filter_integers([]), [])

    def test_no_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, {}, []]), [])

    def test_all_integers(self):
        self.assertEqual(filter_integers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_mixed_types(self):
        self.assertEqual(filter_integers([1, 'a', 2.5, 3, None, 4]), [1, 3, 4])

if __name__ == '__main__':
    unittest.main()