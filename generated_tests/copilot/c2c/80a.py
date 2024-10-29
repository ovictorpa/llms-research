import unittest
from c2c._80a import is_happy

class TestIsHappy(unittest.TestCase):

    def test_happy_string(self):
        self.assertTrue(is_happy("abc"))
        self.assertTrue(is_happy("abcdef"))
        self.assertTrue(is_happy("xyz"))

    def test_unhappy_string(self):
        self.assertFalse(is_happy("aab"))
        self.assertFalse(is_happy("abb"))
        self.assertFalse(is_happy("aabbcc"))

    def test_short_string(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("ab"))

    def test_mixed_characters(self):
        self.assertTrue(is_happy("a1b2c3"))
        self.assertFalse(is_happy("a1a2b2"))

    def test_empty_string(self):
        self.assertFalse(is_happy(""))

if __name__ == '__main__':
    unittest.main()