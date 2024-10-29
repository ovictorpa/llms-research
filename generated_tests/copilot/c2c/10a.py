import unittest
from c2c._10a import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_palindrome_even_length(self):
        self.assertTrue(is_palindrome("abba"))

    def test_palindrome_odd_length(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("a man a plan a canal panama".replace(" ", "")))

    def test_palindrome_with_mixed_case(self):
        self.assertTrue(is_palindrome("Aba".lower()))

    def test_not_palindrome_with_mixed_case(self):
        self.assertFalse(is_palindrome("Hello".lower()))

if __name__ == '__main__':
    unittest.main()