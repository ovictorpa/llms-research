import unittest

def is_palindrome(string: str) -> bool:
    """
    Test if the given string is a palindrome.
    """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with the supplied string.
    """
    if is_palindrome(string):
        return string
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
    return string

class TestPalindromeFunctions(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome(""))

    def test_make_palindrome(self):
        self.assertEqual(make_palindrome(""), "")
        self.assertEqual(make_palindrome("cat"), "catac")
        self.assertEqual(make_palindrome("cata"), "catac")
        self.assertEqual(make_palindrome("race"), "racecar")
        self.assertEqual(make_palindrome("racecar"), "racecar")

if __name__ == '__main__':
    unittest.main()