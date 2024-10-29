import unittest
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings to include only those that start with the given prefix.
    
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])
    
    def test_example(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])
    
    def test_no_match(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde'], 'x'), [])
    
    def test_all_match(self):
        self.assertEqual(filter_by_prefix(['apple', 'apricot', 'avocado'], 'a'), ['apple', 'apricot', 'avocado'])
    
    def test_mixed_case(self):
        self.assertEqual(filter_by_prefix(['Apple', 'apricot', 'Avocado'], 'A'), ['Apple', 'Avocado'])
    
    def test_partial_match(self):
        self.assertEqual(filter_by_prefix(['apple', 'banana', 'apricot', 'avocado'], 'ap'), ['apple', 'apricot'])

if __name__ == '__main__':
    unittest.main()