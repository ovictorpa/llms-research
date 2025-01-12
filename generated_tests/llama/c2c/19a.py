import unittest

class TestSortNumbersFunction(unittest.TestCase):

    def test_empty_string(self):
        # Test that an empty string returns an empty string
        self.assertEqual(sort_numbers(""), "")

    def test_single_number_string(self):
        # Test with a single number string
        self.assertEqual(sort_numbers("five"), "5")

    def test_multiple_number_string(self):
        # Test with a multiple numbers string
        self.assertEqual(sort_numbers("three five two"), "2 3 5")

    def test_non_numeric_characters(self):
        # Test that non-numeric characters are ignored
        self.assertEqual(sort_numbers("one two 33 four"), "1 2 4")

    def test_non_string_input(self):
        # Test that type error is raised when input is not a string
        with self.assertRaises(TypeError):
            sort_numbers(123)

    def test_large_input(self):
        # Test with a large input
        result = sort_numbers("one two three four five six seven eight nine")
        expected = " 0 1 2 3 4 5 6 7 8 9"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()