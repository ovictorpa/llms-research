import unittest
from c2c.18a import how_many_times

class TestHowManyTimes(unittest.TestCase):
    
    def test_substring_present_multiple_times(self):
        self.assertEqual(how_many_times("ababab", "ab"), 3)
    
    def test_substring_present_once(self):
        self.assertEqual(how_many_times("hello world", "world"), 1)
    
    def test_substring_not_present(self):
        self.assertEqual(how_many_times("hello world", "python"), 0)
    
    def test_empty_string(self):
        self.assertEqual(how_many_times("", "a"), 0)
    
    def test_empty_substring(self):
        self.assertEqual(how_many_times("hello", ""), 0)
    
    def test_both_empty_string_and_substring(self):
        self.assertEqual(how_many_times("", ""), 0)
    
    def test_substring_same_as_string(self):
        self.assertEqual(how_many_times("test", "test"), 1)
    
    def test_overlapping_substrings(self):
        self.assertEqual(how_many_times("aaaa", "aa"), 3)

if __name__ == '__main__':
    unittest.main()