import unittest
from your_module import longest  # Replace 'your_module' with the actual module name
from typing import List, Optional

class TestLongest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element_list(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_elements_with_same_max_length(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_no_strings_in_input_list(self):
        with self.assertRaises(TypeError):
            longest(123)

if __name__ == '__main__':
    unittest.main()