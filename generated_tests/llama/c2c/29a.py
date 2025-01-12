import unittest

class TestFilterByPrefixFunction(unittest.TestCase):

    def test_no_matches(self):
        # Test with no matches
        self.assertEqual(filter_by_prefix(["apple", "banana", "cherry"], ""), ["apple", "banana",
"cherry"])

    def test_partial_match(self):
        # Test with partial match
        self.assertEqual(filter_by_prefix(["hello world", "foo bar"], "bar"), ["foo bar"])

    def test_exact_match(self):
        # Test with exact match
        self.assertEqual(filter_by_prefix(["hello", "world"], "hel"), ["hello"])

    def test_no_prefix_provided(self):
        # Test with no prefix provided
        self.assertEqual(filter_by_prefix(["apple", "banana", "cherry"], None), ["apple", "banana",
"cherry"])

    def test_input_not_list(self):
        # Test with input not a list
        with self.assertRaises(TypeError):
            filter_by_prefix("hello world", "bar")

    def test_empty_strings_in_input(self):
        # Test with empty strings in input
        with self.assertRaises(ValueError):  # assuming ValueError is raised for empty strings
            filter_by_prefix(["a", "", "c"], "b")

if __name__ == '__main__':
    unittest.main()