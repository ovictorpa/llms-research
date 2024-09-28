import unittest
from c2c.23a import strlen  # Adjust the import statement as needed

class TestStrlen(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_single_character(self):
        self.assertEqual(strlen("a"), 1)

    def test_multiple_characters(self):
        self.assertEqual(strlen("hello"), 5)

    def test_spaces(self):
        self.assertEqual(strlen("   "), 3)

    def test_mixed_characters(self):
        self.assertEqual(strlen("Hello, World! 123"), 17)

    def test_unicode_characters(self):
        self.assertEqual(strlen("こんにちは"), 5)

    def test_newlines(self):
        self.assertEqual(strlen("Hello\nWorld"), 11)

    def test_tabs(self):
        self.assertEqual(strlen("Hello\tWorld"), 11)

if __name__ == '__main__':
    unittest.main()
