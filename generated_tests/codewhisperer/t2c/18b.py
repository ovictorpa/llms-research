import unittest

def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, counting overlapping cases.
    
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # Function implementation goes here
    # For testing purposes, we'll assume the function is correctly implemented

class TestHowManyTimes(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(how_many_times('', 'a'), 0)
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_empty_string(self):
        self.assertEqual(how_many_times('', ''), 0)
        self.assertEqual(how_many_times('abc', ''), 4)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('abc', 'x'), 0)
        self.assertEqual(how_many_times('hello', 'world'), 0)

    def test_substring_equal_to_string(self):
        self.assertEqual(how_many_times('abc', 'abc'), 1)
        self.assertEqual(how_many_times('hello', 'hello'), 1)

    def test_overlapping_substrings(self):
        self.assertEqual(how_many_times('abcabc', 'abc'), 2)
        self.assertEqual(how_many_times('ababab', 'ab'), 3)

    def test_mixed_cases(self):
        self.assertEqual(how_many_times('AbCaBcABC', 'abc'), 2)

    def test_long_strings(self):
        long_string = 'a' * 1000000
        long_substring = 'a' * 100000
        self.assertEqual(how_many_times(long_string, long_substring), 900001)

    def test_empty_substring(self):
        self.assertEqual(how_many_times('abc', ''), 4)
        self.assertEqual(how_many_times('', ''), 0)

    def test_non_string_inputs(self):
        with self.assertRaises(TypeError):
            how_many_times(123, 'abc')
        with self.assertRaises(TypeError):
            how_many_times('abc', 123)

if __name__ == '__main__':
    unittest.main()
