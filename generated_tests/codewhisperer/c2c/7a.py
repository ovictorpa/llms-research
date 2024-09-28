import unittest
from c2c.7a import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], "foo"), [])

    def test_no_match(self):
        strings = ["hello", "world", "python"]
        self.assertEqual(filter_by_substring(strings, "bar"), [])

    def test_single_match(self):
        strings = ["hello", "world", "python"]
        self.assertEqual(filter_by_substring(strings, "lo"), ["hello", "world"])

    def test_multiple_matches(self):
        strings = ["hello", "world", "python", "loop"]
        self.assertEqual(filter_by_substring(strings, "o"), ["hello", "world", "python", "loop"])

    def test_case_sensitivity(self):
        strings = ["Hello", "World", "Python"]
        self.assertEqual(filter_by_substring(strings, "o"), ["Hello", "World", "Python"])

if __name__ == "__main__":
    unittest.main()
