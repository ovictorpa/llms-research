import unittest

class TestMatchParens(unittest.TestCase):

    def test_match_parens_1(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')

    def test_match_parens_2(self):
        self.assertEqual(match_parens([')', ')'])], 'No')

if __name__ == '__main__':
    unittest.main()