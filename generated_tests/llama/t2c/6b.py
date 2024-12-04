import unittest
from your_module import parse_nested_parens  # Replace 'your_module' with the actual module name
from typing import List

class TestParseNestedParens(unittest.TestCase):

    def test_parse_nested_parens(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

    def test_no_parentheses(self):
        self.assertEqual(parse_nested_parens(''), [])

    def test_single_group(self):
        self.assertEqual(parse_nested_parens('(())'), [2])

    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(''), [])

if __name__ == '__main__':
    unittest.main()