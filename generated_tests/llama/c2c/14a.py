import unittest

class TestAllPrefixesFunction(unittest.TestCase):

    def test_empty_string(self):
        # Test that an empty string is returned
        self.assertEqual(all_prefixes(""), [""])

    def test_single_character_string(self):
        # Test with a single character string
        self.assertEqual(all_prefixes("a"), ["", "a"])

    def test_multiple_characters_string(self):
        # Test with a multiple characters string
        self.assertEqual(all_prefixes("hello"), ["", "h", "he", "hel", "hell", "hello"])

    def test_non_string_input(self):
        # Test that type error is raised when input is not a string
        with self.assertRaises(TypeError):
            all_prefixes(123)

if __name__ == '__main__':
    unittest.main()