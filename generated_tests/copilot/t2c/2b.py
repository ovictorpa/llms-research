import unittest
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those groups into separate strings and return the list of those. 
    Separate groups are balanced (each open brace is properly closed) and not nested within each other. 
    Ignore any spaces in the input string.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Implementation of the function goes here

class TestSeparateParenGroups(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

    def test_empty_string(self):
        self.assertEqual(separate_paren_groups(''), [])

    def test_string_with_spaces(self):
        self.assertEqual(separate_paren_groups(' ( )  (( ))  (( )( )) '), ['()', '(())', '(()())'])

    def test_single_group(self):
        self.assertEqual(separate_paren_groups('((()))'), ['((()))'])

    def test_multiple_groups(self):
        self.assertEqual(separate_paren_groups('()()()'), ['()', '()', '()'])

if __name__ == '__main__':
    unittest.main()