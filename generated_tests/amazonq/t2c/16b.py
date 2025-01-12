import unittest

def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters it consists of, regardless of case.
    
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Function implementation goes here
    # For testing purposes, we'll assume the function is correctly implemented

class TestCountDistinctCharacters(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)
        self.assertEqual(count_distinct_characters('A'), 1)

    def test_all_distinct(self):
        self.assertEqual(count_distinct_characters('abcdef'), 6)

    def test_all_same(self):
        self.assertEqual(count_distinct_characters('aaaaaa'), 1)
        self.assertEqual(count_distinct_characters('AaAaAa'), 1)

    def test_mixed_case(self):
        self.assertEqual(count_distinct_characters('aAbBcC'), 3)

    def test_numbers_and_special_characters(self):
        self.assertEqual(count_distinct_characters('a1B2c3!@#'), 9)

    def test_whitespace(self):
        self.assertEqual(count_distinct_characters('a b c'), 4)  # 'a', 'b', 'c', and space

    def test_unicode(self):
        self.assertEqual(count_distinct_characters('αβγΑΒΓ'), 3)

    def test_long_string(self):
        long_string = 'a' * 1000000 + 'b' * 1000000 + 'c' * 1000000
        self.assertEqual(count_distinct_characters(long_string), 3)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            count_distinct_characters(123)

if __name__ == '__main__':
    unittest.main()
