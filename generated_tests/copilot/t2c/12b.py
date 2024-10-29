import unittest
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from the list of strings.
    If there are multiple strings with the same maximum length, return the first one.
    Return None if the input list is empty.
    """
    if not strings:
        return None
    return max(strings, key=len)

class TestLongestFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(longest([]), None)
    
    def test_same_length_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')
    
    def test_different_length_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')
    
    def test_multiple_max_length_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc', 'ddd']), 'ccc')

if __name__ == '__main__':
    unittest.main()