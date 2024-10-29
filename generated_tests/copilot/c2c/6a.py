import unittest
from c2c.6a import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):
    
    def test_single_group(self):
        self.assertEqual(parse_nested_parens("(())"), [2])
        self.assertEqual(parse_nested_parens("((()))"), [3])
        self.assertEqual(parse_nested_parens("()"), [1])
    
    def test_multiple_groups(self):
        self.assertEqual(parse_nested_parens("(()) ((()))"), [2, 3])
        self.assertEqual(parse_nested_parens("() (()) ((()))"), [1, 2, 3])
    
    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(""), [])
    
    def test_no_parens(self):
        self.assertEqual(parse_nested_parens(" "), [])
    
    def test_mixed_groups(self):
        self.assertEqual(parse_nested_parens("() (()) ((())) ()"), [1, 2, 3, 1])
        self.assertEqual(parse_nested_parens("(((()))) () ((()))"), [4, 1, 3])

if __name__ == '__main__':
    unittest.main()