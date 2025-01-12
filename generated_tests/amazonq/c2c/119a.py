import unittest
from c2c.119a import match_parens  # Adjust the import statement as needed

class TestMatchParens(unittest.TestCase):

    def test_matching_parens(self):
        self.assertEqual(match_parens(["(())", "()"]), "Yes")

    def test_non_matching_parens(self):
        self.assertEqual(match_parens(["(())", "())"]), "No")

    def test_empty_strings(self):
        self.assertEqual(match_parens(["", ""]), "Yes")

    def test_single_open_paren(self):
        self.assertEqual(match_parens(["(", ""]), "Yes")

    def test_single_close_paren(self):
        self.assertEqual(match_parens([")", ""]), "No")

    def test_complex_matching(self):
        self.assertEqual(match_parens(["((()))", "()()())"]), "Yes")

    def test_complex_non_matching(self):
        self.assertEqual(match_parens(["((())", "()()())"]), "No")

    def test_unbalanced_but_matching(self):
        self.assertEqual(match_parens(["((", "))"]), "Yes")

    def test_reversed_matching(self):
        self.assertEqual(match_parens(["))", "(("]), "Yes")

    def test_mixed_content(self):
        self.assertEqual(match_parens(["a(b)c", "d(e)f"]), "Yes")

    def test_nested_parens(self):
        self.assertEqual(match_parens(["((()))", "((()))"]), "Yes")

    def test_overlapping_parens(self):
        self.assertEqual(match_parens(["(()())", "())()"]), "Yes")

    def test_mismatched_lengths(self):
        self.assertEqual(match_parens(["((", ")"]), "No")

    def test_empty_and_non_empty(self):
        self.assertEqual(match_parens(["", "()"]), "Yes")

if __name__ == '__main__':
    unittest.main()
