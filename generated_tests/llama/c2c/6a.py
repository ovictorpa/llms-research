import unittest
from your_module import parse_nested_parens  # Replace with the actual module name

class TestParseNestedParens(unittest.TestCase):
    def test_empty_string(self):
        input_string = ""
        expected_output = []
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_no_parens(self):
        input_string = "hello world"
        expected_output = []
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_single_group(self):
        input_string = "(())"
        expected_output = [2]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_multiple_groups(self):
        input_string = "(()) (()) ()"
        expected_output = [2, 2, 0]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_nested_groups(self):
        input_string = "((())) (() ())"
        expected_output = [3, 1, 1, 0]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

if __name__ == '__main__':
    unittest.main()