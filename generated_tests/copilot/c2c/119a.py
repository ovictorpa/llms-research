import unittest
from c2c._119a import match_parens

class TestMatchParens(unittest.TestCase):
    def test_balanced_pairs(self):
        self.assertEqual(match_parens(["()", "()"]), "Yes")
        self.assertEqual(match_parens(["(())", "()"]), "Yes")
        self.assertEqual(match_parens(["()", "(())"]), "Yes")

    def test_unbalanced_pairs(self):
        self.assertEqual(match_parens(["(", ")"]), "No")
        self.assertEqual(match_parens([")(", "()"]), "No")
        self.assertEqual(match_parens(["()", ")("]), "No")

    def test_single_pair(self):
        self.assertEqual(match_parens(["(", "("]), "No")
        self.assertEqual(match_parens([")", ")"]), "No")
        self.assertEqual(match_parens(["(", ")"]), "No")

    def test_empty_strings(self):
        self.assertEqual(match_parens(["", ""]), "Yes")
        self.assertEqual(match_parens(["(", ""]), "No")
        self.assertEqual(match_parens(["", ")"]), "No")

    def test_complex_cases(self):
        self.assertEqual(match_parens(["(()", "())"]), "Yes")
        self.assertEqual(match_parens(["())", "(()"]), "Yes")
        self.assertEqual(match_parens(["(()", "(()"]), "No")
        self.assertEqual(match_parens(["())", "())"]), "No")

if __name__ == '__main__':
    unittest.main()