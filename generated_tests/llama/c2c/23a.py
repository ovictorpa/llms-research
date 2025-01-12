import unittest

class TestStringLengthFunction(unittest.TestCase):

    def test_empty_string(self):
        # Test with an empty string
        self.assertEqual(strlen(""), 0)

    def test_single_character_string(self):
        # Test with a single character string
        self.assertEqual(strlen("a"), 1)

    def test_multiple_characters_string(self):
        # Test with multiple characters string
        self.assertEqual(strlen("hello"), 5)

    def test_long_string(self):
        # Test with a long string
        self.assertEqual(strlen("abcdefghijklmnopqrstuvwxyz",), 26)

    def test_empty_input(self):
        # Test with non-string input
        with self.assertRaises(TypeError):
            strlen(123)

    def test_none_input(self):
        # Test with None input
        with self.assertRaises(TypeError):
            strlen(None)

if __name__ == '__main__':
    unittest.main()