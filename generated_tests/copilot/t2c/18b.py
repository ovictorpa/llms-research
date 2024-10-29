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
    count = start = 0
    while True:
        start = string.find(substring, start) + 1
        if start > 0:
            count += 1
        else:
            return count

class TestHowManyTimes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)
    
    def test_overlapping_substrings(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)
    
    def test_non_overlapping_substrings(self):
        self.assertEqual(how_many_times('abcabcabc', 'abc'), 3)
    
    def test_no_occurrences(self):
        self.assertEqual(how_many_times('abc', 'd'), 0)
    
    def test_substring_longer_than_string(self):
        self.assertEqual(how_many_times('a', 'abc'), 0)

if __name__ == '__main__':
    unittest.main()