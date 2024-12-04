import unittest
from your_module import how_many_times  # Replace 'your_module' with the actual module name

class TestHowManyTimes(unittest.TestCase):

    def test_zero_length_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_character_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_no_matches(self):
        self.assertEqual(how_many_times('abc', 'z'), 0)

if __name__ == '__main__':
    unittest.main()