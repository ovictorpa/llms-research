import unittest
from your_module import filter_by_substring  # Replace with the actual module name

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_input(self):
        input_strings = []
        substring = "hello"
        expected_output = []
        self.assertEqual(filter_by_substring(input_strings, substring), expected_output)

    def test_no_matches(self):
        input_strings = ["apple", "banana", "orange"]
        substring = "grape"
        expected_output = []
        self.assertEqual(filter_by_substring(input_strings, substring), expected_output)

    def test_single_match(self):
        input_strings = ["hello world", "goodbye world", "foo bar"]
        substring = "world"
        expected_output = ["hello world", "goodbye world"]
        self.assertEqual(filter_by_substring(input_strings, substring), expected_output)

    def test_multiple_matches(self):
        input_strings = ["hello hello", "goodbye goodbye", "foo foo bar"]
        substring = "foo"
        expected_output = ["hello hello", "foo foo bar"]
        self.assertEqual(filter_by_substring(input_strings, substring), expected_output)

if __name__ == '__main__':
    unittest.main()