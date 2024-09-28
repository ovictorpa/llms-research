import unittest
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings, returning only those that contain the given substring.
    
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    # Function implementation goes here
    # For testing purposes, we'll assume the function is correctly implemented

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_example_case(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_no_matches(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ghi'], 'x'), [])

    def test_all_matches(self):
        self.assertEqual(filter_by_substring(['abc', 'abcd', 'abcde'], 'bc'), ['abc', 'abcd', 'abcde'])

    def test_case_sensitivity(self):
        self.assertEqual(filter_by_substring(['ABC', 'abc', 'ABc', 'abC'], 'ab'), ['abc', 'abC'])

    def test_empty_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'def', ''], ''), ['abc', 'def', ''])

    def test_substring_longer_than_strings(self):
        self.assertEqual(filter_by_substring(['a', 'ab', 'abc'], 'abcd'), [])

    def test_special_characters(self):
        self.assertEqual(filter_by_substring(['a@b', 'b#c', 'c$d'], '@'), ['a@b'])

    def test_whitespace_substring(self):
        self.assertEqual(filter_by_substring(['a b', 'ab', 'a  b'], ' '), ['a b', 'a  b'])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            filter_by_substring([1, 2, 3], 'a')

    def test_non_string_substring(self):
        with self.assertRaises(TypeError):
            filter_by_substring(['abc', 'def'], 1)

if __name__ == '__main__':
    unittest.main()
