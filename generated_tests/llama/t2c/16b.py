import unittest

class TestCountDistinctCharacters(unittest.TestCase):

    def test_string_with_distinct_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)

    def test_string_with_repeated_characters(self):
        self.assertEqual(count_distinct_characters('hello'), 4)

    def test_string_with_all_capital_or_all_lowercase(self):
        self.assertEqual(count_distinct_characters('XYZ'), 3)
        self.assertEqual(count_distinct_characters('xyz'), 3)

    def test_string_with_numbers(self):
        self.assertEqual(count_distinct_characters('123abcABC'), 5)

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

if __name__ == '__main__':
    unittest.main()