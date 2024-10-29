import unittest
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes of the input string, from shortest to longest.
    """
    return [string[:i] for i in range(1, len(string) + 1)]

class TestAllPrefixesFunction(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
    
    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [])
    
    def test_single_character(self):
        self.assertEqual(all_prefixes('a'), ['a'])
    
    def test_multiple_characters(self):
        self.assertEqual(all_prefixes('abcd'), ['a', 'ab', 'abc', 'abcd'])

if __name__ == '__main__':
    unittest.main()