import unittest
from typing import List

class TestAllPrefixes(unittest.TestCase):

    def test_all_prefixes_of_small_string(self):
        string = 'abc'
        expected = ['a', 'ab', 'abc']
        self.assertEqual(all_prefixes(string), expected)

    def test_all_prefixes_ofMedium_string(self):
        string = 'abcdefghijklmnopqrstuvwxyz'
        expected = []
        for i in range(1, len(string) + 1):
            prefix = string[:i]
            if all(prefix != s and prefix not in [s[i:] for s in string] for s in expected):
                expected.append(prefix)
        self.assertEqual(all_prefixes(string), expected)

    def test_all_prefixes_of_empty_string(self):
        string = ''
        expected = []
        self.assertEqual(all_prefixes(string), expected)

    def test_single_character_string(self):
        string = 'a'
        expected = ['a']
        self.assertEqual(all_prefixes(string), expected)

if __name__ == '__main__':
    unittest.main()