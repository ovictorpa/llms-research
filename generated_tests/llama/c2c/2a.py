import unittest
from your_module import separate_paren_groups  # Replace with the actual module name

class TestSeparateParenGroups(unittest.TestCase):
    def test_empty_string(self):
        input_string = ""
        expected_output = []
        self.assertEqual(separate_paren_groups(input_string), expected_output)

    def test_single_group(self):
        input_string = "((()))"
        expected_output = ["((()))"]
        self.assertEqual(separate_paren_groups(input_string), expected_output)

    def test_multiple_groups(self):
        input_string = "(()())(())()()"
        expected_output = ["(()())", "(())", "()"]
        self.assertEqual(separate_paren_groups(input_string), expected_output)

    def test_nested_groups(self):
        input_string = "((()))(()())"
        expected_output = ["((()))", "()()]
        self.assertEqual(separate_paren_groups(input_string), expected_output)

    def test_mixed_parens(self):
        input_string = "(hello)(world)"
        expected_output = ["(hello)", "(world)"]
        self.assertEqual(separate_paren_groups(input_string), expected_output)

if __name__ == '__main__':
    unittest.main()