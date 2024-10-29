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
    return [s for s in strings if substring in s]

class TestFilterBySubstring(unittest.TestCase):
    def test_example(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])
    
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])
    
    def test_no_matches(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z'), [])
    
    def test_multiple_matches(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array', 'banana'], 'a'), ['abc', 'bacd', 'array', 'banana'])

if __name__ == '__main__':
    unittest.main()