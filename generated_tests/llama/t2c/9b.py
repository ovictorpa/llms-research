import unittest
from your_module import rolling_max  # Replace 'your_module' with the actual module name
from typing import List

class TestRollingMax(unittest.TestCase):

    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element_list(self):
        self.assertEqual(rolling_max([5]), [5])

if __name__ == '__main__':
    unittest.main()