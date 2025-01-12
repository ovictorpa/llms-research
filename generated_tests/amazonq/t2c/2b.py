import unittest
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those groups into separate strings and return the list of those. 
    Separate groups are balanced (each open brace is properly closed) and not nested within each other. 
    Ignore any spaces in the input string.
    """
    # Function implementation goes here
    # For testing purposes, we'll assume the function is correctly implemented

class TestSeparateParenGroups(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

    def test_empty_string(self):
        self.assertEqual(separate_paren_groups(''), [])

    def test_single_group(self):

    def test_nested_groups(self):
        self.assertEqual(separate_paren_groups('(()) ((()))'), ['(())', '((()))'])

    def test_multiple_simple_groups(self):

    def test_complex_nested_groups(self):
        self.assertEqual(separate_paren_groups('((()())()) (()()) ()'), ['((()())())', '(()())', '()'])

    def test_ignore_spaces(self):
        self.assertEqual(separate_paren_groups('(  )   ((  ))'), ['()', '(())'])

    def test_no_groups(self):
        self.assert
    def test_mixed_content(self):
        self.assertEqual(separate_paren_groups('a(b)c(d(e)f)g'), ['()', '(())'])

    def test_unbalanced_groups(self):
        with self.assertRaises(ValueError):
            separate_paren_groups('(()')

    def test_overlapping_groups(self):
        with self.assertRaises(ValueError):
            separate_paren_groups('(()())')

if __name__ == '__main__':
    unittest.main()
