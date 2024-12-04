import unittest
from your_module import how_many_times  # Replace with the actual module name

class TestHowManyTimes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times("", "abc"), 0)

    def test_no_occurrences(self):
        self.assertEqual(how_many_times("def", "abc"), 0)

    def test_one_occurrence(self):
        self.assertEqual(how_many_times("abcdef", "abc"), 1)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times("abcdeabcdf", "abc"), 2)

    def test_substring_at_end_of_string(self):
        self.assertEqual(how_many_times("abcdefabc", "abc"), 2)

if __name__ == '__main__':
    unittest.main()