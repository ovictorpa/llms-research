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
    # For testing purposes, we'll assume the function is correctly implemented

class TestParseNestedParens(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(''), [])

    def test_single_group(self):
        self.assertEqual(parse_nested_parens('((()))'), [3])

    def test_multiple_simple_groups(self):
        self.assertEqual(parse_nested_parens('() () ()'), [1, 1, 1])

    def test_mixed_nesting_levels(self):
        self.assertEqual(parse_nested_parens('(()) (((())))'), [2, 4])

    def test_complex_nesting(self):
        self.assertEqual(parse_nested_parens('((()())(()())()) (((()))) (())'), [3, 4, 2])

    def test_single_parenthesis(self):
        self.assertEqual(parse_nested_parens('( )'), [1])

    def test_unbalanced_parentheses(self):
        with self.assertRaises(ValueError):
            parse_nested_parens('(()')

    def test_extra_closing_parenthesis(self):
        with self.assertRaises(ValueError):
            parse_nested_parens('(()()()))')

    def test_extra_opening_parenthesis(self):
        with self.assertRaises(ValueError):
            parse_nested_parens('((()()())')

    def test_mixed_characters(self):
        with self.assertRaises(ValueError):
            parse_nested_parens('(a()b())')

    def test_multiple_spaces(self):
        self.assertEqual(parse_nested_parens('()  ()   ()'), [1, 1, 1])

if __name__ == '__main__':
    unittest.main()
