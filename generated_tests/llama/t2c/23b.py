import unittest

class TestLengthString(unittest.TestCase):

    def test_strlen_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_strlen_single_character(self):
        self.assertEqual(strlen('a'), 1)

    def test_strlen_multiple_characters(self):
        self.assertEqual(strlen('abc'), 3)

    def test_strlen_non_string_input(self):
        with self.assertRaises(TypeError):
            strlen(123)  # Replacing the input with a non-string value, e.g., an integer

    def test_strlen_none_value(self):
        with self.assertRaises(AttributeError):  # Assuming strlen() should not be called on None
            strlen(None)

if __name__ == '__main__':
    unittest.main()