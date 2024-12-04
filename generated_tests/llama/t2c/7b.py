import unittest
from your_module import filter_by_substring  # Replace 'your_module' with the actual module name
from typing import List

class TestFilterBySubstring(unittest.TestCase):

    def test_filter_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_filter_no_matches(self):
        self.assertEqual(filter_by_substring(['hello', 'world'], 'x'), [])

    def test_filter_with_matches(self):
        expected_result = ['abc', 'bacd', 'array']
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), expected_result)

if __name__ == '__main__':
    unittest.main()