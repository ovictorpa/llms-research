import unittest
from your_module import match_parens  # Replace with the actual module name

class TestMatchParens(unittest.TestCase):
    def test_matching_parens(self):
        self.assertEqual(match_parens(['(', ')']), 'Yes')
        self.assertEqual(match_parens(['(', ')', '(', ')']), 'Yes')
        self.assertEqual(match_parens(['(', ')', '(', ')', '(']), 'No')

    def test_mismatched_parens(self):
        self.assertEqual(match_parens(['(', ']']), 'No')
        self.assertEqual(match_parens(['(', ')', '[', ']']), 'No')
        self.assertEqual(match_parens(['(', ')', '[', ']', '(', ')']), 'Yes')

    def test_empty_list(self):
        self.assertEqual(match_parens([]), 'No')

if __name__ == '__main__':
    unittest.main()