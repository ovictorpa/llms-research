# t2c/test_6b.txt
import unittest
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string representing multiple groups of nested parentheses separated by spaces.
    For each of the groups, output the deepest level of nesting of parentheses.
    
    For example, (()()) has a maximum of two levels of nesting while ((())) has three.
    
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Function implementation goes here

class TestParseNestedParens(unittest.TestCase):
    def test_example(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(''), [])

    def test_single_group_no_nesting(self):
        self.assertEqual(parse_nested_parens('()'), [1])

    def test_single_group_with_nesting(self):
        self.assertEqual(parse_nested_parens('((()))'), [3])

    def test_multiple_groups(self):
        self.assertEqual(parse_nested_parens('() (()) ((()))'), [1, 2, 3])

    def test_complex_nesting(self):
        self.assertEqual(parse_nested_parens('((())()())'), [3])

if __name__ == '__main__':
    unittest.main()