import unittest
from c2c.7a import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_with_matching_substrings(self):
        self.assertEqual(filter_by_substring(['apple', 'banana', 'apricot'], 'ap'), ['apple', 'apricot'])

    def test_with_no_matching_substrings(self):
        self.assertEqual(filter_by_substring(['apple', 'banana', 'apricot'], 'xy'), [])

    def test_with_empty_string_list(self):
        self.assertEqual(filter_by_substring([], 'ap'), [])

    def test_with_empty_substring(self):
        self.assertEqual(filter_by_substring(['apple', 'banana', 'apricot'], ''), ['apple', 'banana', 'apricot'])

    def test_with_all_matching_substrings(self):
        self.assertEqual(filter_by_substring(['apple', 'apricot', 'apex'], 'ap'), ['apple', 'apricot', 'apex'])

    def test_with_case_sensitivity(self):
        self.assertEqual(filter_by_substring(['Apple', 'banana', 'apricot'], 'ap'), ['apricot'])

if __name__ == '__main__':
    unittest.main()