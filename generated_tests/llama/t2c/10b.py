import unittest
from your_module import make_palindrome  # Replace 'your_module' with the actual module name

class TestMakePalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')

    def test_single_character_string(self):
        self.assertEqual(make_palindrome('a'), 'a')

    def test_non_palindromic_string(self):
        self.assertEqual(make_palindrome('cat'), 'catac')

    def test_palindromic_string(self):
        self.assertEqual(make_palindrome('cata'), 'catac')

if __name__ == '__main__':
    unittest.main()