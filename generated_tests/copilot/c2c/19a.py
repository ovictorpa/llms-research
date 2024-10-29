import unittest
from c2c._19a import sort_numbers

class TestSortNumbers(unittest.TestCase):

    def test_sorted_numbers(self):
        self.assertEqual(sort_numbers("one two three"), "one two three")

    def test_unsorted_numbers(self):
        self.assertEqual(sort_numbers("three one two"), "one two three")

    def test_single_number(self):
        self.assertEqual(sort_numbers("five"), "five")

    def test_empty_string(self):
        self.assertEqual(sort_numbers(""), "")

    def test_all_numbers(self):
        self.assertEqual(sort_numbers("nine eight seven six five four three two one zero"),
                         "zero one two three four five six seven eight nine")

    def test_repeated_numbers(self):
        self.assertEqual(sort_numbers("one one one"), "one one one")

if __name__ == '__main__':
    unittest.main()