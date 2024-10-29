import unittest
from c2c.16a import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_all_unique_characters(self):
        self.assertEqual(count_distinct_characters("abcdef"), 6)

    def test_repeated_characters(self):
        self.assertEqual(count_distinct_characters("aabbcc"), 3)

    def test_mixed_case_characters(self):
        self.assertEqual(count_distinct_characters("AaBbCc"), 3)

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(""), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters("a"), 1)

    def test_special_characters(self):
        self.assertEqual(count_distinct_characters("a!@#a!@#"), 4)

    def test_numbers_in_string(self):
        self.assertEqual(count_distinct_characters("abc123"), 6)

    def test_whitespace_in_string(self):
        self.assertEqual(count_distinct_characters("a b c"), 3)

if __name__ == '__main__':
    unittest.main()