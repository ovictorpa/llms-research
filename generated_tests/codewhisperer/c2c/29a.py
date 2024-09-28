import unittest
from c2c.29a import filter_by_prefix  # Adjust the import statement as needed

class TestFilterByPrefix(unittest.TestCase):

    def test_basic_filtering(self):
        strings = ["abc", "def", "abcd", "ghi"]
        prefix = "ab"
        self.assertEqual(filter_by_prefix(strings, prefix), ["abc", "abcd"])

    def test_no_matches(self):
        strings = ["abc", "def", "ghi"]
        prefix = "x"
        self.assertEqual(filter_by_prefix(strings, prefix), [])

    def test_all_match(self):
        strings = ["abc", "abcd", "abcde"]
        prefix = "ab"
        self.assertEqual(filter_by_prefix(strings, prefix), ["abc", "abcd", "abcde"])

    def test_empty_list(self):
        strings = []
        prefix = "ab"
        self.assertEqual(filter_by_prefix(strings, prefix), [])

    def test_empty_prefix(self):
        strings = ["abc", "def", "ghi"]
        prefix = ""
        self.assertEqual(filter_by_prefix(strings, prefix), ["abc", "def", "ghi"])

    def test_case_sensitivity(self):
        strings = ["Abc", "abc", "ABc", "def"]
        prefix = "ab"
        self.assertEqual(filter_by_prefix(strings, prefix), ["abc"])

    def test_prefix_longer_than_strings(self):
        strings = ["a", "ab", "abc"]
        prefix = "abcd"
        self.assertEqual(filter_by_prefix(strings, prefix), [])

    def test_non_string_elements(self):
        strings = ["abc", 123, "def", True]
        prefix = "a"
        with self.assertRaises(AttributeError):
            filter_by_prefix(strings, prefix)

if __name__ == '__main__':
    unittest.main()
