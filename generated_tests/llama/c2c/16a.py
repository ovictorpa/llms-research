import unittest

class TestDistinctCharactersFunction(unittest.TestCase):

    def test_empty_string(self):
        # Test that an empty string returns 0
        self.assertEqual(count_distinct_characters(""), 0)

    def test_single_character_string(self):
        # Test with a single character string
        self.assertEqual(count_distinct_characters("a"), 1)

    def test_multiple_character_string(self):
        # Test with a multiple characters string
        self.assertEqual(count_distinct_characters("hello"), 4)

    def test_duplicate_characters_string(self):
        # Test with a string containing duplicate characters
        self.assertEqual(count_distinct_characters("aaaabbbccc"), 3)

    def test_non_string_input(self):
        # Test that type error is raised when input is not a string
        with self.assertRaises(TypeError):
            count_distinct_characters(123)

    def test_case_insensitivity(self):
        # Test that the function is case insensitive
        self.assertEqual(count_distinct_characters("Abc"), 3)

if __name__ == '__main__':
    unittest.main()