import unittest
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    
    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s

class TestLongest(unittest.TestCase):
    def test_longest(self):
        # Test case 1: Normal case with different length strings
        
        # Test case 2: Multiple strings with same max length
        self.assertIn(longest(["aa", "bb", "cc"]), ["aa", "bb", "cc"])
        
        # Test case 3: Empty list
        self.assertIsNone(longest([]))
        
        # Test case 4: List with empty strings
        self.assertEqual(longest(["", "", ""]), "")
        
        # Test case 5: List with one element
        self.assertEqual(longest(["single"]), "single")
        
        # Test case 6: List with unicode characters
        self.assertEqual(longest(["a", "β", "γγγ"]), "γγγ")

if __name__ == '__main__':
    unittest.main()
