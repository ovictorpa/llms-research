import unittest

# Import the functions we're testing
from c2c.10a import is_palindrome, make_palindrome

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("abcd"))

    def test_make_palindrome(self):
        self.assertEqual(make_palindrome(""), "")
        self.assertEqual(make_palindrome("a"), "a")
        self.assertEqual(make_palindrome("ab"), "aba")
        self.assertEqual(make_palindrome("abc"), "abcba")
        self.assertEqual(make_palindrome("racecar"), "racecar")
        self.assertEqual(make_palindrome("hello"), "helloleh")
        self.assertEqual(make_palindrome("world"), "worldldrow")

if __name__ == '__main__':
    unittest.main()
