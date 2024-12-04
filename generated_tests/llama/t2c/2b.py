import unittest
from your_module import separate_paren_groups  # Replace 'your_module' with the actual module name
from typing import List

class TestSeparateParenGroups(unittest.TestCase):

    def test_separate_groups(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

    def test_nested_parentheses(self):
        self.assertEqual(separate_paren_groups('((()))'), ['(()[])'])

    def test_unbalanced_parentheses(self):
        with self.assertRaises(ValueError):
            separate_paren_groups('( (')

    def test_empty_string(self):
        self.assertEqual(separate_paren_groups(''), [])

if __name__ == '__main__':
    unittest.main()