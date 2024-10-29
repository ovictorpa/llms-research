import unittest
from c2c._23a import strlen

class TestStrlen(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_single_character(self):
        self.assertEqual(strlen("a"), 1)

    def test_multiple_characters(self):
        self.assertEqual(strlen("hello"), 5)

    def test_whitespace(self):
        self.assertEqual(strlen(" "), 1)
        self.assertEqual(strlen("   "), 3)

    def test_special_characters(self):
        self.assertEqual(strlen("!@#$%^&*()"), 10)

    def test_unicode_characters(self):
        self.assertEqual(strlen("你好"), 2)
        self.assertEqual(strlen("こんにちは"), 5)

if __name__ == '__main__':
    unittest.main()