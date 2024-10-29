import unittest
from c2c import 14a

class TestAllPrefixes(unittest.TestCase):
    def test_all_prefixes_regular_string(self):
        self.assertEqual(14a.all_prefixes("hello"), ["h", "he", "hel", "hell", "hello"])

    def test_all_prefixes_empty_string(self):
        self.assertEqual(14a.all_prefixes(""), [])

    def test_all_prefixes_single_character(self):
        self.assertEqual(14a.all_prefixes("a"), ["a"])

    def test_all_prefixes_repeated_characters(self):
        self.assertEqual(14a.all_prefixes("aaa"), ["a", "aa", "aaa"])

    def test_all_prefixes_mixed_characters(self):
        self.assertEqual(14a.all_prefixes("abc123"), ["a", "ab", "abc", "abc1", "abc12", "abc123"])

if __name__ == '__main__':
    unittest.main()