import unittest
from c2c._29a import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_with_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['apple', 'apricot', 'banana'], 'ap'), ['apple', 'apricot'])

    def test_with_no_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['apple', 'apricot', 'banana'], 'ba'), ['banana'])

    def test_with_empty_prefix(self):
        self.assertEqual(filter_by_prefix(['apple', 'apricot', 'banana'], ''), ['apple', 'apricot', 'banana'])

    def test_with_no_strings(self):
        self.assertEqual(filter_by_prefix([], 'ap'), [])

    def test_with_no_matching_strings(self):
        self.assertEqual(filter_by_prefix(['apple', 'apricot', 'banana'], 'xy'), [])

    def test_with_all_matching_strings(self):
        self.assertEqual(filter_by_prefix(['apple', 'apricot'], 'ap'), ['apple', 'apricot'])

    def test_with_case_sensitive_prefix(self):
        self.assertEqual(filter_by_prefix(['Apple', 'apricot', 'banana'], 'A'), ['Apple'])

if __name__ == '__main__':
    unittest.main()